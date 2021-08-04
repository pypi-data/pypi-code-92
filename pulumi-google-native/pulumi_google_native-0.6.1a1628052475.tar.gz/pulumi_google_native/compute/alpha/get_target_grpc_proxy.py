# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetTargetGrpcProxyResult',
    'AwaitableGetTargetGrpcProxyResult',
    'get_target_grpc_proxy',
]

@pulumi.output_type
class GetTargetGrpcProxyResult:
    def __init__(__self__, creation_timestamp=None, description=None, fingerprint=None, kind=None, name=None, self_link=None, self_link_with_id=None, url_map=None, validate_for_proxyless=None):
        if creation_timestamp and not isinstance(creation_timestamp, str):
            raise TypeError("Expected argument 'creation_timestamp' to be a str")
        pulumi.set(__self__, "creation_timestamp", creation_timestamp)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if fingerprint and not isinstance(fingerprint, str):
            raise TypeError("Expected argument 'fingerprint' to be a str")
        pulumi.set(__self__, "fingerprint", fingerprint)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if self_link and not isinstance(self_link, str):
            raise TypeError("Expected argument 'self_link' to be a str")
        pulumi.set(__self__, "self_link", self_link)
        if self_link_with_id and not isinstance(self_link_with_id, str):
            raise TypeError("Expected argument 'self_link_with_id' to be a str")
        pulumi.set(__self__, "self_link_with_id", self_link_with_id)
        if url_map and not isinstance(url_map, str):
            raise TypeError("Expected argument 'url_map' to be a str")
        pulumi.set(__self__, "url_map", url_map)
        if validate_for_proxyless and not isinstance(validate_for_proxyless, bool):
            raise TypeError("Expected argument 'validate_for_proxyless' to be a bool")
        pulumi.set(__self__, "validate_for_proxyless", validate_for_proxyless)

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
    def fingerprint(self) -> str:
        """
        Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking. This field will be ignored when inserting a TargetGrpcProxy. An up-to-date fingerprint must be provided in order to patch/update the TargetGrpcProxy; otherwise, the request will fail with error 412 conditionNotMet. To see the latest fingerprint, make a get() request to retrieve the TargetGrpcProxy.
        """
        return pulumi.get(self, "fingerprint")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Type of the resource. Always compute#targetGrpcProxy for target grpc proxies.
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
        Server-defined URL with id for the resource.
        """
        return pulumi.get(self, "self_link_with_id")

    @property
    @pulumi.getter(name="urlMap")
    def url_map(self) -> str:
        """
        URL to the UrlMap resource that defines the mapping from URL to the BackendService. The protocol field in the BackendService must be set to GRPC.
        """
        return pulumi.get(self, "url_map")

    @property
    @pulumi.getter(name="validateForProxyless")
    def validate_for_proxyless(self) -> bool:
        """
        If true, indicates that the BackendServices referenced by the urlMap may be accessed by gRPC applications without using a sidecar proxy. This will enable configuration checks on urlMap and its referenced BackendServices to not allow unsupported features. A gRPC application must use "xds:///" scheme in the target URI of the service it is connecting to. If false, indicates that the BackendServices referenced by the urlMap will be accessed by gRPC applications via a sidecar proxy. In this case, a gRPC application must not use "xds:///" scheme in the target URI of the service it is connecting to
        """
        return pulumi.get(self, "validate_for_proxyless")


class AwaitableGetTargetGrpcProxyResult(GetTargetGrpcProxyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTargetGrpcProxyResult(
            creation_timestamp=self.creation_timestamp,
            description=self.description,
            fingerprint=self.fingerprint,
            kind=self.kind,
            name=self.name,
            self_link=self.self_link,
            self_link_with_id=self.self_link_with_id,
            url_map=self.url_map,
            validate_for_proxyless=self.validate_for_proxyless)


def get_target_grpc_proxy(project: Optional[str] = None,
                          target_grpc_proxy: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTargetGrpcProxyResult:
    """
    Returns the specified TargetGrpcProxy resource in the given scope.
    """
    __args__ = dict()
    __args__['project'] = project
    __args__['targetGrpcProxy'] = target_grpc_proxy
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:compute/alpha:getTargetGrpcProxy', __args__, opts=opts, typ=GetTargetGrpcProxyResult).value

    return AwaitableGetTargetGrpcProxyResult(
        creation_timestamp=__ret__.creation_timestamp,
        description=__ret__.description,
        fingerprint=__ret__.fingerprint,
        kind=__ret__.kind,
        name=__ret__.name,
        self_link=__ret__.self_link,
        self_link_with_id=__ret__.self_link_with_id,
        url_map=__ret__.url_map,
        validate_for_proxyless=__ret__.validate_for_proxyless)
