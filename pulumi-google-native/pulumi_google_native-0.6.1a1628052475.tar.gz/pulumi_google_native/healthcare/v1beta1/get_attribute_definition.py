# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetAttributeDefinitionResult',
    'AwaitableGetAttributeDefinitionResult',
    'get_attribute_definition',
]

@pulumi.output_type
class GetAttributeDefinitionResult:
    def __init__(__self__, allowed_values=None, category=None, consent_default_values=None, data_mapping_default_value=None, description=None, name=None):
        if allowed_values and not isinstance(allowed_values, list):
            raise TypeError("Expected argument 'allowed_values' to be a list")
        pulumi.set(__self__, "allowed_values", allowed_values)
        if category and not isinstance(category, str):
            raise TypeError("Expected argument 'category' to be a str")
        pulumi.set(__self__, "category", category)
        if consent_default_values and not isinstance(consent_default_values, list):
            raise TypeError("Expected argument 'consent_default_values' to be a list")
        pulumi.set(__self__, "consent_default_values", consent_default_values)
        if data_mapping_default_value and not isinstance(data_mapping_default_value, str):
            raise TypeError("Expected argument 'data_mapping_default_value' to be a str")
        pulumi.set(__self__, "data_mapping_default_value", data_mapping_default_value)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="allowedValues")
    def allowed_values(self) -> Sequence[str]:
        """
        Possible values for the attribute. The number of allowed values must not exceed 100. An empty list is invalid. The list can only be expanded after creation.
        """
        return pulumi.get(self, "allowed_values")

    @property
    @pulumi.getter
    def category(self) -> str:
        """
        The category of the attribute. The value of this field cannot be changed after creation.
        """
        return pulumi.get(self, "category")

    @property
    @pulumi.getter(name="consentDefaultValues")
    def consent_default_values(self) -> Sequence[str]:
        """
        Optional. Default values of the attribute in Consents. If no default values are specified, it defaults to an empty value.
        """
        return pulumi.get(self, "consent_default_values")

    @property
    @pulumi.getter(name="dataMappingDefaultValue")
    def data_mapping_default_value(self) -> str:
        """
        Optional. Default value of the attribute in User data mappings. If no default value is specified, it defaults to an empty value. This field is only applicable to attributes of the category `RESOURCE`.
        """
        return pulumi.get(self, "data_mapping_default_value")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Optional. A description of the attribute.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name of the Attribute definition, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/consentStores/{consent_store_id}/attributeDefinitions/{attribute_definition_id}`. Cannot be changed after creation.
        """
        return pulumi.get(self, "name")


class AwaitableGetAttributeDefinitionResult(GetAttributeDefinitionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAttributeDefinitionResult(
            allowed_values=self.allowed_values,
            category=self.category,
            consent_default_values=self.consent_default_values,
            data_mapping_default_value=self.data_mapping_default_value,
            description=self.description,
            name=self.name)


def get_attribute_definition(attribute_definition_id: Optional[str] = None,
                             consent_store_id: Optional[str] = None,
                             dataset_id: Optional[str] = None,
                             location: Optional[str] = None,
                             project: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAttributeDefinitionResult:
    """
    Gets the specified Attribute definition.
    """
    __args__ = dict()
    __args__['attributeDefinitionId'] = attribute_definition_id
    __args__['consentStoreId'] = consent_store_id
    __args__['datasetId'] = dataset_id
    __args__['location'] = location
    __args__['project'] = project
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:healthcare/v1beta1:getAttributeDefinition', __args__, opts=opts, typ=GetAttributeDefinitionResult).value

    return AwaitableGetAttributeDefinitionResult(
        allowed_values=__ret__.allowed_values,
        category=__ret__.category,
        consent_default_values=__ret__.consent_default_values,
        data_mapping_default_value=__ret__.data_mapping_default_value,
        description=__ret__.description,
        name=__ret__.name)
