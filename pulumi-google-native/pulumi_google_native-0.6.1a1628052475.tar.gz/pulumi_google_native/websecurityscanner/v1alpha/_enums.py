# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'ScanConfigTargetPlatformsItem',
    'ScanConfigUserAgent',
    'ScanRunExecutionState',
    'ScanRunResultState',
]


class ScanConfigTargetPlatformsItem(str, Enum):
    TARGET_PLATFORM_UNSPECIFIED = "TARGET_PLATFORM_UNSPECIFIED"
    """The target platform is unknown. Requests with this enum value will be rejected with INVALID_ARGUMENT error."""
    APP_ENGINE = "APP_ENGINE"
    """Google App Engine service."""
    COMPUTE = "COMPUTE"
    """Google Compute Engine service."""


class ScanConfigUserAgent(str, Enum):
    """
    The user agent used during scanning.
    """
    USER_AGENT_UNSPECIFIED = "USER_AGENT_UNSPECIFIED"
    """The user agent is unknown. Service will default to CHROME_LINUX."""
    CHROME_LINUX = "CHROME_LINUX"
    """Chrome on Linux. This is the service default if unspecified."""
    CHROME_ANDROID = "CHROME_ANDROID"
    """Chrome on Android."""
    SAFARI_IPHONE = "SAFARI_IPHONE"
    """Safari on IPhone."""


class ScanRunExecutionState(str, Enum):
    """
    The execution state of the ScanRun.
    """
    EXECUTION_STATE_UNSPECIFIED = "EXECUTION_STATE_UNSPECIFIED"
    """Represents an invalid state caused by internal server error. This value should never be returned."""
    QUEUED = "QUEUED"
    """The scan is waiting in the queue."""
    SCANNING = "SCANNING"
    """The scan is in progress."""
    FINISHED = "FINISHED"
    """The scan is either finished or stopped by user."""


class ScanRunResultState(str, Enum):
    """
    The result state of the ScanRun. This field is only available after the execution state reaches "FINISHED".
    """
    RESULT_STATE_UNSPECIFIED = "RESULT_STATE_UNSPECIFIED"
    """Default value. This value is returned when the ScanRun is not yet finished."""
    SUCCESS = "SUCCESS"
    """The scan finished without errors."""
    ERROR = "ERROR"
    """The scan finished with errors."""
    KILLED = "KILLED"
    """The scan was terminated by user."""
