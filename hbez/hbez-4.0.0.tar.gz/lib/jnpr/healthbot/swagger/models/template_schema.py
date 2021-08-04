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


class TemplateSchema(object):
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
        'description': 'str',
        'key_fields': 'list[str]',
        'name': 'str',
        'priority': 'int',
        'protocol_version': 'str',
        'recognition_pattern': 'FlowSchemaFlowRecognitionpattern'
    }

    attribute_map = {
        'description': 'description',
        'key_fields': 'key-fields',
        'name': 'name',
        'priority': 'priority',
        'protocol_version': 'protocol-version',
        'recognition_pattern': 'recognition-pattern'
    }

    def __init__(self, description=None, key_fields=None, name=None, priority=None, protocol_version=None, recognition_pattern=None):  # noqa: E501
        """TemplateSchema - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._key_fields = None
        self._name = None
        self._priority = None
        self._protocol_version = None
        self._recognition_pattern = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if key_fields is not None:
            self.key_fields = key_fields
        self.name = name
        if priority is not None:
            self.priority = priority
        if protocol_version is not None:
            self.protocol_version = protocol_version
        if recognition_pattern is not None:
            self.recognition_pattern = recognition_pattern

    @property
    def description(self):
        """Gets the description of this TemplateSchema.  # noqa: E501

        Template description.  # noqa: E501

        :return: The description of this TemplateSchema.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TemplateSchema.

        Template description.  # noqa: E501

        :param description: The description of this TemplateSchema.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def key_fields(self):
        """Gets the key_fields of this TemplateSchema.  # noqa: E501


        :return: The key_fields of this TemplateSchema.  # noqa: E501
        :rtype: list[str]
        """
        return self._key_fields

    @key_fields.setter
    def key_fields(self, key_fields):
        """Sets the key_fields of this TemplateSchema.


        :param key_fields: The key_fields of this TemplateSchema.  # noqa: E501
        :type: list[str]
        """

        self._key_fields = key_fields

    @property
    def name(self):
        """Gets the name of this TemplateSchema.  # noqa: E501

        Name of the template.  # noqa: E501

        :return: The name of this TemplateSchema.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TemplateSchema.

        Name of the template.  # noqa: E501

        :param name: The name of this TemplateSchema.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def priority(self):
        """Gets the priority of this TemplateSchema.  # noqa: E501

        Priority given to template during matching.  # noqa: E501

        :return: The priority of this TemplateSchema.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this TemplateSchema.

        Priority given to template during matching.  # noqa: E501

        :param priority: The priority of this TemplateSchema.  # noqa: E501
        :type: int
        """

        self._priority = priority

    @property
    def protocol_version(self):
        """Gets the protocol_version of this TemplateSchema.  # noqa: E501

        Flow protocol version.  # noqa: E501

        :return: The protocol_version of this TemplateSchema.  # noqa: E501
        :rtype: str
        """
        return self._protocol_version

    @protocol_version.setter
    def protocol_version(self, protocol_version):
        """Sets the protocol_version of this TemplateSchema.

        Flow protocol version.  # noqa: E501

        :param protocol_version: The protocol_version of this TemplateSchema.  # noqa: E501
        :type: str
        """
        allowed_values = ["v9", "v10"]  # noqa: E501
        if protocol_version not in allowed_values:
            raise ValueError(
                "Invalid value for `protocol_version` ({0}), must be one of {1}"  # noqa: E501
                .format(protocol_version, allowed_values)
            )

        self._protocol_version = protocol_version

    @property
    def recognition_pattern(self):
        """Gets the recognition_pattern of this TemplateSchema.  # noqa: E501


        :return: The recognition_pattern of this TemplateSchema.  # noqa: E501
        :rtype: FlowSchemaFlowRecognitionpattern
        """
        return self._recognition_pattern

    @recognition_pattern.setter
    def recognition_pattern(self, recognition_pattern):
        """Sets the recognition_pattern of this TemplateSchema.


        :param recognition_pattern: The recognition_pattern of this TemplateSchema.  # noqa: E501
        :type: FlowSchemaFlowRecognitionpattern
        """

        self._recognition_pattern = recognition_pattern

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
        if issubclass(TemplateSchema, dict):
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
        if not isinstance(other, TemplateSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
