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


class ModelWorkloadEdges(object):
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
        'access_token': 'ModelAccessToken',
        'billing_histories': 'list[ModelBillingHistory]',
        'created_by': 'ModelUser',
        'histories': 'list[ModelWorkloadHistory]',
        'kernel_cluster': 'ModelKernelCluster',
        'kernel_cluster_node': 'ModelKernelClusterNode',
        'kernel_image': 'ModelKernelImage',
        'kernel_resource_spec': 'ModelKernelResourceSpec',
        'organization': 'ModelOrganization',
        'project': 'ModelProject',
        'sweep': 'ModelSweep'
    }

    attribute_map = {
        'access_token': 'access_token',
        'billing_histories': 'billing_histories',
        'created_by': 'created_by',
        'histories': 'histories',
        'kernel_cluster': 'kernel_cluster',
        'kernel_cluster_node': 'kernel_cluster_node',
        'kernel_image': 'kernel_image',
        'kernel_resource_spec': 'kernel_resource_spec',
        'organization': 'organization',
        'project': 'project',
        'sweep': 'sweep'
    }

    def __init__(self, access_token=None, billing_histories=None, created_by=None, histories=None, kernel_cluster=None, kernel_cluster_node=None, kernel_image=None, kernel_resource_spec=None, organization=None, project=None, sweep=None, local_vars_configuration=None):  # noqa: E501
        """ModelWorkloadEdges - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._access_token = None
        self._billing_histories = None
        self._created_by = None
        self._histories = None
        self._kernel_cluster = None
        self._kernel_cluster_node = None
        self._kernel_image = None
        self._kernel_resource_spec = None
        self._organization = None
        self._project = None
        self._sweep = None
        self.discriminator = None

        if access_token is not None:
            self.access_token = access_token
        if billing_histories is not None:
            self.billing_histories = billing_histories
        if created_by is not None:
            self.created_by = created_by
        if histories is not None:
            self.histories = histories
        if kernel_cluster is not None:
            self.kernel_cluster = kernel_cluster
        if kernel_cluster_node is not None:
            self.kernel_cluster_node = kernel_cluster_node
        if kernel_image is not None:
            self.kernel_image = kernel_image
        if kernel_resource_spec is not None:
            self.kernel_resource_spec = kernel_resource_spec
        if organization is not None:
            self.organization = organization
        if project is not None:
            self.project = project
        if sweep is not None:
            self.sweep = sweep

    @property
    def access_token(self):
        """Gets the access_token of this ModelWorkloadEdges.  # noqa: E501


        :return: The access_token of this ModelWorkloadEdges.  # noqa: E501
        :rtype: ModelAccessToken
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this ModelWorkloadEdges.


        :param access_token: The access_token of this ModelWorkloadEdges.  # noqa: E501
        :type access_token: ModelAccessToken
        """

        self._access_token = access_token

    @property
    def billing_histories(self):
        """Gets the billing_histories of this ModelWorkloadEdges.  # noqa: E501


        :return: The billing_histories of this ModelWorkloadEdges.  # noqa: E501
        :rtype: list[ModelBillingHistory]
        """
        return self._billing_histories

    @billing_histories.setter
    def billing_histories(self, billing_histories):
        """Sets the billing_histories of this ModelWorkloadEdges.


        :param billing_histories: The billing_histories of this ModelWorkloadEdges.  # noqa: E501
        :type billing_histories: list[ModelBillingHistory]
        """

        self._billing_histories = billing_histories

    @property
    def created_by(self):
        """Gets the created_by of this ModelWorkloadEdges.  # noqa: E501


        :return: The created_by of this ModelWorkloadEdges.  # noqa: E501
        :rtype: ModelUser
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this ModelWorkloadEdges.


        :param created_by: The created_by of this ModelWorkloadEdges.  # noqa: E501
        :type created_by: ModelUser
        """

        self._created_by = created_by

    @property
    def histories(self):
        """Gets the histories of this ModelWorkloadEdges.  # noqa: E501


        :return: The histories of this ModelWorkloadEdges.  # noqa: E501
        :rtype: list[ModelWorkloadHistory]
        """
        return self._histories

    @histories.setter
    def histories(self, histories):
        """Sets the histories of this ModelWorkloadEdges.


        :param histories: The histories of this ModelWorkloadEdges.  # noqa: E501
        :type histories: list[ModelWorkloadHistory]
        """

        self._histories = histories

    @property
    def kernel_cluster(self):
        """Gets the kernel_cluster of this ModelWorkloadEdges.  # noqa: E501


        :return: The kernel_cluster of this ModelWorkloadEdges.  # noqa: E501
        :rtype: ModelKernelCluster
        """
        return self._kernel_cluster

    @kernel_cluster.setter
    def kernel_cluster(self, kernel_cluster):
        """Sets the kernel_cluster of this ModelWorkloadEdges.


        :param kernel_cluster: The kernel_cluster of this ModelWorkloadEdges.  # noqa: E501
        :type kernel_cluster: ModelKernelCluster
        """

        self._kernel_cluster = kernel_cluster

    @property
    def kernel_cluster_node(self):
        """Gets the kernel_cluster_node of this ModelWorkloadEdges.  # noqa: E501


        :return: The kernel_cluster_node of this ModelWorkloadEdges.  # noqa: E501
        :rtype: ModelKernelClusterNode
        """
        return self._kernel_cluster_node

    @kernel_cluster_node.setter
    def kernel_cluster_node(self, kernel_cluster_node):
        """Sets the kernel_cluster_node of this ModelWorkloadEdges.


        :param kernel_cluster_node: The kernel_cluster_node of this ModelWorkloadEdges.  # noqa: E501
        :type kernel_cluster_node: ModelKernelClusterNode
        """

        self._kernel_cluster_node = kernel_cluster_node

    @property
    def kernel_image(self):
        """Gets the kernel_image of this ModelWorkloadEdges.  # noqa: E501


        :return: The kernel_image of this ModelWorkloadEdges.  # noqa: E501
        :rtype: ModelKernelImage
        """
        return self._kernel_image

    @kernel_image.setter
    def kernel_image(self, kernel_image):
        """Sets the kernel_image of this ModelWorkloadEdges.


        :param kernel_image: The kernel_image of this ModelWorkloadEdges.  # noqa: E501
        :type kernel_image: ModelKernelImage
        """

        self._kernel_image = kernel_image

    @property
    def kernel_resource_spec(self):
        """Gets the kernel_resource_spec of this ModelWorkloadEdges.  # noqa: E501


        :return: The kernel_resource_spec of this ModelWorkloadEdges.  # noqa: E501
        :rtype: ModelKernelResourceSpec
        """
        return self._kernel_resource_spec

    @kernel_resource_spec.setter
    def kernel_resource_spec(self, kernel_resource_spec):
        """Sets the kernel_resource_spec of this ModelWorkloadEdges.


        :param kernel_resource_spec: The kernel_resource_spec of this ModelWorkloadEdges.  # noqa: E501
        :type kernel_resource_spec: ModelKernelResourceSpec
        """

        self._kernel_resource_spec = kernel_resource_spec

    @property
    def organization(self):
        """Gets the organization of this ModelWorkloadEdges.  # noqa: E501


        :return: The organization of this ModelWorkloadEdges.  # noqa: E501
        :rtype: ModelOrganization
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this ModelWorkloadEdges.


        :param organization: The organization of this ModelWorkloadEdges.  # noqa: E501
        :type organization: ModelOrganization
        """

        self._organization = organization

    @property
    def project(self):
        """Gets the project of this ModelWorkloadEdges.  # noqa: E501


        :return: The project of this ModelWorkloadEdges.  # noqa: E501
        :rtype: ModelProject
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this ModelWorkloadEdges.


        :param project: The project of this ModelWorkloadEdges.  # noqa: E501
        :type project: ModelProject
        """

        self._project = project

    @property
    def sweep(self):
        """Gets the sweep of this ModelWorkloadEdges.  # noqa: E501


        :return: The sweep of this ModelWorkloadEdges.  # noqa: E501
        :rtype: ModelSweep
        """
        return self._sweep

    @sweep.setter
    def sweep(self, sweep):
        """Sets the sweep of this ModelWorkloadEdges.


        :param sweep: The sweep of this ModelWorkloadEdges.  # noqa: E501
        :type sweep: ModelSweep
        """

        self._sweep = sweep

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
        if not isinstance(other, ModelWorkloadEdges):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelWorkloadEdges):
            return True

        return self.to_dict() != other.to_dict()
