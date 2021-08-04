# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetRegionInPlaceSnapshotResult',
    'AwaitableGetRegionInPlaceSnapshotResult',
    'get_region_in_place_snapshot',
]

@pulumi.output_type
class GetRegionInPlaceSnapshotResult:
    def __init__(__self__, creation_timestamp=None, description=None, disk_size_gb=None, guest_flush=None, kind=None, label_fingerprint=None, labels=None, name=None, region=None, self_link=None, self_link_with_id=None, source_disk=None, source_disk_id=None, status=None, zone=None):
        if creation_timestamp and not isinstance(creation_timestamp, str):
            raise TypeError("Expected argument 'creation_timestamp' to be a str")
        pulumi.set(__self__, "creation_timestamp", creation_timestamp)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if disk_size_gb and not isinstance(disk_size_gb, str):
            raise TypeError("Expected argument 'disk_size_gb' to be a str")
        pulumi.set(__self__, "disk_size_gb", disk_size_gb)
        if guest_flush and not isinstance(guest_flush, bool):
            raise TypeError("Expected argument 'guest_flush' to be a bool")
        pulumi.set(__self__, "guest_flush", guest_flush)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if label_fingerprint and not isinstance(label_fingerprint, str):
            raise TypeError("Expected argument 'label_fingerprint' to be a str")
        pulumi.set(__self__, "label_fingerprint", label_fingerprint)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if self_link and not isinstance(self_link, str):
            raise TypeError("Expected argument 'self_link' to be a str")
        pulumi.set(__self__, "self_link", self_link)
        if self_link_with_id and not isinstance(self_link_with_id, str):
            raise TypeError("Expected argument 'self_link_with_id' to be a str")
        pulumi.set(__self__, "self_link_with_id", self_link_with_id)
        if source_disk and not isinstance(source_disk, str):
            raise TypeError("Expected argument 'source_disk' to be a str")
        pulumi.set(__self__, "source_disk", source_disk)
        if source_disk_id and not isinstance(source_disk_id, str):
            raise TypeError("Expected argument 'source_disk_id' to be a str")
        pulumi.set(__self__, "source_disk_id", source_disk_id)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if zone and not isinstance(zone, str):
            raise TypeError("Expected argument 'zone' to be a str")
        pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> str:
        """
        Creation timestamp in RFC3339 text format.
        """
        return pulumi.get(self, "creation_timestamp")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        An optional description of this resource. Provide this property when you create the resource.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="diskSizeGb")
    def disk_size_gb(self) -> str:
        """
        Size of the source disk, specified in GB.
        """
        return pulumi.get(self, "disk_size_gb")

    @property
    @pulumi.getter(name="guestFlush")
    def guest_flush(self) -> bool:
        """
        Specifies to create an application consistent in-place snapshot by informing the OS to prepare for the snapshot process. Currently only supported on Windows instances using the Volume Shadow Copy Service (VSS).
        """
        return pulumi.get(self, "guest_flush")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Type of the resource. Always compute#inPlaceSnapshot for InPlaceSnapshot resources.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="labelFingerprint")
    def label_fingerprint(self) -> str:
        """
        A fingerprint for the labels being applied to this InPlaceSnapshot, which is essentially a hash of the labels set used for optimistic locking. The fingerprint is initially generated by Compute Engine and changes after every request to modify or update labels. You must always provide an up-to-date fingerprint hash in order to update or change labels, otherwise the request will fail with error 412 conditionNotMet. To see the latest fingerprint, make a get() request to retrieve a InPlaceSnapshot.
        """
        return pulumi.get(self, "label_fingerprint")

    @property
    @pulumi.getter
    def labels(self) -> Mapping[str, str]:
        """
        Labels to apply to this InPlaceSnapshot. These can be later modified by the setLabels method. Label values may be empty.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def region(self) -> str:
        """
        URL of the region where the in-place snapshot resides. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> str:
        """
        Server-defined URL for the resource.
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter(name="selfLinkWithId")
    def self_link_with_id(self) -> str:
        """
        Server-defined URL for this resource's resource id.
        """
        return pulumi.get(self, "self_link_with_id")

    @property
    @pulumi.getter(name="sourceDisk")
    def source_disk(self) -> str:
        """
        URL of the source disk used to create this in-place snapshot. Note that the source disk must be in the same zone/region as the in-place snapshot to be created. This can be a full or valid partial URL. For example, the following are valid values: - https://www.googleapis.com/compute/v1/projects/project/zones/zone /disks/disk - projects/project/zones/zone/disks/disk - zones/zone/disks/disk 
        """
        return pulumi.get(self, "source_disk")

    @property
    @pulumi.getter(name="sourceDiskId")
    def source_disk_id(self) -> str:
        """
        The ID value of the disk used to create this InPlaceSnapshot. This value may be used to determine whether the InPlaceSnapshot was taken from the current or a previous instance of a given disk name.
        """
        return pulumi.get(self, "source_disk_id")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The status of the inPlaceSnapshot. This can be CREATING, DELETING, FAILED, or READY.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def zone(self) -> str:
        """
        URL of the zone where the in-place snapshot resides. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body.
        """
        return pulumi.get(self, "zone")


class AwaitableGetRegionInPlaceSnapshotResult(GetRegionInPlaceSnapshotResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRegionInPlaceSnapshotResult(
            creation_timestamp=self.creation_timestamp,
            description=self.description,
            disk_size_gb=self.disk_size_gb,
            guest_flush=self.guest_flush,
            kind=self.kind,
            label_fingerprint=self.label_fingerprint,
            labels=self.labels,
            name=self.name,
            region=self.region,
            self_link=self.self_link,
            self_link_with_id=self.self_link_with_id,
            source_disk=self.source_disk,
            source_disk_id=self.source_disk_id,
            status=self.status,
            zone=self.zone)


def get_region_in_place_snapshot(in_place_snapshot: Optional[str] = None,
                                 project: Optional[str] = None,
                                 region: Optional[str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRegionInPlaceSnapshotResult:
    """
    Returns the specified InPlaceSnapshot resource in the specified region.
    """
    __args__ = dict()
    __args__['inPlaceSnapshot'] = in_place_snapshot
    __args__['project'] = project
    __args__['region'] = region
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:compute/alpha:getRegionInPlaceSnapshot', __args__, opts=opts, typ=GetRegionInPlaceSnapshotResult).value

    return AwaitableGetRegionInPlaceSnapshotResult(
        creation_timestamp=__ret__.creation_timestamp,
        description=__ret__.description,
        disk_size_gb=__ret__.disk_size_gb,
        guest_flush=__ret__.guest_flush,
        kind=__ret__.kind,
        label_fingerprint=__ret__.label_fingerprint,
        labels=__ret__.labels,
        name=__ret__.name,
        region=__ret__.region,
        self_link=__ret__.self_link,
        self_link_with_id=__ret__.self_link_with_id,
        source_disk=__ret__.source_disk,
        source_disk_id=__ret__.source_disk_id,
        status=__ret__.status,
        zone=__ret__.zone)
