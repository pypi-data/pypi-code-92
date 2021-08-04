# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetHubResult',
    'AwaitableGetHubResult',
    'get_hub',
]

@pulumi.output_type
class GetHubResult:
    def __init__(__self__, create_time=None, description=None, labels=None, name=None, state=None, unique_id=None, update_time=None):
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if unique_id and not isinstance(unique_id, str):
            raise TypeError("Expected argument 'unique_id' to be a str")
        pulumi.set(__self__, "unique_id", unique_id)
        if update_time and not isinstance(update_time, str):
            raise TypeError("Expected argument 'update_time' to be a str")
        pulumi.set(__self__, "update_time", update_time)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        Time when the Hub was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Short description of the hub resource.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def labels(self) -> Mapping[str, str]:
        """
        User-defined labels.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Immutable. The name of a Hub resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current lifecycle state of this Hub.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="uniqueId")
    def unique_id(self) -> str:
        """
        Google-generated UUID for this resource. This is unique across all Hub resources. If a Hub resource is deleted and another with the same name is created, it gets a different unique_id.
        """
        return pulumi.get(self, "unique_id")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> str:
        """
        Time when the Hub was updated.
        """
        return pulumi.get(self, "update_time")


class AwaitableGetHubResult(GetHubResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetHubResult(
            create_time=self.create_time,
            description=self.description,
            labels=self.labels,
            name=self.name,
            state=self.state,
            unique_id=self.unique_id,
            update_time=self.update_time)


def get_hub(hub_id: Optional[str] = None,
            project: Optional[str] = None,
            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetHubResult:
    """
    Gets details of a single Hub.
    """
    __args__ = dict()
    __args__['hubId'] = hub_id
    __args__['project'] = project
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:networkconnectivity/v1alpha1:getHub', __args__, opts=opts, typ=GetHubResult).value

    return AwaitableGetHubResult(
        create_time=__ret__.create_time,
        description=__ret__.description,
        labels=__ret__.labels,
        name=__ret__.name,
        state=__ret__.state,
        unique_id=__ret__.unique_id,
        update_time=__ret__.update_time)
