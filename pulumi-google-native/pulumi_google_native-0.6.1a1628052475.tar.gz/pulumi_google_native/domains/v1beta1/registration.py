# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['RegistrationArgs', 'Registration']

@pulumi.input_type
class RegistrationArgs:
    def __init__(__self__, *,
                 contact_settings: pulumi.Input['ContactSettingsArgs'],
                 domain_name: pulumi.Input[str],
                 yearly_price: pulumi.Input['MoneyArgs'],
                 contact_notices: Optional[pulumi.Input[Sequence[pulumi.Input['RegistrationContactNoticesItem']]]] = None,
                 dns_settings: Optional[pulumi.Input['DnsSettingsArgs']] = None,
                 domain_notices: Optional[pulumi.Input[Sequence[pulumi.Input['RegistrationDomainNoticesItem']]]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 management_settings: Optional[pulumi.Input['ManagementSettingsArgs']] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 validate_only: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a Registration resource.
        :param pulumi.Input['ContactSettingsArgs'] contact_settings: Settings for contact information linked to the `Registration`. You cannot update these with the `UpdateRegistration` method. To update these settings, use the `ConfigureContactSettings` method.
        :param pulumi.Input[str] domain_name: Immutable. The domain name. Unicode domain names must be expressed in Punycode format.
        :param pulumi.Input['MoneyArgs'] yearly_price: Yearly price to register or renew the domain. The value that should be put here can be obtained from RetrieveRegisterParameters or SearchDomains calls.
        :param pulumi.Input[Sequence[pulumi.Input['RegistrationContactNoticesItem']]] contact_notices: The list of contact notices that the caller acknowledges. The notices needed here depend on the values specified in `registration.contact_settings`.
        :param pulumi.Input['DnsSettingsArgs'] dns_settings: Settings controlling the DNS configuration of the `Registration`. You cannot update these with the `UpdateRegistration` method. To update these settings, use the `ConfigureDnsSettings` method.
        :param pulumi.Input[Sequence[pulumi.Input['RegistrationDomainNoticesItem']]] domain_notices: The list of domain notices that you acknowledge. Call `RetrieveRegisterParameters` to see the notices that need acknowledgement.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Set of labels associated with the `Registration`.
        :param pulumi.Input['ManagementSettingsArgs'] management_settings: Settings for management of the `Registration`, including renewal, billing, and transfer. You cannot update these with the `UpdateRegistration` method. To update these settings, use the `ConfigureManagementSettings` method.
        :param pulumi.Input[bool] validate_only: When true, only validation will be performed, without actually registering the domain. Follows: https://cloud.google.com/apis/design/design_patterns#request_validation
        """
        pulumi.set(__self__, "contact_settings", contact_settings)
        pulumi.set(__self__, "domain_name", domain_name)
        pulumi.set(__self__, "yearly_price", yearly_price)
        if contact_notices is not None:
            pulumi.set(__self__, "contact_notices", contact_notices)
        if dns_settings is not None:
            pulumi.set(__self__, "dns_settings", dns_settings)
        if domain_notices is not None:
            pulumi.set(__self__, "domain_notices", domain_notices)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if management_settings is not None:
            pulumi.set(__self__, "management_settings", management_settings)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if validate_only is not None:
            pulumi.set(__self__, "validate_only", validate_only)

    @property
    @pulumi.getter(name="contactSettings")
    def contact_settings(self) -> pulumi.Input['ContactSettingsArgs']:
        """
        Settings for contact information linked to the `Registration`. You cannot update these with the `UpdateRegistration` method. To update these settings, use the `ConfigureContactSettings` method.
        """
        return pulumi.get(self, "contact_settings")

    @contact_settings.setter
    def contact_settings(self, value: pulumi.Input['ContactSettingsArgs']):
        pulumi.set(self, "contact_settings", value)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[str]:
        """
        Immutable. The domain name. Unicode domain names must be expressed in Punycode format.
        """
        return pulumi.get(self, "domain_name")

    @domain_name.setter
    def domain_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "domain_name", value)

    @property
    @pulumi.getter(name="yearlyPrice")
    def yearly_price(self) -> pulumi.Input['MoneyArgs']:
        """
        Yearly price to register or renew the domain. The value that should be put here can be obtained from RetrieveRegisterParameters or SearchDomains calls.
        """
        return pulumi.get(self, "yearly_price")

    @yearly_price.setter
    def yearly_price(self, value: pulumi.Input['MoneyArgs']):
        pulumi.set(self, "yearly_price", value)

    @property
    @pulumi.getter(name="contactNotices")
    def contact_notices(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RegistrationContactNoticesItem']]]]:
        """
        The list of contact notices that the caller acknowledges. The notices needed here depend on the values specified in `registration.contact_settings`.
        """
        return pulumi.get(self, "contact_notices")

    @contact_notices.setter
    def contact_notices(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RegistrationContactNoticesItem']]]]):
        pulumi.set(self, "contact_notices", value)

    @property
    @pulumi.getter(name="dnsSettings")
    def dns_settings(self) -> Optional[pulumi.Input['DnsSettingsArgs']]:
        """
        Settings controlling the DNS configuration of the `Registration`. You cannot update these with the `UpdateRegistration` method. To update these settings, use the `ConfigureDnsSettings` method.
        """
        return pulumi.get(self, "dns_settings")

    @dns_settings.setter
    def dns_settings(self, value: Optional[pulumi.Input['DnsSettingsArgs']]):
        pulumi.set(self, "dns_settings", value)

    @property
    @pulumi.getter(name="domainNotices")
    def domain_notices(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RegistrationDomainNoticesItem']]]]:
        """
        The list of domain notices that you acknowledge. Call `RetrieveRegisterParameters` to see the notices that need acknowledgement.
        """
        return pulumi.get(self, "domain_notices")

    @domain_notices.setter
    def domain_notices(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RegistrationDomainNoticesItem']]]]):
        pulumi.set(self, "domain_notices", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Set of labels associated with the `Registration`.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="managementSettings")
    def management_settings(self) -> Optional[pulumi.Input['ManagementSettingsArgs']]:
        """
        Settings for management of the `Registration`, including renewal, billing, and transfer. You cannot update these with the `UpdateRegistration` method. To update these settings, use the `ConfigureManagementSettings` method.
        """
        return pulumi.get(self, "management_settings")

    @management_settings.setter
    def management_settings(self, value: Optional[pulumi.Input['ManagementSettingsArgs']]):
        pulumi.set(self, "management_settings", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter(name="validateOnly")
    def validate_only(self) -> Optional[pulumi.Input[bool]]:
        """
        When true, only validation will be performed, without actually registering the domain. Follows: https://cloud.google.com/apis/design/design_patterns#request_validation
        """
        return pulumi.get(self, "validate_only")

    @validate_only.setter
    def validate_only(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "validate_only", value)


class Registration(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 contact_notices: Optional[pulumi.Input[Sequence[pulumi.Input['RegistrationContactNoticesItem']]]] = None,
                 contact_settings: Optional[pulumi.Input[pulumi.InputType['ContactSettingsArgs']]] = None,
                 dns_settings: Optional[pulumi.Input[pulumi.InputType['DnsSettingsArgs']]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 domain_notices: Optional[pulumi.Input[Sequence[pulumi.Input['RegistrationDomainNoticesItem']]]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 management_settings: Optional[pulumi.Input[pulumi.InputType['ManagementSettingsArgs']]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 validate_only: Optional[pulumi.Input[bool]] = None,
                 yearly_price: Optional[pulumi.Input[pulumi.InputType['MoneyArgs']]] = None,
                 __props__=None):
        """
        Registers a new domain name and creates a corresponding `Registration` resource. Call `RetrieveRegisterParameters` first to check availability of the domain name and determine parameters like price that are needed to build a call to this method. A successful call creates a `Registration` resource in state `REGISTRATION_PENDING`, which resolves to `ACTIVE` within 1-2 minutes, indicating that the domain was successfully registered. If the resource ends up in state `REGISTRATION_FAILED`, it indicates that the domain was not registered successfully, and you can safely delete the resource and retry registration.
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input['RegistrationContactNoticesItem']]] contact_notices: The list of contact notices that the caller acknowledges. The notices needed here depend on the values specified in `registration.contact_settings`.
        :param pulumi.Input[pulumi.InputType['ContactSettingsArgs']] contact_settings: Settings for contact information linked to the `Registration`. You cannot update these with the `UpdateRegistration` method. To update these settings, use the `ConfigureContactSettings` method.
        :param pulumi.Input[pulumi.InputType['DnsSettingsArgs']] dns_settings: Settings controlling the DNS configuration of the `Registration`. You cannot update these with the `UpdateRegistration` method. To update these settings, use the `ConfigureDnsSettings` method.
        :param pulumi.Input[str] domain_name: Immutable. The domain name. Unicode domain names must be expressed in Punycode format.
        :param pulumi.Input[Sequence[pulumi.Input['RegistrationDomainNoticesItem']]] domain_notices: The list of domain notices that you acknowledge. Call `RetrieveRegisterParameters` to see the notices that need acknowledgement.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Set of labels associated with the `Registration`.
        :param pulumi.Input[pulumi.InputType['ManagementSettingsArgs']] management_settings: Settings for management of the `Registration`, including renewal, billing, and transfer. You cannot update these with the `UpdateRegistration` method. To update these settings, use the `ConfigureManagementSettings` method.
        :param pulumi.Input[bool] validate_only: When true, only validation will be performed, without actually registering the domain. Follows: https://cloud.google.com/apis/design/design_patterns#request_validation
        :param pulumi.Input[pulumi.InputType['MoneyArgs']] yearly_price: Yearly price to register or renew the domain. The value that should be put here can be obtained from RetrieveRegisterParameters or SearchDomains calls.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RegistrationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Registers a new domain name and creates a corresponding `Registration` resource. Call `RetrieveRegisterParameters` first to check availability of the domain name and determine parameters like price that are needed to build a call to this method. A successful call creates a `Registration` resource in state `REGISTRATION_PENDING`, which resolves to `ACTIVE` within 1-2 minutes, indicating that the domain was successfully registered. If the resource ends up in state `REGISTRATION_FAILED`, it indicates that the domain was not registered successfully, and you can safely delete the resource and retry registration.
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param RegistrationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RegistrationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 contact_notices: Optional[pulumi.Input[Sequence[pulumi.Input['RegistrationContactNoticesItem']]]] = None,
                 contact_settings: Optional[pulumi.Input[pulumi.InputType['ContactSettingsArgs']]] = None,
                 dns_settings: Optional[pulumi.Input[pulumi.InputType['DnsSettingsArgs']]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 domain_notices: Optional[pulumi.Input[Sequence[pulumi.Input['RegistrationDomainNoticesItem']]]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 management_settings: Optional[pulumi.Input[pulumi.InputType['ManagementSettingsArgs']]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 validate_only: Optional[pulumi.Input[bool]] = None,
                 yearly_price: Optional[pulumi.Input[pulumi.InputType['MoneyArgs']]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RegistrationArgs.__new__(RegistrationArgs)

            __props__.__dict__["contact_notices"] = contact_notices
            if contact_settings is None and not opts.urn:
                raise TypeError("Missing required property 'contact_settings'")
            __props__.__dict__["contact_settings"] = contact_settings
            __props__.__dict__["dns_settings"] = dns_settings
            if domain_name is None and not opts.urn:
                raise TypeError("Missing required property 'domain_name'")
            __props__.__dict__["domain_name"] = domain_name
            __props__.__dict__["domain_notices"] = domain_notices
            __props__.__dict__["labels"] = labels
            __props__.__dict__["location"] = location
            __props__.__dict__["management_settings"] = management_settings
            __props__.__dict__["project"] = project
            __props__.__dict__["validate_only"] = validate_only
            if yearly_price is None and not opts.urn:
                raise TypeError("Missing required property 'yearly_price'")
            __props__.__dict__["yearly_price"] = yearly_price
            __props__.__dict__["create_time"] = None
            __props__.__dict__["expire_time"] = None
            __props__.__dict__["issues"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["pending_contact_settings"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["supported_privacy"] = None
        super(Registration, __self__).__init__(
            'google-native:domains/v1beta1:Registration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Registration':
        """
        Get an existing Registration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = RegistrationArgs.__new__(RegistrationArgs)

        __props__.__dict__["contact_settings"] = None
        __props__.__dict__["create_time"] = None
        __props__.__dict__["dns_settings"] = None
        __props__.__dict__["domain_name"] = None
        __props__.__dict__["expire_time"] = None
        __props__.__dict__["issues"] = None
        __props__.__dict__["labels"] = None
        __props__.__dict__["management_settings"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["pending_contact_settings"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["supported_privacy"] = None
        return Registration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="contactSettings")
    def contact_settings(self) -> pulumi.Output['outputs.ContactSettingsResponse']:
        """
        Settings for contact information linked to the `Registration`. You cannot update these with the `UpdateRegistration` method. To update these settings, use the `ConfigureContactSettings` method.
        """
        return pulumi.get(self, "contact_settings")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        The creation timestamp of the `Registration` resource.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="dnsSettings")
    def dns_settings(self) -> pulumi.Output['outputs.DnsSettingsResponse']:
        """
        Settings controlling the DNS configuration of the `Registration`. You cannot update these with the `UpdateRegistration` method. To update these settings, use the `ConfigureDnsSettings` method.
        """
        return pulumi.get(self, "dns_settings")

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[str]:
        """
        Immutable. The domain name. Unicode domain names must be expressed in Punycode format.
        """
        return pulumi.get(self, "domain_name")

    @property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> pulumi.Output[str]:
        """
        The expiration timestamp of the `Registration`.
        """
        return pulumi.get(self, "expire_time")

    @property
    @pulumi.getter
    def issues(self) -> pulumi.Output[Sequence[str]]:
        """
        The set of issues with the `Registration` that require attention.
        """
        return pulumi.get(self, "issues")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Set of labels associated with the `Registration`.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter(name="managementSettings")
    def management_settings(self) -> pulumi.Output['outputs.ManagementSettingsResponse']:
        """
        Settings for management of the `Registration`, including renewal, billing, and transfer. You cannot update these with the `UpdateRegistration` method. To update these settings, use the `ConfigureManagementSettings` method.
        """
        return pulumi.get(self, "management_settings")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the `Registration` resource, in the format `projects/*/locations/*/registrations/`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="pendingContactSettings")
    def pending_contact_settings(self) -> pulumi.Output['outputs.ContactSettingsResponse']:
        """
        Pending contact settings for the `Registration`. Updates to the `contact_settings` field that change its `registrant_contact` or `privacy` fields require email confirmation by the `registrant_contact` before taking effect. This field is set only if there are pending updates to the `contact_settings` that have not yet been confirmed. To confirm the changes, the `registrant_contact` must follow the instructions in the email they receive.
        """
        return pulumi.get(self, "pending_contact_settings")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The state of the `Registration`
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="supportedPrivacy")
    def supported_privacy(self) -> pulumi.Output[Sequence[str]]:
        """
        Set of options for the `contact_settings.privacy` field that this `Registration` supports.
        """
        return pulumi.get(self, "supported_privacy")

