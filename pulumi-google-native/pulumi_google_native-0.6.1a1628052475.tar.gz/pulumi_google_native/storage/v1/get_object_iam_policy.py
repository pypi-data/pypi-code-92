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
    'GetObjectIamPolicyResult',
    'AwaitableGetObjectIamPolicyResult',
    'get_object_iam_policy',
]

@pulumi.output_type
class GetObjectIamPolicyResult:
    def __init__(__self__, bindings=None, etag=None, kind=None, resource_id=None, version=None):
        if bindings and not isinstance(bindings, list):
            raise TypeError("Expected argument 'bindings' to be a list")
        pulumi.set(__self__, "bindings", bindings)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if resource_id and not isinstance(resource_id, str):
            raise TypeError("Expected argument 'resource_id' to be a str")
        pulumi.set(__self__, "resource_id", resource_id)
        if version and not isinstance(version, int):
            raise TypeError("Expected argument 'version' to be a int")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def bindings(self) -> Sequence['outputs.ObjectIamPolicyBindingsItemResponse']:
        """
        An association between a role, which comes with a set of permissions, and members who may assume that role.
        """
        return pulumi.get(self, "bindings")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        HTTP 1.1  Entity tag for the policy.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        The kind of item this is. For policies, this is always storage#policy. This field is ignored on input.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> str:
        """
        The ID of the resource to which this policy belongs. Will be of the form projects/_/buckets/bucket for buckets, and projects/_/buckets/bucket/objects/object for objects. A specific generation may be specified by appending #generationNumber to the end of the object name, e.g. projects/_/buckets/my-bucket/objects/data.txt#17. The current generation can be denoted with #0. This field is ignored on input.
        """
        return pulumi.get(self, "resource_id")

    @property
    @pulumi.getter
    def version(self) -> int:
        """
        The IAM policy format version.
        """
        return pulumi.get(self, "version")


class AwaitableGetObjectIamPolicyResult(GetObjectIamPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetObjectIamPolicyResult(
            bindings=self.bindings,
            etag=self.etag,
            kind=self.kind,
            resource_id=self.resource_id,
            version=self.version)


def get_object_iam_policy(bucket: Optional[str] = None,
                          generation: Optional[str] = None,
                          object: Optional[str] = None,
                          provisional_user_project: Optional[str] = None,
                          user_project: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetObjectIamPolicyResult:
    """
    Returns an IAM policy for the specified object.
    """
    __args__ = dict()
    __args__['bucket'] = bucket
    __args__['generation'] = generation
    __args__['object'] = object
    __args__['provisionalUserProject'] = provisional_user_project
    __args__['userProject'] = user_project
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:storage/v1:getObjectIamPolicy', __args__, opts=opts, typ=GetObjectIamPolicyResult).value

    return AwaitableGetObjectIamPolicyResult(
        bindings=__ret__.bindings,
        etag=__ret__.etag,
        kind=__ret__.kind,
        resource_id=__ret__.resource_id,
        version=__ret__.version)
