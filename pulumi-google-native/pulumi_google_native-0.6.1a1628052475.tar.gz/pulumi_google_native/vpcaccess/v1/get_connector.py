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
    'GetConnectorResult',
    'AwaitableGetConnectorResult',
    'get_connector',
]

@pulumi.output_type
class GetConnectorResult:
    def __init__(__self__, connected_projects=None, ip_cidr_range=None, machine_type=None, max_instances=None, max_throughput=None, min_instances=None, min_throughput=None, name=None, network=None, state=None, subnet=None):
        if connected_projects and not isinstance(connected_projects, list):
            raise TypeError("Expected argument 'connected_projects' to be a list")
        pulumi.set(__self__, "connected_projects", connected_projects)
        if ip_cidr_range and not isinstance(ip_cidr_range, str):
            raise TypeError("Expected argument 'ip_cidr_range' to be a str")
        pulumi.set(__self__, "ip_cidr_range", ip_cidr_range)
        if machine_type and not isinstance(machine_type, str):
            raise TypeError("Expected argument 'machine_type' to be a str")
        pulumi.set(__self__, "machine_type", machine_type)
        if max_instances and not isinstance(max_instances, int):
            raise TypeError("Expected argument 'max_instances' to be a int")
        pulumi.set(__self__, "max_instances", max_instances)
        if max_throughput and not isinstance(max_throughput, int):
            raise TypeError("Expected argument 'max_throughput' to be a int")
        pulumi.set(__self__, "max_throughput", max_throughput)
        if min_instances and not isinstance(min_instances, int):
            raise TypeError("Expected argument 'min_instances' to be a int")
        pulumi.set(__self__, "min_instances", min_instances)
        if min_throughput and not isinstance(min_throughput, int):
            raise TypeError("Expected argument 'min_throughput' to be a int")
        pulumi.set(__self__, "min_throughput", min_throughput)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network and not isinstance(network, str):
            raise TypeError("Expected argument 'network' to be a str")
        pulumi.set(__self__, "network", network)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if subnet and not isinstance(subnet, dict):
            raise TypeError("Expected argument 'subnet' to be a dict")
        pulumi.set(__self__, "subnet", subnet)

    @property
    @pulumi.getter(name="connectedProjects")
    def connected_projects(self) -> Sequence[str]:
        """
        List of projects using the connector.
        """
        return pulumi.get(self, "connected_projects")

    @property
    @pulumi.getter(name="ipCidrRange")
    def ip_cidr_range(self) -> str:
        """
        The range of internal addresses that follows RFC 4632 notation. Example: `10.132.0.0/28`.
        """
        return pulumi.get(self, "ip_cidr_range")

    @property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> str:
        """
        Machine type of VM Instance underlying connector. Default is e2-micro
        """
        return pulumi.get(self, "machine_type")

    @property
    @pulumi.getter(name="maxInstances")
    def max_instances(self) -> int:
        """
        Maximum value of instances in autoscaling group underlying the connector.
        """
        return pulumi.get(self, "max_instances")

    @property
    @pulumi.getter(name="maxThroughput")
    def max_throughput(self) -> int:
        """
        Maximum throughput of the connector in Mbps. Default is 300, max is 1000.
        """
        return pulumi.get(self, "max_throughput")

    @property
    @pulumi.getter(name="minInstances")
    def min_instances(self) -> int:
        """
        Minimum value of instances in autoscaling group underlying the connector.
        """
        return pulumi.get(self, "min_instances")

    @property
    @pulumi.getter(name="minThroughput")
    def min_throughput(self) -> int:
        """
        Minimum throughput of the connector in Mbps. Default and min is 200.
        """
        return pulumi.get(self, "min_throughput")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The resource name in the format `projects/*/locations/*/connectors/*`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def network(self) -> str:
        """
        Name of a VPC network.
        """
        return pulumi.get(self, "network")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        State of the VPC access connector.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def subnet(self) -> 'outputs.SubnetResponse':
        """
        The subnet in which to house the VPC Access Connector.
        """
        return pulumi.get(self, "subnet")


class AwaitableGetConnectorResult(GetConnectorResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetConnectorResult(
            connected_projects=self.connected_projects,
            ip_cidr_range=self.ip_cidr_range,
            machine_type=self.machine_type,
            max_instances=self.max_instances,
            max_throughput=self.max_throughput,
            min_instances=self.min_instances,
            min_throughput=self.min_throughput,
            name=self.name,
            network=self.network,
            state=self.state,
            subnet=self.subnet)


def get_connector(connector_id: Optional[str] = None,
                  location: Optional[str] = None,
                  project: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetConnectorResult:
    """
    Gets a Serverless VPC Access connector. Returns NOT_FOUND if the resource does not exist.
    """
    __args__ = dict()
    __args__['connectorId'] = connector_id
    __args__['location'] = location
    __args__['project'] = project
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:vpcaccess/v1:getConnector', __args__, opts=opts, typ=GetConnectorResult).value

    return AwaitableGetConnectorResult(
        connected_projects=__ret__.connected_projects,
        ip_cidr_range=__ret__.ip_cidr_range,
        machine_type=__ret__.machine_type,
        max_instances=__ret__.max_instances,
        max_throughput=__ret__.max_throughput,
        min_instances=__ret__.min_instances,
        min_throughput=__ret__.min_throughput,
        name=__ret__.name,
        network=__ret__.network,
        state=__ret__.state,
        subnet=__ret__.subnet)
