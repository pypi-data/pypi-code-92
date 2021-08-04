# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._inputs import *

__all__ = ['DatabaseArgs', 'Database']

@pulumi.input_type
class DatabaseArgs:
    def __init__(__self__, *,
                 instance: pulumi.Input[str],
                 charset: Optional[pulumi.Input[str]] = None,
                 collation: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 self_link: Optional[pulumi.Input[str]] = None,
                 sqlserver_database_details: Optional[pulumi.Input['SqlServerDatabaseDetailsArgs']] = None):
        """
        The set of arguments for constructing a Database resource.
        :param pulumi.Input[str] instance: The name of the Cloud SQL instance. This does not include the project ID.
        :param pulumi.Input[str] charset: The Cloud SQL charset value.
        :param pulumi.Input[str] collation: The Cloud SQL collation value.
        :param pulumi.Input[str] kind: This is always *sql#database*.
        :param pulumi.Input[str] name: The name of the database in the Cloud SQL instance. This does not include the project ID or instance name.
        :param pulumi.Input[str] project: The project ID of the project containing the Cloud SQL database. The Google apps domain is prefixed if applicable.
        :param pulumi.Input[str] self_link: The URI of this resource.
        """
        pulumi.set(__self__, "instance", instance)
        if charset is not None:
            pulumi.set(__self__, "charset", charset)
        if collation is not None:
            pulumi.set(__self__, "collation", collation)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if self_link is not None:
            pulumi.set(__self__, "self_link", self_link)
        if sqlserver_database_details is not None:
            pulumi.set(__self__, "sqlserver_database_details", sqlserver_database_details)

    @property
    @pulumi.getter
    def instance(self) -> pulumi.Input[str]:
        """
        The name of the Cloud SQL instance. This does not include the project ID.
        """
        return pulumi.get(self, "instance")

    @instance.setter
    def instance(self, value: pulumi.Input[str]):
        pulumi.set(self, "instance", value)

    @property
    @pulumi.getter
    def charset(self) -> Optional[pulumi.Input[str]]:
        """
        The Cloud SQL charset value.
        """
        return pulumi.get(self, "charset")

    @charset.setter
    def charset(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "charset", value)

    @property
    @pulumi.getter
    def collation(self) -> Optional[pulumi.Input[str]]:
        """
        The Cloud SQL collation value.
        """
        return pulumi.get(self, "collation")

    @collation.setter
    def collation(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "collation", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        This is always *sql#database*.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the database in the Cloud SQL instance. This does not include the project ID or instance name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The project ID of the project containing the Cloud SQL database. The Google apps domain is prefixed if applicable.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[str]]:
        """
        The URI of this resource.
        """
        return pulumi.get(self, "self_link")

    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "self_link", value)

    @property
    @pulumi.getter(name="sqlserverDatabaseDetails")
    def sqlserver_database_details(self) -> Optional[pulumi.Input['SqlServerDatabaseDetailsArgs']]:
        return pulumi.get(self, "sqlserver_database_details")

    @sqlserver_database_details.setter
    def sqlserver_database_details(self, value: Optional[pulumi.Input['SqlServerDatabaseDetailsArgs']]):
        pulumi.set(self, "sqlserver_database_details", value)


class Database(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 charset: Optional[pulumi.Input[str]] = None,
                 collation: Optional[pulumi.Input[str]] = None,
                 instance: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 self_link: Optional[pulumi.Input[str]] = None,
                 sqlserver_database_details: Optional[pulumi.Input[pulumi.InputType['SqlServerDatabaseDetailsArgs']]] = None,
                 __props__=None):
        """
        Inserts a resource containing information about a database inside a Cloud SQL instance.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] charset: The Cloud SQL charset value.
        :param pulumi.Input[str] collation: The Cloud SQL collation value.
        :param pulumi.Input[str] instance: The name of the Cloud SQL instance. This does not include the project ID.
        :param pulumi.Input[str] kind: This is always *sql#database*.
        :param pulumi.Input[str] name: The name of the database in the Cloud SQL instance. This does not include the project ID or instance name.
        :param pulumi.Input[str] project: The project ID of the project containing the Cloud SQL database. The Google apps domain is prefixed if applicable.
        :param pulumi.Input[str] self_link: The URI of this resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DatabaseArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Inserts a resource containing information about a database inside a Cloud SQL instance.

        :param str resource_name: The name of the resource.
        :param DatabaseArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DatabaseArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 charset: Optional[pulumi.Input[str]] = None,
                 collation: Optional[pulumi.Input[str]] = None,
                 instance: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 self_link: Optional[pulumi.Input[str]] = None,
                 sqlserver_database_details: Optional[pulumi.Input[pulumi.InputType['SqlServerDatabaseDetailsArgs']]] = None,
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
            __props__ = DatabaseArgs.__new__(DatabaseArgs)

            __props__.__dict__["charset"] = charset
            __props__.__dict__["collation"] = collation
            if instance is None and not opts.urn:
                raise TypeError("Missing required property 'instance'")
            __props__.__dict__["instance"] = instance
            __props__.__dict__["kind"] = kind
            __props__.__dict__["name"] = name
            __props__.__dict__["project"] = project
            __props__.__dict__["self_link"] = self_link
            __props__.__dict__["sqlserver_database_details"] = sqlserver_database_details
        super(Database, __self__).__init__(
            'google-native:sqladmin/v1beta4:Database',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Database':
        """
        Get an existing Database resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DatabaseArgs.__new__(DatabaseArgs)

        __props__.__dict__["charset"] = None
        __props__.__dict__["collation"] = None
        __props__.__dict__["instance"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["project"] = None
        __props__.__dict__["self_link"] = None
        __props__.__dict__["sqlserver_database_details"] = None
        return Database(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def charset(self) -> pulumi.Output[str]:
        """
        The Cloud SQL charset value.
        """
        return pulumi.get(self, "charset")

    @property
    @pulumi.getter
    def collation(self) -> pulumi.Output[str]:
        """
        The Cloud SQL collation value.
        """
        return pulumi.get(self, "collation")

    @property
    @pulumi.getter
    def instance(self) -> pulumi.Output[str]:
        """
        The name of the Cloud SQL instance. This does not include the project ID.
        """
        return pulumi.get(self, "instance")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        This is always *sql#database*.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the database in the Cloud SQL instance. This does not include the project ID or instance name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The project ID of the project containing the Cloud SQL database. The Google apps domain is prefixed if applicable.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[str]:
        """
        The URI of this resource.
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter(name="sqlserverDatabaseDetails")
    def sqlserver_database_details(self) -> pulumi.Output['outputs.SqlServerDatabaseDetailsResponse']:
        return pulumi.get(self, "sqlserver_database_details")

