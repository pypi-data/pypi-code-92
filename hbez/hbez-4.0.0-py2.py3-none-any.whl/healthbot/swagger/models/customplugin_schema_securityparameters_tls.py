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


class CustompluginSchemaSecurityparametersTls(object):
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
        'ca_profile': 'str',
        'insecure_skip_verify': 'bool',
        'local_certificate_profile': 'str'
    }

    attribute_map = {
        'ca_profile': 'ca-profile',
        'insecure_skip_verify': 'insecure-skip-verify',
        'local_certificate_profile': 'local-certificate-profile'
    }

    def __init__(self, ca_profile=None, insecure_skip_verify=None, local_certificate_profile=None):  # noqa: E501
        """CustompluginSchemaSecurityparametersTls - a model defined in Swagger"""  # noqa: E501

        self._ca_profile = None
        self._insecure_skip_verify = None
        self._local_certificate_profile = None
        self.discriminator = None

        if ca_profile is not None:
            self.ca_profile = ca_profile
        if insecure_skip_verify is not None:
            self.insecure_skip_verify = insecure_skip_verify
        if local_certificate_profile is not None:
            self.local_certificate_profile = local_certificate_profile

    @property
    def ca_profile(self):
        """Gets the ca_profile of this CustompluginSchemaSecurityparametersTls.  # noqa: E501

        CA profile name  # noqa: E501

        :return: The ca_profile of this CustompluginSchemaSecurityparametersTls.  # noqa: E501
        :rtype: str
        """
        return self._ca_profile

    @ca_profile.setter
    def ca_profile(self, ca_profile):
        """Sets the ca_profile of this CustompluginSchemaSecurityparametersTls.

        CA profile name  # noqa: E501

        :param ca_profile: The ca_profile of this CustompluginSchemaSecurityparametersTls.  # noqa: E501
        :type: str
        """

        self._ca_profile = ca_profile

    @property
    def insecure_skip_verify(self):
        """Gets the insecure_skip_verify of this CustompluginSchemaSecurityparametersTls.  # noqa: E501

        Use TLS but skip verification of certificate chain and host  # noqa: E501

        :return: The insecure_skip_verify of this CustompluginSchemaSecurityparametersTls.  # noqa: E501
        :rtype: bool
        """
        return self._insecure_skip_verify

    @insecure_skip_verify.setter
    def insecure_skip_verify(self, insecure_skip_verify):
        """Sets the insecure_skip_verify of this CustompluginSchemaSecurityparametersTls.

        Use TLS but skip verification of certificate chain and host  # noqa: E501

        :param insecure_skip_verify: The insecure_skip_verify of this CustompluginSchemaSecurityparametersTls.  # noqa: E501
        :type: bool
        """

        self._insecure_skip_verify = insecure_skip_verify

    @property
    def local_certificate_profile(self):
        """Gets the local_certificate_profile of this CustompluginSchemaSecurityparametersTls.  # noqa: E501

        Local certificate profile name  # noqa: E501

        :return: The local_certificate_profile of this CustompluginSchemaSecurityparametersTls.  # noqa: E501
        :rtype: str
        """
        return self._local_certificate_profile

    @local_certificate_profile.setter
    def local_certificate_profile(self, local_certificate_profile):
        """Sets the local_certificate_profile of this CustompluginSchemaSecurityparametersTls.

        Local certificate profile name  # noqa: E501

        :param local_certificate_profile: The local_certificate_profile of this CustompluginSchemaSecurityparametersTls.  # noqa: E501
        :type: str
        """

        self._local_certificate_profile = local_certificate_profile

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
        if issubclass(CustompluginSchemaSecurityparametersTls, dict):
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
        if not isinstance(other, CustompluginSchemaSecurityparametersTls):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
