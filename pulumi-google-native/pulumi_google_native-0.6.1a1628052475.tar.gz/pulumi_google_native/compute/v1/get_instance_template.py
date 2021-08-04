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
    'GetInstanceTemplateResult',
    'AwaitableGetInstanceTemplateResult',
    'get_instance_template',
]

@pulumi.output_type
class GetInstanceTemplateResult:
    def __init__(__self__, creation_timestamp=None, description=None, kind=None, name=None, properties=None, self_link=None, source_instance=None, source_instance_params=None):
        if creation_timestamp and not isinstance(creation_timestamp, str):
            raise TypeError("Expected argument 'creation_timestamp' to be a str")
        pulumi.set(__self__, "creation_timestamp", creation_timestamp)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)
        if self_link and not isinstance(self_link, str):
            raise TypeError("Expected argument 'self_link' to be a str")
        pulumi.set(__self__, "self_link", self_link)
        if source_instance and not isinstance(source_instance, str):
            raise TypeError("Expected argument 'source_instance' to be a str")
        pulumi.set(__self__, "source_instance", source_instance)
        if source_instance_params and not isinstance(source_instance_params, dict):
            raise TypeError("Expected argument 'source_instance_params' to be a dict")
        pulumi.set(__self__, "source_instance_params", source_instance_params)

    @property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> str:
        """
        The creation timestamp for this instance template in RFC3339 text format.
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
    def kind(self) -> str:
        """
        The resource type, which is always compute#instanceTemplate for instance templates.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> 'outputs.InstancePropertiesResponse':
        """
        The instance properties for this instance template.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> str:
        """
        The URL for this instance template. The server defines this URL.
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter(name="sourceInstance")
    def source_instance(self) -> str:
        """
        The source instance used to create the template. You can provide this as a partial or full URL to the resource. For example, the following are valid values: - https://www.googleapis.com/compute/v1/projects/project/zones/zone /instances/instance - projects/project/zones/zone/instances/instance 
        """
        return pulumi.get(self, "source_instance")

    @property
    @pulumi.getter(name="sourceInstanceParams")
    def source_instance_params(self) -> 'outputs.SourceInstanceParamsResponse':
        """
        The source instance params to use to create this instance template.
        """
        return pulumi.get(self, "source_instance_params")


class AwaitableGetInstanceTemplateResult(GetInstanceTemplateResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInstanceTemplateResult(
            creation_timestamp=self.creation_timestamp,
            description=self.description,
            kind=self.kind,
            name=self.name,
            properties=self.properties,
            self_link=self.self_link,
            source_instance=self.source_instance,
            source_instance_params=self.source_instance_params)


def get_instance_template(instance_template: Optional[str] = None,
                          project: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetInstanceTemplateResult:
    """
    Returns the specified instance template. Gets a list of available instance templates by making a list() request.
    """
    __args__ = dict()
    __args__['instanceTemplate'] = instance_template
    __args__['project'] = project
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:compute/v1:getInstanceTemplate', __args__, opts=opts, typ=GetInstanceTemplateResult).value

    return AwaitableGetInstanceTemplateResult(
        creation_timestamp=__ret__.creation_timestamp,
        description=__ret__.description,
        kind=__ret__.kind,
        name=__ret__.name,
        properties=__ret__.properties,
        self_link=__ret__.self_link,
        source_instance=__ret__.source_instance,
        source_instance_params=__ret__.source_instance_params)
