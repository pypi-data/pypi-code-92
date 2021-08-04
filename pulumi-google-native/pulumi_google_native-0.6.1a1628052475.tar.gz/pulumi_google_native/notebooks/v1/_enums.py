# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AcceleratorConfigType',
    'InstanceBootDiskType',
    'InstanceDataDiskType',
    'InstanceDiskEncryption',
    'InstanceNicType',
    'LocalDiskInitializeParamsDiskType',
    'ReservationAffinityConsumeReservationType',
    'RuntimeAcceleratorConfigType',
    'RuntimeAccessConfigAccessType',
    'ScheduleState',
    'SchedulerAcceleratorConfigType',
    'UpgradeHistoryEntryAction',
    'UpgradeHistoryEntryState',
    'VirtualMachineConfigNicType',
]


class AcceleratorConfigType(str, Enum):
    """
    Type of this accelerator.
    """
    ACCELERATOR_TYPE_UNSPECIFIED = "ACCELERATOR_TYPE_UNSPECIFIED"
    """Accelerator type is not specified."""
    NVIDIA_TESLA_K80 = "NVIDIA_TESLA_K80"
    """Accelerator type is Nvidia Tesla K80."""
    NVIDIA_TESLA_P100 = "NVIDIA_TESLA_P100"
    """Accelerator type is Nvidia Tesla P100."""
    NVIDIA_TESLA_V100 = "NVIDIA_TESLA_V100"
    """Accelerator type is Nvidia Tesla V100."""
    NVIDIA_TESLA_P4 = "NVIDIA_TESLA_P4"
    """Accelerator type is Nvidia Tesla P4."""
    NVIDIA_TESLA_T4 = "NVIDIA_TESLA_T4"
    """Accelerator type is Nvidia Tesla T4."""
    NVIDIA_TESLA_A100 = "NVIDIA_TESLA_A100"
    """Accelerator type is Nvidia Tesla A100."""
    NVIDIA_TESLA_T4_VWS = "NVIDIA_TESLA_T4_VWS"
    """Accelerator type is NVIDIA Tesla T4 Virtual Workstations."""
    NVIDIA_TESLA_P100_VWS = "NVIDIA_TESLA_P100_VWS"
    """Accelerator type is NVIDIA Tesla P100 Virtual Workstations."""
    NVIDIA_TESLA_P4_VWS = "NVIDIA_TESLA_P4_VWS"
    """Accelerator type is NVIDIA Tesla P4 Virtual Workstations."""
    TPU_V2 = "TPU_V2"
    """(Coming soon) Accelerator type is TPU V2."""
    TPU_V3 = "TPU_V3"
    """(Coming soon) Accelerator type is TPU V3."""


class InstanceBootDiskType(str, Enum):
    """
    Input only. The type of the boot disk attached to this instance, defaults to standard persistent disk (`PD_STANDARD`).
    """
    DISK_TYPE_UNSPECIFIED = "DISK_TYPE_UNSPECIFIED"
    """Disk type not set."""
    PD_STANDARD = "PD_STANDARD"
    """Standard persistent disk type."""
    PD_SSD = "PD_SSD"
    """SSD persistent disk type."""
    PD_BALANCED = "PD_BALANCED"
    """Balanced persistent disk type."""


class InstanceDataDiskType(str, Enum):
    """
    Input only. The type of the data disk attached to this instance, defaults to standard persistent disk (`PD_STANDARD`).
    """
    DISK_TYPE_UNSPECIFIED = "DISK_TYPE_UNSPECIFIED"
    """Disk type not set."""
    PD_STANDARD = "PD_STANDARD"
    """Standard persistent disk type."""
    PD_SSD = "PD_SSD"
    """SSD persistent disk type."""
    PD_BALANCED = "PD_BALANCED"
    """Balanced persistent disk type."""


class InstanceDiskEncryption(str, Enum):
    """
    Input only. Disk encryption method used on the boot and data disks, defaults to GMEK.
    """
    DISK_ENCRYPTION_UNSPECIFIED = "DISK_ENCRYPTION_UNSPECIFIED"
    """Disk encryption is not specified."""
    GMEK = "GMEK"
    """Use Google managed encryption keys to encrypt the boot disk."""
    CMEK = "CMEK"
    """Use customer managed encryption keys to encrypt the boot disk."""


class InstanceNicType(str, Enum):
    """
    Optional. The type of vNIC to be used on this interface. This may be gVNIC or VirtioNet.
    """
    UNSPECIFIED_NIC_TYPE = "UNSPECIFIED_NIC_TYPE"
    """No type specified."""
    VIRTIO_NET = "VIRTIO_NET"
    """VIRTIO"""
    GVNIC = "GVNIC"
    """GVNIC"""


class LocalDiskInitializeParamsDiskType(str, Enum):
    """
    Input only. The type of the boot disk attached to this instance, defaults to standard persistent disk (`PD_STANDARD`).
    """
    DISK_TYPE_UNSPECIFIED = "DISK_TYPE_UNSPECIFIED"
    """Disk type not set."""
    PD_STANDARD = "PD_STANDARD"
    """Standard persistent disk type."""
    PD_SSD = "PD_SSD"
    """SSD persistent disk type."""
    PD_BALANCED = "PD_BALANCED"
    """Balanced persistent disk type."""


class ReservationAffinityConsumeReservationType(str, Enum):
    """
    Optional. Type of reservation to consume
    """
    TYPE_UNSPECIFIED = "TYPE_UNSPECIFIED"
    """Default type."""
    NO_RESERVATION = "NO_RESERVATION"
    """Do not consume from any allocated capacity."""
    ANY_RESERVATION = "ANY_RESERVATION"
    """Consume any reservation available."""
    SPECIFIC_RESERVATION = "SPECIFIC_RESERVATION"
    """Must consume from a specific reservation. Must specify key value fields for specifying the reservations."""


class RuntimeAcceleratorConfigType(str, Enum):
    """
    Accelerator model.
    """
    ACCELERATOR_TYPE_UNSPECIFIED = "ACCELERATOR_TYPE_UNSPECIFIED"
    """Accelerator type is not specified."""
    NVIDIA_TESLA_K80 = "NVIDIA_TESLA_K80"
    """Accelerator type is Nvidia Tesla K80."""
    NVIDIA_TESLA_P100 = "NVIDIA_TESLA_P100"
    """Accelerator type is Nvidia Tesla P100."""
    NVIDIA_TESLA_V100 = "NVIDIA_TESLA_V100"
    """Accelerator type is Nvidia Tesla V100."""
    NVIDIA_TESLA_P4 = "NVIDIA_TESLA_P4"
    """Accelerator type is Nvidia Tesla P4."""
    NVIDIA_TESLA_T4 = "NVIDIA_TESLA_T4"
    """Accelerator type is Nvidia Tesla T4."""
    NVIDIA_TESLA_A100 = "NVIDIA_TESLA_A100"
    """Accelerator type is Nvidia Tesla A100."""
    TPU_V2 = "TPU_V2"
    """(Coming soon) Accelerator type is TPU V2."""
    TPU_V3 = "TPU_V3"
    """(Coming soon) Accelerator type is TPU V3."""
    NVIDIA_TESLA_T4_VWS = "NVIDIA_TESLA_T4_VWS"
    """Accelerator type is NVIDIA Tesla T4 Virtual Workstations."""
    NVIDIA_TESLA_P100_VWS = "NVIDIA_TESLA_P100_VWS"
    """Accelerator type is NVIDIA Tesla P100 Virtual Workstations."""
    NVIDIA_TESLA_P4_VWS = "NVIDIA_TESLA_P4_VWS"
    """Accelerator type is NVIDIA Tesla P4 Virtual Workstations."""


class RuntimeAccessConfigAccessType(str, Enum):
    """
    The type of access mode this instance.
    """
    RUNTIME_ACCESS_TYPE_UNSPECIFIED = "RUNTIME_ACCESS_TYPE_UNSPECIFIED"
    """Unspecified access."""
    SINGLE_USER = "SINGLE_USER"
    """Single user login."""


class ScheduleState(str, Enum):
    STATE_UNSPECIFIED = "STATE_UNSPECIFIED"
    """Unspecified state."""
    ENABLED = "ENABLED"
    """The job is executing normally."""
    PAUSED = "PAUSED"
    """The job is paused by the user. It will not execute. A user can intentionally pause the job using PauseJobRequest."""
    DISABLED = "DISABLED"
    """The job is disabled by the system due to error. The user cannot directly set a job to be disabled."""
    UPDATE_FAILED = "UPDATE_FAILED"
    """The job state resulting from a failed CloudScheduler.UpdateJob operation. To recover a job from this state, retry CloudScheduler.UpdateJob until a successful response is received."""
    INITIALIZING = "INITIALIZING"
    """The schedule resource is being created."""
    DELETING = "DELETING"
    """The schedule resource is being deleted."""


class SchedulerAcceleratorConfigType(str, Enum):
    """
    Type of this accelerator.
    """
    SCHEDULER_ACCELERATOR_TYPE_UNSPECIFIED = "SCHEDULER_ACCELERATOR_TYPE_UNSPECIFIED"
    """Unspecified accelerator type. Default to no GPU."""
    NVIDIA_TESLA_K80 = "NVIDIA_TESLA_K80"
    """Nvidia Tesla K80 GPU."""
    NVIDIA_TESLA_P100 = "NVIDIA_TESLA_P100"
    """Nvidia Tesla P100 GPU."""
    NVIDIA_TESLA_V100 = "NVIDIA_TESLA_V100"
    """Nvidia Tesla V100 GPU."""
    NVIDIA_TESLA_P4 = "NVIDIA_TESLA_P4"
    """Nvidia Tesla P4 GPU."""
    NVIDIA_TESLA_T4 = "NVIDIA_TESLA_T4"
    """Nvidia Tesla T4 GPU."""
    TPU_V2 = "TPU_V2"
    """TPU v2."""
    TPU_V3 = "TPU_V3"
    """TPU v3."""


class UpgradeHistoryEntryAction(str, Enum):
    """
    Action. Rolloback or Upgrade.
    """
    ACTION_UNSPECIFIED = "ACTION_UNSPECIFIED"
    """Operation is not specified."""
    UPGRADE = "UPGRADE"
    """Upgrade."""
    ROLLBACK = "ROLLBACK"
    """Rollback."""


class UpgradeHistoryEntryState(str, Enum):
    """
    The state of this instance upgrade history entry.
    """
    STATE_UNSPECIFIED = "STATE_UNSPECIFIED"
    """State is not specified."""
    STARTED = "STARTED"
    """The instance upgrade is started."""
    SUCCEEDED = "SUCCEEDED"
    """The instance upgrade is succeeded."""
    FAILED = "FAILED"
    """The instance upgrade is failed."""


class VirtualMachineConfigNicType(str, Enum):
    """
    Optional. The type of vNIC to be used on this interface. This may be gVNIC or VirtioNet.
    """
    UNSPECIFIED_NIC_TYPE = "UNSPECIFIED_NIC_TYPE"
    """No type specified."""
    VIRTIO_NET = "VIRTIO_NET"
    """VIRTIO"""
    GVNIC = "GVNIC"
    """GVNIC"""
