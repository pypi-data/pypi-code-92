# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3351
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class PortfoliosReconciliationRequestPreview(object):
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
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'tolerance': 'dict(str, Tolerance)',
        'left': 'PortfolioReconciliationRequest',
        'right': 'PortfolioReconciliationRequest',
        'instrument_property_keys': 'list[str]'
    }

    attribute_map = {
        'tolerance': 'tolerance',
        'left': 'left',
        'right': 'right',
        'instrument_property_keys': 'instrumentPropertyKeys'
    }

    required_map = {
        'tolerance': 'optional',
        'left': 'required',
        'right': 'required',
        'instrument_property_keys': 'required'
    }

    def __init__(self, tolerance=None, left=None, right=None, instrument_property_keys=None):  # noqa: E501
        """
        PortfoliosReconciliationRequestPreview - a model defined in OpenAPI

        :param tolerance:  Tolerance to be included for the units and cost.
        :type tolerance: dict[str, lusid.Tolerance]
        :param left:  (required)
        :type left: lusid.PortfolioReconciliationRequest
        :param right:  (required)
        :type right: lusid.PortfolioReconciliationRequest
        :param instrument_property_keys:  Instrument properties to be included with any identified breaks. These properties will be in the effective and AsAt dates of the left portfolio (required)
        :type instrument_property_keys: list[str]

        """  # noqa: E501

        self._tolerance = None
        self._left = None
        self._right = None
        self._instrument_property_keys = None
        self.discriminator = None

        self.tolerance = tolerance
        self.left = left
        self.right = right
        self.instrument_property_keys = instrument_property_keys

    @property
    def tolerance(self):
        """Gets the tolerance of this PortfoliosReconciliationRequestPreview.  # noqa: E501

        Tolerance to be included for the units and cost.  # noqa: E501

        :return: The tolerance of this PortfoliosReconciliationRequestPreview.  # noqa: E501
        :rtype: dict(str, Tolerance)
        """
        return self._tolerance

    @tolerance.setter
    def tolerance(self, tolerance):
        """Sets the tolerance of this PortfoliosReconciliationRequestPreview.

        Tolerance to be included for the units and cost.  # noqa: E501

        :param tolerance: The tolerance of this PortfoliosReconciliationRequestPreview.  # noqa: E501
        :type: dict(str, Tolerance)
        """

        self._tolerance = tolerance

    @property
    def left(self):
        """Gets the left of this PortfoliosReconciliationRequestPreview.  # noqa: E501


        :return: The left of this PortfoliosReconciliationRequestPreview.  # noqa: E501
        :rtype: PortfolioReconciliationRequest
        """
        return self._left

    @left.setter
    def left(self, left):
        """Sets the left of this PortfoliosReconciliationRequestPreview.


        :param left: The left of this PortfoliosReconciliationRequestPreview.  # noqa: E501
        :type: PortfolioReconciliationRequest
        """
        if left is None:
            raise ValueError("Invalid value for `left`, must not be `None`")  # noqa: E501

        self._left = left

    @property
    def right(self):
        """Gets the right of this PortfoliosReconciliationRequestPreview.  # noqa: E501


        :return: The right of this PortfoliosReconciliationRequestPreview.  # noqa: E501
        :rtype: PortfolioReconciliationRequest
        """
        return self._right

    @right.setter
    def right(self, right):
        """Sets the right of this PortfoliosReconciliationRequestPreview.


        :param right: The right of this PortfoliosReconciliationRequestPreview.  # noqa: E501
        :type: PortfolioReconciliationRequest
        """
        if right is None:
            raise ValueError("Invalid value for `right`, must not be `None`")  # noqa: E501

        self._right = right

    @property
    def instrument_property_keys(self):
        """Gets the instrument_property_keys of this PortfoliosReconciliationRequestPreview.  # noqa: E501

        Instrument properties to be included with any identified breaks. These properties will be in the effective and AsAt dates of the left portfolio  # noqa: E501

        :return: The instrument_property_keys of this PortfoliosReconciliationRequestPreview.  # noqa: E501
        :rtype: list[str]
        """
        return self._instrument_property_keys

    @instrument_property_keys.setter
    def instrument_property_keys(self, instrument_property_keys):
        """Sets the instrument_property_keys of this PortfoliosReconciliationRequestPreview.

        Instrument properties to be included with any identified breaks. These properties will be in the effective and AsAt dates of the left portfolio  # noqa: E501

        :param instrument_property_keys: The instrument_property_keys of this PortfoliosReconciliationRequestPreview.  # noqa: E501
        :type: list[str]
        """
        if instrument_property_keys is None:
            raise ValueError("Invalid value for `instrument_property_keys`, must not be `None`")  # noqa: E501

        self._instrument_property_keys = instrument_property_keys

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PortfoliosReconciliationRequestPreview):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
