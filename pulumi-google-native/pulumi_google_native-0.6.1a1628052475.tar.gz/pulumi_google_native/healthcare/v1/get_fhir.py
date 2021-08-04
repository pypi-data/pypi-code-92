# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetFhirResult',
    'AwaitableGetFhirResult',
    'get_fhir',
]

@pulumi.output_type
class GetFhirResult:
    def __init__(__self__, content_type=None, data=None, extensions=None):
        if content_type and not isinstance(content_type, str):
            raise TypeError("Expected argument 'content_type' to be a str")
        pulumi.set(__self__, "content_type", content_type)
        if data and not isinstance(data, str):
            raise TypeError("Expected argument 'data' to be a str")
        pulumi.set(__self__, "data", data)
        if extensions and not isinstance(extensions, list):
            raise TypeError("Expected argument 'extensions' to be a list")
        pulumi.set(__self__, "extensions", extensions)

    @property
    @pulumi.getter(name="contentType")
    def content_type(self) -> str:
        """
        The HTTP Content-Type header value specifying the content type of the body.
        """
        return pulumi.get(self, "content_type")

    @property
    @pulumi.getter
    def data(self) -> str:
        """
        The HTTP request/response body as raw binary.
        """
        return pulumi.get(self, "data")

    @property
    @pulumi.getter
    def extensions(self) -> Sequence[Mapping[str, str]]:
        """
        Application specific response metadata. Must be set in the first response for streaming APIs.
        """
        return pulumi.get(self, "extensions")


class AwaitableGetFhirResult(GetFhirResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFhirResult(
            content_type=self.content_type,
            data=self.data,
            extensions=self.extensions)


def get_fhir(dataset_id: Optional[str] = None,
             fhir_id: Optional[str] = None,
             fhir_id1: Optional[str] = None,
             fhir_store_id: Optional[str] = None,
             location: Optional[str] = None,
             project: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFhirResult:
    """
    Gets the contents of a FHIR resource. Implements the FHIR standard read interaction ([DSTU2](http://hl7.org/implement/standards/fhir/DSTU2/http.html#read), [STU3](http://hl7.org/implement/standards/fhir/STU3/http.html#read), [R4](http://hl7.org/implement/standards/fhir/R4/http.html#read)). Also supports the FHIR standard conditional read interaction ([DSTU2](http://hl7.org/implement/standards/fhir/DSTU2/http.html#cread), [STU3](http://hl7.org/implement/standards/fhir/STU3/http.html#cread), [R4](http://hl7.org/implement/standards/fhir/R4/http.html#cread)) specified by supplying an `If-Modified-Since` header with a date/time value or an `If-None-Match` header with an ETag value. On success, the response body contains a JSON-encoded representation of the resource. Errors generated by the FHIR store contain a JSON-encoded `OperationOutcome` resource describing the reason for the error. If the request cannot be mapped to a valid API method on a FHIR store, a generic GCP error might be returned instead. For samples that show how to call `read`, see [Getting a FHIR resource](/healthcare/docs/how-tos/fhir-resources#getting_a_fhir_resource).
    """
    __args__ = dict()
    __args__['datasetId'] = dataset_id
    __args__['fhirId'] = fhir_id
    __args__['fhirId1'] = fhir_id1
    __args__['fhirStoreId'] = fhir_store_id
    __args__['location'] = location
    __args__['project'] = project
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:healthcare/v1:getFhir', __args__, opts=opts, typ=GetFhirResult).value

    return AwaitableGetFhirResult(
        content_type=__ret__.content_type,
        data=__ret__.data,
        extensions=__ret__.extensions)
