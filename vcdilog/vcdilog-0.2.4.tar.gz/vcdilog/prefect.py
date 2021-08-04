import os
from functools import partial
from typing import Dict, Union

import vcdilog

from .obj import get_logging_attr


def get_prefect_logger(name: str = "logger"):
    import prefect

    return prefect.context.get(name)


def set_prefect_extra_loggers(loggers_list):
    formatted = repr(loggers_list)

    VAR = "PREFECT__LOGGING__EXTRA_LOGGERS"
    os.environ[VAR] = formatted


class PrefectLogger:
    def __init__(self, pipeline_stage: str = "NA", **kwargs) -> None:
        import prefect

        self._prefect = prefect

        try:
            # ensure we are in a prefect flow
            if "flow_name" not in prefect.context:
                raise NameError

            self._logger = vcdilog.get_prefect_logger()
            self._kwargs = self.__standardise_kwargs(**kwargs)
            self._kwargs["pipeline-stage"] = pipeline_stage

        except NameError:
            raise RuntimeError("This must be executed within a prefect context")

    @staticmethod
    def __standardise_kwargs(**kwargs):
        return {k.replace("_", "-"): v for k, v in kwargs.items()}

    def log(
        self,
        msg: Union[str, Dict[str, str]],
        log_level: Union[int, str],
        **kwargs,
    ) -> None:

        log_level = log_level or "INFO"

        if isinstance(log_level, str):
            log_level = get_logging_attr(log_level)

        prefect = self._prefect
        _m = dict(
            {
                "flow-name": prefect.context.flow_name,
                "flow-task": prefect.context.task_name,
                "flow-run-id": prefect.context.flow_run_id,
                "status": kwargs.get("status", "SUCCESS"),
            },
            **self._kwargs,
        )

        _m.update({"msg": msg} if isinstance(msg, str) else msg)
        _m.update(self.__standardise_kwargs(**kwargs))

        self._logger.log(log_level, _m)

    def __getattr__(self, method):

        if method.startswith("_"):
            raise AttributeError

        return partial(self.log, log_level=method.upper())
