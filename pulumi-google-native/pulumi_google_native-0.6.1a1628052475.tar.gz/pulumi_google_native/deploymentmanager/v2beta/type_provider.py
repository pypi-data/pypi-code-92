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

__all__ = ['TypeProviderArgs', 'TypeProvider']

@pulumi.input_type
class TypeProviderArgs:
    def __init__(__self__, *,
                 collection_overrides: Optional[pulumi.Input[Sequence[pulumi.Input['CollectionOverrideArgs']]]] = None,
                 credential: Optional[pulumi.Input['CredentialArgs']] = None,
                 custom_certificate_authority_roots: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 descriptor_url: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Sequence[pulumi.Input['TypeProviderLabelEntryArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 options: Optional[pulumi.Input['OptionsArgs']] = None,
                 project: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a TypeProvider resource.
        :param pulumi.Input[Sequence[pulumi.Input['CollectionOverrideArgs']]] collection_overrides: Allows resource handling overrides for specific collections
        :param pulumi.Input['CredentialArgs'] credential: Credential used when interacting with this type.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] custom_certificate_authority_roots: List of up to 2 custom certificate authority roots to use for TLS authentication when making calls on behalf of this type provider. If set, TLS authentication will exclusively use these roots instead of relying on publicly trusted certificate authorities when validating TLS certificate authenticity. The certificates must be in base64-encoded PEM format. The maximum size of each certificate must not exceed 10KB.
        :param pulumi.Input[str] description: An optional textual description of the resource; provided by the client when the resource is created.
        :param pulumi.Input[str] descriptor_url: Descriptor Url for the this type provider.
        :param pulumi.Input[Sequence[pulumi.Input['TypeProviderLabelEntryArgs']]] labels: Map of One Platform labels; provided by the client when the resource is created or updated. Specifically: Label keys must be between 1 and 63 characters long and must conform to the following regular expression: `[a-z]([-a-z0-9]*[a-z0-9])?` Label values must be between 0 and 63 characters long and must conform to the regular expression `([a-z]([-a-z0-9]*[a-z0-9])?)?`
        :param pulumi.Input[str] name: Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        :param pulumi.Input['OptionsArgs'] options: Options to apply when handling any resources in this service.
        """
        if collection_overrides is not None:
            pulumi.set(__self__, "collection_overrides", collection_overrides)
        if credential is not None:
            pulumi.set(__self__, "credential", credential)
        if custom_certificate_authority_roots is not None:
            pulumi.set(__self__, "custom_certificate_authority_roots", custom_certificate_authority_roots)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if descriptor_url is not None:
            pulumi.set(__self__, "descriptor_url", descriptor_url)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if options is not None:
            pulumi.set(__self__, "options", options)
        if project is not None:
            pulumi.set(__self__, "project", project)

    @property
    @pulumi.getter(name="collectionOverrides")
    def collection_overrides(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CollectionOverrideArgs']]]]:
        """
        Allows resource handling overrides for specific collections
        """
        return pulumi.get(self, "collection_overrides")

    @collection_overrides.setter
    def collection_overrides(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CollectionOverrideArgs']]]]):
        pulumi.set(self, "collection_overrides", value)

    @property
    @pulumi.getter
    def credential(self) -> Optional[pulumi.Input['CredentialArgs']]:
        """
        Credential used when interacting with this type.
        """
        return pulumi.get(self, "credential")

    @credential.setter
    def credential(self, value: Optional[pulumi.Input['CredentialArgs']]):
        pulumi.set(self, "credential", value)

    @property
    @pulumi.getter(name="customCertificateAuthorityRoots")
    def custom_certificate_authority_roots(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of up to 2 custom certificate authority roots to use for TLS authentication when making calls on behalf of this type provider. If set, TLS authentication will exclusively use these roots instead of relying on publicly trusted certificate authorities when validating TLS certificate authenticity. The certificates must be in base64-encoded PEM format. The maximum size of each certificate must not exceed 10KB.
        """
        return pulumi.get(self, "custom_certificate_authority_roots")

    @custom_certificate_authority_roots.setter
    def custom_certificate_authority_roots(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "custom_certificate_authority_roots", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        An optional textual description of the resource; provided by the client when the resource is created.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="descriptorUrl")
    def descriptor_url(self) -> Optional[pulumi.Input[str]]:
        """
        Descriptor Url for the this type provider.
        """
        return pulumi.get(self, "descriptor_url")

    @descriptor_url.setter
    def descriptor_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "descriptor_url", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TypeProviderLabelEntryArgs']]]]:
        """
        Map of One Platform labels; provided by the client when the resource is created or updated. Specifically: Label keys must be between 1 and 63 characters long and must conform to the following regular expression: `[a-z]([-a-z0-9]*[a-z0-9])?` Label values must be between 0 and 63 characters long and must conform to the regular expression `([a-z]([-a-z0-9]*[a-z0-9])?)?`
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TypeProviderLabelEntryArgs']]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def options(self) -> Optional[pulumi.Input['OptionsArgs']]:
        """
        Options to apply when handling any resources in this service.
        """
        return pulumi.get(self, "options")

    @options.setter
    def options(self, value: Optional[pulumi.Input['OptionsArgs']]):
        pulumi.set(self, "options", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)


class TypeProvider(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 collection_overrides: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CollectionOverrideArgs']]]]] = None,
                 credential: Optional[pulumi.Input[pulumi.InputType['CredentialArgs']]] = None,
                 custom_certificate_authority_roots: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 descriptor_url: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TypeProviderLabelEntryArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 options: Optional[pulumi.Input[pulumi.InputType['OptionsArgs']]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a type provider.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CollectionOverrideArgs']]]] collection_overrides: Allows resource handling overrides for specific collections
        :param pulumi.Input[pulumi.InputType['CredentialArgs']] credential: Credential used when interacting with this type.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] custom_certificate_authority_roots: List of up to 2 custom certificate authority roots to use for TLS authentication when making calls on behalf of this type provider. If set, TLS authentication will exclusively use these roots instead of relying on publicly trusted certificate authorities when validating TLS certificate authenticity. The certificates must be in base64-encoded PEM format. The maximum size of each certificate must not exceed 10KB.
        :param pulumi.Input[str] description: An optional textual description of the resource; provided by the client when the resource is created.
        :param pulumi.Input[str] descriptor_url: Descriptor Url for the this type provider.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TypeProviderLabelEntryArgs']]]] labels: Map of One Platform labels; provided by the client when the resource is created or updated. Specifically: Label keys must be between 1 and 63 characters long and must conform to the following regular expression: `[a-z]([-a-z0-9]*[a-z0-9])?` Label values must be between 0 and 63 characters long and must conform to the regular expression `([a-z]([-a-z0-9]*[a-z0-9])?)?`
        :param pulumi.Input[str] name: Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        :param pulumi.Input[pulumi.InputType['OptionsArgs']] options: Options to apply when handling any resources in this service.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[TypeProviderArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a type provider.

        :param str resource_name: The name of the resource.
        :param TypeProviderArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TypeProviderArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 collection_overrides: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CollectionOverrideArgs']]]]] = None,
                 credential: Optional[pulumi.Input[pulumi.InputType['CredentialArgs']]] = None,
                 custom_certificate_authority_roots: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 descriptor_url: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TypeProviderLabelEntryArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 options: Optional[pulumi.Input[pulumi.InputType['OptionsArgs']]] = None,
                 project: Optional[pulumi.Input[str]] = None,
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
            __props__ = TypeProviderArgs.__new__(TypeProviderArgs)

            __props__.__dict__["collection_overrides"] = collection_overrides
            __props__.__dict__["credential"] = credential
            __props__.__dict__["custom_certificate_authority_roots"] = custom_certificate_authority_roots
            __props__.__dict__["description"] = description
            __props__.__dict__["descriptor_url"] = descriptor_url
            __props__.__dict__["labels"] = labels
            __props__.__dict__["name"] = name
            __props__.__dict__["options"] = options
            __props__.__dict__["project"] = project
            __props__.__dict__["insert_time"] = None
            __props__.__dict__["operation"] = None
            __props__.__dict__["self_link"] = None
        super(TypeProvider, __self__).__init__(
            'google-native:deploymentmanager/v2beta:TypeProvider',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'TypeProvider':
        """
        Get an existing TypeProvider resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = TypeProviderArgs.__new__(TypeProviderArgs)

        __props__.__dict__["collection_overrides"] = None
        __props__.__dict__["credential"] = None
        __props__.__dict__["custom_certificate_authority_roots"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["descriptor_url"] = None
        __props__.__dict__["insert_time"] = None
        __props__.__dict__["labels"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["operation"] = None
        __props__.__dict__["options"] = None
        __props__.__dict__["self_link"] = None
        return TypeProvider(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="collectionOverrides")
    def collection_overrides(self) -> pulumi.Output[Sequence['outputs.CollectionOverrideResponse']]:
        """
        Allows resource handling overrides for specific collections
        """
        return pulumi.get(self, "collection_overrides")

    @property
    @pulumi.getter
    def credential(self) -> pulumi.Output['outputs.CredentialResponse']:
        """
        Credential used when interacting with this type.
        """
        return pulumi.get(self, "credential")

    @property
    @pulumi.getter(name="customCertificateAuthorityRoots")
    def custom_certificate_authority_roots(self) -> pulumi.Output[Sequence[str]]:
        """
        List of up to 2 custom certificate authority roots to use for TLS authentication when making calls on behalf of this type provider. If set, TLS authentication will exclusively use these roots instead of relying on publicly trusted certificate authorities when validating TLS certificate authenticity. The certificates must be in base64-encoded PEM format. The maximum size of each certificate must not exceed 10KB.
        """
        return pulumi.get(self, "custom_certificate_authority_roots")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        An optional textual description of the resource; provided by the client when the resource is created.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="descriptorUrl")
    def descriptor_url(self) -> pulumi.Output[str]:
        """
        Descriptor Url for the this type provider.
        """
        return pulumi.get(self, "descriptor_url")

    @property
    @pulumi.getter(name="insertTime")
    def insert_time(self) -> pulumi.Output[str]:
        """
        Creation timestamp in RFC3339 text format.
        """
        return pulumi.get(self, "insert_time")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Sequence['outputs.TypeProviderLabelEntryResponse']]:
        """
        Map of One Platform labels; provided by the client when the resource is created or updated. Specifically: Label keys must be between 1 and 63 characters long and must conform to the following regular expression: `[a-z]([-a-z0-9]*[a-z0-9])?` Label values must be between 0 and 63 characters long and must conform to the regular expression `([a-z]([-a-z0-9]*[a-z0-9])?)?`
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def operation(self) -> pulumi.Output['outputs.OperationResponse']:
        """
        The Operation that most recently ran, or is currently running, on this type provider.
        """
        return pulumi.get(self, "operation")

    @property
    @pulumi.getter
    def options(self) -> pulumi.Output['outputs.OptionsResponse']:
        """
        Options to apply when handling any resources in this service.
        """
        return pulumi.get(self, "options")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[str]:
        """
        Self link for the type provider.
        """
        return pulumi.get(self, "self_link")

