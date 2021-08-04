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


class ModelProjectEdges(object):
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
        'organization': 'ModelOrganization',
        'primary_owner': 'ModelUser',
        'volume': 'ModelVolume',
        'workloads': 'list[ModelWorkload]'
    }

    attribute_map = {
        'organization': 'organization',
        'primary_owner': 'primary_owner',
        'volume': 'volume',
        'workloads': 'workloads'
    }

    def __init__(self, organization=None, primary_owner=None, volume=None, workloads=None, local_vars_configuration=None):  # noqa: E501
        """ModelProjectEdges - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._organization = None
        self._primary_owner = None
        self._volume = None
        self._workloads = None
        self.discriminator = None

        if organization is not None:
            self.organization = organization
        if primary_owner is not None:
            self.primary_owner = primary_owner
        if volume is not None:
            self.volume = volume
        if workloads is not None:
            self.workloads = workloads

    @property
    def organization(self):
        """Gets the organization of this ModelProjectEdges.  # noqa: E501


        :return: The organization of this ModelProjectEdges.  # noqa: E501
        :rtype: ModelOrganization
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this ModelProjectEdges.


        :param organization: The organization of this ModelProjectEdges.  # noqa: E501
        :type organization: ModelOrganization
        """

        self._organization = organization

    @property
    def primary_owner(self):
        """Gets the primary_owner of this ModelProjectEdges.  # noqa: E501


        :return: The primary_owner of this ModelProjectEdges.  # noqa: E501
        :rtype: ModelUser
        """
        return self._primary_owner

    @primary_owner.setter
    def primary_owner(self, primary_owner):
        """Sets the primary_owner of this ModelProjectEdges.


        :param primary_owner: The primary_owner of this ModelProjectEdges.  # noqa: E501
        :type primary_owner: ModelUser
        """

        self._primary_owner = primary_owner

    @property
    def volume(self):
        """Gets the volume of this ModelProjectEdges.  # noqa: E501


        :return: The volume of this ModelProjectEdges.  # noqa: E501
        :rtype: ModelVolume
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this ModelProjectEdges.


        :param volume: The volume of this ModelProjectEdges.  # noqa: E501
        :type volume: ModelVolume
        """

        self._volume = volume

    @property
    def workloads(self):
        """Gets the workloads of this ModelProjectEdges.  # noqa: E501


        :return: The workloads of this ModelProjectEdges.  # noqa: E501
        :rtype: list[ModelWorkload]
        """
        return self._workloads

    @workloads.setter
    def workloads(self, workloads):
        """Sets the workloads of this ModelProjectEdges.


        :param workloads: The workloads of this ModelProjectEdges.  # noqa: E501
        :type workloads: list[ModelWorkload]
        """

        self._workloads = workloads

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
        if not isinstance(other, ModelProjectEdges):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelProjectEdges):
            return True

        return self.to_dict() != other.to_dict()
