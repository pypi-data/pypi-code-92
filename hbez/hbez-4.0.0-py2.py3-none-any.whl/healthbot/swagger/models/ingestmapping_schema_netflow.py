# coding: utf-8

"""
    Paragon Insights APIs

    API interface for PI application  # noqa: E501

    OpenAPI spec version: 4.0.0
    Contact: healthbot-feedback@juniper.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class IngestmappingSchemaNetflow(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'for_device_groups': 'list[str]',
        'use_plugin': 'IngestmappingSchemaIAgentUseplugin'
    }

    attribute_map = {
        'for_device_groups': 'for-device-groups',
        'use_plugin': 'use-plugin'
    }

    def __init__(self, for_device_groups=None, use_plugin=None):  # noqa: E501
        """IngestmappingSchemaNetflow - a model defined in Swagger"""  # noqa: E501

        self._for_device_groups = None
        self._use_plugin = None
        self.discriminator = None

        if for_device_groups is not None:
            self.for_device_groups = for_device_groups
        if use_plugin is not None:
            self.use_plugin = use_plugin

    @property
    def for_device_groups(self):
        """Gets the for_device_groups of this IngestmappingSchemaNetflow.  # noqa: E501


        :return: The for_device_groups of this IngestmappingSchemaNetflow.  # noqa: E501
        :rtype: list[str]
        """
        return self._for_device_groups

    @for_device_groups.setter
    def for_device_groups(self, for_device_groups):
        """Sets the for_device_groups of this IngestmappingSchemaNetflow.


        :param for_device_groups: The for_device_groups of this IngestmappingSchemaNetflow.  # noqa: E501
        :type: list[str]
        """

        self._for_device_groups = for_device_groups

    @property
    def use_plugin(self):
        """Gets the use_plugin of this IngestmappingSchemaNetflow.  # noqa: E501


        :return: The use_plugin of this IngestmappingSchemaNetflow.  # noqa: E501
        :rtype: IngestmappingSchemaIAgentUseplugin
        """
        return self._use_plugin

    @use_plugin.setter
    def use_plugin(self, use_plugin):
        """Sets the use_plugin of this IngestmappingSchemaNetflow.


        :param use_plugin: The use_plugin of this IngestmappingSchemaNetflow.  # noqa: E501
        :type: IngestmappingSchemaIAgentUseplugin
        """

        self._use_plugin = use_plugin

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(IngestmappingSchemaNetflow, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, IngestmappingSchemaNetflow):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
