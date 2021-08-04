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


class ModelKernelResourceSpec(object):
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
        'available': 'bool',
        'cpu_limit': 'float',
        'cpu_type': 'str',
        'created_dt': 'datetime',
        'description': 'str',
        'gpu_labels': 'dict(str, object)',
        'gpu_limit': 'int',
        'gpu_type': 'str',
        'id': 'int',
        'immutable_slug': 'str',
        'memory_limit': 'str',
        'name': 'str',
        'priority': 'int',
        'processor_type': 'str',
        'region': 'str',
        'spot': 'bool',
        'updated_dt': 'datetime'
    }

    attribute_map = {
        'available': 'available',
        'cpu_limit': 'cpu_limit',
        'cpu_type': 'cpu_type',
        'created_dt': 'created_dt',
        'description': 'description',
        'gpu_labels': 'gpu_labels',
        'gpu_limit': 'gpu_limit',
        'gpu_type': 'gpu_type',
        'id': 'id',
        'immutable_slug': 'immutable_slug',
        'memory_limit': 'memory_limit',
        'name': 'name',
        'priority': 'priority',
        'processor_type': 'processor_type',
        'region': 'region',
        'spot': 'spot',
        'updated_dt': 'updated_dt'
    }

    def __init__(self, available=None, cpu_limit=None, cpu_type=None, created_dt=None, description=None, gpu_labels=None, gpu_limit=None, gpu_type=None, id=None, immutable_slug=None, memory_limit=None, name=None, priority=None, processor_type=None, region=None, spot=None, updated_dt=None, local_vars_configuration=None):  # noqa: E501
        """ModelKernelResourceSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._available = None
        self._cpu_limit = None
        self._cpu_type = None
        self._created_dt = None
        self._description = None
        self._gpu_labels = None
        self._gpu_limit = None
        self._gpu_type = None
        self._id = None
        self._immutable_slug = None
        self._memory_limit = None
        self._name = None
        self._priority = None
        self._processor_type = None
        self._region = None
        self._spot = None
        self._updated_dt = None
        self.discriminator = None

        if available is not None:
            self.available = available
        if cpu_limit is not None:
            self.cpu_limit = cpu_limit
        if cpu_type is not None:
            self.cpu_type = cpu_type
        self.created_dt = created_dt
        self.description = description
        if gpu_labels is not None:
            self.gpu_labels = gpu_labels
        if gpu_limit is not None:
            self.gpu_limit = gpu_limit
        if gpu_type is not None:
            self.gpu_type = gpu_type
        if id is not None:
            self.id = id
        if immutable_slug is not None:
            self.immutable_slug = immutable_slug
        if memory_limit is not None:
            self.memory_limit = memory_limit
        if name is not None:
            self.name = name
        if priority is not None:
            self.priority = priority
        if processor_type is not None:
            self.processor_type = processor_type
        if region is not None:
            self.region = region
        if spot is not None:
            self.spot = spot
        self.updated_dt = updated_dt

    @property
    def available(self):
        """Gets the available of this ModelKernelResourceSpec.  # noqa: E501


        :return: The available of this ModelKernelResourceSpec.  # noqa: E501
        :rtype: bool
        """
        return self._available

    @available.setter
    def available(self, available):
        """Sets the available of this ModelKernelResourceSpec.


        :param available: The available of this ModelKernelResourceSpec.  # noqa: E501
        :type available: bool
        """

        self._available = available

    @property
    def cpu_limit(self):
        """Gets the cpu_limit of this ModelKernelResourceSpec.  # noqa: E501


        :return: The cpu_limit of this ModelKernelResourceSpec.  # noqa: E501
        :rtype: float
        """
        return self._cpu_limit

    @cpu_limit.setter
    def cpu_limit(self, cpu_limit):
        """Sets the cpu_limit of this ModelKernelResourceSpec.


        :param cpu_limit: The cpu_limit of this ModelKernelResourceSpec.  # noqa: E501
        :type cpu_limit: float
        """

        self._cpu_limit = cpu_limit

    @property
    def cpu_type(self):
        """Gets the cpu_type of this ModelKernelResourceSpec.  # noqa: E501


        :return: The cpu_type of this ModelKernelResourceSpec.  # noqa: E501
        :rtype: str
        """
        return self._cpu_type

    @cpu_type.setter
    def cpu_type(self, cpu_type):
        """Sets the cpu_type of this ModelKernelResourceSpec.


        :param cpu_type: The cpu_type of this ModelKernelResourceSpec.  # noqa: E501
        :type cpu_type: str
        """

        self._cpu_type = cpu_type

    @property
    def created_dt(self):
        """Gets the created_dt of this ModelKernelResourceSpec.  # noqa: E501


        :return: The created_dt of this ModelKernelResourceSpec.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this ModelKernelResourceSpec.


        :param created_dt: The created_dt of this ModelKernelResourceSpec.  # noqa: E501
        :type created_dt: datetime
        """

        self._created_dt = created_dt

    @property
    def description(self):
        """Gets the description of this ModelKernelResourceSpec.  # noqa: E501


        :return: The description of this ModelKernelResourceSpec.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ModelKernelResourceSpec.


        :param description: The description of this ModelKernelResourceSpec.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def gpu_labels(self):
        """Gets the gpu_labels of this ModelKernelResourceSpec.  # noqa: E501


        :return: The gpu_labels of this ModelKernelResourceSpec.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._gpu_labels

    @gpu_labels.setter
    def gpu_labels(self, gpu_labels):
        """Sets the gpu_labels of this ModelKernelResourceSpec.


        :param gpu_labels: The gpu_labels of this ModelKernelResourceSpec.  # noqa: E501
        :type gpu_labels: dict(str, object)
        """

        self._gpu_labels = gpu_labels

    @property
    def gpu_limit(self):
        """Gets the gpu_limit of this ModelKernelResourceSpec.  # noqa: E501


        :return: The gpu_limit of this ModelKernelResourceSpec.  # noqa: E501
        :rtype: int
        """
        return self._gpu_limit

    @gpu_limit.setter
    def gpu_limit(self, gpu_limit):
        """Sets the gpu_limit of this ModelKernelResourceSpec.


        :param gpu_limit: The gpu_limit of this ModelKernelResourceSpec.  # noqa: E501
        :type gpu_limit: int
        """

        self._gpu_limit = gpu_limit

    @property
    def gpu_type(self):
        """Gets the gpu_type of this ModelKernelResourceSpec.  # noqa: E501


        :return: The gpu_type of this ModelKernelResourceSpec.  # noqa: E501
        :rtype: str
        """
        return self._gpu_type

    @gpu_type.setter
    def gpu_type(self, gpu_type):
        """Sets the gpu_type of this ModelKernelResourceSpec.


        :param gpu_type: The gpu_type of this ModelKernelResourceSpec.  # noqa: E501
        :type gpu_type: str
        """

        self._gpu_type = gpu_type

    @property
    def id(self):
        """Gets the id of this ModelKernelResourceSpec.  # noqa: E501


        :return: The id of this ModelKernelResourceSpec.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ModelKernelResourceSpec.


        :param id: The id of this ModelKernelResourceSpec.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def immutable_slug(self):
        """Gets the immutable_slug of this ModelKernelResourceSpec.  # noqa: E501


        :return: The immutable_slug of this ModelKernelResourceSpec.  # noqa: E501
        :rtype: str
        """
        return self._immutable_slug

    @immutable_slug.setter
    def immutable_slug(self, immutable_slug):
        """Sets the immutable_slug of this ModelKernelResourceSpec.


        :param immutable_slug: The immutable_slug of this ModelKernelResourceSpec.  # noqa: E501
        :type immutable_slug: str
        """

        self._immutable_slug = immutable_slug

    @property
    def memory_limit(self):
        """Gets the memory_limit of this ModelKernelResourceSpec.  # noqa: E501


        :return: The memory_limit of this ModelKernelResourceSpec.  # noqa: E501
        :rtype: str
        """
        return self._memory_limit

    @memory_limit.setter
    def memory_limit(self, memory_limit):
        """Sets the memory_limit of this ModelKernelResourceSpec.


        :param memory_limit: The memory_limit of this ModelKernelResourceSpec.  # noqa: E501
        :type memory_limit: str
        """

        self._memory_limit = memory_limit

    @property
    def name(self):
        """Gets the name of this ModelKernelResourceSpec.  # noqa: E501


        :return: The name of this ModelKernelResourceSpec.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModelKernelResourceSpec.


        :param name: The name of this ModelKernelResourceSpec.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def priority(self):
        """Gets the priority of this ModelKernelResourceSpec.  # noqa: E501


        :return: The priority of this ModelKernelResourceSpec.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this ModelKernelResourceSpec.


        :param priority: The priority of this ModelKernelResourceSpec.  # noqa: E501
        :type priority: int
        """

        self._priority = priority

    @property
    def processor_type(self):
        """Gets the processor_type of this ModelKernelResourceSpec.  # noqa: E501


        :return: The processor_type of this ModelKernelResourceSpec.  # noqa: E501
        :rtype: str
        """
        return self._processor_type

    @processor_type.setter
    def processor_type(self, processor_type):
        """Sets the processor_type of this ModelKernelResourceSpec.


        :param processor_type: The processor_type of this ModelKernelResourceSpec.  # noqa: E501
        :type processor_type: str
        """

        self._processor_type = processor_type

    @property
    def region(self):
        """Gets the region of this ModelKernelResourceSpec.  # noqa: E501


        :return: The region of this ModelKernelResourceSpec.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ModelKernelResourceSpec.


        :param region: The region of this ModelKernelResourceSpec.  # noqa: E501
        :type region: str
        """

        self._region = region

    @property
    def spot(self):
        """Gets the spot of this ModelKernelResourceSpec.  # noqa: E501


        :return: The spot of this ModelKernelResourceSpec.  # noqa: E501
        :rtype: bool
        """
        return self._spot

    @spot.setter
    def spot(self, spot):
        """Sets the spot of this ModelKernelResourceSpec.


        :param spot: The spot of this ModelKernelResourceSpec.  # noqa: E501
        :type spot: bool
        """

        self._spot = spot

    @property
    def updated_dt(self):
        """Gets the updated_dt of this ModelKernelResourceSpec.  # noqa: E501


        :return: The updated_dt of this ModelKernelResourceSpec.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_dt

    @updated_dt.setter
    def updated_dt(self, updated_dt):
        """Sets the updated_dt of this ModelKernelResourceSpec.


        :param updated_dt: The updated_dt of this ModelKernelResourceSpec.  # noqa: E501
        :type updated_dt: datetime
        """

        self._updated_dt = updated_dt

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
        if not isinstance(other, ModelKernelResourceSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelKernelResourceSpec):
            return True

        return self.to_dict() != other.to_dict()
