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

__all__ = ['IndexArgs', 'Index']

@pulumi.input_type
class IndexArgs:
    def __init__(__self__, *,
                 database_id: pulumi.Input[str],
                 collection_id: Optional[pulumi.Input[str]] = None,
                 fields: Optional[pulumi.Input[Sequence[pulumi.Input['GoogleFirestoreAdminV1beta1IndexFieldArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input['IndexState']] = None):
        """
        The set of arguments for constructing a Index resource.
        :param pulumi.Input[str] collection_id: The collection ID to which this index applies. Required.
        :param pulumi.Input[Sequence[pulumi.Input['GoogleFirestoreAdminV1beta1IndexFieldArgs']]] fields: The fields to index.
        :param pulumi.Input[str] name: The resource name of the index. Output only.
        :param pulumi.Input['IndexState'] state: The state of the index. Output only.
        """
        pulumi.set(__self__, "database_id", database_id)
        if collection_id is not None:
            pulumi.set(__self__, "collection_id", collection_id)
        if fields is not None:
            pulumi.set(__self__, "fields", fields)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if state is not None:
            pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="databaseId")
    def database_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "database_id")

    @database_id.setter
    def database_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "database_id", value)

    @property
    @pulumi.getter(name="collectionId")
    def collection_id(self) -> Optional[pulumi.Input[str]]:
        """
        The collection ID to which this index applies. Required.
        """
        return pulumi.get(self, "collection_id")

    @collection_id.setter
    def collection_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "collection_id", value)

    @property
    @pulumi.getter
    def fields(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['GoogleFirestoreAdminV1beta1IndexFieldArgs']]]]:
        """
        The fields to index.
        """
        return pulumi.get(self, "fields")

    @fields.setter
    def fields(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['GoogleFirestoreAdminV1beta1IndexFieldArgs']]]]):
        pulumi.set(self, "fields", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The resource name of the index. Output only.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input['IndexState']]:
        """
        The state of the index. Output only.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input['IndexState']]):
        pulumi.set(self, "state", value)


class Index(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 collection_id: Optional[pulumi.Input[str]] = None,
                 database_id: Optional[pulumi.Input[str]] = None,
                 fields: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleFirestoreAdminV1beta1IndexFieldArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input['IndexState']] = None,
                 __props__=None):
        """
        Creates the specified index. A newly created index's initial state is `CREATING`. On completion of the returned google.longrunning.Operation, the state will be `READY`. If the index already exists, the call will return an `ALREADY_EXISTS` status. During creation, the process could result in an error, in which case the index will move to the `ERROR` state. The process can be recovered by fixing the data that caused the error, removing the index with delete, then re-creating the index with create. Indexes with a single field cannot be created.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] collection_id: The collection ID to which this index applies. Required.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleFirestoreAdminV1beta1IndexFieldArgs']]]] fields: The fields to index.
        :param pulumi.Input[str] name: The resource name of the index. Output only.
        :param pulumi.Input['IndexState'] state: The state of the index. Output only.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IndexArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates the specified index. A newly created index's initial state is `CREATING`. On completion of the returned google.longrunning.Operation, the state will be `READY`. If the index already exists, the call will return an `ALREADY_EXISTS` status. During creation, the process could result in an error, in which case the index will move to the `ERROR` state. The process can be recovered by fixing the data that caused the error, removing the index with delete, then re-creating the index with create. Indexes with a single field cannot be created.

        :param str resource_name: The name of the resource.
        :param IndexArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IndexArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 collection_id: Optional[pulumi.Input[str]] = None,
                 database_id: Optional[pulumi.Input[str]] = None,
                 fields: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleFirestoreAdminV1beta1IndexFieldArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input['IndexState']] = None,
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
            __props__ = IndexArgs.__new__(IndexArgs)

            __props__.__dict__["collection_id"] = collection_id
            if database_id is None and not opts.urn:
                raise TypeError("Missing required property 'database_id'")
            __props__.__dict__["database_id"] = database_id
            __props__.__dict__["fields"] = fields
            __props__.__dict__["name"] = name
            __props__.__dict__["project"] = project
            __props__.__dict__["state"] = state
        super(Index, __self__).__init__(
            'google-native:firestore/v1beta1:Index',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Index':
        """
        Get an existing Index resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = IndexArgs.__new__(IndexArgs)

        __props__.__dict__["collection_id"] = None
        __props__.__dict__["fields"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["state"] = None
        return Index(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="collectionId")
    def collection_id(self) -> pulumi.Output[str]:
        """
        The collection ID to which this index applies. Required.
        """
        return pulumi.get(self, "collection_id")

    @property
    @pulumi.getter
    def fields(self) -> pulumi.Output[Sequence['outputs.GoogleFirestoreAdminV1beta1IndexFieldResponse']]:
        """
        The fields to index.
        """
        return pulumi.get(self, "fields")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The resource name of the index. Output only.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The state of the index. Output only.
        """
        return pulumi.get(self, "state")

