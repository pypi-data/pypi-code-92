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
    'GetConfigResult',
    'AwaitableGetConfigResult',
    'get_config',
]

@pulumi.output_type
class GetConfigResult:
    def __init__(__self__, create_time=None, description=None, fleet_configs=None, labels=None, name=None, scaling_configs=None, update_time=None):
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if fleet_configs and not isinstance(fleet_configs, list):
            raise TypeError("Expected argument 'fleet_configs' to be a list")
        pulumi.set(__self__, "fleet_configs", fleet_configs)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if scaling_configs and not isinstance(scaling_configs, list):
            raise TypeError("Expected argument 'scaling_configs' to be a list")
        pulumi.set(__self__, "scaling_configs", scaling_configs)
        if update_time and not isinstance(update_time, str):
            raise TypeError("Expected argument 'update_time' to be a str")
        pulumi.set(__self__, "update_time", update_time)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        The creation time.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The description of the game server config.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="fleetConfigs")
    def fleet_configs(self) -> Sequence['outputs.FleetConfigResponse']:
        """
        FleetConfig contains a list of Agones fleet specs. Only one FleetConfig is allowed.
        """
        return pulumi.get(self, "fleet_configs")

    @property
    @pulumi.getter
    def labels(self) -> Mapping[str, str]:
        """
        The labels associated with this game server config. Each label is a key-value pair.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The resource name of the game server config, in the following form: `projects/{project}/locations/{location}/gameServerDeployments/{deployment}/configs/{config}`. For example, `projects/my-project/locations/global/gameServerDeployments/my-game/configs/my-config`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="scalingConfigs")
    def scaling_configs(self) -> Sequence['outputs.ScalingConfigResponse']:
        """
        The autoscaling settings.
        """
        return pulumi.get(self, "scaling_configs")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> str:
        """
        The last-modified time.
        """
        return pulumi.get(self, "update_time")


class AwaitableGetConfigResult(GetConfigResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetConfigResult(
            create_time=self.create_time,
            description=self.description,
            fleet_configs=self.fleet_configs,
            labels=self.labels,
            name=self.name,
            scaling_configs=self.scaling_configs,
            update_time=self.update_time)


def get_config(config_id: Optional[str] = None,
               game_server_deployment_id: Optional[str] = None,
               location: Optional[str] = None,
               project: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetConfigResult:
    """
    Gets details of a single game server config.
    """
    __args__ = dict()
    __args__['configId'] = config_id
    __args__['gameServerDeploymentId'] = game_server_deployment_id
    __args__['location'] = location
    __args__['project'] = project
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:gameservices/v1:getConfig', __args__, opts=opts, typ=GetConfigResult).value

    return AwaitableGetConfigResult(
        create_time=__ret__.create_time,
        description=__ret__.description,
        fleet_configs=__ret__.fleet_configs,
        labels=__ret__.labels,
        name=__ret__.name,
        scaling_configs=__ret__.scaling_configs,
        update_time=__ret__.update_time)
