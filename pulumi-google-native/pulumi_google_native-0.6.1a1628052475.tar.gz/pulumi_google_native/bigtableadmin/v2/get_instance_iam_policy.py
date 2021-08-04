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
    'GetInstanceIamPolicyResult',
    'AwaitableGetInstanceIamPolicyResult',
    'get_instance_iam_policy',
]

@pulumi.output_type
class GetInstanceIamPolicyResult:
    def __init__(__self__, audit_configs=None, bindings=None, etag=None, version=None):
        if audit_configs and not isinstance(audit_configs, list):
            raise TypeError("Expected argument 'audit_configs' to be a list")
        pulumi.set(__self__, "audit_configs", audit_configs)
        if bindings and not isinstance(bindings, list):
            raise TypeError("Expected argument 'bindings' to be a list")
        pulumi.set(__self__, "bindings", bindings)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if version and not isinstance(version, int):
            raise TypeError("Expected argument 'version' to be a int")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="auditConfigs")
    def audit_configs(self) -> Sequence['outputs.AuditConfigResponse']:
        """
        Specifies cloud audit logging configuration for this policy.
        """
        return pulumi.get(self, "audit_configs")

    @property
    @pulumi.getter
    def bindings(self) -> Sequence['outputs.BindingResponse']:
        """
        Associates a list of `members` to a `role`. Optionally, may specify a `condition` that determines how and when the `bindings` are applied. Each of the `bindings` must contain at least one member.
        """
        return pulumi.get(self, "bindings")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other. It is strongly suggested that systems make use of the `etag` in the read-modify-write cycle to perform policy updates in order to avoid race conditions: An `etag` is returned in the response to `getIamPolicy`, and systems are expected to put that etag in the request to `setIamPolicy` to ensure that their change will be applied to the same version of the policy. **Important:** If you use IAM Conditions, you must include the `etag` field whenever you call `setIamPolicy`. If you omit this field, then IAM allows you to overwrite a version `3` policy with a version `1` policy, and all of the conditions in the version `3` policy are lost.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def version(self) -> int:
        """
        Specifies the format of the policy. Valid values are `0`, `1`, and `3`. Requests that specify an invalid value are rejected. Any operation that affects conditional role bindings must specify version `3`. This requirement applies to the following operations: * Getting a policy that includes a conditional role binding * Adding a conditional role binding to a policy * Changing a conditional role binding in a policy * Removing any role binding, with or without a condition, from a policy that includes conditions **Important:** If you use IAM Conditions, you must include the `etag` field whenever you call `setIamPolicy`. If you omit this field, then IAM allows you to overwrite a version `3` policy with a version `1` policy, and all of the conditions in the version `3` policy are lost. If a policy does not include any conditions, operations on that policy may specify any valid version or leave the field unset. To learn which resources support conditions in their IAM policies, see the [IAM documentation](https://cloud.google.com/iam/help/conditions/resource-policies).
        """
        return pulumi.get(self, "version")


class AwaitableGetInstanceIamPolicyResult(GetInstanceIamPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInstanceIamPolicyResult(
            audit_configs=self.audit_configs,
            bindings=self.bindings,
            etag=self.etag,
            version=self.version)


def get_instance_iam_policy(instance_id: Optional[str] = None,
                            project: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetInstanceIamPolicyResult:
    """
    Gets the access control policy for an instance resource. Returns an empty policy if an instance exists but does not have a policy set.
    """
    __args__ = dict()
    __args__['instanceId'] = instance_id
    __args__['project'] = project
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:bigtableadmin/v2:getInstanceIamPolicy', __args__, opts=opts, typ=GetInstanceIamPolicyResult).value

    return AwaitableGetInstanceIamPolicyResult(
        audit_configs=__ret__.audit_configs,
        bindings=__ret__.bindings,
        etag=__ret__.etag,
        version=__ret__.version)
