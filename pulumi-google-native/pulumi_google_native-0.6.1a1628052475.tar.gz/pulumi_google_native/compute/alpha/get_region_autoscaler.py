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
    'GetRegionAutoscalerResult',
    'AwaitableGetRegionAutoscalerResult',
    'get_region_autoscaler',
]

@pulumi.output_type
class GetRegionAutoscalerResult:
    def __init__(__self__, autoscaling_policy=None, creation_timestamp=None, description=None, kind=None, name=None, recommended_size=None, region=None, scaling_schedule_status=None, self_link=None, self_link_with_id=None, status=None, status_details=None, target=None, zone=None):
        if autoscaling_policy and not isinstance(autoscaling_policy, dict):
            raise TypeError("Expected argument 'autoscaling_policy' to be a dict")
        pulumi.set(__self__, "autoscaling_policy", autoscaling_policy)
        if creation_timestamp and not isinstance(creation_timestamp, str):
            raise TypeError("Expected argument 'creation_timestamp' to be a str")
        pulumi.set(__self__, "creation_timestamp", creation_timestamp)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if recommended_size and not isinstance(recommended_size, int):
            raise TypeError("Expected argument 'recommended_size' to be a int")
        pulumi.set(__self__, "recommended_size", recommended_size)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if scaling_schedule_status and not isinstance(scaling_schedule_status, dict):
            raise TypeError("Expected argument 'scaling_schedule_status' to be a dict")
        pulumi.set(__self__, "scaling_schedule_status", scaling_schedule_status)
        if self_link and not isinstance(self_link, str):
            raise TypeError("Expected argument 'self_link' to be a str")
        pulumi.set(__self__, "self_link", self_link)
        if self_link_with_id and not isinstance(self_link_with_id, str):
            raise TypeError("Expected argument 'self_link_with_id' to be a str")
        pulumi.set(__self__, "self_link_with_id", self_link_with_id)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if status_details and not isinstance(status_details, list):
            raise TypeError("Expected argument 'status_details' to be a list")
        pulumi.set(__self__, "status_details", status_details)
        if target and not isinstance(target, str):
            raise TypeError("Expected argument 'target' to be a str")
        pulumi.set(__self__, "target", target)
        if zone and not isinstance(zone, str):
            raise TypeError("Expected argument 'zone' to be a str")
        pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter(name="autoscalingPolicy")
    def autoscaling_policy(self) -> 'outputs.AutoscalingPolicyResponse':
        """
        The configuration parameters for the autoscaling algorithm. You can define one or more signals for an autoscaler: cpuUtilization, customMetricUtilizations, and loadBalancingUtilization. If none of these are specified, the default will be to autoscale based on cpuUtilization to 0.6 or 60%.
        """
        return pulumi.get(self, "autoscaling_policy")

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
    @pulumi.getter
    def kind(self) -> str:
        """
        Type of the resource. Always compute#autoscaler for autoscalers.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="recommendedSize")
    def recommended_size(self) -> int:
        """
        Target recommended MIG size (number of instances) computed by autoscaler. Autoscaler calculates the recommended MIG size even when the autoscaling policy mode is different from ON. This field is empty when autoscaler is not connected to an existing managed instance group or autoscaler did not generate its prediction.
        """
        return pulumi.get(self, "recommended_size")

    @property
    @pulumi.getter
    def region(self) -> str:
        """
        URL of the region where the instance group resides (for autoscalers living in regional scope).
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="scalingScheduleStatus")
    def scaling_schedule_status(self) -> Mapping[str, str]:
        """
        Status information of existing scaling schedules.
        """
        return pulumi.get(self, "scaling_schedule_status")

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
        Server-defined URL for this resource with the resource id.
        """
        return pulumi.get(self, "self_link_with_id")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The status of the autoscaler configuration. Current set of possible values: - PENDING: Autoscaler backend hasn't read new/updated configuration. - DELETING: Configuration is being deleted. - ACTIVE: Configuration is acknowledged to be effective. Some warnings might be present in the statusDetails field. - ERROR: Configuration has errors. Actionable for users. Details are present in the statusDetails field. New values might be added in the future.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="statusDetails")
    def status_details(self) -> Sequence['outputs.AutoscalerStatusDetailsResponse']:
        """
        Human-readable details about the current state of the autoscaler. Read the documentation for Commonly returned status messages for examples of status messages you might encounter.
        """
        return pulumi.get(self, "status_details")

    @property
    @pulumi.getter
    def target(self) -> str:
        """
        URL of the managed instance group that this autoscaler will scale. This field is required when creating an autoscaler.
        """
        return pulumi.get(self, "target")

    @property
    @pulumi.getter
    def zone(self) -> str:
        """
        URL of the zone where the instance group resides (for autoscalers living in zonal scope).
        """
        return pulumi.get(self, "zone")


class AwaitableGetRegionAutoscalerResult(GetRegionAutoscalerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRegionAutoscalerResult(
            autoscaling_policy=self.autoscaling_policy,
            creation_timestamp=self.creation_timestamp,
            description=self.description,
            kind=self.kind,
            name=self.name,
            recommended_size=self.recommended_size,
            region=self.region,
            scaling_schedule_status=self.scaling_schedule_status,
            self_link=self.self_link,
            self_link_with_id=self.self_link_with_id,
            status=self.status,
            status_details=self.status_details,
            target=self.target,
            zone=self.zone)


def get_region_autoscaler(autoscaler: Optional[str] = None,
                          project: Optional[str] = None,
                          region: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRegionAutoscalerResult:
    """
    Returns the specified autoscaler.
    """
    __args__ = dict()
    __args__['autoscaler'] = autoscaler
    __args__['project'] = project
    __args__['region'] = region
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:compute/alpha:getRegionAutoscaler', __args__, opts=opts, typ=GetRegionAutoscalerResult).value

    return AwaitableGetRegionAutoscalerResult(
        autoscaling_policy=__ret__.autoscaling_policy,
        creation_timestamp=__ret__.creation_timestamp,
        description=__ret__.description,
        kind=__ret__.kind,
        name=__ret__.name,
        recommended_size=__ret__.recommended_size,
        region=__ret__.region,
        scaling_schedule_status=__ret__.scaling_schedule_status,
        self_link=__ret__.self_link,
        self_link_with_id=__ret__.self_link_with_id,
        status=__ret__.status,
        status_details=__ret__.status_details,
        target=__ret__.target,
        zone=__ret__.zone)
