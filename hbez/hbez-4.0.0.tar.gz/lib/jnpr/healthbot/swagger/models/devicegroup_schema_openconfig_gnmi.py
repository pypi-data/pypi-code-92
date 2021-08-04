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


class DevicegroupSchemaOpenconfigGnmi(object):
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
        'enable': 'bool',
        'encoding': 'str'
    }

    attribute_map = {
        'enable': 'enable',
        'encoding': 'encoding'
    }

    def __init__(self, enable=None, encoding=None):  # noqa: E501
        """DevicegroupSchemaOpenconfigGnmi - a model defined in Swagger"""  # noqa: E501

        self._enable = None
        self._encoding = None
        self.discriminator = None

        if enable is not None:
            self.enable = enable
        if encoding is not None:
            self.encoding = encoding

    @property
    def enable(self):
        """Gets the enable of this DevicegroupSchemaOpenconfigGnmi.  # noqa: E501

        If true, enable gnmi  # noqa: E501

        :return: The enable of this DevicegroupSchemaOpenconfigGnmi.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this DevicegroupSchemaOpenconfigGnmi.

        If true, enable gnmi  # noqa: E501

        :param enable: The enable of this DevicegroupSchemaOpenconfigGnmi.  # noqa: E501
        :type: bool
        """

        self._enable = enable

    @property
    def encoding(self):
        """Gets the encoding of this DevicegroupSchemaOpenconfigGnmi.  # noqa: E501

        Encoding to be used, default is protobuf  # noqa: E501

        :return: The encoding of this DevicegroupSchemaOpenconfigGnmi.  # noqa: E501
        :rtype: str
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        """Sets the encoding of this DevicegroupSchemaOpenconfigGnmi.

        Encoding to be used, default is protobuf  # noqa: E501

        :param encoding: The encoding of this DevicegroupSchemaOpenconfigGnmi.  # noqa: E501
        :type: str
        """
        allowed_values = ["protobuf", "json", "json_ietf"]  # noqa: E501
        if encoding not in allowed_values:
            raise ValueError(
                "Invalid value for `encoding` ({0}), must be one of {1}"  # noqa: E501
                .format(encoding, allowed_values)
            )

        self._encoding = encoding

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
        if issubclass(DevicegroupSchemaOpenconfigGnmi, dict):
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
        if not isinstance(other, DevicegroupSchemaOpenconfigGnmi):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
