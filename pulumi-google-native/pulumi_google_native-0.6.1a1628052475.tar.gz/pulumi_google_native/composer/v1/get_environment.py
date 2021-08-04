# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = [
    'GetEnvironmentResult',
    'AwaitableGetEnvironmentResult',
    'get_environment',
]

@pulumi.output_type
class GetEnvironmentResult:
    def __init__(__self__, config=None, create_time=None, labels=None, name=None, state=None, update_time=None, uuid=None):
        if config and not isinstance(config, dict):
            raise TypeError("Expected argument 'config' to be a dict")
        pulumi.set(__self__, "config", config)
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
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
        if uuid and not isinstance(uuid, str):
            raise TypeError("Expected argument 'uuid' to be a str")
        pulumi.set(__self__, "uuid", uuid)

    @property
    @pulumi.getter
    def config(self) -> 'outputs.EnvironmentConfigResponse':
        """
        Configuration parameters for this environment.
        """
        return pulumi.get(self, "config")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        The time at which this environment was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def labels(self) -> Mapping[str, str]:
        """
        Optional. User-defined labels for this environment. The labels map can contain no more than 64 entries. Entries of the labels map are UTF8 strings that comply with the following restrictions: * Keys must conform to regexp: \p{Ll}\p{Lo}{0,62} * Values must conform to regexp: [\p{Ll}\p{Lo}\p{N}_-]{0,63} * Both keys and values are additionally constrained to be <= 128 bytes in size.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The resource name of the environment, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}" EnvironmentId must start with a lowercase letter followed by up to 63 lowercase letters, numbers, or hyphens, and cannot end with a hyphen.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current state of the environment.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> str:
        """
        The time at which this environment was last modified.
        """
        return pulumi.get(self, "update_time")

    @property
    @pulumi.getter
    def uuid(self) -> str:
        """
        The UUID (Universally Unique IDentifier) associated with this environment. This value is generated when the environment is created.
        """
        return pulumi.get(self, "uuid")


class AwaitableGetEnvironmentResult(GetEnvironmentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEnvironmentResult(
            config=self.config,
            create_time=self.create_time,
            labels=self.labels,
            name=self.name,
            state=self.state,
            update_time=self.update_time,
            uuid=self.uuid)


def get_environment(environment_id: Optional[str] = None,
                    location: Optional[str] = None,
                    project: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEnvironmentResult:
    """
    Get an existing environment.
    """
    __args__ = dict()
    __args__['environmentId'] = environment_id
    __args__['location'] = location
    __args__['project'] = project
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:composer/v1:getEnvironment', __args__, opts=opts, typ=GetEnvironmentResult).value

    return AwaitableGetEnvironmentResult(
        config=__ret__.config,
        create_time=__ret__.create_time,
        labels=__ret__.labels,
        name=__ret__.name,
        state=__ret__.state,
        update_time=__ret__.update_time,
        uuid=__ret__.uuid)
