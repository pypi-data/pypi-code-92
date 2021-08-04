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


class ModelBillingHistory(object):
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
        'amount': 'float',
        'billing_history_organization': 'int',
        'billing_history_workload': 'int',
        'created_dt': 'datetime',
        'edges': 'ModelBillingHistoryEdges',
        'id': 'int',
        'month': 'datetime',
        'total': 'float',
        'updated_dt': 'datetime',
        'workload_created_dt': 'datetime'
    }

    attribute_map = {
        'amount': 'amount',
        'billing_history_organization': 'billing_history_organization',
        'billing_history_workload': 'billing_history_workload',
        'created_dt': 'created_dt',
        'edges': 'edges',
        'id': 'id',
        'month': 'month',
        'total': 'total',
        'updated_dt': 'updated_dt',
        'workload_created_dt': 'workload_created_dt'
    }

    def __init__(self, amount=None, billing_history_organization=None, billing_history_workload=None, created_dt=None, edges=None, id=None, month=None, total=None, updated_dt=None, workload_created_dt=None, local_vars_configuration=None):  # noqa: E501
        """ModelBillingHistory - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._amount = None
        self._billing_history_organization = None
        self._billing_history_workload = None
        self._created_dt = None
        self._edges = None
        self._id = None
        self._month = None
        self._total = None
        self._updated_dt = None
        self._workload_created_dt = None
        self.discriminator = None

        if amount is not None:
            self.amount = amount
        if billing_history_organization is not None:
            self.billing_history_organization = billing_history_organization
        if billing_history_workload is not None:
            self.billing_history_workload = billing_history_workload
        self.created_dt = created_dt
        if edges is not None:
            self.edges = edges
        if id is not None:
            self.id = id
        if month is not None:
            self.month = month
        if total is not None:
            self.total = total
        self.updated_dt = updated_dt
        if workload_created_dt is not None:
            self.workload_created_dt = workload_created_dt

    @property
    def amount(self):
        """Gets the amount of this ModelBillingHistory.  # noqa: E501


        :return: The amount of this ModelBillingHistory.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this ModelBillingHistory.


        :param amount: The amount of this ModelBillingHistory.  # noqa: E501
        :type amount: float
        """

        self._amount = amount

    @property
    def billing_history_organization(self):
        """Gets the billing_history_organization of this ModelBillingHistory.  # noqa: E501


        :return: The billing_history_organization of this ModelBillingHistory.  # noqa: E501
        :rtype: int
        """
        return self._billing_history_organization

    @billing_history_organization.setter
    def billing_history_organization(self, billing_history_organization):
        """Sets the billing_history_organization of this ModelBillingHistory.


        :param billing_history_organization: The billing_history_organization of this ModelBillingHistory.  # noqa: E501
        :type billing_history_organization: int
        """

        self._billing_history_organization = billing_history_organization

    @property
    def billing_history_workload(self):
        """Gets the billing_history_workload of this ModelBillingHistory.  # noqa: E501


        :return: The billing_history_workload of this ModelBillingHistory.  # noqa: E501
        :rtype: int
        """
        return self._billing_history_workload

    @billing_history_workload.setter
    def billing_history_workload(self, billing_history_workload):
        """Sets the billing_history_workload of this ModelBillingHistory.


        :param billing_history_workload: The billing_history_workload of this ModelBillingHistory.  # noqa: E501
        :type billing_history_workload: int
        """

        self._billing_history_workload = billing_history_workload

    @property
    def created_dt(self):
        """Gets the created_dt of this ModelBillingHistory.  # noqa: E501


        :return: The created_dt of this ModelBillingHistory.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this ModelBillingHistory.


        :param created_dt: The created_dt of this ModelBillingHistory.  # noqa: E501
        :type created_dt: datetime
        """

        self._created_dt = created_dt

    @property
    def edges(self):
        """Gets the edges of this ModelBillingHistory.  # noqa: E501


        :return: The edges of this ModelBillingHistory.  # noqa: E501
        :rtype: ModelBillingHistoryEdges
        """
        return self._edges

    @edges.setter
    def edges(self, edges):
        """Sets the edges of this ModelBillingHistory.


        :param edges: The edges of this ModelBillingHistory.  # noqa: E501
        :type edges: ModelBillingHistoryEdges
        """

        self._edges = edges

    @property
    def id(self):
        """Gets the id of this ModelBillingHistory.  # noqa: E501


        :return: The id of this ModelBillingHistory.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ModelBillingHistory.


        :param id: The id of this ModelBillingHistory.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def month(self):
        """Gets the month of this ModelBillingHistory.  # noqa: E501


        :return: The month of this ModelBillingHistory.  # noqa: E501
        :rtype: datetime
        """
        return self._month

    @month.setter
    def month(self, month):
        """Sets the month of this ModelBillingHistory.


        :param month: The month of this ModelBillingHistory.  # noqa: E501
        :type month: datetime
        """

        self._month = month

    @property
    def total(self):
        """Gets the total of this ModelBillingHistory.  # noqa: E501


        :return: The total of this ModelBillingHistory.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ModelBillingHistory.


        :param total: The total of this ModelBillingHistory.  # noqa: E501
        :type total: float
        """

        self._total = total

    @property
    def updated_dt(self):
        """Gets the updated_dt of this ModelBillingHistory.  # noqa: E501


        :return: The updated_dt of this ModelBillingHistory.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_dt

    @updated_dt.setter
    def updated_dt(self, updated_dt):
        """Sets the updated_dt of this ModelBillingHistory.


        :param updated_dt: The updated_dt of this ModelBillingHistory.  # noqa: E501
        :type updated_dt: datetime
        """

        self._updated_dt = updated_dt

    @property
    def workload_created_dt(self):
        """Gets the workload_created_dt of this ModelBillingHistory.  # noqa: E501


        :return: The workload_created_dt of this ModelBillingHistory.  # noqa: E501
        :rtype: datetime
        """
        return self._workload_created_dt

    @workload_created_dt.setter
    def workload_created_dt(self, workload_created_dt):
        """Sets the workload_created_dt of this ModelBillingHistory.


        :param workload_created_dt: The workload_created_dt of this ModelBillingHistory.  # noqa: E501
        :type workload_created_dt: datetime
        """

        self._workload_created_dt = workload_created_dt

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
        if not isinstance(other, ModelBillingHistory):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelBillingHistory):
            return True

        return self.to_dict() != other.to_dict()
