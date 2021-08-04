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
    'GetOccurrenceResult',
    'AwaitableGetOccurrenceResult',
    'get_occurrence',
]

@pulumi.output_type
class GetOccurrenceResult:
    def __init__(__self__, attestation=None, build=None, create_time=None, deployment=None, derived_image=None, discovered=None, installation=None, intoto=None, kind=None, name=None, note_name=None, remediation=None, resource=None, update_time=None, vulnerability=None):
        if attestation and not isinstance(attestation, dict):
            raise TypeError("Expected argument 'attestation' to be a dict")
        pulumi.set(__self__, "attestation", attestation)
        if build and not isinstance(build, dict):
            raise TypeError("Expected argument 'build' to be a dict")
        pulumi.set(__self__, "build", build)
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if deployment and not isinstance(deployment, dict):
            raise TypeError("Expected argument 'deployment' to be a dict")
        pulumi.set(__self__, "deployment", deployment)
        if derived_image and not isinstance(derived_image, dict):
            raise TypeError("Expected argument 'derived_image' to be a dict")
        pulumi.set(__self__, "derived_image", derived_image)
        if discovered and not isinstance(discovered, dict):
            raise TypeError("Expected argument 'discovered' to be a dict")
        pulumi.set(__self__, "discovered", discovered)
        if installation and not isinstance(installation, dict):
            raise TypeError("Expected argument 'installation' to be a dict")
        pulumi.set(__self__, "installation", installation)
        if intoto and not isinstance(intoto, dict):
            raise TypeError("Expected argument 'intoto' to be a dict")
        pulumi.set(__self__, "intoto", intoto)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if note_name and not isinstance(note_name, str):
            raise TypeError("Expected argument 'note_name' to be a str")
        pulumi.set(__self__, "note_name", note_name)
        if remediation and not isinstance(remediation, str):
            raise TypeError("Expected argument 'remediation' to be a str")
        pulumi.set(__self__, "remediation", remediation)
        if resource and not isinstance(resource, dict):
            raise TypeError("Expected argument 'resource' to be a dict")
        pulumi.set(__self__, "resource", resource)
        if update_time and not isinstance(update_time, str):
            raise TypeError("Expected argument 'update_time' to be a str")
        pulumi.set(__self__, "update_time", update_time)
        if vulnerability and not isinstance(vulnerability, dict):
            raise TypeError("Expected argument 'vulnerability' to be a dict")
        pulumi.set(__self__, "vulnerability", vulnerability)

    @property
    @pulumi.getter
    def attestation(self) -> 'outputs.DetailsResponse':
        """
        Describes an attestation of an artifact.
        """
        return pulumi.get(self, "attestation")

    @property
    @pulumi.getter
    def build(self) -> 'outputs.GrafeasV1beta1BuildDetailsResponse':
        """
        Describes a verifiable build.
        """
        return pulumi.get(self, "build")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        The time this occurrence was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def deployment(self) -> 'outputs.GrafeasV1beta1DeploymentDetailsResponse':
        """
        Describes the deployment of an artifact on a runtime.
        """
        return pulumi.get(self, "deployment")

    @property
    @pulumi.getter(name="derivedImage")
    def derived_image(self) -> 'outputs.GrafeasV1beta1ImageDetailsResponse':
        """
        Describes how this resource derives from the basis in the associated note.
        """
        return pulumi.get(self, "derived_image")

    @property
    @pulumi.getter
    def discovered(self) -> 'outputs.GrafeasV1beta1DiscoveryDetailsResponse':
        """
        Describes when a resource was discovered.
        """
        return pulumi.get(self, "discovered")

    @property
    @pulumi.getter
    def installation(self) -> 'outputs.GrafeasV1beta1PackageDetailsResponse':
        """
        Describes the installation of a package on the linked resource.
        """
        return pulumi.get(self, "installation")

    @property
    @pulumi.getter
    def intoto(self) -> 'outputs.GrafeasV1beta1IntotoDetailsResponse':
        """
        Describes a specific in-toto link.
        """
        return pulumi.get(self, "intoto")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        This explicitly denotes which of the occurrence details are specified. This field can be used as a filter in list requests.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the occurrence in the form of `projects/[PROJECT_ID]/occurrences/[OCCURRENCE_ID]`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="noteName")
    def note_name(self) -> str:
        """
        Immutable. The analysis note associated with this occurrence, in the form of `projects/[PROVIDER_ID]/notes/[NOTE_ID]`. This field can be used as a filter in list requests.
        """
        return pulumi.get(self, "note_name")

    @property
    @pulumi.getter
    def remediation(self) -> str:
        """
        A description of actions that can be taken to remedy the note.
        """
        return pulumi.get(self, "remediation")

    @property
    @pulumi.getter
    def resource(self) -> 'outputs.ResourceResponse':
        """
        Immutable. The resource for which the occurrence applies.
        """
        return pulumi.get(self, "resource")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> str:
        """
        The time this occurrence was last updated.
        """
        return pulumi.get(self, "update_time")

    @property
    @pulumi.getter
    def vulnerability(self) -> 'outputs.GrafeasV1beta1VulnerabilityDetailsResponse':
        """
        Describes a security vulnerability.
        """
        return pulumi.get(self, "vulnerability")


class AwaitableGetOccurrenceResult(GetOccurrenceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetOccurrenceResult(
            attestation=self.attestation,
            build=self.build,
            create_time=self.create_time,
            deployment=self.deployment,
            derived_image=self.derived_image,
            discovered=self.discovered,
            installation=self.installation,
            intoto=self.intoto,
            kind=self.kind,
            name=self.name,
            note_name=self.note_name,
            remediation=self.remediation,
            resource=self.resource,
            update_time=self.update_time,
            vulnerability=self.vulnerability)


def get_occurrence(occurrence_id: Optional[str] = None,
                   project: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetOccurrenceResult:
    """
    Gets the specified occurrence.
    """
    __args__ = dict()
    __args__['occurrenceId'] = occurrence_id
    __args__['project'] = project
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:containeranalysis/v1beta1:getOccurrence', __args__, opts=opts, typ=GetOccurrenceResult).value

    return AwaitableGetOccurrenceResult(
        attestation=__ret__.attestation,
        build=__ret__.build,
        create_time=__ret__.create_time,
        deployment=__ret__.deployment,
        derived_image=__ret__.derived_image,
        discovered=__ret__.discovered,
        installation=__ret__.installation,
        intoto=__ret__.intoto,
        kind=__ret__.kind,
        name=__ret__.name,
        note_name=__ret__.note_name,
        remediation=__ret__.remediation,
        resource=__ret__.resource,
        update_time=__ret__.update_time,
        vulnerability=__ret__.vulnerability)
