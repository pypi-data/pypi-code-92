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

__all__ = ['DicomStoreArgs', 'DicomStore']

@pulumi.input_type
class DicomStoreArgs:
    def __init__(__self__, *,
                 dataset_id: pulumi.Input[str],
                 dicom_store_id: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 notification_config: Optional[pulumi.Input['NotificationConfigArgs']] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 stream_configs: Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudHealthcareV1beta1DicomStreamConfigArgs']]]] = None):
        """
        The set of arguments for constructing a DicomStore resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: User-supplied key-value pairs used to organize DICOM stores. Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: \p{Ll}\p{Lo}{0,62} Label values are optional, must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: [\p{Ll}\p{Lo}\p{N}_-]{0,63} No more than 64 labels can be associated with a given store.
        :param pulumi.Input[str] name: Resource name of the DICOM store, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/dicomStores/{dicom_store_id}`.
        :param pulumi.Input['NotificationConfigArgs'] notification_config: Notification destination for new DICOM instances. Supplied by the client.
        :param pulumi.Input[Sequence[pulumi.Input['GoogleCloudHealthcareV1beta1DicomStreamConfigArgs']]] stream_configs: A list of streaming configs used to configure the destination of streaming exports for every DICOM instance insertion in this DICOM store. After a new config is added to `stream_configs`, DICOM instance insertions are streamed to the new destination. When a config is removed from `stream_configs`, the server stops streaming to that destination. Each config must contain a unique destination.
        """
        pulumi.set(__self__, "dataset_id", dataset_id)
        if dicom_store_id is not None:
            pulumi.set(__self__, "dicom_store_id", dicom_store_id)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if notification_config is not None:
            pulumi.set(__self__, "notification_config", notification_config)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if stream_configs is not None:
            pulumi.set(__self__, "stream_configs", stream_configs)

    @property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "dataset_id")

    @dataset_id.setter
    def dataset_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "dataset_id", value)

    @property
    @pulumi.getter(name="dicomStoreId")
    def dicom_store_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "dicom_store_id")

    @dicom_store_id.setter
    def dicom_store_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dicom_store_id", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        User-supplied key-value pairs used to organize DICOM stores. Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: \p{Ll}\p{Lo}{0,62} Label values are optional, must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: [\p{Ll}\p{Lo}\p{N}_-]{0,63} No more than 64 labels can be associated with a given store.
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
        Resource name of the DICOM store, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/dicomStores/{dicom_store_id}`.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="notificationConfig")
    def notification_config(self) -> Optional[pulumi.Input['NotificationConfigArgs']]:
        """
        Notification destination for new DICOM instances. Supplied by the client.
        """
        return pulumi.get(self, "notification_config")

    @notification_config.setter
    def notification_config(self, value: Optional[pulumi.Input['NotificationConfigArgs']]):
        pulumi.set(self, "notification_config", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter(name="streamConfigs")
    def stream_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudHealthcareV1beta1DicomStreamConfigArgs']]]]:
        """
        A list of streaming configs used to configure the destination of streaming exports for every DICOM instance insertion in this DICOM store. After a new config is added to `stream_configs`, DICOM instance insertions are streamed to the new destination. When a config is removed from `stream_configs`, the server stops streaming to that destination. Each config must contain a unique destination.
        """
        return pulumi.get(self, "stream_configs")

    @stream_configs.setter
    def stream_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudHealthcareV1beta1DicomStreamConfigArgs']]]]):
        pulumi.set(self, "stream_configs", value)


class DicomStore(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dataset_id: Optional[pulumi.Input[str]] = None,
                 dicom_store_id: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 notification_config: Optional[pulumi.Input[pulumi.InputType['NotificationConfigArgs']]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 stream_configs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudHealthcareV1beta1DicomStreamConfigArgs']]]]] = None,
                 __props__=None):
        """
        Creates a new DICOM store within the parent dataset.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: User-supplied key-value pairs used to organize DICOM stores. Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: \p{Ll}\p{Lo}{0,62} Label values are optional, must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: [\p{Ll}\p{Lo}\p{N}_-]{0,63} No more than 64 labels can be associated with a given store.
        :param pulumi.Input[str] name: Resource name of the DICOM store, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/dicomStores/{dicom_store_id}`.
        :param pulumi.Input[pulumi.InputType['NotificationConfigArgs']] notification_config: Notification destination for new DICOM instances. Supplied by the client.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudHealthcareV1beta1DicomStreamConfigArgs']]]] stream_configs: A list of streaming configs used to configure the destination of streaming exports for every DICOM instance insertion in this DICOM store. After a new config is added to `stream_configs`, DICOM instance insertions are streamed to the new destination. When a config is removed from `stream_configs`, the server stops streaming to that destination. Each config must contain a unique destination.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DicomStoreArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a new DICOM store within the parent dataset.

        :param str resource_name: The name of the resource.
        :param DicomStoreArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DicomStoreArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dataset_id: Optional[pulumi.Input[str]] = None,
                 dicom_store_id: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 notification_config: Optional[pulumi.Input[pulumi.InputType['NotificationConfigArgs']]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 stream_configs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudHealthcareV1beta1DicomStreamConfigArgs']]]]] = None,
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
            __props__ = DicomStoreArgs.__new__(DicomStoreArgs)

            if dataset_id is None and not opts.urn:
                raise TypeError("Missing required property 'dataset_id'")
            __props__.__dict__["dataset_id"] = dataset_id
            __props__.__dict__["dicom_store_id"] = dicom_store_id
            __props__.__dict__["labels"] = labels
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            __props__.__dict__["notification_config"] = notification_config
            __props__.__dict__["project"] = project
            __props__.__dict__["stream_configs"] = stream_configs
        super(DicomStore, __self__).__init__(
            'google-native:healthcare/v1beta1:DicomStore',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DicomStore':
        """
        Get an existing DicomStore resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DicomStoreArgs.__new__(DicomStoreArgs)

        __props__.__dict__["labels"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["notification_config"] = None
        __props__.__dict__["stream_configs"] = None
        return DicomStore(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Mapping[str, str]]:
        """
        User-supplied key-value pairs used to organize DICOM stores. Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: \p{Ll}\p{Lo}{0,62} Label values are optional, must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: [\p{Ll}\p{Lo}\p{N}_-]{0,63} No more than 64 labels can be associated with a given store.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name of the DICOM store, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/dicomStores/{dicom_store_id}`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="notificationConfig")
    def notification_config(self) -> pulumi.Output['outputs.NotificationConfigResponse']:
        """
        Notification destination for new DICOM instances. Supplied by the client.
        """
        return pulumi.get(self, "notification_config")

    @property
    @pulumi.getter(name="streamConfigs")
    def stream_configs(self) -> pulumi.Output[Sequence['outputs.GoogleCloudHealthcareV1beta1DicomStreamConfigResponse']]:
        """
        A list of streaming configs used to configure the destination of streaming exports for every DICOM instance insertion in this DICOM store. After a new config is added to `stream_configs`, DICOM instance insertions are streamed to the new destination. When a config is removed from `stream_configs`, the server stops streaming to that destination. Each config must contain a unique destination.
        """
        return pulumi.get(self, "stream_configs")

