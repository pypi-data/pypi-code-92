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

__all__ = ['WorkloadArgs', 'Workload']

@pulumi.input_type
class WorkloadArgs:
    def __init__(__self__, *,
                 billing_account: pulumi.Input[str],
                 compliance_regime: pulumi.Input['WorkloadComplianceRegime'],
                 display_name: pulumi.Input[str],
                 organization_id: pulumi.Input[str],
                 etag: Optional[pulumi.Input[str]] = None,
                 external_id: Optional[pulumi.Input[str]] = None,
                 kms_settings: Optional[pulumi.Input['GoogleCloudAssuredworkloadsV1WorkloadKMSSettingsArgs']] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 provisioned_resources_parent: Optional[pulumi.Input[str]] = None,
                 resource_settings: Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudAssuredworkloadsV1WorkloadResourceSettingsArgs']]]] = None):
        """
        The set of arguments for constructing a Workload resource.
        :param pulumi.Input[str] billing_account: Input only. The billing account used for the resources which are direct children of workload. This billing account is initially associated with the resources created as part of Workload creation. After the initial creation of these resources, the customer can change the assigned billing account. The resource name has the form `billingAccounts/{billing_account_id}`. For example, `billingAccounts/012345-567890-ABCDEF`.
        :param pulumi.Input['WorkloadComplianceRegime'] compliance_regime: Immutable. Compliance Regime associated with this workload.
        :param pulumi.Input[str] display_name: The user-assigned display name of the Workload. When present it must be between 4 to 30 characters. Allowed characters are: lowercase and uppercase letters, numbers, hyphen, and spaces. Example: My Workload
        :param pulumi.Input[str] etag: Optional. ETag of the workload, it is calculated on the basis of the Workload contents. It will be used in Update & Delete operations.
        :param pulumi.Input['GoogleCloudAssuredworkloadsV1WorkloadKMSSettingsArgs'] kms_settings: Input only. Settings used to create a CMEK crypto key. When set a project with a KMS CMEK key is provisioned. This field is mandatory for a subset of Compliance Regimes.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Optional. Labels applied to the workload.
        :param pulumi.Input[str] name: Optional. The resource name of the workload. Format: organizations/{organization}/locations/{location}/workloads/{workload} Read-only.
        :param pulumi.Input[str] provisioned_resources_parent: Input only. The parent resource for the resources managed by this Assured Workload. May be either an organization or a folder. Must be the same or a child of the Workload parent. If not specified all resources are created under the Workload parent. Formats: folders/{folder_id} organizations/{organization_id}
        :param pulumi.Input[Sequence[pulumi.Input['GoogleCloudAssuredworkloadsV1WorkloadResourceSettingsArgs']]] resource_settings: Input only. Resource properties that are used to customize workload resources. These properties (such as custom project id) will be used to create workload resources if possible. This field is optional.
        """
        pulumi.set(__self__, "billing_account", billing_account)
        pulumi.set(__self__, "compliance_regime", compliance_regime)
        pulumi.set(__self__, "display_name", display_name)
        pulumi.set(__self__, "organization_id", organization_id)
        if etag is not None:
            pulumi.set(__self__, "etag", etag)
        if external_id is not None:
            pulumi.set(__self__, "external_id", external_id)
        if kms_settings is not None:
            pulumi.set(__self__, "kms_settings", kms_settings)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if provisioned_resources_parent is not None:
            pulumi.set(__self__, "provisioned_resources_parent", provisioned_resources_parent)
        if resource_settings is not None:
            pulumi.set(__self__, "resource_settings", resource_settings)

    @property
    @pulumi.getter(name="billingAccount")
    def billing_account(self) -> pulumi.Input[str]:
        """
        Input only. The billing account used for the resources which are direct children of workload. This billing account is initially associated with the resources created as part of Workload creation. After the initial creation of these resources, the customer can change the assigned billing account. The resource name has the form `billingAccounts/{billing_account_id}`. For example, `billingAccounts/012345-567890-ABCDEF`.
        """
        return pulumi.get(self, "billing_account")

    @billing_account.setter
    def billing_account(self, value: pulumi.Input[str]):
        pulumi.set(self, "billing_account", value)

    @property
    @pulumi.getter(name="complianceRegime")
    def compliance_regime(self) -> pulumi.Input['WorkloadComplianceRegime']:
        """
        Immutable. Compliance Regime associated with this workload.
        """
        return pulumi.get(self, "compliance_regime")

    @compliance_regime.setter
    def compliance_regime(self, value: pulumi.Input['WorkloadComplianceRegime']):
        pulumi.set(self, "compliance_regime", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[str]:
        """
        The user-assigned display name of the Workload. When present it must be between 4 to 30 characters. Allowed characters are: lowercase and uppercase letters, numbers, hyphen, and spaces. Example: My Workload
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "organization_id")

    @organization_id.setter
    def organization_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "organization_id", value)

    @property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. ETag of the workload, it is calculated on the basis of the Workload contents. It will be used in Update & Delete operations.
        """
        return pulumi.get(self, "etag")

    @etag.setter
    def etag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "etag", value)

    @property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "external_id")

    @external_id.setter
    def external_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "external_id", value)

    @property
    @pulumi.getter(name="kmsSettings")
    def kms_settings(self) -> Optional[pulumi.Input['GoogleCloudAssuredworkloadsV1WorkloadKMSSettingsArgs']]:
        """
        Input only. Settings used to create a CMEK crypto key. When set a project with a KMS CMEK key is provisioned. This field is mandatory for a subset of Compliance Regimes.
        """
        return pulumi.get(self, "kms_settings")

    @kms_settings.setter
    def kms_settings(self, value: Optional[pulumi.Input['GoogleCloudAssuredworkloadsV1WorkloadKMSSettingsArgs']]):
        pulumi.set(self, "kms_settings", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Optional. Labels applied to the workload.
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
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. The resource name of the workload. Format: organizations/{organization}/locations/{location}/workloads/{workload} Read-only.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="provisionedResourcesParent")
    def provisioned_resources_parent(self) -> Optional[pulumi.Input[str]]:
        """
        Input only. The parent resource for the resources managed by this Assured Workload. May be either an organization or a folder. Must be the same or a child of the Workload parent. If not specified all resources are created under the Workload parent. Formats: folders/{folder_id} organizations/{organization_id}
        """
        return pulumi.get(self, "provisioned_resources_parent")

    @provisioned_resources_parent.setter
    def provisioned_resources_parent(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "provisioned_resources_parent", value)

    @property
    @pulumi.getter(name="resourceSettings")
    def resource_settings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudAssuredworkloadsV1WorkloadResourceSettingsArgs']]]]:
        """
        Input only. Resource properties that are used to customize workload resources. These properties (such as custom project id) will be used to create workload resources if possible. This field is optional.
        """
        return pulumi.get(self, "resource_settings")

    @resource_settings.setter
    def resource_settings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudAssuredworkloadsV1WorkloadResourceSettingsArgs']]]]):
        pulumi.set(self, "resource_settings", value)


class Workload(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 billing_account: Optional[pulumi.Input[str]] = None,
                 compliance_regime: Optional[pulumi.Input['WorkloadComplianceRegime']] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 external_id: Optional[pulumi.Input[str]] = None,
                 kms_settings: Optional[pulumi.Input[pulumi.InputType['GoogleCloudAssuredworkloadsV1WorkloadKMSSettingsArgs']]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organization_id: Optional[pulumi.Input[str]] = None,
                 provisioned_resources_parent: Optional[pulumi.Input[str]] = None,
                 resource_settings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudAssuredworkloadsV1WorkloadResourceSettingsArgs']]]]] = None,
                 __props__=None):
        """
        Creates Assured Workload.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] billing_account: Input only. The billing account used for the resources which are direct children of workload. This billing account is initially associated with the resources created as part of Workload creation. After the initial creation of these resources, the customer can change the assigned billing account. The resource name has the form `billingAccounts/{billing_account_id}`. For example, `billingAccounts/012345-567890-ABCDEF`.
        :param pulumi.Input['WorkloadComplianceRegime'] compliance_regime: Immutable. Compliance Regime associated with this workload.
        :param pulumi.Input[str] display_name: The user-assigned display name of the Workload. When present it must be between 4 to 30 characters. Allowed characters are: lowercase and uppercase letters, numbers, hyphen, and spaces. Example: My Workload
        :param pulumi.Input[str] etag: Optional. ETag of the workload, it is calculated on the basis of the Workload contents. It will be used in Update & Delete operations.
        :param pulumi.Input[pulumi.InputType['GoogleCloudAssuredworkloadsV1WorkloadKMSSettingsArgs']] kms_settings: Input only. Settings used to create a CMEK crypto key. When set a project with a KMS CMEK key is provisioned. This field is mandatory for a subset of Compliance Regimes.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Optional. Labels applied to the workload.
        :param pulumi.Input[str] name: Optional. The resource name of the workload. Format: organizations/{organization}/locations/{location}/workloads/{workload} Read-only.
        :param pulumi.Input[str] provisioned_resources_parent: Input only. The parent resource for the resources managed by this Assured Workload. May be either an organization or a folder. Must be the same or a child of the Workload parent. If not specified all resources are created under the Workload parent. Formats: folders/{folder_id} organizations/{organization_id}
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudAssuredworkloadsV1WorkloadResourceSettingsArgs']]]] resource_settings: Input only. Resource properties that are used to customize workload resources. These properties (such as custom project id) will be used to create workload resources if possible. This field is optional.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WorkloadArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates Assured Workload.

        :param str resource_name: The name of the resource.
        :param WorkloadArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WorkloadArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 billing_account: Optional[pulumi.Input[str]] = None,
                 compliance_regime: Optional[pulumi.Input['WorkloadComplianceRegime']] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 external_id: Optional[pulumi.Input[str]] = None,
                 kms_settings: Optional[pulumi.Input[pulumi.InputType['GoogleCloudAssuredworkloadsV1WorkloadKMSSettingsArgs']]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organization_id: Optional[pulumi.Input[str]] = None,
                 provisioned_resources_parent: Optional[pulumi.Input[str]] = None,
                 resource_settings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudAssuredworkloadsV1WorkloadResourceSettingsArgs']]]]] = None,
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
            __props__ = WorkloadArgs.__new__(WorkloadArgs)

            if billing_account is None and not opts.urn:
                raise TypeError("Missing required property 'billing_account'")
            __props__.__dict__["billing_account"] = billing_account
            if compliance_regime is None and not opts.urn:
                raise TypeError("Missing required property 'compliance_regime'")
            __props__.__dict__["compliance_regime"] = compliance_regime
            if display_name is None and not opts.urn:
                raise TypeError("Missing required property 'display_name'")
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["etag"] = etag
            __props__.__dict__["external_id"] = external_id
            __props__.__dict__["kms_settings"] = kms_settings
            __props__.__dict__["labels"] = labels
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            if organization_id is None and not opts.urn:
                raise TypeError("Missing required property 'organization_id'")
            __props__.__dict__["organization_id"] = organization_id
            __props__.__dict__["provisioned_resources_parent"] = provisioned_resources_parent
            __props__.__dict__["resource_settings"] = resource_settings
            __props__.__dict__["create_time"] = None
            __props__.__dict__["resources"] = None
        super(Workload, __self__).__init__(
            'google-native:assuredworkloads/v1:Workload',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Workload':
        """
        Get an existing Workload resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = WorkloadArgs.__new__(WorkloadArgs)

        __props__.__dict__["billing_account"] = None
        __props__.__dict__["compliance_regime"] = None
        __props__.__dict__["create_time"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["kms_settings"] = None
        __props__.__dict__["labels"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioned_resources_parent"] = None
        __props__.__dict__["resource_settings"] = None
        __props__.__dict__["resources"] = None
        return Workload(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="billingAccount")
    def billing_account(self) -> pulumi.Output[str]:
        """
        Input only. The billing account used for the resources which are direct children of workload. This billing account is initially associated with the resources created as part of Workload creation. After the initial creation of these resources, the customer can change the assigned billing account. The resource name has the form `billingAccounts/{billing_account_id}`. For example, `billingAccounts/012345-567890-ABCDEF`.
        """
        return pulumi.get(self, "billing_account")

    @property
    @pulumi.getter(name="complianceRegime")
    def compliance_regime(self) -> pulumi.Output[str]:
        """
        Immutable. Compliance Regime associated with this workload.
        """
        return pulumi.get(self, "compliance_regime")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        Immutable. The Workload creation timestamp.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        The user-assigned display name of the Workload. When present it must be between 4 to 30 characters. Allowed characters are: lowercase and uppercase letters, numbers, hyphen, and spaces. Example: My Workload
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        Optional. ETag of the workload, it is calculated on the basis of the Workload contents. It will be used in Update & Delete operations.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="kmsSettings")
    def kms_settings(self) -> pulumi.Output['outputs.GoogleCloudAssuredworkloadsV1WorkloadKMSSettingsResponse']:
        """
        Input only. Settings used to create a CMEK crypto key. When set a project with a KMS CMEK key is provisioned. This field is mandatory for a subset of Compliance Regimes.
        """
        return pulumi.get(self, "kms_settings")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Optional. Labels applied to the workload.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Optional. The resource name of the workload. Format: organizations/{organization}/locations/{location}/workloads/{workload} Read-only.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisionedResourcesParent")
    def provisioned_resources_parent(self) -> pulumi.Output[str]:
        """
        Input only. The parent resource for the resources managed by this Assured Workload. May be either an organization or a folder. Must be the same or a child of the Workload parent. If not specified all resources are created under the Workload parent. Formats: folders/{folder_id} organizations/{organization_id}
        """
        return pulumi.get(self, "provisioned_resources_parent")

    @property
    @pulumi.getter(name="resourceSettings")
    def resource_settings(self) -> pulumi.Output[Sequence['outputs.GoogleCloudAssuredworkloadsV1WorkloadResourceSettingsResponse']]:
        """
        Input only. Resource properties that are used to customize workload resources. These properties (such as custom project id) will be used to create workload resources if possible. This field is optional.
        """
        return pulumi.get(self, "resource_settings")

    @property
    @pulumi.getter
    def resources(self) -> pulumi.Output[Sequence['outputs.GoogleCloudAssuredworkloadsV1WorkloadResourceInfoResponse']]:
        """
        The resources associated with this workload. These resources will be created when creating the workload. If any of the projects already exist, the workload creation will fail. Always read only.
        """
        return pulumi.get(self, "resources")

