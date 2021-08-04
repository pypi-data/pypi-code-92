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
    'GetSslCertificateResult',
    'AwaitableGetSslCertificateResult',
    'get_ssl_certificate',
]

@pulumi.output_type
class GetSslCertificateResult:
    def __init__(__self__, certificate=None, creation_timestamp=None, description=None, expire_time=None, kind=None, managed=None, name=None, private_key=None, region=None, self_link=None, self_managed=None, subject_alternative_names=None, type=None):
        if certificate and not isinstance(certificate, str):
            raise TypeError("Expected argument 'certificate' to be a str")
        pulumi.set(__self__, "certificate", certificate)
        if creation_timestamp and not isinstance(creation_timestamp, str):
            raise TypeError("Expected argument 'creation_timestamp' to be a str")
        pulumi.set(__self__, "creation_timestamp", creation_timestamp)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if expire_time and not isinstance(expire_time, str):
            raise TypeError("Expected argument 'expire_time' to be a str")
        pulumi.set(__self__, "expire_time", expire_time)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if managed and not isinstance(managed, dict):
            raise TypeError("Expected argument 'managed' to be a dict")
        pulumi.set(__self__, "managed", managed)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if private_key and not isinstance(private_key, str):
            raise TypeError("Expected argument 'private_key' to be a str")
        pulumi.set(__self__, "private_key", private_key)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if self_link and not isinstance(self_link, str):
            raise TypeError("Expected argument 'self_link' to be a str")
        pulumi.set(__self__, "self_link", self_link)
        if self_managed and not isinstance(self_managed, dict):
            raise TypeError("Expected argument 'self_managed' to be a dict")
        pulumi.set(__self__, "self_managed", self_managed)
        if subject_alternative_names and not isinstance(subject_alternative_names, list):
            raise TypeError("Expected argument 'subject_alternative_names' to be a list")
        pulumi.set(__self__, "subject_alternative_names", subject_alternative_names)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def certificate(self) -> str:
        """
        A value read into memory from a certificate file. The certificate file must be in PEM format. The certificate chain must be no greater than 5 certs long. The chain must include at least one intermediate cert.
        """
        return pulumi.get(self, "certificate")

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
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> str:
        """
        Expire time of the certificate. RFC3339
        """
        return pulumi.get(self, "expire_time")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Type of the resource. Always compute#sslCertificate for SSL certificates.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def managed(self) -> 'outputs.SslCertificateManagedSslCertificateResponse':
        """
        Configuration and status of a managed SSL certificate.
        """
        return pulumi.get(self, "managed")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> str:
        """
        A value read into memory from a write-only private key file. The private key file must be in PEM format. For security, only insert requests include this field.
        """
        return pulumi.get(self, "private_key")

    @property
    @pulumi.getter
    def region(self) -> str:
        """
        URL of the region where the regional SSL Certificate resides. This field is not applicable to global SSL Certificate.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> str:
        """
        [Output only] Server-defined URL for the resource.
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter(name="selfManaged")
    def self_managed(self) -> 'outputs.SslCertificateSelfManagedSslCertificateResponse':
        """
        Configuration and status of a self-managed SSL certificate.
        """
        return pulumi.get(self, "self_managed")

    @property
    @pulumi.getter(name="subjectAlternativeNames")
    def subject_alternative_names(self) -> Sequence[str]:
        """
        Domains associated with the certificate via Subject Alternative Name.
        """
        return pulumi.get(self, "subject_alternative_names")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        (Optional) Specifies the type of SSL certificate, either "SELF_MANAGED" or "MANAGED". If not specified, the certificate is self-managed and the fields certificate and private_key are used.
        """
        return pulumi.get(self, "type")


class AwaitableGetSslCertificateResult(GetSslCertificateResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSslCertificateResult(
            certificate=self.certificate,
            creation_timestamp=self.creation_timestamp,
            description=self.description,
            expire_time=self.expire_time,
            kind=self.kind,
            managed=self.managed,
            name=self.name,
            private_key=self.private_key,
            region=self.region,
            self_link=self.self_link,
            self_managed=self.self_managed,
            subject_alternative_names=self.subject_alternative_names,
            type=self.type)


def get_ssl_certificate(project: Optional[str] = None,
                        ssl_certificate: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSslCertificateResult:
    """
    Returns the specified SslCertificate resource. Gets a list of available SSL certificates by making a list() request.
    """
    __args__ = dict()
    __args__['project'] = project
    __args__['sslCertificate'] = ssl_certificate
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:compute/beta:getSslCertificate', __args__, opts=opts, typ=GetSslCertificateResult).value

    return AwaitableGetSslCertificateResult(
        certificate=__ret__.certificate,
        creation_timestamp=__ret__.creation_timestamp,
        description=__ret__.description,
        expire_time=__ret__.expire_time,
        kind=__ret__.kind,
        managed=__ret__.managed,
        name=__ret__.name,
        private_key=__ret__.private_key,
        region=__ret__.region,
        self_link=__ret__.self_link,
        self_managed=__ret__.self_managed,
        subject_alternative_names=__ret__.subject_alternative_names,
        type=__ret__.type)
