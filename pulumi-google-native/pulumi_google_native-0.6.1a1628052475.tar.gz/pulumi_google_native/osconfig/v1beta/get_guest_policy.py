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
    'GetGuestPolicyResult',
    'AwaitableGetGuestPolicyResult',
    'get_guest_policy',
]

@pulumi.output_type
class GetGuestPolicyResult:
    def __init__(__self__, assignment=None, create_time=None, description=None, etag=None, name=None, package_repositories=None, packages=None, recipes=None, update_time=None):
        if assignment and not isinstance(assignment, dict):
            raise TypeError("Expected argument 'assignment' to be a dict")
        pulumi.set(__self__, "assignment", assignment)
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
        if package_repositories and not isinstance(package_repositories, list):
            raise TypeError("Expected argument 'package_repositories' to be a list")
        pulumi.set(__self__, "package_repositories", package_repositories)
        if packages and not isinstance(packages, list):
            raise TypeError("Expected argument 'packages' to be a list")
        pulumi.set(__self__, "packages", packages)
        if recipes and not isinstance(recipes, list):
            raise TypeError("Expected argument 'recipes' to be a list")
        pulumi.set(__self__, "recipes", recipes)
        if update_time and not isinstance(update_time, str):
            raise TypeError("Expected argument 'update_time' to be a str")
        pulumi.set(__self__, "update_time", update_time)

    @property
    @pulumi.getter
    def assignment(self) -> 'outputs.AssignmentResponse':
        """
        Specifies the VM instances that are assigned to this policy. This allows you to target sets or groups of VM instances by different parameters such as labels, names, OS, or zones. If left empty, all VM instances underneath this policy are targeted. At the same level in the resource hierarchy (that is within a project), the service prevents the creation of multiple policies that conflict with each other. For more information, see how the service [handles assignment conflicts](/compute/docs/os-config-management/create-guest-policy#handle-conflicts).
        """
        return pulumi.get(self, "assignment")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        Time this guest policy was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Description of the guest policy. Length of the description is limited to 1024 characters.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        The etag for this guest policy. If this is provided on update, it must match the server's etag.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Unique name of the resource in this project using one of the following forms: `projects/{project_number}/guestPolicies/{guest_policy_id}`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="packageRepositories")
    def package_repositories(self) -> Sequence['outputs.PackageRepositoryResponse']:
        """
        A list of package repositories to configure on the VM instance. This is done before any other configs are applied so they can use these repos. Package repositories are only configured if the corresponding package manager(s) are available.
        """
        return pulumi.get(self, "package_repositories")

    @property
    @pulumi.getter
    def packages(self) -> Sequence['outputs.PackageResponse']:
        """
        The software packages to be managed by this policy.
        """
        return pulumi.get(self, "packages")

    @property
    @pulumi.getter
    def recipes(self) -> Sequence['outputs.SoftwareRecipeResponse']:
        """
        A list of Recipes to install on the VM instance.
        """
        return pulumi.get(self, "recipes")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> str:
        """
        Last time this guest policy was updated.
        """
        return pulumi.get(self, "update_time")


class AwaitableGetGuestPolicyResult(GetGuestPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetGuestPolicyResult(
            assignment=self.assignment,
            create_time=self.create_time,
            description=self.description,
            etag=self.etag,
            name=self.name,
            package_repositories=self.package_repositories,
            packages=self.packages,
            recipes=self.recipes,
            update_time=self.update_time)


def get_guest_policy(guest_policy_id: Optional[str] = None,
                     project: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetGuestPolicyResult:
    """
    Get an OS Config guest policy.
    """
    __args__ = dict()
    __args__['guestPolicyId'] = guest_policy_id
    __args__['project'] = project
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:osconfig/v1beta:getGuestPolicy', __args__, opts=opts, typ=GetGuestPolicyResult).value

    return AwaitableGetGuestPolicyResult(
        assignment=__ret__.assignment,
        create_time=__ret__.create_time,
        description=__ret__.description,
        etag=__ret__.etag,
        name=__ret__.name,
        package_repositories=__ret__.package_repositories,
        packages=__ret__.packages,
        recipes=__ret__.recipes,
        update_time=__ret__.update_time)
