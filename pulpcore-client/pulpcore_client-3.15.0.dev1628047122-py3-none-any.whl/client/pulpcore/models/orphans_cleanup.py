# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pulpcore.client.pulpcore.configuration import Configuration


class OrphansCleanup(object):
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
        'content_hrefs': 'list[object]'
    }

    attribute_map = {
        'content_hrefs': 'content_hrefs'
    }

    def __init__(self, content_hrefs=None, local_vars_configuration=None):  # noqa: E501
        """OrphansCleanup - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._content_hrefs = None
        self.discriminator = None

        if content_hrefs is not None:
            self.content_hrefs = content_hrefs

    @property
    def content_hrefs(self):
        """Gets the content_hrefs of this OrphansCleanup.  # noqa: E501

        Will delete specified content and associated Artifacts if they are orphans.  # noqa: E501

        :return: The content_hrefs of this OrphansCleanup.  # noqa: E501
        :rtype: list[object]
        """
        return self._content_hrefs

    @content_hrefs.setter
    def content_hrefs(self, content_hrefs):
        """Sets the content_hrefs of this OrphansCleanup.

        Will delete specified content and associated Artifacts if they are orphans.  # noqa: E501

        :param content_hrefs: The content_hrefs of this OrphansCleanup.  # noqa: E501
        :type: list[object]
        """

        self._content_hrefs = content_hrefs

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
        if not isinstance(other, OrphansCleanup):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrphansCleanup):
            return True

        return self.to_dict() != other.to_dict()
