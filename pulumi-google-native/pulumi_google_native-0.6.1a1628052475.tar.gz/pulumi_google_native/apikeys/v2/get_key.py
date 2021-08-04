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
    'GetKeyResult',
    'AwaitableGetKeyResult',
    'get_key',
]

@pulumi.output_type
class GetKeyResult:
    def __init__(__self__, create_time=None, delete_time=None, display_name=None, etag=None, key_string=None, name=None, restrictions=None, uid=None, update_time=None):
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
        if key_string and not isinstance(key_string, str):
            raise TypeError("Expected argument 'key_string' to be a str")
        pulumi.set(__self__, "key_string", key_string)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if restrictions and not isinstance(restrictions, dict):
            raise TypeError("Expected argument 'restrictions' to be a dict")
        pulumi.set(__self__, "restrictions", restrictions)
        if uid and not isinstance(uid, str):
            raise TypeError("Expected argument 'uid' to be a str")
        pulumi.set(__self__, "uid", uid)
        if update_time and not isinstance(update_time, str):
            raise TypeError("Expected argument 'update_time' to be a str")
        pulumi.set(__self__, "update_time", update_time)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        A timestamp identifying the time this key was originally created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="deleteTime")
    def delete_time(self) -> str:
        """
        A timestamp when this key was deleted. If the resource is not deleted, this must be empty.
        """
        return pulumi.get(self, "delete_time")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        Human-readable display name of this key that you can modify. The maximum length is 63 characters.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        A checksum computed by the server based on the current value of the Key resource. This may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="keyString")
    def key_string(self) -> str:
        """
        An encrypted and signed value held by this key. This field can be accessed only through the `GetKeyString` method.
        """
        return pulumi.get(self, "key_string")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The resource name of the key. The `name` has the form: `projects//locations/global/keys/`. For example: `projects/123456867718/locations/global/keys/b7ff1f9f-8275-410a-94dd-3855ee9b5dd2` NOTE: Key is a global resource; hence the only supported value for location is `global`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def restrictions(self) -> 'outputs.V2RestrictionsResponse':
        """
        Key restrictions.
        """
        return pulumi.get(self, "restrictions")

    @property
    @pulumi.getter
    def uid(self) -> str:
        """
        Unique id in UUID4 format.
        """
        return pulumi.get(self, "uid")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> str:
        """
        A timestamp identifying the time this key was last updated.
        """
        return pulumi.get(self, "update_time")


class AwaitableGetKeyResult(GetKeyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetKeyResult(
            create_time=self.create_time,
            delete_time=self.delete_time,
            display_name=self.display_name,
            etag=self.etag,
            key_string=self.key_string,
            name=self.name,
            restrictions=self.restrictions,
            uid=self.uid,
            update_time=self.update_time)


def get_key(key_id: Optional[str] = None,
            location: Optional[str] = None,
            project: Optional[str] = None,
            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetKeyResult:
    """
    Gets the metadata for an API key. The key string of the API key isn't included in the response. NOTE: Key is a global resource; hence the only supported value for location is `global`.
    """
    __args__ = dict()
    __args__['keyId'] = key_id
    __args__['location'] = location
    __args__['project'] = project
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:apikeys/v2:getKey', __args__, opts=opts, typ=GetKeyResult).value

    return AwaitableGetKeyResult(
        create_time=__ret__.create_time,
        delete_time=__ret__.delete_time,
        display_name=__ret__.display_name,
        etag=__ret__.etag,
        key_string=__ret__.key_string,
        name=__ret__.name,
        restrictions=__ret__.restrictions,
        uid=__ret__.uid,
        update_time=__ret__.update_time)
