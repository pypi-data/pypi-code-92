import logging
import asyncio
import typing
from typing import Any, Tuple, Callable, Iterable

import grpc

from kikimr.public.sdk.python.client import _apis

from kikimr.public.sdk.python.client.connection import (
    _log_request,
    _log_response,
    _rpc_error_handler,
    _construct_metadata,
    _get_request_timeout,
    _set_server_timeouts,
    _RpcState as RpcState,
    channel_factory
)
from kikimr.public.sdk.python.client.driver import DriverConfig
from kikimr.public.sdk.python.client.settings import BaseRequestSettings
from kikimr.public.sdk.python.client import issues

_stubs_list = (
    _apis.TableService.Stub,
    _apis.SchemeService.Stub,
    _apis.DiscoveryService.Stub,
    _apis.CmsService.Stub
)
logger = logging.getLogger(__name__)


class _RpcState(RpcState):
    __slots__ = ('rpc', 'request_id', 'response_future', 'result_future', 'rpc_name', 'endpoint')

    def __init__(self, stub_instance: Any, rpc_name: str, endpoint: str):
        super().__init__(stub_instance, rpc_name, endpoint)

    async def __call__(self, *args, **kwargs):
        resp = self.rpc(*args, **kwargs)
        if hasattr(resp, "__await__"):  # Check to support async iterators from streams
            return await resp
        return resp

    def future(self, *args, **kwargs):
        raise NotImplementedError


class Connection:
    __slots__ = (
        'endpoint', '_channel', '_call_states', '_stub_instances', '_driver_config', '_cleanup_callbacks',
        '__weakref__', 'lock', 'calls', 'closing',
    )

    def __init__(self, endpoint: str, driver_config: DriverConfig = None):
        global _stubs_list
        self.endpoint = endpoint
        self._channel = channel_factory(self.endpoint, driver_config, grpc.aio)
        self._driver_config = driver_config

        self._stub_instances = {}
        self._cleanup_callbacks = []
        for stub in _stubs_list:
            self._stub_instances[stub] = stub(self._channel)

        self.calls = {}
        self.closing = False

    def _prepare_stub_instance(self, stub: Any):
        if stub not in self._stub_instances:
            self._stub_instances[stub] = stub(self._channel)

    def _prepare_call(
        self,
        stub: Any,
        rpc_name: str,
        request: Any,
        settings: BaseRequestSettings
    ) -> Tuple[_RpcState, float, Any]:

        timeout, metadata = _get_request_timeout(settings), _construct_metadata(self._driver_config, settings)
        _set_server_timeouts(request, settings, timeout)
        self._prepare_stub_instance(stub)
        rpc_state = _RpcState(self._stub_instances[stub], rpc_name, self.endpoint)
        logger.debug("%s: creating call state", rpc_state)

        if self.closing:
            raise issues.ConnectionLost("Couldn't start call")

        # Call successfully prepared and registered
        _log_request(rpc_state, request)
        return rpc_state, timeout, metadata

    async def __call__(
        self,
        request: Any,
        stub: Any,
        rpc_name: str,
        wrap_result: Callable = None,
        settings: BaseRequestSettings = None,
        wrap_args: Iterable = (),
        on_disconnected: Callable = None
    ) -> Any:
        """
        Async method to execute request
        :param request:  A request constructed by client
        :param stub:  A stub instance to wrap channel
        :param rpc_name: A name of RPC to be executed
        :param wrap_result: A callable that intercepts call and wraps received response
        :param settings: An instance of BaseRequestSettings that can be used
        for RPC metadata construction
        :param on_disconnected: A callable to be executed when underlying channel becomes disconnected
        :param wrap_args: And arguments to be passed into wrap_result callable
        :return: A result of computation
        """
        rpc_state, timeout, metadata = self._prepare_call(stub, rpc_name, request, settings)
        try:
            feature = asyncio.ensure_future(rpc_state(request, timeout=timeout, metadata=metadata))

            # Add feature to dict to wait until it finished when close called
            self.calls[rpc_state.request_id] = feature

            response = await feature
            _log_response(rpc_state, response)
            return response if wrap_result is None else wrap_result(rpc_state, response, *wrap_args)
        except grpc.RpcError as rpc_error:
            if on_disconnected:
                coro = on_disconnected()
                if asyncio.iscoroutine(coro):
                    await coro
                on_disconnected = None
            raise _rpc_error_handler(rpc_state, rpc_error, on_disconnected)
        finally:
            self._finish_call(rpc_state)

    def _finish_call(self, call_state: _RpcState):
        self.calls.pop(call_state.request_id)

    async def destroy(self, grace: float = 0):
        """
        Destroys the underlying gRPC channel
        This method does not cancel tasks, but destroys them.
        :param grace:
        :return: None
        """
        if hasattr(self, '_channel') and hasattr(self._channel, 'close'):
            await self._channel.close(grace)

    def add_cleanup_callback(self, callback):
        self._cleanup_callbacks.append(callback)

    async def connection_ready(self, ready_timeout=7):
        """
        Awaits until channel is ready
        :return: None
        """

        await asyncio.wait_for(self._channel.channel_ready(), timeout=ready_timeout)

    async def close(self, grace: float = None):
        """
        Closes the underlying gRPC channel
        :param: grace: If a grace period is specified, this method wait until all active
        RPCs are finshed, once the grace period is reached the ones that haven't
        been terminated are cancelled. If grace is None, this method will wait until all tasks are finished.
        :return: None
        """
        logger.info("Closing channel for endpoint %s", self.endpoint)

        self.closing = True

        if self.calls:
            await asyncio.wait(self.calls.values(), timeout=grace)

        for callback in self._cleanup_callbacks:
            callback(self)

        await self.destroy()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()
