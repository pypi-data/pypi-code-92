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
    'GetDiskResult',
    'AwaitableGetDiskResult',
    'get_disk',
]

@pulumi.output_type
class GetDiskResult:
    def __init__(__self__, creation_timestamp=None, description=None, disk_encryption_key=None, erase_windows_vss_signature=None, guest_os_features=None, interface=None, kind=None, label_fingerprint=None, labels=None, last_attach_timestamp=None, last_detach_timestamp=None, license_codes=None, licenses=None, location_hint=None, multi_writer=None, name=None, options=None, physical_block_size_bytes=None, provisioned_iops=None, region=None, replica_zones=None, resource_policies=None, satisfies_pzs=None, self_link=None, self_link_with_id=None, size_gb=None, source_disk=None, source_disk_id=None, source_image=None, source_image_encryption_key=None, source_image_id=None, source_instant_snapshot=None, source_instant_snapshot_id=None, source_snapshot=None, source_snapshot_encryption_key=None, source_snapshot_id=None, source_storage_object=None, status=None, type=None, user_licenses=None, users=None, zone=None):
        if creation_timestamp and not isinstance(creation_timestamp, str):
            raise TypeError("Expected argument 'creation_timestamp' to be a str")
        pulumi.set(__self__, "creation_timestamp", creation_timestamp)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if disk_encryption_key and not isinstance(disk_encryption_key, dict):
            raise TypeError("Expected argument 'disk_encryption_key' to be a dict")
        pulumi.set(__self__, "disk_encryption_key", disk_encryption_key)
        if erase_windows_vss_signature and not isinstance(erase_windows_vss_signature, bool):
            raise TypeError("Expected argument 'erase_windows_vss_signature' to be a bool")
        pulumi.set(__self__, "erase_windows_vss_signature", erase_windows_vss_signature)
        if guest_os_features and not isinstance(guest_os_features, list):
            raise TypeError("Expected argument 'guest_os_features' to be a list")
        pulumi.set(__self__, "guest_os_features", guest_os_features)
        if interface and not isinstance(interface, str):
            raise TypeError("Expected argument 'interface' to be a str")
        pulumi.set(__self__, "interface", interface)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if label_fingerprint and not isinstance(label_fingerprint, str):
            raise TypeError("Expected argument 'label_fingerprint' to be a str")
        pulumi.set(__self__, "label_fingerprint", label_fingerprint)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if last_attach_timestamp and not isinstance(last_attach_timestamp, str):
            raise TypeError("Expected argument 'last_attach_timestamp' to be a str")
        pulumi.set(__self__, "last_attach_timestamp", last_attach_timestamp)
        if last_detach_timestamp and not isinstance(last_detach_timestamp, str):
            raise TypeError("Expected argument 'last_detach_timestamp' to be a str")
        pulumi.set(__self__, "last_detach_timestamp", last_detach_timestamp)
        if license_codes and not isinstance(license_codes, list):
            raise TypeError("Expected argument 'license_codes' to be a list")
        pulumi.set(__self__, "license_codes", license_codes)
        if licenses and not isinstance(licenses, list):
            raise TypeError("Expected argument 'licenses' to be a list")
        pulumi.set(__self__, "licenses", licenses)
        if location_hint and not isinstance(location_hint, str):
            raise TypeError("Expected argument 'location_hint' to be a str")
        pulumi.set(__self__, "location_hint", location_hint)
        if multi_writer and not isinstance(multi_writer, bool):
            raise TypeError("Expected argument 'multi_writer' to be a bool")
        pulumi.set(__self__, "multi_writer", multi_writer)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if options and not isinstance(options, str):
            raise TypeError("Expected argument 'options' to be a str")
        pulumi.set(__self__, "options", options)
        if physical_block_size_bytes and not isinstance(physical_block_size_bytes, str):
            raise TypeError("Expected argument 'physical_block_size_bytes' to be a str")
        pulumi.set(__self__, "physical_block_size_bytes", physical_block_size_bytes)
        if provisioned_iops and not isinstance(provisioned_iops, str):
            raise TypeError("Expected argument 'provisioned_iops' to be a str")
        pulumi.set(__self__, "provisioned_iops", provisioned_iops)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if replica_zones and not isinstance(replica_zones, list):
            raise TypeError("Expected argument 'replica_zones' to be a list")
        pulumi.set(__self__, "replica_zones", replica_zones)
        if resource_policies and not isinstance(resource_policies, list):
            raise TypeError("Expected argument 'resource_policies' to be a list")
        pulumi.set(__self__, "resource_policies", resource_policies)
        if satisfies_pzs and not isinstance(satisfies_pzs, bool):
            raise TypeError("Expected argument 'satisfies_pzs' to be a bool")
        pulumi.set(__self__, "satisfies_pzs", satisfies_pzs)
        if self_link and not isinstance(self_link, str):
            raise TypeError("Expected argument 'self_link' to be a str")
        pulumi.set(__self__, "self_link", self_link)
        if self_link_with_id and not isinstance(self_link_with_id, str):
            raise TypeError("Expected argument 'self_link_with_id' to be a str")
        pulumi.set(__self__, "self_link_with_id", self_link_with_id)
        if size_gb and not isinstance(size_gb, str):
            raise TypeError("Expected argument 'size_gb' to be a str")
        pulumi.set(__self__, "size_gb", size_gb)
        if source_disk and not isinstance(source_disk, str):
            raise TypeError("Expected argument 'source_disk' to be a str")
        pulumi.set(__self__, "source_disk", source_disk)
        if source_disk_id and not isinstance(source_disk_id, str):
            raise TypeError("Expected argument 'source_disk_id' to be a str")
        pulumi.set(__self__, "source_disk_id", source_disk_id)
        if source_image and not isinstance(source_image, str):
            raise TypeError("Expected argument 'source_image' to be a str")
        pulumi.set(__self__, "source_image", source_image)
        if source_image_encryption_key and not isinstance(source_image_encryption_key, dict):
            raise TypeError("Expected argument 'source_image_encryption_key' to be a dict")
        pulumi.set(__self__, "source_image_encryption_key", source_image_encryption_key)
        if source_image_id and not isinstance(source_image_id, str):
            raise TypeError("Expected argument 'source_image_id' to be a str")
        pulumi.set(__self__, "source_image_id", source_image_id)
        if source_instant_snapshot and not isinstance(source_instant_snapshot, str):
            raise TypeError("Expected argument 'source_instant_snapshot' to be a str")
        pulumi.set(__self__, "source_instant_snapshot", source_instant_snapshot)
        if source_instant_snapshot_id and not isinstance(source_instant_snapshot_id, str):
            raise TypeError("Expected argument 'source_instant_snapshot_id' to be a str")
        pulumi.set(__self__, "source_instant_snapshot_id", source_instant_snapshot_id)
        if source_snapshot and not isinstance(source_snapshot, str):
            raise TypeError("Expected argument 'source_snapshot' to be a str")
        pulumi.set(__self__, "source_snapshot", source_snapshot)
        if source_snapshot_encryption_key and not isinstance(source_snapshot_encryption_key, dict):
            raise TypeError("Expected argument 'source_snapshot_encryption_key' to be a dict")
        pulumi.set(__self__, "source_snapshot_encryption_key", source_snapshot_encryption_key)
        if source_snapshot_id and not isinstance(source_snapshot_id, str):
            raise TypeError("Expected argument 'source_snapshot_id' to be a str")
        pulumi.set(__self__, "source_snapshot_id", source_snapshot_id)
        if source_storage_object and not isinstance(source_storage_object, str):
            raise TypeError("Expected argument 'source_storage_object' to be a str")
        pulumi.set(__self__, "source_storage_object", source_storage_object)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if user_licenses and not isinstance(user_licenses, list):
            raise TypeError("Expected argument 'user_licenses' to be a list")
        pulumi.set(__self__, "user_licenses", user_licenses)
        if users and not isinstance(users, list):
            raise TypeError("Expected argument 'users' to be a list")
        pulumi.set(__self__, "users", users)
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
    @pulumi.getter(name="diskEncryptionKey")
    def disk_encryption_key(self) -> 'outputs.CustomerEncryptionKeyResponse':
        """
        Encrypts the disk using a customer-supplied encryption key. After you encrypt a disk with a customer-supplied key, you must provide the same key if you use the disk later (e.g. to create a disk snapshot, to create a disk image, to create a machine image, or to attach the disk to a virtual machine). Customer-supplied encryption keys do not protect access to metadata of the disk. If you do not provide an encryption key when creating the disk, then the disk will be encrypted using an automatically generated key and you do not need to provide a key to use the disk later.
        """
        return pulumi.get(self, "disk_encryption_key")

    @property
    @pulumi.getter(name="eraseWindowsVssSignature")
    def erase_windows_vss_signature(self) -> bool:
        """
        Specifies whether the disk restored from a source snapshot should erase Windows specific VSS signature.
        """
        return pulumi.get(self, "erase_windows_vss_signature")

    @property
    @pulumi.getter(name="guestOsFeatures")
    def guest_os_features(self) -> Sequence['outputs.GuestOsFeatureResponse']:
        """
        A list of features to enable on the guest operating system. Applicable only for bootable images. Read Enabling guest operating system features to see a list of available options.
        """
        return pulumi.get(self, "guest_os_features")

    @property
    @pulumi.getter
    def interface(self) -> str:
        """
        Specifies the disk interface to use for attaching this disk, which is either SCSI or NVME. The default is SCSI.
        """
        return pulumi.get(self, "interface")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Type of the resource. Always compute#disk for disks.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="labelFingerprint")
    def label_fingerprint(self) -> str:
        """
        A fingerprint for the labels being applied to this disk, which is essentially a hash of the labels set used for optimistic locking. The fingerprint is initially generated by Compute Engine and changes after every request to modify or update labels. You must always provide an up-to-date fingerprint hash in order to update or change labels, otherwise the request will fail with error 412 conditionNotMet. To see the latest fingerprint, make a get() request to retrieve a disk.
        """
        return pulumi.get(self, "label_fingerprint")

    @property
    @pulumi.getter
    def labels(self) -> Mapping[str, str]:
        """
        Labels to apply to this disk. These can be later modified by the setLabels method.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter(name="lastAttachTimestamp")
    def last_attach_timestamp(self) -> str:
        """
        Last attach timestamp in RFC3339 text format.
        """
        return pulumi.get(self, "last_attach_timestamp")

    @property
    @pulumi.getter(name="lastDetachTimestamp")
    def last_detach_timestamp(self) -> str:
        """
        Last detach timestamp in RFC3339 text format.
        """
        return pulumi.get(self, "last_detach_timestamp")

    @property
    @pulumi.getter(name="licenseCodes")
    def license_codes(self) -> Sequence[str]:
        """
        Integer license codes indicating which licenses are attached to this disk.
        """
        return pulumi.get(self, "license_codes")

    @property
    @pulumi.getter
    def licenses(self) -> Sequence[str]:
        """
        A list of publicly visible licenses. Reserved for Google's use.
        """
        return pulumi.get(self, "licenses")

    @property
    @pulumi.getter(name="locationHint")
    def location_hint(self) -> str:
        """
        An opaque location hint used to place the disk close to other resources. This field is for use by internal tools that use the public API.
        """
        return pulumi.get(self, "location_hint")

    @property
    @pulumi.getter(name="multiWriter")
    def multi_writer(self) -> bool:
        """
        Indicates whether or not the disk can be read/write attached to more than one instance.
        """
        return pulumi.get(self, "multi_writer")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def options(self) -> str:
        """
        Internal use only.
        """
        return pulumi.get(self, "options")

    @property
    @pulumi.getter(name="physicalBlockSizeBytes")
    def physical_block_size_bytes(self) -> str:
        """
        Physical block size of the persistent disk, in bytes. If not present in a request, a default value is used. The currently supported size is 4096, other sizes may be added in the future. If an unsupported value is requested, the error message will list the supported values for the caller's project.
        """
        return pulumi.get(self, "physical_block_size_bytes")

    @property
    @pulumi.getter(name="provisionedIops")
    def provisioned_iops(self) -> str:
        """
        Indicates how many IOPS to provision for the disk. This sets the number of I/O operations per second that the disk can handle. Values must be between 10,000 and 120,000. For more details, see the Extreme persistent disk documentation.
        """
        return pulumi.get(self, "provisioned_iops")

    @property
    @pulumi.getter
    def region(self) -> str:
        """
        URL of the region where the disk resides. Only applicable for regional resources. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="replicaZones")
    def replica_zones(self) -> Sequence[str]:
        """
        URLs of the zones where the disk should be replicated to. Only applicable for regional resources.
        """
        return pulumi.get(self, "replica_zones")

    @property
    @pulumi.getter(name="resourcePolicies")
    def resource_policies(self) -> Sequence[str]:
        """
        Resource policies applied to this disk for automatic snapshot creations.
        """
        return pulumi.get(self, "resource_policies")

    @property
    @pulumi.getter(name="satisfiesPzs")
    def satisfies_pzs(self) -> bool:
        """
        Reserved for future use.
        """
        return pulumi.get(self, "satisfies_pzs")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> str:
        """
        Server-defined fully-qualified URL for this resource.
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
    @pulumi.getter(name="sizeGb")
    def size_gb(self) -> str:
        """
        Size, in GB, of the persistent disk. You can specify this field when creating a persistent disk using the sourceImage, sourceSnapshot, or sourceDisk parameter, or specify it alone to create an empty persistent disk. If you specify this field along with a source, the value of sizeGb must not be less than the size of the source. Acceptable values are 1 to 65536, inclusive.
        """
        return pulumi.get(self, "size_gb")

    @property
    @pulumi.getter(name="sourceDisk")
    def source_disk(self) -> str:
        """
        The source disk used to create this disk. You can provide this as a partial or full URL to the resource. For example, the following are valid values: - https://www.googleapis.com/compute/v1/projects/project/zones/zone /disks/disk - https://www.googleapis.com/compute/v1/projects/project/regions/region /disks/disk - projects/project/zones/zone/disks/disk - projects/project/regions/region/disks/disk - zones/zone/disks/disk - regions/region/disks/disk 
        """
        return pulumi.get(self, "source_disk")

    @property
    @pulumi.getter(name="sourceDiskId")
    def source_disk_id(self) -> str:
        """
        The unique ID of the disk used to create this disk. This value identifies the exact disk that was used to create this persistent disk. For example, if you created the persistent disk from a disk that was later deleted and recreated under the same name, the source disk ID would identify the exact version of the disk that was used.
        """
        return pulumi.get(self, "source_disk_id")

    @property
    @pulumi.getter(name="sourceImage")
    def source_image(self) -> str:
        """
        The source image used to create this disk. If the source image is deleted, this field will not be set. To create a disk with one of the public operating system images, specify the image by its family name. For example, specify family/debian-9 to use the latest Debian 9 image: projects/debian-cloud/global/images/family/debian-9 Alternatively, use a specific version of a public operating system image: projects/debian-cloud/global/images/debian-9-stretch-vYYYYMMDD To create a disk with a custom image that you created, specify the image name in the following format: global/images/my-custom-image You can also specify a custom image by its image family, which returns the latest version of the image in that family. Replace the image name with family/family-name: global/images/family/my-image-family 
        """
        return pulumi.get(self, "source_image")

    @property
    @pulumi.getter(name="sourceImageEncryptionKey")
    def source_image_encryption_key(self) -> 'outputs.CustomerEncryptionKeyResponse':
        """
        The customer-supplied encryption key of the source image. Required if the source image is protected by a customer-supplied encryption key.
        """
        return pulumi.get(self, "source_image_encryption_key")

    @property
    @pulumi.getter(name="sourceImageId")
    def source_image_id(self) -> str:
        """
        The ID value of the image used to create this disk. This value identifies the exact image that was used to create this persistent disk. For example, if you created the persistent disk from an image that was later deleted and recreated under the same name, the source image ID would identify the exact version of the image that was used.
        """
        return pulumi.get(self, "source_image_id")

    @property
    @pulumi.getter(name="sourceInstantSnapshot")
    def source_instant_snapshot(self) -> str:
        """
        The source instant snapshot used to create this disk. You can provide this as a partial or full URL to the resource. For example, the following are valid values: - https://www.googleapis.com/compute/v1/projects/project/zones/zone /instantSnapshots/instantSnapshot - projects/project/zones/zone/instantSnapshots/instantSnapshot - zones/zone/instantSnapshots/instantSnapshot 
        """
        return pulumi.get(self, "source_instant_snapshot")

    @property
    @pulumi.getter(name="sourceInstantSnapshotId")
    def source_instant_snapshot_id(self) -> str:
        """
        The unique ID of the instant snapshot used to create this disk. This value identifies the exact instant snapshot that was used to create this persistent disk. For example, if you created the persistent disk from an instant snapshot that was later deleted and recreated under the same name, the source instant snapshot ID would identify the exact version of the instant snapshot that was used.
        """
        return pulumi.get(self, "source_instant_snapshot_id")

    @property
    @pulumi.getter(name="sourceSnapshot")
    def source_snapshot(self) -> str:
        """
        The source snapshot used to create this disk. You can provide this as a partial or full URL to the resource. For example, the following are valid values: - https://www.googleapis.com/compute/v1/projects/project /global/snapshots/snapshot - projects/project/global/snapshots/snapshot - global/snapshots/snapshot 
        """
        return pulumi.get(self, "source_snapshot")

    @property
    @pulumi.getter(name="sourceSnapshotEncryptionKey")
    def source_snapshot_encryption_key(self) -> 'outputs.CustomerEncryptionKeyResponse':
        """
        The customer-supplied encryption key of the source snapshot. Required if the source snapshot is protected by a customer-supplied encryption key.
        """
        return pulumi.get(self, "source_snapshot_encryption_key")

    @property
    @pulumi.getter(name="sourceSnapshotId")
    def source_snapshot_id(self) -> str:
        """
        The unique ID of the snapshot used to create this disk. This value identifies the exact snapshot that was used to create this persistent disk. For example, if you created the persistent disk from a snapshot that was later deleted and recreated under the same name, the source snapshot ID would identify the exact version of the snapshot that was used.
        """
        return pulumi.get(self, "source_snapshot_id")

    @property
    @pulumi.getter(name="sourceStorageObject")
    def source_storage_object(self) -> str:
        """
        The full Google Cloud Storage URI where the disk image is stored. This file must be a gzip-compressed tarball whose name ends in .tar.gz or virtual machine disk whose name ends in vmdk. Valid URIs may start with gs:// or https://storage.googleapis.com/. This flag is not optimized for creating multiple disks from a source storage object. To create many disks from a source storage object, use gcloud compute images import instead.
        """
        return pulumi.get(self, "source_storage_object")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The status of disk creation. - CREATING: Disk is provisioning. - RESTORING: Source data is being copied into the disk. - FAILED: Disk creation failed. - READY: Disk is ready for use. - DELETING: Disk is deleting. 
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        URL of the disk type resource describing which disk type to use to create the disk. Provide this when creating the disk. For example: projects/project /zones/zone/diskTypes/pd-ssd . See Persistent disk types.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="userLicenses")
    def user_licenses(self) -> Sequence[str]:
        """
        A list of publicly visible user-licenses. Unlike regular licenses, user provided licenses can be modified after the disk is created. This includes a list of URLs to the license resource. For example, to provide a debian license: https://www.googleapis.com/compute/v1/projects/debian-cloud/global/licenses/debian-9-stretch 
        """
        return pulumi.get(self, "user_licenses")

    @property
    @pulumi.getter
    def users(self) -> Sequence[str]:
        """
        Links to the users of the disk (attached instances) in form: projects/project/zones/zone/instances/instance
        """
        return pulumi.get(self, "users")

    @property
    @pulumi.getter
    def zone(self) -> str:
        """
        URL of the zone where the disk resides. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body.
        """
        return pulumi.get(self, "zone")


class AwaitableGetDiskResult(GetDiskResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDiskResult(
            creation_timestamp=self.creation_timestamp,
            description=self.description,
            disk_encryption_key=self.disk_encryption_key,
            erase_windows_vss_signature=self.erase_windows_vss_signature,
            guest_os_features=self.guest_os_features,
            interface=self.interface,
            kind=self.kind,
            label_fingerprint=self.label_fingerprint,
            labels=self.labels,
            last_attach_timestamp=self.last_attach_timestamp,
            last_detach_timestamp=self.last_detach_timestamp,
            license_codes=self.license_codes,
            licenses=self.licenses,
            location_hint=self.location_hint,
            multi_writer=self.multi_writer,
            name=self.name,
            options=self.options,
            physical_block_size_bytes=self.physical_block_size_bytes,
            provisioned_iops=self.provisioned_iops,
            region=self.region,
            replica_zones=self.replica_zones,
            resource_policies=self.resource_policies,
            satisfies_pzs=self.satisfies_pzs,
            self_link=self.self_link,
            self_link_with_id=self.self_link_with_id,
            size_gb=self.size_gb,
            source_disk=self.source_disk,
            source_disk_id=self.source_disk_id,
            source_image=self.source_image,
            source_image_encryption_key=self.source_image_encryption_key,
            source_image_id=self.source_image_id,
            source_instant_snapshot=self.source_instant_snapshot,
            source_instant_snapshot_id=self.source_instant_snapshot_id,
            source_snapshot=self.source_snapshot,
            source_snapshot_encryption_key=self.source_snapshot_encryption_key,
            source_snapshot_id=self.source_snapshot_id,
            source_storage_object=self.source_storage_object,
            status=self.status,
            type=self.type,
            user_licenses=self.user_licenses,
            users=self.users,
            zone=self.zone)


def get_disk(disk: Optional[str] = None,
             project: Optional[str] = None,
             zone: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDiskResult:
    """
    Returns a specified persistent disk. Gets a list of available persistent disks by making a list() request.
    """
    __args__ = dict()
    __args__['disk'] = disk
    __args__['project'] = project
    __args__['zone'] = zone
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:compute/alpha:getDisk', __args__, opts=opts, typ=GetDiskResult).value

    return AwaitableGetDiskResult(
        creation_timestamp=__ret__.creation_timestamp,
        description=__ret__.description,
        disk_encryption_key=__ret__.disk_encryption_key,
        erase_windows_vss_signature=__ret__.erase_windows_vss_signature,
        guest_os_features=__ret__.guest_os_features,
        interface=__ret__.interface,
        kind=__ret__.kind,
        label_fingerprint=__ret__.label_fingerprint,
        labels=__ret__.labels,
        last_attach_timestamp=__ret__.last_attach_timestamp,
        last_detach_timestamp=__ret__.last_detach_timestamp,
        license_codes=__ret__.license_codes,
        licenses=__ret__.licenses,
        location_hint=__ret__.location_hint,
        multi_writer=__ret__.multi_writer,
        name=__ret__.name,
        options=__ret__.options,
        physical_block_size_bytes=__ret__.physical_block_size_bytes,
        provisioned_iops=__ret__.provisioned_iops,
        region=__ret__.region,
        replica_zones=__ret__.replica_zones,
        resource_policies=__ret__.resource_policies,
        satisfies_pzs=__ret__.satisfies_pzs,
        self_link=__ret__.self_link,
        self_link_with_id=__ret__.self_link_with_id,
        size_gb=__ret__.size_gb,
        source_disk=__ret__.source_disk,
        source_disk_id=__ret__.source_disk_id,
        source_image=__ret__.source_image,
        source_image_encryption_key=__ret__.source_image_encryption_key,
        source_image_id=__ret__.source_image_id,
        source_instant_snapshot=__ret__.source_instant_snapshot,
        source_instant_snapshot_id=__ret__.source_instant_snapshot_id,
        source_snapshot=__ret__.source_snapshot,
        source_snapshot_encryption_key=__ret__.source_snapshot_encryption_key,
        source_snapshot_id=__ret__.source_snapshot_id,
        source_storage_object=__ret__.source_storage_object,
        status=__ret__.status,
        type=__ret__.type,
        user_licenses=__ret__.user_licenses,
        users=__ret__.users,
        zone=__ret__.zone)
