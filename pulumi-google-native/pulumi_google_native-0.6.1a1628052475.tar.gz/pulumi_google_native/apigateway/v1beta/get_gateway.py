# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetGatewayResult',
    'AwaitableGetGatewayResult',
    'get_gateway',
]

@pulumi.output_type
class GetGatewayResult:
    def __init__(__self__, api_config=None, create_time=None, default_hostname=None, display_name=None, labels=None, name=None, state=None, update_time=None):
        if api_config and not isinstance(api_config, str):
            raise TypeError("Expected argument 'api_config' to be a str")
        pulumi.set(__self__, "api_config", api_config)
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if default_hostname and not isinstance(default_hostname, str):
            raise TypeError("Expected argument 'default_hostname' to be a str")
        pulumi.set(__self__, "default_hostname", default_hostname)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if update_time and not isinstance(update_time, str):
            raise TypeError("Expected argument 'update_time' to be a str")
        pulumi.set(__self__, "update_time", update_time)

    @property
    @pulumi.getter(name="apiConfig")
    def api_config(self) -> str:
        """
        Resource name of the API Config for this Gateway. Format: projects/{project}/locations/global/apis/{api}/configs/{apiConfig}
        """
        return pulumi.get(self, "api_config")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        Created time.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="defaultHostname")
    def default_hostname(self) -> str:
        """
        The default API Gateway host name of the form `{gateway_id}-{hash}.{region_code}.gateway.dev`.
        """
        return pulumi.get(self, "default_hostname")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        Optional. Display name.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def labels(self) -> Mapping[str, str]:
        """
        Optional. Resource labels to represent user-provided metadata. Refer to cloud documentation on labels for more details. https://cloud.google.com/compute/docs/labeling-resources
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name of the Gateway. Format: projects/{project}/locations/{location}/gateways/{gateway}
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current state of the Gateway.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> str:
        """
        Updated time.
        """
        return pulumi.get(self, "update_time")


class AwaitableGetGatewayResult(GetGatewayResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetGatewayResult(
            api_config=self.api_config,
            create_time=self.create_time,
            default_hostname=self.default_hostname,
            display_name=self.display_name,
            labels=self.labels,
            name=self.name,
            state=self.state,
            update_time=self.update_time)


def get_gateway(gateway_id: Optional[str] = None,
                location: Optional[str] = None,
                project: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetGatewayResult:
    """
    Gets details of a single Gateway.
    """
    __args__ = dict()
    __args__['gatewayId'] = gateway_id
    __args__['location'] = location
    __args__['project'] = project
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:apigateway/v1beta:getGateway', __args__, opts=opts, typ=GetGatewayResult).value

    return AwaitableGetGatewayResult(
        api_config=__ret__.api_config,
        create_time=__ret__.create_time,
        default_hostname=__ret__.default_hostname,
        display_name=__ret__.display_name,
        labels=__ret__.labels,
        name=__ret__.name,
        state=__ret__.state,
        update_time=__ret__.update_time)
