# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetTagValueResult',
    'AwaitableGetTagValueResult',
    'get_tag_value',
]

@pulumi.output_type
class GetTagValueResult:
    def __init__(__self__, create_time=None, description=None, etag=None, name=None, namespaced_name=None, parent=None, short_name=None, update_time=None):
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if namespaced_name and not isinstance(namespaced_name, str):
            raise TypeError("Expected argument 'namespaced_name' to be a str")
        pulumi.set(__self__, "namespaced_name", namespaced_name)
        if parent and not isinstance(parent, str):
            raise TypeError("Expected argument 'parent' to be a str")
        pulumi.set(__self__, "parent", parent)
        if short_name and not isinstance(short_name, str):
            raise TypeError("Expected argument 'short_name' to be a str")
        pulumi.set(__self__, "short_name", short_name)
        if update_time and not isinstance(update_time, str):
            raise TypeError("Expected argument 'update_time' to be a str")
        pulumi.set(__self__, "update_time", update_time)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        Creation time.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Optional. User-assigned description of the TagValue. Must not exceed 256 characters. Read-write.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        Optional. Entity tag which users can pass to prevent race conditions. This field is always set in server responses. See UpdateTagValueRequest for details.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Immutable. Resource name for TagValue in the format `tagValues/456`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="namespacedName")
    def namespaced_name(self) -> str:
        """
        Namespaced name of the TagValue. Must be in the format `{organization_id}/{tag_key_short_name}/{short_name}`.
        """
        return pulumi.get(self, "namespaced_name")

    @property
    @pulumi.getter
    def parent(self) -> str:
        """
        Immutable. The resource name of the new TagValue's parent TagKey. Must be of the form `tagKeys/{tag_key_id}`.
        """
        return pulumi.get(self, "parent")

    @property
    @pulumi.getter(name="shortName")
    def short_name(self) -> str:
        """
        Immutable. User-assigned short name for TagValue. The short name should be unique for TagValues within the same parent TagKey. The short name must be 63 characters or less, beginning and ending with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores (_), dots (.), and alphanumerics between.
        """
        return pulumi.get(self, "short_name")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> str:
        """
        Update time.
        """
        return pulumi.get(self, "update_time")


class AwaitableGetTagValueResult(GetTagValueResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTagValueResult(
            create_time=self.create_time,
            description=self.description,
            etag=self.etag,
            name=self.name,
            namespaced_name=self.namespaced_name,
            parent=self.parent,
            short_name=self.short_name,
            update_time=self.update_time)


def get_tag_value(tag_value_id: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTagValueResult:
    """
    Retrieves TagValue. If the TagValue or namespaced name does not exist, or if the user does not have permission to view it, this method will return `PERMISSION_DENIED`.
    """
    __args__ = dict()
    __args__['tagValueId'] = tag_value_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:cloudresourcemanager/v3:getTagValue', __args__, opts=opts, typ=GetTagValueResult).value

    return AwaitableGetTagValueResult(
        create_time=__ret__.create_time,
        description=__ret__.description,
        etag=__ret__.etag,
        name=__ret__.name,
        namespaced_name=__ret__.namespaced_name,
        parent=__ret__.parent,
        short_name=__ret__.short_name,
        update_time=__ret__.update_time)
