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
    'GetSnapshotResult',
    'AwaitableGetSnapshotResult',
    'get_snapshot',
]

@pulumi.output_type
class GetSnapshotResult:
    def __init__(__self__, auto_created=None, chain_name=None, creation_timestamp=None, description=None, disk_size_gb=None, download_bytes=None, guest_flush=None, guest_os_features=None, kind=None, label_fingerprint=None, labels=None, license_codes=None, licenses=None, location_hint=None, name=None, satisfies_pzs=None, self_link=None, self_link_with_id=None, snapshot_encryption_key=None, source_disk=None, source_disk_encryption_key=None, source_disk_id=None, source_instant_snapshot=None, source_instant_snapshot_id=None, status=None, storage_bytes=None, storage_bytes_status=None, storage_locations=None, user_licenses=None):
        if auto_created and not isinstance(auto_created, bool):
            raise TypeError("Expected argument 'auto_created' to be a bool")
        pulumi.set(__self__, "auto_created", auto_created)
        if chain_name and not isinstance(chain_name, str):
            raise TypeError("Expected argument 'chain_name' to be a str")
        pulumi.set(__self__, "chain_name", chain_name)
        if creation_timestamp and not isinstance(creation_timestamp, str):
            raise TypeError("Expected argument 'creation_timestamp' to be a str")
        pulumi.set(__self__, "creation_timestamp", creation_timestamp)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if disk_size_gb and not isinstance(disk_size_gb, str):
            raise TypeError("Expected argument 'disk_size_gb' to be a str")
        pulumi.set(__self__, "disk_size_gb", disk_size_gb)
        if download_bytes and not isinstance(download_bytes, str):
            raise TypeError("Expected argument 'download_bytes' to be a str")
        pulumi.set(__self__, "download_bytes", download_bytes)
        if guest_flush and not isinstance(guest_flush, bool):
            raise TypeError("Expected argument 'guest_flush' to be a bool")
        pulumi.set(__self__, "guest_flush", guest_flush)
        if guest_os_features and not isinstance(guest_os_features, list):
            raise TypeError("Expected argument 'guest_os_features' to be a list")
        pulumi.set(__self__, "guest_os_features", guest_os_features)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if label_fingerprint and not isinstance(label_fingerprint, str):
            raise TypeError("Expected argument 'label_fingerprint' to be a str")
        pulumi.set(__self__, "label_fingerprint", label_fingerprint)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if license_codes and not isinstance(license_codes, list):
            raise TypeError("Expected argument 'license_codes' to be a list")
        pulumi.set(__self__, "license_codes", license_codes)
        if licenses and not isinstance(licenses, list):
            raise TypeError("Expected argument 'licenses' to be a list")
        pulumi.set(__self__, "licenses", licenses)
        if location_hint and not isinstance(location_hint, str):
            raise TypeError("Expected argument 'location_hint' to be a str")
        pulumi.set(__self__, "location_hint", location_hint)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if satisfies_pzs and not isinstance(satisfies_pzs, bool):
            raise TypeError("Expected argument 'satisfies_pzs' to be a bool")
        pulumi.set(__self__, "satisfies_pzs", satisfies_pzs)
        if self_link and not isinstance(self_link, str):
            raise TypeError("Expected argument 'self_link' to be a str")
        pulumi.set(__self__, "self_link", self_link)
        if self_link_with_id and not isinstance(self_link_with_id, str):
            raise TypeError("Expected argument 'self_link_with_id' to be a str")
        pulumi.set(__self__, "self_link_with_id", self_link_with_id)
        if snapshot_encryption_key and not isinstance(snapshot_encryption_key, dict):
            raise TypeError("Expected argument 'snapshot_encryption_key' to be a dict")
        pulumi.set(__self__, "snapshot_encryption_key", snapshot_encryption_key)
        if source_disk and not isinstance(source_disk, str):
            raise TypeError("Expected argument 'source_disk' to be a str")
        pulumi.set(__self__, "source_disk", source_disk)
        if source_disk_encryption_key and not isinstance(source_disk_encryption_key, dict):
            raise TypeError("Expected argument 'source_disk_encryption_key' to be a dict")
        pulumi.set(__self__, "source_disk_encryption_key", source_disk_encryption_key)
        if source_disk_id and not isinstance(source_disk_id, str):
            raise TypeError("Expected argument 'source_disk_id' to be a str")
        pulumi.set(__self__, "source_disk_id", source_disk_id)
        if source_instant_snapshot and not isinstance(source_instant_snapshot, str):
            raise TypeError("Expected argument 'source_instant_snapshot' to be a str")
        pulumi.set(__self__, "source_instant_snapshot", source_instant_snapshot)
        if source_instant_snapshot_id and not isinstance(source_instant_snapshot_id, str):
            raise TypeError("Expected argument 'source_instant_snapshot_id' to be a str")
        pulumi.set(__self__, "source_instant_snapshot_id", source_instant_snapshot_id)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if storage_bytes and not isinstance(storage_bytes, str):
            raise TypeError("Expected argument 'storage_bytes' to be a str")
        pulumi.set(__self__, "storage_bytes", storage_bytes)
        if storage_bytes_status and not isinstance(storage_bytes_status, str):
            raise TypeError("Expected argument 'storage_bytes_status' to be a str")
        pulumi.set(__self__, "storage_bytes_status", storage_bytes_status)
        if storage_locations and not isinstance(storage_locations, list):
            raise TypeError("Expected argument 'storage_locations' to be a list")
        pulumi.set(__self__, "storage_locations", storage_locations)
        if user_licenses and not isinstance(user_licenses, list):
            raise TypeError("Expected argument 'user_licenses' to be a list")
        pulumi.set(__self__, "user_licenses", user_licenses)

    @property
    @pulumi.getter(name="autoCreated")
    def auto_created(self) -> bool:
        """
        Set to true if snapshots are automatically created by applying resource policy on the target disk.
        """
        return pulumi.get(self, "auto_created")

    @property
    @pulumi.getter(name="chainName")
    def chain_name(self) -> str:
        """
        Creates the new snapshot in the snapshot chain labeled with the specified name. The chain name must be 1-63 characters long and comply with RFC1035. This is an uncommon option only for advanced service owners who needs to create separate snapshot chains, for example, for chargeback tracking. When you describe your snapshot resource, this field is visible only if it has a non-empty value.
        """
        return pulumi.get(self, "chain_name")

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
    @pulumi.getter(name="downloadBytes")
    def download_bytes(self) -> str:
        """
        Number of bytes downloaded to restore a snapshot to a disk.
        """
        return pulumi.get(self, "download_bytes")

    @property
    @pulumi.getter(name="guestFlush")
    def guest_flush(self) -> bool:
        """
        [Input Only] Whether to attempt an application consistent snapshot by informing the OS to prepare for the snapshot process. Currently only supported on Windows instances using the Volume Shadow Copy Service (VSS).
        """
        return pulumi.get(self, "guest_flush")

    @property
    @pulumi.getter(name="guestOsFeatures")
    def guest_os_features(self) -> Sequence['outputs.GuestOsFeatureResponse']:
        """
        A list of features to enable on the guest operating system. Applicable only for bootable images. Read Enabling guest operating system features to see a list of available options.
        """
        return pulumi.get(self, "guest_os_features")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Type of the resource. Always compute#snapshot for Snapshot resources.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="labelFingerprint")
    def label_fingerprint(self) -> str:
        """
        A fingerprint for the labels being applied to this snapshot, which is essentially a hash of the labels set used for optimistic locking. The fingerprint is initially generated by Compute Engine and changes after every request to modify or update labels. You must always provide an up-to-date fingerprint hash in order to update or change labels, otherwise the request will fail with error 412 conditionNotMet. To see the latest fingerprint, make a get() request to retrieve a snapshot.
        """
        return pulumi.get(self, "label_fingerprint")

    @property
    @pulumi.getter
    def labels(self) -> Mapping[str, str]:
        """
        Labels to apply to this snapshot. These can be later modified by the setLabels method. Label values may be empty.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter(name="licenseCodes")
    def license_codes(self) -> Sequence[str]:
        """
        Integer license codes indicating which licenses are attached to this snapshot.
        """
        return pulumi.get(self, "license_codes")

    @property
    @pulumi.getter
    def licenses(self) -> Sequence[str]:
        """
        A list of public visible licenses that apply to this snapshot. This can be because the original image had licenses attached (such as a Windows image).
        """
        return pulumi.get(self, "licenses")

    @property
    @pulumi.getter(name="locationHint")
    def location_hint(self) -> str:
        """
        An opaque location hint used to place the snapshot close to other resources. This field is for use by internal tools that use the public API.
        """
        return pulumi.get(self, "location_hint")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        """
        return pulumi.get(self, "name")

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
    @pulumi.getter(name="snapshotEncryptionKey")
    def snapshot_encryption_key(self) -> 'outputs.CustomerEncryptionKeyResponse':
        """
        Encrypts the snapshot using a customer-supplied encryption key. After you encrypt a snapshot using a customer-supplied key, you must provide the same key if you use the snapshot later. For example, you must provide the encryption key when you create a disk from the encrypted snapshot in a future request. Customer-supplied encryption keys do not protect access to metadata of the snapshot. If you do not provide an encryption key when creating the snapshot, then the snapshot will be encrypted using an automatically generated key and you do not need to provide a key to use the snapshot later.
        """
        return pulumi.get(self, "snapshot_encryption_key")

    @property
    @pulumi.getter(name="sourceDisk")
    def source_disk(self) -> str:
        """
        The source disk used to create this snapshot.
        """
        return pulumi.get(self, "source_disk")

    @property
    @pulumi.getter(name="sourceDiskEncryptionKey")
    def source_disk_encryption_key(self) -> 'outputs.CustomerEncryptionKeyResponse':
        """
        The customer-supplied encryption key of the source disk. Required if the source disk is protected by a customer-supplied encryption key.
        """
        return pulumi.get(self, "source_disk_encryption_key")

    @property
    @pulumi.getter(name="sourceDiskId")
    def source_disk_id(self) -> str:
        """
        The ID value of the disk used to create this snapshot. This value may be used to determine whether the snapshot was taken from the current or a previous instance of a given disk name.
        """
        return pulumi.get(self, "source_disk_id")

    @property
    @pulumi.getter(name="sourceInstantSnapshot")
    def source_instant_snapshot(self) -> str:
        """
        The source instant snapshot used to create this snapshot. You can provide this as a partial or full URL to the resource. For example, the following are valid values: - https://www.googleapis.com/compute/v1/projects/project/zones/zone /instantSnapshots/instantSnapshot - projects/project/zones/zone/instantSnapshots/instantSnapshot - zones/zone/instantSnapshots/instantSnapshot 
        """
        return pulumi.get(self, "source_instant_snapshot")

    @property
    @pulumi.getter(name="sourceInstantSnapshotId")
    def source_instant_snapshot_id(self) -> str:
        """
        The unique ID of the instant snapshot used to create this snapshot. This value identifies the exact instant snapshot that was used to create this persistent disk. For example, if you created the persistent disk from an instant snapshot that was later deleted and recreated under the same name, the source instant snapshot ID would identify the exact instant snapshot that was used.
        """
        return pulumi.get(self, "source_instant_snapshot_id")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The status of the snapshot. This can be CREATING, DELETING, FAILED, READY, or UPLOADING.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="storageBytes")
    def storage_bytes(self) -> str:
        """
        A size of the storage used by the snapshot. As snapshots share storage, this number is expected to change with snapshot creation/deletion.
        """
        return pulumi.get(self, "storage_bytes")

    @property
    @pulumi.getter(name="storageBytesStatus")
    def storage_bytes_status(self) -> str:
        """
        An indicator whether storageBytes is in a stable state or it is being adjusted as a result of shared storage reallocation. This status can either be UPDATING, meaning the size of the snapshot is being updated, or UP_TO_DATE, meaning the size of the snapshot is up-to-date.
        """
        return pulumi.get(self, "storage_bytes_status")

    @property
    @pulumi.getter(name="storageLocations")
    def storage_locations(self) -> Sequence[str]:
        """
        Cloud Storage bucket storage location of the snapshot (regional or multi-regional).
        """
        return pulumi.get(self, "storage_locations")

    @property
    @pulumi.getter(name="userLicenses")
    def user_licenses(self) -> Sequence[str]:
        """
        A list of user provided licenses represented by a list of URLs to the license resource.
        """
        return pulumi.get(self, "user_licenses")


class AwaitableGetSnapshotResult(GetSnapshotResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSnapshotResult(
            auto_created=self.auto_created,
            chain_name=self.chain_name,
            creation_timestamp=self.creation_timestamp,
            description=self.description,
            disk_size_gb=self.disk_size_gb,
            download_bytes=self.download_bytes,
            guest_flush=self.guest_flush,
            guest_os_features=self.guest_os_features,
            kind=self.kind,
            label_fingerprint=self.label_fingerprint,
            labels=self.labels,
            license_codes=self.license_codes,
            licenses=self.licenses,
            location_hint=self.location_hint,
            name=self.name,
            satisfies_pzs=self.satisfies_pzs,
            self_link=self.self_link,
            self_link_with_id=self.self_link_with_id,
            snapshot_encryption_key=self.snapshot_encryption_key,
            source_disk=self.source_disk,
            source_disk_encryption_key=self.source_disk_encryption_key,
            source_disk_id=self.source_disk_id,
            source_instant_snapshot=self.source_instant_snapshot,
            source_instant_snapshot_id=self.source_instant_snapshot_id,
            status=self.status,
            storage_bytes=self.storage_bytes,
            storage_bytes_status=self.storage_bytes_status,
            storage_locations=self.storage_locations,
            user_licenses=self.user_licenses)


def get_snapshot(project: Optional[str] = None,
                 snapshot: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSnapshotResult:
    """
    Returns the specified Snapshot resource. Gets a list of available snapshots by making a list() request.
    """
    __args__ = dict()
    __args__['project'] = project
    __args__['snapshot'] = snapshot
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:compute/alpha:getSnapshot', __args__, opts=opts, typ=GetSnapshotResult).value

    return AwaitableGetSnapshotResult(
        auto_created=__ret__.auto_created,
        chain_name=__ret__.chain_name,
        creation_timestamp=__ret__.creation_timestamp,
        description=__ret__.description,
        disk_size_gb=__ret__.disk_size_gb,
        download_bytes=__ret__.download_bytes,
        guest_flush=__ret__.guest_flush,
        guest_os_features=__ret__.guest_os_features,
        kind=__ret__.kind,
        label_fingerprint=__ret__.label_fingerprint,
        labels=__ret__.labels,
        license_codes=__ret__.license_codes,
        licenses=__ret__.licenses,
        location_hint=__ret__.location_hint,
        name=__ret__.name,
        satisfies_pzs=__ret__.satisfies_pzs,
        self_link=__ret__.self_link,
        self_link_with_id=__ret__.self_link_with_id,
        snapshot_encryption_key=__ret__.snapshot_encryption_key,
        source_disk=__ret__.source_disk,
        source_disk_encryption_key=__ret__.source_disk_encryption_key,
        source_disk_id=__ret__.source_disk_id,
        source_instant_snapshot=__ret__.source_instant_snapshot,
        source_instant_snapshot_id=__ret__.source_instant_snapshot_id,
        status=__ret__.status,
        storage_bytes=__ret__.storage_bytes,
        storage_bytes_status=__ret__.storage_bytes_status,
        storage_locations=__ret__.storage_locations,
        user_licenses=__ret__.user_licenses)
