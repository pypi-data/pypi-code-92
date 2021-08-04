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


class ProfilesSchemaProfile(object):
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
        'security': 'ProfileSchemaSecurity',
        'data_summarization': 'ProfileSchemaDatasummarization',
        'rollup_summarization': 'ProfileSchemaRollupsummarization'
    }

    attribute_map = {
        'security': 'security',
        'data_summarization': 'data-summarization',
        'rollup_summarization': 'rollup-summarization'
    }

    def __init__(self, security=None, data_summarization=None, rollup_summarization=None):  # noqa: E501
        """ProfilesSchemaProfile - a model defined in Swagger"""  # noqa: E501

        self._security = None
        self._data_summarization = None
        self._rollup_summarization = None
        self.discriminator = None

        if security is not None:
            self.security = security
        if data_summarization is not None:
            self.data_summarization = data_summarization
        if rollup_summarization is not None:
            self.rollup_summarization = rollup_summarization

    @property
    def security(self):
        """Gets the security of this ProfilesSchemaProfile.  # noqa: E501


        :return: The security of this ProfilesSchemaProfile.  # noqa: E501
        :rtype: ProfileSchemaSecurity
        """
        return self._security

    @security.setter
    def security(self, security):
        """Sets the security of this ProfilesSchemaProfile.


        :param security: The security of this ProfilesSchemaProfile.  # noqa: E501
        :type: ProfileSchemaSecurity
        """

        self._security = security

    @property
    def data_summarization(self):
        """Gets the data_summarization of this ProfilesSchemaProfile.  # noqa: E501


        :return: The data_summarization of this ProfilesSchemaProfile.  # noqa: E501
        :rtype: ProfileSchemaDatasummarization
        """
        return self._data_summarization

    @data_summarization.setter
    def data_summarization(self, data_summarization):
        """Sets the data_summarization of this ProfilesSchemaProfile.


        :param data_summarization: The data_summarization of this ProfilesSchemaProfile.  # noqa: E501
        :type: ProfileSchemaDatasummarization
        """

        self._data_summarization = data_summarization

    @property
    def rollup_summarization(self):
        """Gets the rollup_summarization of this ProfilesSchemaProfile.  # noqa: E501


        :return: The rollup_summarization of this ProfilesSchemaProfile.  # noqa: E501
        :rtype: ProfileSchemaRollupsummarization
        """
        return self._rollup_summarization

    @rollup_summarization.setter
    def rollup_summarization(self, rollup_summarization):
        """Sets the rollup_summarization of this ProfilesSchemaProfile.


        :param rollup_summarization: The rollup_summarization of this ProfilesSchemaProfile.  # noqa: E501
        :type: ProfileSchemaRollupsummarization
        """

        self._rollup_summarization = rollup_summarization

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
        if issubclass(ProfilesSchemaProfile, dict):
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
        if not isinstance(other, ProfilesSchemaProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
