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
    'GetSpokeResult',
    'AwaitableGetSpokeResult',
    'get_spoke',
]

@pulumi.output_type
class GetSpokeResult:
    def __init__(__self__, create_time=None, description=None, hub=None, labels=None, linked_interconnect_attachments=None, linked_router_appliance_instances=None, linked_vpn_tunnels=None, name=None, state=None, unique_id=None, update_time=None):
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if hub and not isinstance(hub, str):
            raise TypeError("Expected argument 'hub' to be a str")
        pulumi.set(__self__, "hub", hub)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if linked_interconnect_attachments and not isinstance(linked_interconnect_attachments, list):
            raise TypeError("Expected argument 'linked_interconnect_attachments' to be a list")
        pulumi.set(__self__, "linked_interconnect_attachments", linked_interconnect_attachments)
        if linked_router_appliance_instances and not isinstance(linked_router_appliance_instances, list):
            raise TypeError("Expected argument 'linked_router_appliance_instances' to be a list")
        pulumi.set(__self__, "linked_router_appliance_instances", linked_router_appliance_instances)
        if linked_vpn_tunnels and not isinstance(linked_vpn_tunnels, list):
            raise TypeError("Expected argument 'linked_vpn_tunnels' to be a list")
        pulumi.set(__self__, "linked_vpn_tunnels", linked_vpn_tunnels)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if unique_id and not isinstance(unique_id, str):
            raise TypeError("Expected argument 'unique_id' to be a str")
        pulumi.set(__self__, "unique_id", unique_id)
        if update_time and not isinstance(update_time, str):
            raise TypeError("Expected argument 'update_time' to be a str")
        pulumi.set(__self__, "update_time", update_time)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        The time when the Spoke was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Short description of the spoke resource
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def hub(self) -> str:
        """
        The resource URL of the hub resource that the spoke is attached to
        """
        return pulumi.get(self, "hub")

    @property
    @pulumi.getter
    def labels(self) -> Mapping[str, str]:
        """
        User-defined labels.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter(name="linkedInterconnectAttachments")
    def linked_interconnect_attachments(self) -> Sequence[str]:
        """
        The URIs of linked interconnect attachment resources
        """
        return pulumi.get(self, "linked_interconnect_attachments")

    @property
    @pulumi.getter(name="linkedRouterApplianceInstances")
    def linked_router_appliance_instances(self) -> Sequence['outputs.RouterApplianceInstanceResponse']:
        """
        The URIs of linked Router appliance resources
        """
        return pulumi.get(self, "linked_router_appliance_instances")

    @property
    @pulumi.getter(name="linkedVpnTunnels")
    def linked_vpn_tunnels(self) -> Sequence[str]:
        """
        The URIs of linked VPN tunnel resources
        """
        return pulumi.get(self, "linked_vpn_tunnels")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Immutable. The name of a Spoke resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current lifecycle state of this Hub.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="uniqueId")
    def unique_id(self) -> str:
        """
        Google-generated UUID for this resource. This is unique across all Spoke resources. If a Spoke resource is deleted and another with the same name is created, it gets a different unique_id.
        """
        return pulumi.get(self, "unique_id")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> str:
        """
        The time when the Spoke was updated.
        """
        return pulumi.get(self, "update_time")


class AwaitableGetSpokeResult(GetSpokeResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSpokeResult(
            create_time=self.create_time,
            description=self.description,
            hub=self.hub,
            labels=self.labels,
            linked_interconnect_attachments=self.linked_interconnect_attachments,
            linked_router_appliance_instances=self.linked_router_appliance_instances,
            linked_vpn_tunnels=self.linked_vpn_tunnels,
            name=self.name,
            state=self.state,
            unique_id=self.unique_id,
            update_time=self.update_time)


def get_spoke(location: Optional[str] = None,
              project: Optional[str] = None,
              spoke_id: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSpokeResult:
    """
    Gets details of a single Spoke.
    """
    __args__ = dict()
    __args__['location'] = location
    __args__['project'] = project
    __args__['spokeId'] = spoke_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:networkconnectivity/v1alpha1:getSpoke', __args__, opts=opts, typ=GetSpokeResult).value

    return AwaitableGetSpokeResult(
        create_time=__ret__.create_time,
        description=__ret__.description,
        hub=__ret__.hub,
        labels=__ret__.labels,
        linked_interconnect_attachments=__ret__.linked_interconnect_attachments,
        linked_router_appliance_instances=__ret__.linked_router_appliance_instances,
        linked_vpn_tunnels=__ret__.linked_vpn_tunnels,
        name=__ret__.name,
        state=__ret__.state,
        unique_id=__ret__.unique_id,
        update_time=__ret__.update_time)
