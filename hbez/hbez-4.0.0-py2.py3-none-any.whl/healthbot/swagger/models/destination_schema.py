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


class DestinationSchema(object):
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
        'disk': 'DestinationSchemaDisk',
        'email': 'DestinationSchemaEmail',
        'name': 'str'
    }

    attribute_map = {
        'disk': 'disk',
        'email': 'email',
        'name': 'name'
    }

    def __init__(self, disk=None, email=None, name=None):  # noqa: E501
        """DestinationSchema - a model defined in Swagger"""  # noqa: E501

        self._disk = None
        self._email = None
        self._name = None
        self.discriminator = None

        if disk is not None:
            self.disk = disk
        if email is not None:
            self.email = email
        self.name = name

    @property
    def disk(self):
        """Gets the disk of this DestinationSchema.  # noqa: E501


        :return: The disk of this DestinationSchema.  # noqa: E501
        :rtype: DestinationSchemaDisk
        """
        return self._disk

    @disk.setter
    def disk(self, disk):
        """Sets the disk of this DestinationSchema.


        :param disk: The disk of this DestinationSchema.  # noqa: E501
        :type: DestinationSchemaDisk
        """

        self._disk = disk

    @property
    def email(self):
        """Gets the email of this DestinationSchema.  # noqa: E501


        :return: The email of this DestinationSchema.  # noqa: E501
        :rtype: DestinationSchemaEmail
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this DestinationSchema.


        :param email: The email of this DestinationSchema.  # noqa: E501
        :type: DestinationSchemaEmail
        """

        self._email = email

    @property
    def name(self):
        """Gets the name of this DestinationSchema.  # noqa: E501

        Name of the destination. Should be of pattern [a-zA-Z][a-zA-Z0-9_-]*  # noqa: E501

        :return: The name of this DestinationSchema.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DestinationSchema.

        Name of the destination. Should be of pattern [a-zA-Z][a-zA-Z0-9_-]*  # noqa: E501

        :param name: The name of this DestinationSchema.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 64:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `64`")  # noqa: E501
        if name is not None and not re.search(r'^[a-zA-Z][a-zA-Z0-9_-]*$', name):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^[a-zA-Z][a-zA-Z0-9_-]*$/`")  # noqa: E501

        self._name = name

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
        if issubclass(DestinationSchema, dict):
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
        if not isinstance(other, DestinationSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
