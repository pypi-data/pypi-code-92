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
    def __init__(__self__, attestation=None, build_details=None, compliance=None, create_time=None, deployment=None, derived_image=None, discovered=None, installation=None, kind=None, name=None, note_name=None, remediation=None, resource=None, resource_url=None, update_time=None, upgrade=None, vulnerability_details=None):
        if attestation and not isinstance(attestation, dict):
            raise TypeError("Expected argument 'attestation' to be a dict")
        pulumi.set(__self__, "attestation", attestation)
        if build_details and not isinstance(build_details, dict):
            raise TypeError("Expected argument 'build_details' to be a dict")
        pulumi.set(__self__, "build_details", build_details)
        if compliance and not isinstance(compliance, dict):
            raise TypeError("Expected argument 'compliance' to be a dict")
        pulumi.set(__self__, "compliance", compliance)
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
        if resource_url and not isinstance(resource_url, str):
            raise TypeError("Expected argument 'resource_url' to be a str")
        pulumi.set(__self__, "resource_url", resource_url)
        if update_time and not isinstance(update_time, str):
            raise TypeError("Expected argument 'update_time' to be a str")
        pulumi.set(__self__, "update_time", update_time)
        if upgrade and not isinstance(upgrade, dict):
            raise TypeError("Expected argument 'upgrade' to be a dict")
        pulumi.set(__self__, "upgrade", upgrade)
        if vulnerability_details and not isinstance(vulnerability_details, dict):
            raise TypeError("Expected argument 'vulnerability_details' to be a dict")
        pulumi.set(__self__, "vulnerability_details", vulnerability_details)

    @property
    @pulumi.getter
    def attestation(self) -> 'outputs.AttestationResponse':
        """
        Describes an attestation of an artifact.
        """
        return pulumi.get(self, "attestation")

    @property
    @pulumi.getter(name="buildDetails")
    def build_details(self) -> 'outputs.BuildDetailsResponse':
        """
        Build details for a verifiable build.
        """
        return pulumi.get(self, "build_details")

    @property
    @pulumi.getter
    def compliance(self) -> 'outputs.ComplianceOccurrenceResponse':
        """
        Describes whether or not a resource passes compliance checks.
        """
        return pulumi.get(self, "compliance")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        The time this `Occurrence` was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def deployment(self) -> 'outputs.DeploymentResponse':
        """
        Describes the deployment of an artifact on a runtime.
        """
        return pulumi.get(self, "deployment")

    @property
    @pulumi.getter(name="derivedImage")
    def derived_image(self) -> 'outputs.DerivedResponse':
        """
        Describes how this resource derives from the basis in the associated note.
        """
        return pulumi.get(self, "derived_image")

    @property
    @pulumi.getter
    def discovered(self) -> 'outputs.DiscoveredResponse':
        """
        Describes the initial scan status for this resource.
        """
        return pulumi.get(self, "discovered")

    @property
    @pulumi.getter
    def installation(self) -> 'outputs.InstallationResponse':
        """
        Describes the installation of a package on the linked resource.
        """
        return pulumi.get(self, "installation")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        This explicitly denotes which of the `Occurrence` details are specified. This field can be used as a filter in list requests.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the `Occurrence` in the form "projects/{project_id}/occurrences/{OCCURRENCE_ID}"
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="noteName")
    def note_name(self) -> str:
        """
        An analysis note associated with this image, in the form "providers/{provider_id}/notes/{NOTE_ID}" This field can be used as a filter in list requests.
        """
        return pulumi.get(self, "note_name")

    @property
    @pulumi.getter
    def remediation(self) -> str:
        """
        A description of actions that can be taken to remedy the `Note`
        """
        return pulumi.get(self, "remediation")

    @property
    @pulumi.getter
    def resource(self) -> 'outputs.ResourceResponse':
        """
         The resource for which the `Occurrence` applies.
        """
        return pulumi.get(self, "resource")

    @property
    @pulumi.getter(name="resourceUrl")
    def resource_url(self) -> str:
        """
        The unique URL of the image or the container for which the `Occurrence` applies. For example, https://gcr.io/project/image@sha256:foo This field can be used as a filter in list requests.
        """
        return pulumi.get(self, "resource_url")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> str:
        """
        The time this `Occurrence` was last updated.
        """
        return pulumi.get(self, "update_time")

    @property
    @pulumi.getter
    def upgrade(self) -> 'outputs.UpgradeOccurrenceResponse':
        """
        Describes an upgrade.
        """
        return pulumi.get(self, "upgrade")

    @property
    @pulumi.getter(name="vulnerabilityDetails")
    def vulnerability_details(self) -> 'outputs.VulnerabilityDetailsResponse':
        """
        Details of a security vulnerability note.
        """
        return pulumi.get(self, "vulnerability_details")


class AwaitableGetOccurrenceResult(GetOccurrenceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetOccurrenceResult(
            attestation=self.attestation,
            build_details=self.build_details,
            compliance=self.compliance,
            create_time=self.create_time,
            deployment=self.deployment,
            derived_image=self.derived_image,
            discovered=self.discovered,
            installation=self.installation,
            kind=self.kind,
            name=self.name,
            note_name=self.note_name,
            remediation=self.remediation,
            resource=self.resource,
            resource_url=self.resource_url,
            update_time=self.update_time,
            upgrade=self.upgrade,
            vulnerability_details=self.vulnerability_details)


def get_occurrence(occurrence_id: Optional[str] = None,
                   project: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetOccurrenceResult:
    """
    Returns the requested `Occurrence`.
    """
    __args__ = dict()
    __args__['occurrenceId'] = occurrence_id
    __args__['project'] = project
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:containeranalysis/v1alpha1:getOccurrence', __args__, opts=opts, typ=GetOccurrenceResult).value

    return AwaitableGetOccurrenceResult(
        attestation=__ret__.attestation,
        build_details=__ret__.build_details,
        compliance=__ret__.compliance,
        create_time=__ret__.create_time,
        deployment=__ret__.deployment,
        derived_image=__ret__.derived_image,
        discovered=__ret__.discovered,
        installation=__ret__.installation,
        kind=__ret__.kind,
        name=__ret__.name,
        note_name=__ret__.note_name,
        remediation=__ret__.remediation,
        resource=__ret__.resource,
        resource_url=__ret__.resource_url,
        update_time=__ret__.update_time,
        upgrade=__ret__.upgrade,
        vulnerability_details=__ret__.vulnerability_details)
