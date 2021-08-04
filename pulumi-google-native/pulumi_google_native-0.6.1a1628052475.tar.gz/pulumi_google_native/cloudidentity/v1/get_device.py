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
    'GetDeviceResult',
    'AwaitableGetDeviceResult',
    'get_device',
]

@pulumi.output_type
class GetDeviceResult:
    def __init__(__self__, android_specific_attributes=None, asset_tag=None, baseband_version=None, bootloader_version=None, brand=None, build_number=None, compromised_state=None, create_time=None, device_type=None, enabled_developer_options=None, enabled_usb_debugging=None, encryption_state=None, imei=None, kernel_version=None, last_sync_time=None, management_state=None, manufacturer=None, meid=None, model=None, name=None, network_operator=None, os_version=None, other_accounts=None, owner_type=None, release_version=None, security_patch_time=None, serial_number=None, wifi_mac_addresses=None):
        if android_specific_attributes and not isinstance(android_specific_attributes, dict):
            raise TypeError("Expected argument 'android_specific_attributes' to be a dict")
        pulumi.set(__self__, "android_specific_attributes", android_specific_attributes)
        if asset_tag and not isinstance(asset_tag, str):
            raise TypeError("Expected argument 'asset_tag' to be a str")
        pulumi.set(__self__, "asset_tag", asset_tag)
        if baseband_version and not isinstance(baseband_version, str):
            raise TypeError("Expected argument 'baseband_version' to be a str")
        pulumi.set(__self__, "baseband_version", baseband_version)
        if bootloader_version and not isinstance(bootloader_version, str):
            raise TypeError("Expected argument 'bootloader_version' to be a str")
        pulumi.set(__self__, "bootloader_version", bootloader_version)
        if brand and not isinstance(brand, str):
            raise TypeError("Expected argument 'brand' to be a str")
        pulumi.set(__self__, "brand", brand)
        if build_number and not isinstance(build_number, str):
            raise TypeError("Expected argument 'build_number' to be a str")
        pulumi.set(__self__, "build_number", build_number)
        if compromised_state and not isinstance(compromised_state, str):
            raise TypeError("Expected argument 'compromised_state' to be a str")
        pulumi.set(__self__, "compromised_state", compromised_state)
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if device_type and not isinstance(device_type, str):
            raise TypeError("Expected argument 'device_type' to be a str")
        pulumi.set(__self__, "device_type", device_type)
        if enabled_developer_options and not isinstance(enabled_developer_options, bool):
            raise TypeError("Expected argument 'enabled_developer_options' to be a bool")
        pulumi.set(__self__, "enabled_developer_options", enabled_developer_options)
        if enabled_usb_debugging and not isinstance(enabled_usb_debugging, bool):
            raise TypeError("Expected argument 'enabled_usb_debugging' to be a bool")
        pulumi.set(__self__, "enabled_usb_debugging", enabled_usb_debugging)
        if encryption_state and not isinstance(encryption_state, str):
            raise TypeError("Expected argument 'encryption_state' to be a str")
        pulumi.set(__self__, "encryption_state", encryption_state)
        if imei and not isinstance(imei, str):
            raise TypeError("Expected argument 'imei' to be a str")
        pulumi.set(__self__, "imei", imei)
        if kernel_version and not isinstance(kernel_version, str):
            raise TypeError("Expected argument 'kernel_version' to be a str")
        pulumi.set(__self__, "kernel_version", kernel_version)
        if last_sync_time and not isinstance(last_sync_time, str):
            raise TypeError("Expected argument 'last_sync_time' to be a str")
        pulumi.set(__self__, "last_sync_time", last_sync_time)
        if management_state and not isinstance(management_state, str):
            raise TypeError("Expected argument 'management_state' to be a str")
        pulumi.set(__self__, "management_state", management_state)
        if manufacturer and not isinstance(manufacturer, str):
            raise TypeError("Expected argument 'manufacturer' to be a str")
        pulumi.set(__self__, "manufacturer", manufacturer)
        if meid and not isinstance(meid, str):
            raise TypeError("Expected argument 'meid' to be a str")
        pulumi.set(__self__, "meid", meid)
        if model and not isinstance(model, str):
            raise TypeError("Expected argument 'model' to be a str")
        pulumi.set(__self__, "model", model)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_operator and not isinstance(network_operator, str):
            raise TypeError("Expected argument 'network_operator' to be a str")
        pulumi.set(__self__, "network_operator", network_operator)
        if os_version and not isinstance(os_version, str):
            raise TypeError("Expected argument 'os_version' to be a str")
        pulumi.set(__self__, "os_version", os_version)
        if other_accounts and not isinstance(other_accounts, list):
            raise TypeError("Expected argument 'other_accounts' to be a list")
        pulumi.set(__self__, "other_accounts", other_accounts)
        if owner_type and not isinstance(owner_type, str):
            raise TypeError("Expected argument 'owner_type' to be a str")
        pulumi.set(__self__, "owner_type", owner_type)
        if release_version and not isinstance(release_version, str):
            raise TypeError("Expected argument 'release_version' to be a str")
        pulumi.set(__self__, "release_version", release_version)
        if security_patch_time and not isinstance(security_patch_time, str):
            raise TypeError("Expected argument 'security_patch_time' to be a str")
        pulumi.set(__self__, "security_patch_time", security_patch_time)
        if serial_number and not isinstance(serial_number, str):
            raise TypeError("Expected argument 'serial_number' to be a str")
        pulumi.set(__self__, "serial_number", serial_number)
        if wifi_mac_addresses and not isinstance(wifi_mac_addresses, list):
            raise TypeError("Expected argument 'wifi_mac_addresses' to be a list")
        pulumi.set(__self__, "wifi_mac_addresses", wifi_mac_addresses)

    @property
    @pulumi.getter(name="androidSpecificAttributes")
    def android_specific_attributes(self) -> 'outputs.GoogleAppsCloudidentityDevicesV1AndroidAttributesResponse':
        """
        Attributes specific to Android devices.
        """
        return pulumi.get(self, "android_specific_attributes")

    @property
    @pulumi.getter(name="assetTag")
    def asset_tag(self) -> str:
        """
        Asset tag of the device.
        """
        return pulumi.get(self, "asset_tag")

    @property
    @pulumi.getter(name="basebandVersion")
    def baseband_version(self) -> str:
        """
        Baseband version of the device.
        """
        return pulumi.get(self, "baseband_version")

    @property
    @pulumi.getter(name="bootloaderVersion")
    def bootloader_version(self) -> str:
        """
        Device bootloader version. Example: 0.6.7.
        """
        return pulumi.get(self, "bootloader_version")

    @property
    @pulumi.getter
    def brand(self) -> str:
        """
        Device brand. Example: Samsung.
        """
        return pulumi.get(self, "brand")

    @property
    @pulumi.getter(name="buildNumber")
    def build_number(self) -> str:
        """
        Build number of the device.
        """
        return pulumi.get(self, "build_number")

    @property
    @pulumi.getter(name="compromisedState")
    def compromised_state(self) -> str:
        """
        Represents whether the Device is compromised.
        """
        return pulumi.get(self, "compromised_state")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        When the Company-Owned device was imported. This field is empty for BYOD devices.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="deviceType")
    def device_type(self) -> str:
        """
        Type of device.
        """
        return pulumi.get(self, "device_type")

    @property
    @pulumi.getter(name="enabledDeveloperOptions")
    def enabled_developer_options(self) -> bool:
        """
        Whether developer options is enabled on device.
        """
        return pulumi.get(self, "enabled_developer_options")

    @property
    @pulumi.getter(name="enabledUsbDebugging")
    def enabled_usb_debugging(self) -> bool:
        """
        Whether USB debugging is enabled on device.
        """
        return pulumi.get(self, "enabled_usb_debugging")

    @property
    @pulumi.getter(name="encryptionState")
    def encryption_state(self) -> str:
        """
        Device encryption state.
        """
        return pulumi.get(self, "encryption_state")

    @property
    @pulumi.getter
    def imei(self) -> str:
        """
        IMEI number of device if GSM device; empty otherwise.
        """
        return pulumi.get(self, "imei")

    @property
    @pulumi.getter(name="kernelVersion")
    def kernel_version(self) -> str:
        """
        Kernel version of the device.
        """
        return pulumi.get(self, "kernel_version")

    @property
    @pulumi.getter(name="lastSyncTime")
    def last_sync_time(self) -> str:
        """
        Most recent time when device synced with this service.
        """
        return pulumi.get(self, "last_sync_time")

    @property
    @pulumi.getter(name="managementState")
    def management_state(self) -> str:
        """
        Management state of the device
        """
        return pulumi.get(self, "management_state")

    @property
    @pulumi.getter
    def manufacturer(self) -> str:
        """
        Device manufacturer. Example: Motorola.
        """
        return pulumi.get(self, "manufacturer")

    @property
    @pulumi.getter
    def meid(self) -> str:
        """
        MEID number of device if CDMA device; empty otherwise.
        """
        return pulumi.get(self, "meid")

    @property
    @pulumi.getter
    def model(self) -> str:
        """
        Model name of device. Example: Pixel 3.
        """
        return pulumi.get(self, "model")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        [Resource name](https://cloud.google.com/apis/design/resource_names) of the Device in format: `devices/{device_id}`, where device_id is the unique id assigned to the Device.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkOperator")
    def network_operator(self) -> str:
        """
        Mobile or network operator of device, if available.
        """
        return pulumi.get(self, "network_operator")

    @property
    @pulumi.getter(name="osVersion")
    def os_version(self) -> str:
        """
        OS version of the device. Example: Android 8.1.0.
        """
        return pulumi.get(self, "os_version")

    @property
    @pulumi.getter(name="otherAccounts")
    def other_accounts(self) -> Sequence[str]:
        """
        Domain name for Google accounts on device. Type for other accounts on device. On Android, will only be populated if |ownership_privilege| is |PROFILE_OWNER| or |DEVICE_OWNER|. Does not include the account signed in to the device policy app if that account's domain has only one account. Examples: "com.example", "xyz.com".
        """
        return pulumi.get(self, "other_accounts")

    @property
    @pulumi.getter(name="ownerType")
    def owner_type(self) -> str:
        """
        Whether the device is owned by the company or an individual
        """
        return pulumi.get(self, "owner_type")

    @property
    @pulumi.getter(name="releaseVersion")
    def release_version(self) -> str:
        """
        OS release version. Example: 6.0.
        """
        return pulumi.get(self, "release_version")

    @property
    @pulumi.getter(name="securityPatchTime")
    def security_patch_time(self) -> str:
        """
        OS security patch update time on device.
        """
        return pulumi.get(self, "security_patch_time")

    @property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> str:
        """
        Serial Number of device. Example: HT82V1A01076.
        """
        return pulumi.get(self, "serial_number")

    @property
    @pulumi.getter(name="wifiMacAddresses")
    def wifi_mac_addresses(self) -> Sequence[str]:
        """
        WiFi MAC addresses of device.
        """
        return pulumi.get(self, "wifi_mac_addresses")


class AwaitableGetDeviceResult(GetDeviceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDeviceResult(
            android_specific_attributes=self.android_specific_attributes,
            asset_tag=self.asset_tag,
            baseband_version=self.baseband_version,
            bootloader_version=self.bootloader_version,
            brand=self.brand,
            build_number=self.build_number,
            compromised_state=self.compromised_state,
            create_time=self.create_time,
            device_type=self.device_type,
            enabled_developer_options=self.enabled_developer_options,
            enabled_usb_debugging=self.enabled_usb_debugging,
            encryption_state=self.encryption_state,
            imei=self.imei,
            kernel_version=self.kernel_version,
            last_sync_time=self.last_sync_time,
            management_state=self.management_state,
            manufacturer=self.manufacturer,
            meid=self.meid,
            model=self.model,
            name=self.name,
            network_operator=self.network_operator,
            os_version=self.os_version,
            other_accounts=self.other_accounts,
            owner_type=self.owner_type,
            release_version=self.release_version,
            security_patch_time=self.security_patch_time,
            serial_number=self.serial_number,
            wifi_mac_addresses=self.wifi_mac_addresses)


def get_device(customer: Optional[str] = None,
               device_id: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDeviceResult:
    """
    Retrieves the specified device.
    """
    __args__ = dict()
    __args__['customer'] = customer
    __args__['deviceId'] = device_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:cloudidentity/v1:getDevice', __args__, opts=opts, typ=GetDeviceResult).value

    return AwaitableGetDeviceResult(
        android_specific_attributes=__ret__.android_specific_attributes,
        asset_tag=__ret__.asset_tag,
        baseband_version=__ret__.baseband_version,
        bootloader_version=__ret__.bootloader_version,
        brand=__ret__.brand,
        build_number=__ret__.build_number,
        compromised_state=__ret__.compromised_state,
        create_time=__ret__.create_time,
        device_type=__ret__.device_type,
        enabled_developer_options=__ret__.enabled_developer_options,
        enabled_usb_debugging=__ret__.enabled_usb_debugging,
        encryption_state=__ret__.encryption_state,
        imei=__ret__.imei,
        kernel_version=__ret__.kernel_version,
        last_sync_time=__ret__.last_sync_time,
        management_state=__ret__.management_state,
        manufacturer=__ret__.manufacturer,
        meid=__ret__.meid,
        model=__ret__.model,
        name=__ret__.name,
        network_operator=__ret__.network_operator,
        os_version=__ret__.os_version,
        other_accounts=__ret__.other_accounts,
        owner_type=__ret__.owner_type,
        release_version=__ret__.release_version,
        security_patch_time=__ret__.security_patch_time,
        serial_number=__ret__.serial_number,
        wifi_mac_addresses=__ret__.wifi_mac_addresses)
