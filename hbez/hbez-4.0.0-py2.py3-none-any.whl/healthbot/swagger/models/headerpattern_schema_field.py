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


class HeaderpatternSchemaField(object):
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
        '_from': 'str',
        'name': 'str',
        'type': 'str'
    }

    attribute_map = {
        'description': 'description',
        '_from': 'from',
        'name': 'name',
        'type': 'type'
    }

    def __init__(self, description=None, _from=None, name=None, type=None):  # noqa: E501
        """HeaderpatternSchemaField - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self.__from = None
        self._name = None
        self._type = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self._from = _from
        self.name = name
        if type is not None:
            self.type = type

    @property
    def description(self):
        """Gets the description of this HeaderpatternSchemaField.  # noqa: E501

        Field description  # noqa: E501

        :return: The description of this HeaderpatternSchemaField.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this HeaderpatternSchemaField.

        Field description  # noqa: E501

        :param description: The description of this HeaderpatternSchemaField.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def _from(self):
        """Gets the _from of this HeaderpatternSchemaField.  # noqa: E501

        Field that supplies the value. For a structured syslog, this will be the attribute name from the message. For a grok pattern, this will be name of the field given in the pattern. For a regex pattern, this will be the capture group number prefixed by $, eg: $1, $2  # noqa: E501

        :return: The _from of this HeaderpatternSchemaField.  # noqa: E501
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this HeaderpatternSchemaField.

        Field that supplies the value. For a structured syslog, this will be the attribute name from the message. For a grok pattern, this will be name of the field given in the pattern. For a regex pattern, this will be the capture group number prefixed by $, eg: $1, $2  # noqa: E501

        :param _from: The _from of this HeaderpatternSchemaField.  # noqa: E501
        :type: str
        """
        if _from is None:
            raise ValueError("Invalid value for `_from`, must not be `None`")  # noqa: E501

        self.__from = _from

    @property
    def name(self):
        """Gets the name of this HeaderpatternSchemaField.  # noqa: E501

        Field name  # noqa: E501

        :return: The name of this HeaderpatternSchemaField.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HeaderpatternSchemaField.

        Field name  # noqa: E501

        :param name: The name of this HeaderpatternSchemaField.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this HeaderpatternSchemaField.  # noqa: E501


        :return: The type of this HeaderpatternSchemaField.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this HeaderpatternSchemaField.


        :param type: The type of this HeaderpatternSchemaField.  # noqa: E501
        :type: str
        """
        allowed_values = ["integer", "unsigned-integer", "float", "string"]  # noqa: E501
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
        if issubclass(HeaderpatternSchemaField, dict):
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
        if not isinstance(other, HeaderpatternSchemaField):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
