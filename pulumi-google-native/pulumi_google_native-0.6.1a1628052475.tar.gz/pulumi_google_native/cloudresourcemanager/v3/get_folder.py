# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetFolderResult',
    'AwaitableGetFolderResult',
    'get_folder',
]

@pulumi.output_type
class GetFolderResult:
    def __init__(__self__, create_time=None, delete_time=None, display_name=None, etag=None, name=None, parent=None, state=None, update_time=None):
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if delete_time and not isinstance(delete_time, str):
            raise TypeError("Expected argument 'delete_time' to be a str")
        pulumi.set(__self__, "delete_time", delete_time)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if parent and not isinstance(parent, str):
            raise TypeError("Expected argument 'parent' to be a str")
        pulumi.set(__self__, "parent", parent)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if update_time and not isinstance(update_time, str):
            raise TypeError("Expected argument 'update_time' to be a str")
        pulumi.set(__self__, "update_time", update_time)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        Timestamp when the folder was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="deleteTime")
    def delete_time(self) -> str:
        """
        Timestamp when the folder was requested to be deleted.
        """
        return pulumi.get(self, "delete_time")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The folder's display name. A folder's display name must be unique amongst its siblings. For example, no two folders with the same parent can share the same display name. The display name must start and end with a letter or digit, may contain letters, digits, spaces, hyphens and underscores and can be no longer than 30 characters. This is captured by the regular expression: `[\p{L}\p{N}]([\p{L}\p{N}_- ]{0,28}[\p{L}\p{N}])?`.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        A checksum computed by the server based on the current value of the folder resource. This may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The resource name of the folder. Its format is `folders/{folder_id}`, for example: "folders/1234".
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def parent(self) -> str:
        """
        The folder's parent's resource name. Updates to the folder's parent must be performed using MoveFolder.
        """
        return pulumi.get(self, "parent")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The lifecycle state of the folder. Updates to the state must be performed using DeleteFolder and UndeleteFolder.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> str:
        """
        Timestamp when the folder was last modified.
        """
        return pulumi.get(self, "update_time")


class AwaitableGetFolderResult(GetFolderResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFolderResult(
            create_time=self.create_time,
            delete_time=self.delete_time,
            display_name=self.display_name,
            etag=self.etag,
            name=self.name,
            parent=self.parent,
            state=self.state,
            update_time=self.update_time)


def get_folder(folder_id: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFolderResult:
    """
    Retrieves a folder identified by the supplied resource name. Valid folder resource names have the format `folders/{folder_id}` (for example, `folders/1234`). The caller must have `resourcemanager.folders.get` permission on the identified folder.
    """
    __args__ = dict()
    __args__['folderId'] = folder_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:cloudresourcemanager/v3:getFolder', __args__, opts=opts, typ=GetFolderResult).value

    return AwaitableGetFolderResult(
        create_time=__ret__.create_time,
        delete_time=__ret__.delete_time,
        display_name=__ret__.display_name,
        etag=__ret__.etag,
        name=__ret__.name,
        parent=__ret__.parent,
        state=__ret__.state,
        update_time=__ret__.update_time)
