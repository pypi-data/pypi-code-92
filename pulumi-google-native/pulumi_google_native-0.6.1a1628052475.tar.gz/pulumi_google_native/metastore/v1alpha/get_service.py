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
    'GetServiceResult',
    'AwaitableGetServiceResult',
    'get_service',
]

@pulumi.output_type
class GetServiceResult:
    def __init__(__self__, artifact_gcs_uri=None, create_time=None, encryption_config=None, endpoint_uri=None, hive_metastore_config=None, labels=None, maintenance_window=None, metadata_integration=None, metadata_management_activity=None, name=None, network=None, port=None, release_channel=None, state=None, state_message=None, tier=None, uid=None, update_time=None):
        if artifact_gcs_uri and not isinstance(artifact_gcs_uri, str):
            raise TypeError("Expected argument 'artifact_gcs_uri' to be a str")
        pulumi.set(__self__, "artifact_gcs_uri", artifact_gcs_uri)
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if encryption_config and not isinstance(encryption_config, dict):
            raise TypeError("Expected argument 'encryption_config' to be a dict")
        pulumi.set(__self__, "encryption_config", encryption_config)
        if endpoint_uri and not isinstance(endpoint_uri, str):
            raise TypeError("Expected argument 'endpoint_uri' to be a str")
        pulumi.set(__self__, "endpoint_uri", endpoint_uri)
        if hive_metastore_config and not isinstance(hive_metastore_config, dict):
            raise TypeError("Expected argument 'hive_metastore_config' to be a dict")
        pulumi.set(__self__, "hive_metastore_config", hive_metastore_config)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if maintenance_window and not isinstance(maintenance_window, dict):
            raise TypeError("Expected argument 'maintenance_window' to be a dict")
        pulumi.set(__self__, "maintenance_window", maintenance_window)
        if metadata_integration and not isinstance(metadata_integration, dict):
            raise TypeError("Expected argument 'metadata_integration' to be a dict")
        pulumi.set(__self__, "metadata_integration", metadata_integration)
        if metadata_management_activity and not isinstance(metadata_management_activity, dict):
            raise TypeError("Expected argument 'metadata_management_activity' to be a dict")
        pulumi.set(__self__, "metadata_management_activity", metadata_management_activity)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network and not isinstance(network, str):
            raise TypeError("Expected argument 'network' to be a str")
        pulumi.set(__self__, "network", network)
        if port and not isinstance(port, int):
            raise TypeError("Expected argument 'port' to be a int")
        pulumi.set(__self__, "port", port)
        if release_channel and not isinstance(release_channel, str):
            raise TypeError("Expected argument 'release_channel' to be a str")
        pulumi.set(__self__, "release_channel", release_channel)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if state_message and not isinstance(state_message, str):
            raise TypeError("Expected argument 'state_message' to be a str")
        pulumi.set(__self__, "state_message", state_message)
        if tier and not isinstance(tier, str):
            raise TypeError("Expected argument 'tier' to be a str")
        pulumi.set(__self__, "tier", tier)
        if uid and not isinstance(uid, str):
            raise TypeError("Expected argument 'uid' to be a str")
        pulumi.set(__self__, "uid", uid)
        if update_time and not isinstance(update_time, str):
            raise TypeError("Expected argument 'update_time' to be a str")
        pulumi.set(__self__, "update_time", update_time)

    @property
    @pulumi.getter(name="artifactGcsUri")
    def artifact_gcs_uri(self) -> str:
        """
        A Cloud Storage URI (starting with gs://) that specifies where artifacts related to the metastore service are stored.
        """
        return pulumi.get(self, "artifact_gcs_uri")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        The time when the metastore service was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="encryptionConfig")
    def encryption_config(self) -> 'outputs.EncryptionConfigResponse':
        """
        Immutable. Information used to configure the Dataproc Metastore service to encrypt customer data at rest. Cannot be updated.
        """
        return pulumi.get(self, "encryption_config")

    @property
    @pulumi.getter(name="endpointUri")
    def endpoint_uri(self) -> str:
        """
        The URI of the endpoint used to access the metastore service.
        """
        return pulumi.get(self, "endpoint_uri")

    @property
    @pulumi.getter(name="hiveMetastoreConfig")
    def hive_metastore_config(self) -> 'outputs.HiveMetastoreConfigResponse':
        """
        Configuration information specific to running Hive metastore software as the metastore service.
        """
        return pulumi.get(self, "hive_metastore_config")

    @property
    @pulumi.getter
    def labels(self) -> Mapping[str, str]:
        """
        User-defined labels for the metastore service.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> 'outputs.MaintenanceWindowResponse':
        """
        The one hour maintenance window of the metastore service. This specifies when the service can be restarted for maintenance purposes in UTC time.
        """
        return pulumi.get(self, "maintenance_window")

    @property
    @pulumi.getter(name="metadataIntegration")
    def metadata_integration(self) -> 'outputs.MetadataIntegrationResponse':
        """
        The setting that defines how metastore metadata should be integrated with external services and systems.
        """
        return pulumi.get(self, "metadata_integration")

    @property
    @pulumi.getter(name="metadataManagementActivity")
    def metadata_management_activity(self) -> 'outputs.MetadataManagementActivityResponse':
        """
        The metadata management activities of the metastore service.
        """
        return pulumi.get(self, "metadata_management_activity")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Immutable. The relative resource name of the metastore service, of the form:projects/{project_number}/locations/{location_id}/services/{service_id}.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def network(self) -> str:
        """
        Immutable. The relative resource name of the VPC network on which the instance can be accessed. It is specified in the following form:projects/{project_number}/global/networks/{network_id}.
        """
        return pulumi.get(self, "network")

    @property
    @pulumi.getter
    def port(self) -> int:
        """
        The TCP port at which the metastore service is reached. Default: 9083.
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter(name="releaseChannel")
    def release_channel(self) -> str:
        """
        Immutable. The release channel of the service. If unspecified, defaults to STABLE.
        """
        return pulumi.get(self, "release_channel")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current state of the metastore service.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="stateMessage")
    def state_message(self) -> str:
        """
        Additional information about the current state of the metastore service, if available.
        """
        return pulumi.get(self, "state_message")

    @property
    @pulumi.getter
    def tier(self) -> str:
        """
        The tier of the service.
        """
        return pulumi.get(self, "tier")

    @property
    @pulumi.getter
    def uid(self) -> str:
        """
        The globally unique resource identifier of the metastore service.
        """
        return pulumi.get(self, "uid")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> str:
        """
        The time when the metastore service was last updated.
        """
        return pulumi.get(self, "update_time")


class AwaitableGetServiceResult(GetServiceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetServiceResult(
            artifact_gcs_uri=self.artifact_gcs_uri,
            create_time=self.create_time,
            encryption_config=self.encryption_config,
            endpoint_uri=self.endpoint_uri,
            hive_metastore_config=self.hive_metastore_config,
            labels=self.labels,
            maintenance_window=self.maintenance_window,
            metadata_integration=self.metadata_integration,
            metadata_management_activity=self.metadata_management_activity,
            name=self.name,
            network=self.network,
            port=self.port,
            release_channel=self.release_channel,
            state=self.state,
            state_message=self.state_message,
            tier=self.tier,
            uid=self.uid,
            update_time=self.update_time)


def get_service(location: Optional[str] = None,
                project: Optional[str] = None,
                service_id: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetServiceResult:
    """
    Gets the details of a single service.
    """
    __args__ = dict()
    __args__['location'] = location
    __args__['project'] = project
    __args__['serviceId'] = service_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:metastore/v1alpha:getService', __args__, opts=opts, typ=GetServiceResult).value

    return AwaitableGetServiceResult(
        artifact_gcs_uri=__ret__.artifact_gcs_uri,
        create_time=__ret__.create_time,
        encryption_config=__ret__.encryption_config,
        endpoint_uri=__ret__.endpoint_uri,
        hive_metastore_config=__ret__.hive_metastore_config,
        labels=__ret__.labels,
        maintenance_window=__ret__.maintenance_window,
        metadata_integration=__ret__.metadata_integration,
        metadata_management_activity=__ret__.metadata_management_activity,
        name=__ret__.name,
        network=__ret__.network,
        port=__ret__.port,
        release_channel=__ret__.release_channel,
        state=__ret__.state,
        state_message=__ret__.state_message,
        tier=__ret__.tier,
        uid=__ret__.uid,
        update_time=__ret__.update_time)
