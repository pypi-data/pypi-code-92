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
    'GetUptimeCheckConfigResult',
    'AwaitableGetUptimeCheckConfigResult',
    'get_uptime_check_config',
]

@pulumi.output_type
class GetUptimeCheckConfigResult:
    def __init__(__self__, content_matchers=None, display_name=None, http_check=None, internal_checkers=None, is_internal=None, monitored_resource=None, name=None, period=None, resource_group=None, selected_regions=None, tcp_check=None, timeout=None):
        if content_matchers and not isinstance(content_matchers, list):
            raise TypeError("Expected argument 'content_matchers' to be a list")
        pulumi.set(__self__, "content_matchers", content_matchers)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if http_check and not isinstance(http_check, dict):
            raise TypeError("Expected argument 'http_check' to be a dict")
        pulumi.set(__self__, "http_check", http_check)
        if internal_checkers and not isinstance(internal_checkers, list):
            raise TypeError("Expected argument 'internal_checkers' to be a list")
        pulumi.set(__self__, "internal_checkers", internal_checkers)
        if is_internal and not isinstance(is_internal, bool):
            raise TypeError("Expected argument 'is_internal' to be a bool")
        pulumi.set(__self__, "is_internal", is_internal)
        if monitored_resource and not isinstance(monitored_resource, dict):
            raise TypeError("Expected argument 'monitored_resource' to be a dict")
        pulumi.set(__self__, "monitored_resource", monitored_resource)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if period and not isinstance(period, str):
            raise TypeError("Expected argument 'period' to be a str")
        pulumi.set(__self__, "period", period)
        if resource_group and not isinstance(resource_group, dict):
            raise TypeError("Expected argument 'resource_group' to be a dict")
        pulumi.set(__self__, "resource_group", resource_group)
        if selected_regions and not isinstance(selected_regions, list):
            raise TypeError("Expected argument 'selected_regions' to be a list")
        pulumi.set(__self__, "selected_regions", selected_regions)
        if tcp_check and not isinstance(tcp_check, dict):
            raise TypeError("Expected argument 'tcp_check' to be a dict")
        pulumi.set(__self__, "tcp_check", tcp_check)
        if timeout and not isinstance(timeout, str):
            raise TypeError("Expected argument 'timeout' to be a str")
        pulumi.set(__self__, "timeout", timeout)

    @property
    @pulumi.getter(name="contentMatchers")
    def content_matchers(self) -> Sequence['outputs.ContentMatcherResponse']:
        """
        The content that is expected to appear in the data returned by the target server against which the check is run. Currently, only the first entry in the content_matchers list is supported, and additional entries will be ignored. This field is optional and should only be specified if a content match is required as part of the/ Uptime check.
        """
        return pulumi.get(self, "content_matchers")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        A human-friendly name for the Uptime check configuration. The display name should be unique within a Stackdriver Workspace in order to make it easier to identify; however, uniqueness is not enforced. Required.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="httpCheck")
    def http_check(self) -> 'outputs.HttpCheckResponse':
        """
        Contains information needed to make an HTTP or HTTPS check.
        """
        return pulumi.get(self, "http_check")

    @property
    @pulumi.getter(name="internalCheckers")
    def internal_checkers(self) -> Sequence['outputs.InternalCheckerResponse']:
        """
        The internal checkers that this check will egress from. If is_internal is true and this list is empty, the check will egress from all the InternalCheckers configured for the project that owns this UptimeCheckConfig.
        """
        return pulumi.get(self, "internal_checkers")

    @property
    @pulumi.getter(name="isInternal")
    def is_internal(self) -> bool:
        """
        If this is true, then checks are made only from the 'internal_checkers'. If it is false, then checks are made only from the 'selected_regions'. It is an error to provide 'selected_regions' when is_internal is true, or to provide 'internal_checkers' when is_internal is false.
        """
        return pulumi.get(self, "is_internal")

    @property
    @pulumi.getter(name="monitoredResource")
    def monitored_resource(self) -> 'outputs.MonitoredResourceResponse':
        """
        The monitored resource (https://cloud.google.com/monitoring/api/resources) associated with the configuration. The following monitored resource types are valid for this field: uptime_url, gce_instance, gae_app, aws_ec2_instance, aws_elb_load_balancer
        """
        return pulumi.get(self, "monitored_resource")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        A unique resource name for this Uptime check configuration. The format is: projects/[PROJECT_ID_OR_NUMBER]/uptimeCheckConfigs/[UPTIME_CHECK_ID] [PROJECT_ID_OR_NUMBER] is the Workspace host project associated with the Uptime check.This field should be omitted when creating the Uptime check configuration; on create, the resource name is assigned by the server and included in the response.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def period(self) -> str:
        """
        How often, in seconds, the Uptime check is performed. Currently, the only supported values are 60s (1 minute), 300s (5 minutes), 600s (10 minutes), and 900s (15 minutes). Optional, defaults to 60s.
        """
        return pulumi.get(self, "period")

    @property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> 'outputs.ResourceGroupResponse':
        """
        The group resource associated with the configuration.
        """
        return pulumi.get(self, "resource_group")

    @property
    @pulumi.getter(name="selectedRegions")
    def selected_regions(self) -> Sequence[str]:
        """
        The list of regions from which the check will be run. Some regions contain one location, and others contain more than one. If this field is specified, enough regions must be provided to include a minimum of 3 locations. Not specifying this field will result in Uptime checks running from all available regions.
        """
        return pulumi.get(self, "selected_regions")

    @property
    @pulumi.getter(name="tcpCheck")
    def tcp_check(self) -> 'outputs.TcpCheckResponse':
        """
        Contains information needed to make a TCP check.
        """
        return pulumi.get(self, "tcp_check")

    @property
    @pulumi.getter
    def timeout(self) -> str:
        """
        The maximum amount of time to wait for the request to complete (must be between 1 and 60 seconds). Required.
        """
        return pulumi.get(self, "timeout")


class AwaitableGetUptimeCheckConfigResult(GetUptimeCheckConfigResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetUptimeCheckConfigResult(
            content_matchers=self.content_matchers,
            display_name=self.display_name,
            http_check=self.http_check,
            internal_checkers=self.internal_checkers,
            is_internal=self.is_internal,
            monitored_resource=self.monitored_resource,
            name=self.name,
            period=self.period,
            resource_group=self.resource_group,
            selected_regions=self.selected_regions,
            tcp_check=self.tcp_check,
            timeout=self.timeout)


def get_uptime_check_config(project: Optional[str] = None,
                            uptime_check_config_id: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetUptimeCheckConfigResult:
    """
    Gets a single Uptime check configuration.
    """
    __args__ = dict()
    __args__['project'] = project
    __args__['uptimeCheckConfigId'] = uptime_check_config_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:monitoring/v3:getUptimeCheckConfig', __args__, opts=opts, typ=GetUptimeCheckConfigResult).value

    return AwaitableGetUptimeCheckConfigResult(
        content_matchers=__ret__.content_matchers,
        display_name=__ret__.display_name,
        http_check=__ret__.http_check,
        internal_checkers=__ret__.internal_checkers,
        is_internal=__ret__.is_internal,
        monitored_resource=__ret__.monitored_resource,
        name=__ret__.name,
        period=__ret__.period,
        resource_group=__ret__.resource_group,
        selected_regions=__ret__.selected_regions,
        tcp_check=__ret__.tcp_check,
        timeout=__ret__.timeout)
