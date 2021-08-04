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


class RuleSchemaWhenRange(object):
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
        'all': 'list[object]',
        'any': 'list[object]',
        'field_name': 'str',
        'max': 'float',
        'min': 'float',
        'time_range': 'str'
    }

    attribute_map = {
        'all': 'all',
        'any': 'any',
        'field_name': 'field-name',
        'max': 'max',
        'min': 'min',
        'time_range': 'time-range'
    }

    def __init__(self, all=None, any=None, field_name=None, max=None, min=None, time_range=None):  # noqa: E501
        """RuleSchemaWhenRange - a model defined in Swagger"""  # noqa: E501

        self._all = None
        self._any = None
        self._field_name = None
        self._max = None
        self._min = None
        self._time_range = None
        self.discriminator = None

        if all is not None:
            self.all = all
        if any is not None:
            self.any = any
        self.field_name = field_name
        self.max = max
        self.min = min
        if time_range is not None:
            self.time_range = time_range

    @property
    def all(self):
        """Gets the all of this RuleSchemaWhenRange.  # noqa: E501

        With this flag, result is set to True only if all the data matches the given condition  # noqa: E501

        :return: The all of this RuleSchemaWhenRange.  # noqa: E501
        :rtype: list[object]
        """
        return self._all

    @all.setter
    def all(self, all):
        """Sets the all of this RuleSchemaWhenRange.

        With this flag, result is set to True only if all the data matches the given condition  # noqa: E501

        :param all: The all of this RuleSchemaWhenRange.  # noqa: E501
        :type: list[object]
        """

        self._all = all

    @property
    def any(self):
        """Gets the any of this RuleSchemaWhenRange.  # noqa: E501

        With this flag, result is set to True if any one of the data matches the condition  # noqa: E501

        :return: The any of this RuleSchemaWhenRange.  # noqa: E501
        :rtype: list[object]
        """
        return self._any

    @any.setter
    def any(self, any):
        """Sets the any of this RuleSchemaWhenRange.

        With this flag, result is set to True if any one of the data matches the condition  # noqa: E501

        :param any: The any of this RuleSchemaWhenRange.  # noqa: E501
        :type: list[object]
        """

        self._any = any

    @property
    def field_name(self):
        """Gets the field_name of this RuleSchemaWhenRange.  # noqa: E501

        Field name on which range should be applied  # noqa: E501

        :return: The field_name of this RuleSchemaWhenRange.  # noqa: E501
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """Sets the field_name of this RuleSchemaWhenRange.

        Field name on which range should be applied  # noqa: E501

        :param field_name: The field_name of this RuleSchemaWhenRange.  # noqa: E501
        :type: str
        """
        if field_name is None:
            raise ValueError("Invalid value for `field_name`, must not be `None`")  # noqa: E501

        self._field_name = field_name

    @property
    def max(self):
        """Gets the max of this RuleSchemaWhenRange.  # noqa: E501

        Maximum value in the range  # noqa: E501

        :return: The max of this RuleSchemaWhenRange.  # noqa: E501
        :rtype: float
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this RuleSchemaWhenRange.

        Maximum value in the range  # noqa: E501

        :param max: The max of this RuleSchemaWhenRange.  # noqa: E501
        :type: float
        """
        if max is None:
            raise ValueError("Invalid value for `max`, must not be `None`")  # noqa: E501

        self._max = max

    @property
    def min(self):
        """Gets the min of this RuleSchemaWhenRange.  # noqa: E501

        Minumum value in the range  # noqa: E501

        :return: The min of this RuleSchemaWhenRange.  # noqa: E501
        :rtype: float
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this RuleSchemaWhenRange.

        Minumum value in the range  # noqa: E501

        :param min: The min of this RuleSchemaWhenRange.  # noqa: E501
        :type: float
        """
        if min is None:
            raise ValueError("Invalid value for `min`, must not be `None`")  # noqa: E501

        self._min = min

    @property
    def time_range(self):
        """Gets the time_range of this RuleSchemaWhenRange.  # noqa: E501

        How much back in time should we look for data. Specify positive integer followed by s/m/h/d/w/y/o representing seconds/minutes/hours/days/weeks/years/offset. Eg: 2s  # noqa: E501

        :return: The time_range of this RuleSchemaWhenRange.  # noqa: E501
        :rtype: str
        """
        return self._time_range

    @time_range.setter
    def time_range(self, time_range):
        """Sets the time_range of this RuleSchemaWhenRange.

        How much back in time should we look for data. Specify positive integer followed by s/m/h/d/w/y/o representing seconds/minutes/hours/days/weeks/years/offset. Eg: 2s  # noqa: E501

        :param time_range: The time_range of this RuleSchemaWhenRange.  # noqa: E501
        :type: str
        """
        if time_range is not None and not re.search(r'^[1-9][0-9]*(\\.[0-9]+)?(o|s|m|h|d|w|y|offset)$', time_range):  # noqa: E501
            raise ValueError(r"Invalid value for `time_range`, must be a follow pattern or equal to `/^[1-9][0-9]*(\\.[0-9]+)?(o|s|m|h|d|w|y|offset)$/`")  # noqa: E501

        self._time_range = time_range

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
        if issubclass(RuleSchemaWhenRange, dict):
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
        if not isinstance(other, RuleSchemaWhenRange):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
