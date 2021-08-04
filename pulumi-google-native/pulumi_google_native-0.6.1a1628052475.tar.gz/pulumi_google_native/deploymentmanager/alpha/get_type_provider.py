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
    'GetTypeProviderResult',
    'AwaitableGetTypeProviderResult',
    'get_type_provider',
]

@pulumi.output_type
class GetTypeProviderResult:
    def __init__(__self__, collection_overrides=None, credential=None, custom_certificate_authority_roots=None, description=None, descriptor_url=None, insert_time=None, labels=None, name=None, operation=None, options=None, self_link=None):
        if collection_overrides and not isinstance(collection_overrides, list):
            raise TypeError("Expected argument 'collection_overrides' to be a list")
        pulumi.set(__self__, "collection_overrides", collection_overrides)
        if credential and not isinstance(credential, dict):
            raise TypeError("Expected argument 'credential' to be a dict")
        pulumi.set(__self__, "credential", credential)
        if custom_certificate_authority_roots and not isinstance(custom_certificate_authority_roots, list):
            raise TypeError("Expected argument 'custom_certificate_authority_roots' to be a list")
        pulumi.set(__self__, "custom_certificate_authority_roots", custom_certificate_authority_roots)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if descriptor_url and not isinstance(descriptor_url, str):
            raise TypeError("Expected argument 'descriptor_url' to be a str")
        pulumi.set(__self__, "descriptor_url", descriptor_url)
        if insert_time and not isinstance(insert_time, str):
            raise TypeError("Expected argument 'insert_time' to be a str")
        pulumi.set(__self__, "insert_time", insert_time)
        if labels and not isinstance(labels, list):
            raise TypeError("Expected argument 'labels' to be a list")
        pulumi.set(__self__, "labels", labels)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if operation and not isinstance(operation, dict):
            raise TypeError("Expected argument 'operation' to be a dict")
        pulumi.set(__self__, "operation", operation)
        if options and not isinstance(options, dict):
            raise TypeError("Expected argument 'options' to be a dict")
        pulumi.set(__self__, "options", options)
        if self_link and not isinstance(self_link, str):
            raise TypeError("Expected argument 'self_link' to be a str")
        pulumi.set(__self__, "self_link", self_link)

    @property
    @pulumi.getter(name="collectionOverrides")
    def collection_overrides(self) -> Sequence['outputs.CollectionOverrideResponse']:
        """
        Allows resource handling overrides for specific collections
        """
        return pulumi.get(self, "collection_overrides")

    @property
    @pulumi.getter
    def credential(self) -> 'outputs.CredentialResponse':
        """
        Credential used when interacting with this type.
        """
        return pulumi.get(self, "credential")

    @property
    @pulumi.getter(name="customCertificateAuthorityRoots")
    def custom_certificate_authority_roots(self) -> Sequence[str]:
        """
        List of up to 2 custom certificate authority roots to use for TLS authentication when making calls on behalf of this type provider. If set, TLS authentication will exclusively use these roots instead of relying on publicly trusted certificate authorities when validating TLS certificate authenticity. The certificates must be in base64-encoded PEM format. The maximum size of each certificate must not exceed 10KB.
        """
        return pulumi.get(self, "custom_certificate_authority_roots")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        An optional textual description of the resource; provided by the client when the resource is created.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="descriptorUrl")
    def descriptor_url(self) -> str:
        """
        Descriptor Url for the this type provider.
        """
        return pulumi.get(self, "descriptor_url")

    @property
    @pulumi.getter(name="insertTime")
    def insert_time(self) -> str:
        """
        Creation timestamp in RFC3339 text format.
        """
        return pulumi.get(self, "insert_time")

    @property
    @pulumi.getter
    def labels(self) -> Sequence['outputs.TypeProviderLabelEntryResponse']:
        """
        Map of One Platform labels; provided by the client when the resource is created or updated. Specifically: Label keys must be between 1 and 63 characters long and must conform to the following regular expression: `[a-z]([-a-z0-9]*[a-z0-9])?` Label values must be between 0 and 63 characters long and must conform to the regular expression `([a-z]([-a-z0-9]*[a-z0-9])?)?`
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def operation(self) -> 'outputs.OperationResponse':
        """
        The Operation that most recently ran, or is currently running, on this type provider.
        """
        return pulumi.get(self, "operation")

    @property
    @pulumi.getter
    def options(self) -> 'outputs.OptionsResponse':
        """
        Options to apply when handling any resources in this service.
        """
        return pulumi.get(self, "options")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> str:
        """
        Self link for the type provider.
        """
        return pulumi.get(self, "self_link")


class AwaitableGetTypeProviderResult(GetTypeProviderResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTypeProviderResult(
            collection_overrides=self.collection_overrides,
            credential=self.credential,
            custom_certificate_authority_roots=self.custom_certificate_authority_roots,
            description=self.description,
            descriptor_url=self.descriptor_url,
            insert_time=self.insert_time,
            labels=self.labels,
            name=self.name,
            operation=self.operation,
            options=self.options,
            self_link=self.self_link)


def get_type_provider(project: Optional[str] = None,
                      type_provider: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTypeProviderResult:
    """
    Gets information about a specific type provider.
    """
    __args__ = dict()
    __args__['project'] = project
    __args__['typeProvider'] = type_provider
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:deploymentmanager/alpha:getTypeProvider', __args__, opts=opts, typ=GetTypeProviderResult).value

    return AwaitableGetTypeProviderResult(
        collection_overrides=__ret__.collection_overrides,
        credential=__ret__.credential,
        custom_certificate_authority_roots=__ret__.custom_certificate_authority_roots,
        description=__ret__.description,
        descriptor_url=__ret__.descriptor_url,
        insert_time=__ret__.insert_time,
        labels=__ret__.labels,
        name=__ret__.name,
        operation=__ret__.operation,
        options=__ret__.options,
        self_link=__ret__.self_link)
