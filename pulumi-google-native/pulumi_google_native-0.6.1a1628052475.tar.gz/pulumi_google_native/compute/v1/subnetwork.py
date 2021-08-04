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

__all__ = ['SubnetworkArgs', 'Subnetwork']

@pulumi.input_type
class SubnetworkArgs:
    def __init__(__self__, *,
                 region: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 enable_flow_logs: Optional[pulumi.Input[bool]] = None,
                 ip_cidr_range: Optional[pulumi.Input[str]] = None,
                 ipv6_access_type: Optional[pulumi.Input['SubnetworkIpv6AccessType']] = None,
                 log_config: Optional[pulumi.Input['SubnetworkLogConfigArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network: Optional[pulumi.Input[str]] = None,
                 private_ip_google_access: Optional[pulumi.Input[bool]] = None,
                 private_ipv6_google_access: Optional[pulumi.Input['SubnetworkPrivateIpv6GoogleAccess']] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 purpose: Optional[pulumi.Input['SubnetworkPurpose']] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input['SubnetworkRole']] = None,
                 secondary_ip_ranges: Optional[pulumi.Input[Sequence[pulumi.Input['SubnetworkSecondaryRangeArgs']]]] = None,
                 stack_type: Optional[pulumi.Input['SubnetworkStackType']] = None):
        """
        The set of arguments for constructing a Subnetwork resource.
        :param pulumi.Input[str] region: URL of the region where the Subnetwork resides. This field can be set only at resource creation time.
        :param pulumi.Input[str] description: An optional description of this resource. Provide this property when you create the resource. This field can be set only at resource creation time.
        :param pulumi.Input[bool] enable_flow_logs: Whether to enable flow logging for this subnetwork. If this field is not explicitly set, it will not appear in get listings. If not set the default behavior is to disable flow logging. This field isn't supported with the purpose field set to INTERNAL_HTTPS_LOAD_BALANCER.
        :param pulumi.Input[str] ip_cidr_range: The range of internal addresses that are owned by this subnetwork. Provide this property when you create the subnetwork. For example, 10.0.0.0/8 or 100.64.0.0/10. Ranges must be unique and non-overlapping within a network. Only IPv4 is supported. This field is set at resource creation time. The range can be any range listed in the Valid ranges list. The range can be expanded after creation using expandIpCidrRange.
        :param pulumi.Input['SubnetworkIpv6AccessType'] ipv6_access_type: The access type of IPv6 address this subnet holds. It's immutable and can only be specified during creation or the first time the subnet is updated into IPV4_IPV6 dual stack. If the ipv6_type is EXTERNAL then this subnet cannot enable direct path.
        :param pulumi.Input['SubnetworkLogConfigArgs'] log_config: This field denotes the VPC flow logging options for this subnetwork. If logging is enabled, logs are exported to Cloud Logging.
        :param pulumi.Input[str] name: The name of the resource, provided by the client when initially creating the resource. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        :param pulumi.Input[str] network: The URL of the network to which this subnetwork belongs, provided by the client when initially creating the subnetwork. Only networks that are in the distributed mode can have subnetworks. This field can be set only at resource creation time.
        :param pulumi.Input[bool] private_ip_google_access: Whether the VMs in this subnet can access Google services without assigned external IP addresses. This field can be both set at resource creation time and updated using setPrivateIpGoogleAccess.
        :param pulumi.Input['SubnetworkPrivateIpv6GoogleAccess'] private_ipv6_google_access: The private IPv6 google access type for the VMs in this subnet. This is an expanded field of enablePrivateV6Access. If both fields are set, privateIpv6GoogleAccess will take priority. This field can be both set at resource creation time and updated using patch.
        :param pulumi.Input['SubnetworkPurpose'] purpose: The purpose of the resource. This field can be either PRIVATE_RFC_1918 or INTERNAL_HTTPS_LOAD_BALANCER. A subnetwork with purpose set to INTERNAL_HTTPS_LOAD_BALANCER is a user-created subnetwork that is reserved for Internal HTTP(S) Load Balancing. If unspecified, the purpose defaults to PRIVATE_RFC_1918. The enableFlowLogs field isn't supported with the purpose field set to INTERNAL_HTTPS_LOAD_BALANCER.
        :param pulumi.Input['SubnetworkRole'] role: The role of subnetwork. Currently, this field is only used when purpose = INTERNAL_HTTPS_LOAD_BALANCER. The value can be set to ACTIVE or BACKUP. An ACTIVE subnetwork is one that is currently being used for Internal HTTP(S) Load Balancing. A BACKUP subnetwork is one that is ready to be promoted to ACTIVE or is currently draining. This field can be updated with a patch request.
        :param pulumi.Input[Sequence[pulumi.Input['SubnetworkSecondaryRangeArgs']]] secondary_ip_ranges: An array of configurations for secondary IP ranges for VM instances contained in this subnetwork. The primary IP of such VM must belong to the primary ipCidrRange of the subnetwork. The alias IPs may belong to either primary or secondary ranges. This field can be updated with a patch request.
        :param pulumi.Input['SubnetworkStackType'] stack_type: The stack type for this subnet to identify whether the IPv6 feature is enabled or not. If not specified IPV4_ONLY will be used. This field can be both set at resource creation time and updated using patch.
        """
        pulumi.set(__self__, "region", region)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if enable_flow_logs is not None:
            pulumi.set(__self__, "enable_flow_logs", enable_flow_logs)
        if ip_cidr_range is not None:
            pulumi.set(__self__, "ip_cidr_range", ip_cidr_range)
        if ipv6_access_type is not None:
            pulumi.set(__self__, "ipv6_access_type", ipv6_access_type)
        if log_config is not None:
            pulumi.set(__self__, "log_config", log_config)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if network is not None:
            pulumi.set(__self__, "network", network)
        if private_ip_google_access is not None:
            pulumi.set(__self__, "private_ip_google_access", private_ip_google_access)
        if private_ipv6_google_access is not None:
            pulumi.set(__self__, "private_ipv6_google_access", private_ipv6_google_access)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if purpose is not None:
            pulumi.set(__self__, "purpose", purpose)
        if request_id is not None:
            pulumi.set(__self__, "request_id", request_id)
        if role is not None:
            pulumi.set(__self__, "role", role)
        if secondary_ip_ranges is not None:
            pulumi.set(__self__, "secondary_ip_ranges", secondary_ip_ranges)
        if stack_type is not None:
            pulumi.set(__self__, "stack_type", stack_type)

    @property
    @pulumi.getter
    def region(self) -> pulumi.Input[str]:
        """
        URL of the region where the Subnetwork resides. This field can be set only at resource creation time.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: pulumi.Input[str]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        An optional description of this resource. Provide this property when you create the resource. This field can be set only at resource creation time.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="enableFlowLogs")
    def enable_flow_logs(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to enable flow logging for this subnetwork. If this field is not explicitly set, it will not appear in get listings. If not set the default behavior is to disable flow logging. This field isn't supported with the purpose field set to INTERNAL_HTTPS_LOAD_BALANCER.
        """
        return pulumi.get(self, "enable_flow_logs")

    @enable_flow_logs.setter
    def enable_flow_logs(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_flow_logs", value)

    @property
    @pulumi.getter(name="ipCidrRange")
    def ip_cidr_range(self) -> Optional[pulumi.Input[str]]:
        """
        The range of internal addresses that are owned by this subnetwork. Provide this property when you create the subnetwork. For example, 10.0.0.0/8 or 100.64.0.0/10. Ranges must be unique and non-overlapping within a network. Only IPv4 is supported. This field is set at resource creation time. The range can be any range listed in the Valid ranges list. The range can be expanded after creation using expandIpCidrRange.
        """
        return pulumi.get(self, "ip_cidr_range")

    @ip_cidr_range.setter
    def ip_cidr_range(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ip_cidr_range", value)

    @property
    @pulumi.getter(name="ipv6AccessType")
    def ipv6_access_type(self) -> Optional[pulumi.Input['SubnetworkIpv6AccessType']]:
        """
        The access type of IPv6 address this subnet holds. It's immutable and can only be specified during creation or the first time the subnet is updated into IPV4_IPV6 dual stack. If the ipv6_type is EXTERNAL then this subnet cannot enable direct path.
        """
        return pulumi.get(self, "ipv6_access_type")

    @ipv6_access_type.setter
    def ipv6_access_type(self, value: Optional[pulumi.Input['SubnetworkIpv6AccessType']]):
        pulumi.set(self, "ipv6_access_type", value)

    @property
    @pulumi.getter(name="logConfig")
    def log_config(self) -> Optional[pulumi.Input['SubnetworkLogConfigArgs']]:
        """
        This field denotes the VPC flow logging options for this subnetwork. If logging is enabled, logs are exported to Cloud Logging.
        """
        return pulumi.get(self, "log_config")

    @log_config.setter
    def log_config(self, value: Optional[pulumi.Input['SubnetworkLogConfigArgs']]):
        pulumi.set(self, "log_config", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the resource, provided by the client when initially creating the resource. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[str]]:
        """
        The URL of the network to which this subnetwork belongs, provided by the client when initially creating the subnetwork. Only networks that are in the distributed mode can have subnetworks. This field can be set only at resource creation time.
        """
        return pulumi.get(self, "network")

    @network.setter
    def network(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network", value)

    @property
    @pulumi.getter(name="privateIpGoogleAccess")
    def private_ip_google_access(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the VMs in this subnet can access Google services without assigned external IP addresses. This field can be both set at resource creation time and updated using setPrivateIpGoogleAccess.
        """
        return pulumi.get(self, "private_ip_google_access")

    @private_ip_google_access.setter
    def private_ip_google_access(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "private_ip_google_access", value)

    @property
    @pulumi.getter(name="privateIpv6GoogleAccess")
    def private_ipv6_google_access(self) -> Optional[pulumi.Input['SubnetworkPrivateIpv6GoogleAccess']]:
        """
        The private IPv6 google access type for the VMs in this subnet. This is an expanded field of enablePrivateV6Access. If both fields are set, privateIpv6GoogleAccess will take priority. This field can be both set at resource creation time and updated using patch.
        """
        return pulumi.get(self, "private_ipv6_google_access")

    @private_ipv6_google_access.setter
    def private_ipv6_google_access(self, value: Optional[pulumi.Input['SubnetworkPrivateIpv6GoogleAccess']]):
        pulumi.set(self, "private_ipv6_google_access", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter
    def purpose(self) -> Optional[pulumi.Input['SubnetworkPurpose']]:
        """
        The purpose of the resource. This field can be either PRIVATE_RFC_1918 or INTERNAL_HTTPS_LOAD_BALANCER. A subnetwork with purpose set to INTERNAL_HTTPS_LOAD_BALANCER is a user-created subnetwork that is reserved for Internal HTTP(S) Load Balancing. If unspecified, the purpose defaults to PRIVATE_RFC_1918. The enableFlowLogs field isn't supported with the purpose field set to INTERNAL_HTTPS_LOAD_BALANCER.
        """
        return pulumi.get(self, "purpose")

    @purpose.setter
    def purpose(self, value: Optional[pulumi.Input['SubnetworkPurpose']]):
        pulumi.set(self, "purpose", value)

    @property
    @pulumi.getter(name="requestId")
    def request_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "request_id")

    @request_id.setter
    def request_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "request_id", value)

    @property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input['SubnetworkRole']]:
        """
        The role of subnetwork. Currently, this field is only used when purpose = INTERNAL_HTTPS_LOAD_BALANCER. The value can be set to ACTIVE or BACKUP. An ACTIVE subnetwork is one that is currently being used for Internal HTTP(S) Load Balancing. A BACKUP subnetwork is one that is ready to be promoted to ACTIVE or is currently draining. This field can be updated with a patch request.
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: Optional[pulumi.Input['SubnetworkRole']]):
        pulumi.set(self, "role", value)

    @property
    @pulumi.getter(name="secondaryIpRanges")
    def secondary_ip_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SubnetworkSecondaryRangeArgs']]]]:
        """
        An array of configurations for secondary IP ranges for VM instances contained in this subnetwork. The primary IP of such VM must belong to the primary ipCidrRange of the subnetwork. The alias IPs may belong to either primary or secondary ranges. This field can be updated with a patch request.
        """
        return pulumi.get(self, "secondary_ip_ranges")

    @secondary_ip_ranges.setter
    def secondary_ip_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SubnetworkSecondaryRangeArgs']]]]):
        pulumi.set(self, "secondary_ip_ranges", value)

    @property
    @pulumi.getter(name="stackType")
    def stack_type(self) -> Optional[pulumi.Input['SubnetworkStackType']]:
        """
        The stack type for this subnet to identify whether the IPv6 feature is enabled or not. If not specified IPV4_ONLY will be used. This field can be both set at resource creation time and updated using patch.
        """
        return pulumi.get(self, "stack_type")

    @stack_type.setter
    def stack_type(self, value: Optional[pulumi.Input['SubnetworkStackType']]):
        pulumi.set(self, "stack_type", value)


class Subnetwork(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enable_flow_logs: Optional[pulumi.Input[bool]] = None,
                 ip_cidr_range: Optional[pulumi.Input[str]] = None,
                 ipv6_access_type: Optional[pulumi.Input['SubnetworkIpv6AccessType']] = None,
                 log_config: Optional[pulumi.Input[pulumi.InputType['SubnetworkLogConfigArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network: Optional[pulumi.Input[str]] = None,
                 private_ip_google_access: Optional[pulumi.Input[bool]] = None,
                 private_ipv6_google_access: Optional[pulumi.Input['SubnetworkPrivateIpv6GoogleAccess']] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 purpose: Optional[pulumi.Input['SubnetworkPurpose']] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input['SubnetworkRole']] = None,
                 secondary_ip_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubnetworkSecondaryRangeArgs']]]]] = None,
                 stack_type: Optional[pulumi.Input['SubnetworkStackType']] = None,
                 __props__=None):
        """
        Creates a subnetwork in the specified project using the data included in the request.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: An optional description of this resource. Provide this property when you create the resource. This field can be set only at resource creation time.
        :param pulumi.Input[bool] enable_flow_logs: Whether to enable flow logging for this subnetwork. If this field is not explicitly set, it will not appear in get listings. If not set the default behavior is to disable flow logging. This field isn't supported with the purpose field set to INTERNAL_HTTPS_LOAD_BALANCER.
        :param pulumi.Input[str] ip_cidr_range: The range of internal addresses that are owned by this subnetwork. Provide this property when you create the subnetwork. For example, 10.0.0.0/8 or 100.64.0.0/10. Ranges must be unique and non-overlapping within a network. Only IPv4 is supported. This field is set at resource creation time. The range can be any range listed in the Valid ranges list. The range can be expanded after creation using expandIpCidrRange.
        :param pulumi.Input['SubnetworkIpv6AccessType'] ipv6_access_type: The access type of IPv6 address this subnet holds. It's immutable and can only be specified during creation or the first time the subnet is updated into IPV4_IPV6 dual stack. If the ipv6_type is EXTERNAL then this subnet cannot enable direct path.
        :param pulumi.Input[pulumi.InputType['SubnetworkLogConfigArgs']] log_config: This field denotes the VPC flow logging options for this subnetwork. If logging is enabled, logs are exported to Cloud Logging.
        :param pulumi.Input[str] name: The name of the resource, provided by the client when initially creating the resource. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        :param pulumi.Input[str] network: The URL of the network to which this subnetwork belongs, provided by the client when initially creating the subnetwork. Only networks that are in the distributed mode can have subnetworks. This field can be set only at resource creation time.
        :param pulumi.Input[bool] private_ip_google_access: Whether the VMs in this subnet can access Google services without assigned external IP addresses. This field can be both set at resource creation time and updated using setPrivateIpGoogleAccess.
        :param pulumi.Input['SubnetworkPrivateIpv6GoogleAccess'] private_ipv6_google_access: The private IPv6 google access type for the VMs in this subnet. This is an expanded field of enablePrivateV6Access. If both fields are set, privateIpv6GoogleAccess will take priority. This field can be both set at resource creation time and updated using patch.
        :param pulumi.Input['SubnetworkPurpose'] purpose: The purpose of the resource. This field can be either PRIVATE_RFC_1918 or INTERNAL_HTTPS_LOAD_BALANCER. A subnetwork with purpose set to INTERNAL_HTTPS_LOAD_BALANCER is a user-created subnetwork that is reserved for Internal HTTP(S) Load Balancing. If unspecified, the purpose defaults to PRIVATE_RFC_1918. The enableFlowLogs field isn't supported with the purpose field set to INTERNAL_HTTPS_LOAD_BALANCER.
        :param pulumi.Input[str] region: URL of the region where the Subnetwork resides. This field can be set only at resource creation time.
        :param pulumi.Input['SubnetworkRole'] role: The role of subnetwork. Currently, this field is only used when purpose = INTERNAL_HTTPS_LOAD_BALANCER. The value can be set to ACTIVE or BACKUP. An ACTIVE subnetwork is one that is currently being used for Internal HTTP(S) Load Balancing. A BACKUP subnetwork is one that is ready to be promoted to ACTIVE or is currently draining. This field can be updated with a patch request.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubnetworkSecondaryRangeArgs']]]] secondary_ip_ranges: An array of configurations for secondary IP ranges for VM instances contained in this subnetwork. The primary IP of such VM must belong to the primary ipCidrRange of the subnetwork. The alias IPs may belong to either primary or secondary ranges. This field can be updated with a patch request.
        :param pulumi.Input['SubnetworkStackType'] stack_type: The stack type for this subnet to identify whether the IPv6 feature is enabled or not. If not specified IPV4_ONLY will be used. This field can be both set at resource creation time and updated using patch.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SubnetworkArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a subnetwork in the specified project using the data included in the request.

        :param str resource_name: The name of the resource.
        :param SubnetworkArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SubnetworkArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enable_flow_logs: Optional[pulumi.Input[bool]] = None,
                 ip_cidr_range: Optional[pulumi.Input[str]] = None,
                 ipv6_access_type: Optional[pulumi.Input['SubnetworkIpv6AccessType']] = None,
                 log_config: Optional[pulumi.Input[pulumi.InputType['SubnetworkLogConfigArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network: Optional[pulumi.Input[str]] = None,
                 private_ip_google_access: Optional[pulumi.Input[bool]] = None,
                 private_ipv6_google_access: Optional[pulumi.Input['SubnetworkPrivateIpv6GoogleAccess']] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 purpose: Optional[pulumi.Input['SubnetworkPurpose']] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input['SubnetworkRole']] = None,
                 secondary_ip_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubnetworkSecondaryRangeArgs']]]]] = None,
                 stack_type: Optional[pulumi.Input['SubnetworkStackType']] = None,
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
            __props__ = SubnetworkArgs.__new__(SubnetworkArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["enable_flow_logs"] = enable_flow_logs
            __props__.__dict__["ip_cidr_range"] = ip_cidr_range
            __props__.__dict__["ipv6_access_type"] = ipv6_access_type
            __props__.__dict__["log_config"] = log_config
            __props__.__dict__["name"] = name
            __props__.__dict__["network"] = network
            __props__.__dict__["private_ip_google_access"] = private_ip_google_access
            __props__.__dict__["private_ipv6_google_access"] = private_ipv6_google_access
            __props__.__dict__["project"] = project
            __props__.__dict__["purpose"] = purpose
            if region is None and not opts.urn:
                raise TypeError("Missing required property 'region'")
            __props__.__dict__["region"] = region
            __props__.__dict__["request_id"] = request_id
            __props__.__dict__["role"] = role
            __props__.__dict__["secondary_ip_ranges"] = secondary_ip_ranges
            __props__.__dict__["stack_type"] = stack_type
            __props__.__dict__["creation_timestamp"] = None
            __props__.__dict__["external_ipv6_prefix"] = None
            __props__.__dict__["fingerprint"] = None
            __props__.__dict__["gateway_address"] = None
            __props__.__dict__["ipv6_cidr_range"] = None
            __props__.__dict__["kind"] = None
            __props__.__dict__["self_link"] = None
            __props__.__dict__["state"] = None
        super(Subnetwork, __self__).__init__(
            'google-native:compute/v1:Subnetwork',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Subnetwork':
        """
        Get an existing Subnetwork resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SubnetworkArgs.__new__(SubnetworkArgs)

        __props__.__dict__["creation_timestamp"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["enable_flow_logs"] = None
        __props__.__dict__["external_ipv6_prefix"] = None
        __props__.__dict__["fingerprint"] = None
        __props__.__dict__["gateway_address"] = None
        __props__.__dict__["ip_cidr_range"] = None
        __props__.__dict__["ipv6_access_type"] = None
        __props__.__dict__["ipv6_cidr_range"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["log_config"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["network"] = None
        __props__.__dict__["private_ip_google_access"] = None
        __props__.__dict__["private_ipv6_google_access"] = None
        __props__.__dict__["purpose"] = None
        __props__.__dict__["region"] = None
        __props__.__dict__["role"] = None
        __props__.__dict__["secondary_ip_ranges"] = None
        __props__.__dict__["self_link"] = None
        __props__.__dict__["stack_type"] = None
        __props__.__dict__["state"] = None
        return Subnetwork(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> pulumi.Output[str]:
        """
        Creation timestamp in RFC3339 text format.
        """
        return pulumi.get(self, "creation_timestamp")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        An optional description of this resource. Provide this property when you create the resource. This field can be set only at resource creation time.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="enableFlowLogs")
    def enable_flow_logs(self) -> pulumi.Output[bool]:
        """
        Whether to enable flow logging for this subnetwork. If this field is not explicitly set, it will not appear in get listings. If not set the default behavior is to disable flow logging. This field isn't supported with the purpose field set to INTERNAL_HTTPS_LOAD_BALANCER.
        """
        return pulumi.get(self, "enable_flow_logs")

    @property
    @pulumi.getter(name="externalIpv6Prefix")
    def external_ipv6_prefix(self) -> pulumi.Output[str]:
        """
        The range of external IPv6 addresses that are owned by this subnetwork.
        """
        return pulumi.get(self, "external_ipv6_prefix")

    @property
    @pulumi.getter
    def fingerprint(self) -> pulumi.Output[str]:
        """
        Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking. This field will be ignored when inserting a Subnetwork. An up-to-date fingerprint must be provided in order to update the Subnetwork, otherwise the request will fail with error 412 conditionNotMet. To see the latest fingerprint, make a get() request to retrieve a Subnetwork.
        """
        return pulumi.get(self, "fingerprint")

    @property
    @pulumi.getter(name="gatewayAddress")
    def gateway_address(self) -> pulumi.Output[str]:
        """
        The gateway address for default routes to reach destination addresses outside this subnetwork.
        """
        return pulumi.get(self, "gateway_address")

    @property
    @pulumi.getter(name="ipCidrRange")
    def ip_cidr_range(self) -> pulumi.Output[str]:
        """
        The range of internal addresses that are owned by this subnetwork. Provide this property when you create the subnetwork. For example, 10.0.0.0/8 or 100.64.0.0/10. Ranges must be unique and non-overlapping within a network. Only IPv4 is supported. This field is set at resource creation time. The range can be any range listed in the Valid ranges list. The range can be expanded after creation using expandIpCidrRange.
        """
        return pulumi.get(self, "ip_cidr_range")

    @property
    @pulumi.getter(name="ipv6AccessType")
    def ipv6_access_type(self) -> pulumi.Output[str]:
        """
        The access type of IPv6 address this subnet holds. It's immutable and can only be specified during creation or the first time the subnet is updated into IPV4_IPV6 dual stack. If the ipv6_type is EXTERNAL then this subnet cannot enable direct path.
        """
        return pulumi.get(self, "ipv6_access_type")

    @property
    @pulumi.getter(name="ipv6CidrRange")
    def ipv6_cidr_range(self) -> pulumi.Output[str]:
        """
        The range of internal IPv6 addresses that are owned by this subnetwork.
        """
        return pulumi.get(self, "ipv6_cidr_range")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        Type of the resource. Always compute#subnetwork for Subnetwork resources.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="logConfig")
    def log_config(self) -> pulumi.Output['outputs.SubnetworkLogConfigResponse']:
        """
        This field denotes the VPC flow logging options for this subnetwork. If logging is enabled, logs are exported to Cloud Logging.
        """
        return pulumi.get(self, "log_config")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource, provided by the client when initially creating the resource. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def network(self) -> pulumi.Output[str]:
        """
        The URL of the network to which this subnetwork belongs, provided by the client when initially creating the subnetwork. Only networks that are in the distributed mode can have subnetworks. This field can be set only at resource creation time.
        """
        return pulumi.get(self, "network")

    @property
    @pulumi.getter(name="privateIpGoogleAccess")
    def private_ip_google_access(self) -> pulumi.Output[bool]:
        """
        Whether the VMs in this subnet can access Google services without assigned external IP addresses. This field can be both set at resource creation time and updated using setPrivateIpGoogleAccess.
        """
        return pulumi.get(self, "private_ip_google_access")

    @property
    @pulumi.getter(name="privateIpv6GoogleAccess")
    def private_ipv6_google_access(self) -> pulumi.Output[str]:
        """
        The private IPv6 google access type for the VMs in this subnet. This is an expanded field of enablePrivateV6Access. If both fields are set, privateIpv6GoogleAccess will take priority. This field can be both set at resource creation time and updated using patch.
        """
        return pulumi.get(self, "private_ipv6_google_access")

    @property
    @pulumi.getter
    def purpose(self) -> pulumi.Output[str]:
        """
        The purpose of the resource. This field can be either PRIVATE_RFC_1918 or INTERNAL_HTTPS_LOAD_BALANCER. A subnetwork with purpose set to INTERNAL_HTTPS_LOAD_BALANCER is a user-created subnetwork that is reserved for Internal HTTP(S) Load Balancing. If unspecified, the purpose defaults to PRIVATE_RFC_1918. The enableFlowLogs field isn't supported with the purpose field set to INTERNAL_HTTPS_LOAD_BALANCER.
        """
        return pulumi.get(self, "purpose")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        URL of the region where the Subnetwork resides. This field can be set only at resource creation time.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def role(self) -> pulumi.Output[str]:
        """
        The role of subnetwork. Currently, this field is only used when purpose = INTERNAL_HTTPS_LOAD_BALANCER. The value can be set to ACTIVE or BACKUP. An ACTIVE subnetwork is one that is currently being used for Internal HTTP(S) Load Balancing. A BACKUP subnetwork is one that is ready to be promoted to ACTIVE or is currently draining. This field can be updated with a patch request.
        """
        return pulumi.get(self, "role")

    @property
    @pulumi.getter(name="secondaryIpRanges")
    def secondary_ip_ranges(self) -> pulumi.Output[Sequence['outputs.SubnetworkSecondaryRangeResponse']]:
        """
        An array of configurations for secondary IP ranges for VM instances contained in this subnetwork. The primary IP of such VM must belong to the primary ipCidrRange of the subnetwork. The alias IPs may belong to either primary or secondary ranges. This field can be updated with a patch request.
        """
        return pulumi.get(self, "secondary_ip_ranges")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[str]:
        """
        Server-defined URL for the resource.
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter(name="stackType")
    def stack_type(self) -> pulumi.Output[str]:
        """
        The stack type for this subnet to identify whether the IPv6 feature is enabled or not. If not specified IPV4_ONLY will be used. This field can be both set at resource creation time and updated using patch.
        """
        return pulumi.get(self, "stack_type")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The state of the subnetwork, which can be one of the following values: READY: Subnetwork is created and ready to use DRAINING: only applicable to subnetworks that have the purpose set to INTERNAL_HTTPS_LOAD_BALANCER and indicates that connections to the load balancer are being drained. A subnetwork that is draining cannot be used or modified until it reaches a status of READY
        """
        return pulumi.get(self, "state")

