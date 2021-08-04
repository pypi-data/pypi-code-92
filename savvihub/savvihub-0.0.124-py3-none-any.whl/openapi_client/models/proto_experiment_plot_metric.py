# coding: utf-8

"""
    Aron API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from openapi_client.configuration import Configuration


class ProtoExperimentPlotMetric(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'step': 'int',
        'timestamp': 'float',
        'value': 'float'
    }

    attribute_map = {
        'step': 'step',
        'timestamp': 'timestamp',
        'value': 'value'
    }

    def __init__(self, step=None, timestamp=None, value=None, local_vars_configuration=None):  # noqa: E501
        """ProtoExperimentPlotMetric - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._step = None
        self._timestamp = None
        self._value = None
        self.discriminator = None

        self.step = step
        self.timestamp = timestamp
        self.value = value

    @property
    def step(self):
        """Gets the step of this ProtoExperimentPlotMetric.  # noqa: E501


        :return: The step of this ProtoExperimentPlotMetric.  # noqa: E501
        :rtype: int
        """
        return self._step

    @step.setter
    def step(self, step):
        """Sets the step of this ProtoExperimentPlotMetric.


        :param step: The step of this ProtoExperimentPlotMetric.  # noqa: E501
        :type step: int
        """

        self._step = step

    @property
    def timestamp(self):
        """Gets the timestamp of this ProtoExperimentPlotMetric.  # noqa: E501


        :return: The timestamp of this ProtoExperimentPlotMetric.  # noqa: E501
        :rtype: float
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this ProtoExperimentPlotMetric.


        :param timestamp: The timestamp of this ProtoExperimentPlotMetric.  # noqa: E501
        :type timestamp: float
        """
        if self.local_vars_configuration.client_side_validation and timestamp is None:  # noqa: E501
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def value(self):
        """Gets the value of this ProtoExperimentPlotMetric.  # noqa: E501


        :return: The value of this ProtoExperimentPlotMetric.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ProtoExperimentPlotMetric.


        :param value: The value of this ProtoExperimentPlotMetric.  # noqa: E501
        :type value: float
        """
        if self.local_vars_configuration.client_side_validation and value is None:  # noqa: E501
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ProtoExperimentPlotMetric):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProtoExperimentPlotMetric):
            return True

        return self.to_dict() != other.to_dict()
