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

class UpsertComplexMarketDataRequest(object):
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
        'market_data_id': 'ComplexMarketDataId',
        'market_data': 'ComplexMarketData'
    }

    attribute_map = {
        'market_data_id': 'marketDataId',
        'market_data': 'marketData'
    }

    required_map = {
        'market_data_id': 'required',
        'market_data': 'required'
    }

    def __init__(self, market_data_id=None, market_data=None):  # noqa: E501
        """
        UpsertComplexMarketDataRequest - a model defined in OpenAPI

        :param market_data_id:  (required)
        :type market_data_id: lusid.ComplexMarketDataId
        :param market_data:  (required)
        :type market_data: lusid.ComplexMarketData

        """  # noqa: E501

        self._market_data_id = None
        self._market_data = None
        self.discriminator = None

        self.market_data_id = market_data_id
        self.market_data = market_data

    @property
    def market_data_id(self):
        """Gets the market_data_id of this UpsertComplexMarketDataRequest.  # noqa: E501


        :return: The market_data_id of this UpsertComplexMarketDataRequest.  # noqa: E501
        :rtype: ComplexMarketDataId
        """
        return self._market_data_id

    @market_data_id.setter
    def market_data_id(self, market_data_id):
        """Sets the market_data_id of this UpsertComplexMarketDataRequest.


        :param market_data_id: The market_data_id of this UpsertComplexMarketDataRequest.  # noqa: E501
        :type: ComplexMarketDataId
        """
        if market_data_id is None:
            raise ValueError("Invalid value for `market_data_id`, must not be `None`")  # noqa: E501

        self._market_data_id = market_data_id

    @property
    def market_data(self):
        """Gets the market_data of this UpsertComplexMarketDataRequest.  # noqa: E501


        :return: The market_data of this UpsertComplexMarketDataRequest.  # noqa: E501
        :rtype: ComplexMarketData
        """
        return self._market_data

    @market_data.setter
    def market_data(self, market_data):
        """Sets the market_data of this UpsertComplexMarketDataRequest.


        :param market_data: The market_data of this UpsertComplexMarketDataRequest.  # noqa: E501
        :type: ComplexMarketData
        """
        if market_data is None:
            raise ValueError("Invalid value for `market_data`, must not be `None`")  # noqa: E501

        self._market_data = market_data

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
        if not isinstance(other, UpsertComplexMarketDataRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
