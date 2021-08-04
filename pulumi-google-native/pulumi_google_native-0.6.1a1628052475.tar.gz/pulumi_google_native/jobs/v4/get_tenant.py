# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetTenantResult',
    'AwaitableGetTenantResult',
    'get_tenant',
]

@pulumi.output_type
class GetTenantResult:
    def __init__(__self__, external_id=None, name=None):
        if external_id and not isinstance(external_id, str):
            raise TypeError("Expected argument 'external_id' to be a str")
        pulumi.set(__self__, "external_id", external_id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="externalId")
    def external_id(self) -> str:
        """
        Client side tenant identifier, used to uniquely identify the tenant. The maximum number of allowed characters is 255.
        """
        return pulumi.get(self, "external_id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Required during tenant update. The resource name for a tenant. This is generated by the service when a tenant is created. The format is "projects/{project_id}/tenants/{tenant_id}", for example, "projects/foo/tenants/bar".
        """
        return pulumi.get(self, "name")


class AwaitableGetTenantResult(GetTenantResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTenantResult(
            external_id=self.external_id,
            name=self.name)


def get_tenant(project: Optional[str] = None,
               tenant_id: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTenantResult:
    """
    Retrieves specified tenant.
    """
    __args__ = dict()
    __args__['project'] = project
    __args__['tenantId'] = tenant_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:jobs/v4:getTenant', __args__, opts=opts, typ=GetTenantResult).value

    return AwaitableGetTenantResult(
        external_id=__ret__.external_id,
        name=__ret__.name)
