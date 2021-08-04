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


class TopicSchemaField(object):
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
        'field_name': 'str',
        'source': 'TopicSchemaSource',
        'type': 'str'
    }

    attribute_map = {
        'description': 'description',
        'field_name': 'field-name',
        'source': 'source',
        'type': 'type'
    }

    def __init__(self, description=None, field_name=None, source=None, type=None):  # noqa: E501
        """TopicSchemaField - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._field_name = None
        self._source = None
        self._type = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.field_name = field_name
        if source is not None:
            self.source = source
        self.type = type

    @property
    def description(self):
        """Gets the description of this TopicSchemaField.  # noqa: E501

        Description about resource field  # noqa: E501

        :return: The description of this TopicSchemaField.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TopicSchemaField.

        Description about resource field  # noqa: E501

        :param description: The description of this TopicSchemaField.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def field_name(self):
        """Gets the field_name of this TopicSchemaField.  # noqa: E501

        Name of the resource field. Should be of pattern [a-z][a-zA-Z0-9-]*  # noqa: E501

        :return: The field_name of this TopicSchemaField.  # noqa: E501
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """Sets the field_name of this TopicSchemaField.

        Name of the resource field. Should be of pattern [a-z][a-zA-Z0-9-]*  # noqa: E501

        :param field_name: The field_name of this TopicSchemaField.  # noqa: E501
        :type: str
        """
        if field_name is None:
            raise ValueError("Invalid value for `field_name`, must not be `None`")  # noqa: E501
        if field_name is not None and len(field_name) > 64:
            raise ValueError("Invalid value for `field_name`, length must be less than or equal to `64`")  # noqa: E501
        if field_name is not None and len(field_name) < 1:
            raise ValueError("Invalid value for `field_name`, length must be greater than or equal to `1`")  # noqa: E501
        if field_name is not None and not re.search(r'^[a-z][a-zA-Z0-9-]*$', field_name):  # noqa: E501
            raise ValueError(r"Invalid value for `field_name`, must be a follow pattern or equal to `/^[a-z][a-zA-Z0-9-]*$/`")  # noqa: E501

        self._field_name = field_name

    @property
    def source(self):
        """Gets the source of this TopicSchemaField.  # noqa: E501


        :return: The source of this TopicSchemaField.  # noqa: E501
        :rtype: TopicSchemaSource
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this TopicSchemaField.


        :param source: The source of this TopicSchemaField.  # noqa: E501
        :type: TopicSchemaSource
        """

        self._source = source

    @property
    def type(self):
        """Gets the type of this TopicSchemaField.  # noqa: E501

        Resource field type  # noqa: E501

        :return: The type of this TopicSchemaField.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TopicSchemaField.

        Resource field type  # noqa: E501

        :param type: The type of this TopicSchemaField.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["string", "integer", "unsigned-integer", "float"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if issubclass(TopicSchemaField, dict):
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
        if not isinstance(other, TopicSchemaField):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
