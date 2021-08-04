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


class ResponseProject(object):
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
        'cached_git_default_branch': 'str',
        'cached_git_http_url_to_repo': 'str',
        'cached_git_owner_slug': 'str',
        'cached_git_repo_slug': 'str',
        'cached_git_ssh_url_to_repo': 'str',
        'created_dt': 'datetime',
        'description': 'str',
        'git_provider': 'str',
        'id': 'int',
        'immutable_slug': 'str',
        'is_public': 'bool',
        'name': 'str',
        'organization_id': 'int',
        'primary_owner_id': 'int',
        'project_organization': 'int',
        'project_primary_owner': 'int',
        'project_volume': 'int',
        'type': 'str',
        'updated_dt': 'datetime',
        'volume_id': 'int'
    }

    attribute_map = {
        'cached_git_default_branch': 'cached_git_default_branch',
        'cached_git_http_url_to_repo': 'cached_git_http_url_to_repo',
        'cached_git_owner_slug': 'cached_git_owner_slug',
        'cached_git_repo_slug': 'cached_git_repo_slug',
        'cached_git_ssh_url_to_repo': 'cached_git_ssh_url_to_repo',
        'created_dt': 'created_dt',
        'description': 'description',
        'git_provider': 'git_provider',
        'id': 'id',
        'immutable_slug': 'immutable_slug',
        'is_public': 'is_public',
        'name': 'name',
        'organization_id': 'organization_id',
        'primary_owner_id': 'primary_owner_id',
        'project_organization': 'project_organization',
        'project_primary_owner': 'project_primary_owner',
        'project_volume': 'project_volume',
        'type': 'type',
        'updated_dt': 'updated_dt',
        'volume_id': 'volume_id'
    }

    def __init__(self, cached_git_default_branch=None, cached_git_http_url_to_repo=None, cached_git_owner_slug=None, cached_git_repo_slug=None, cached_git_ssh_url_to_repo=None, created_dt=None, description=None, git_provider=None, id=None, immutable_slug=None, is_public=None, name=None, organization_id=None, primary_owner_id=None, project_organization=None, project_primary_owner=None, project_volume=None, type=None, updated_dt=None, volume_id=None, local_vars_configuration=None):  # noqa: E501
        """ResponseProject - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._cached_git_default_branch = None
        self._cached_git_http_url_to_repo = None
        self._cached_git_owner_slug = None
        self._cached_git_repo_slug = None
        self._cached_git_ssh_url_to_repo = None
        self._created_dt = None
        self._description = None
        self._git_provider = None
        self._id = None
        self._immutable_slug = None
        self._is_public = None
        self._name = None
        self._organization_id = None
        self._primary_owner_id = None
        self._project_organization = None
        self._project_primary_owner = None
        self._project_volume = None
        self._type = None
        self._updated_dt = None
        self._volume_id = None
        self.discriminator = None

        self.cached_git_default_branch = cached_git_default_branch
        self.cached_git_http_url_to_repo = cached_git_http_url_to_repo
        self.cached_git_owner_slug = cached_git_owner_slug
        self.cached_git_repo_slug = cached_git_repo_slug
        self.cached_git_ssh_url_to_repo = cached_git_ssh_url_to_repo
        self.created_dt = created_dt
        self.description = description
        self.git_provider = git_provider
        self.id = id
        self.immutable_slug = immutable_slug
        self.is_public = is_public
        self.name = name
        self.organization_id = organization_id
        self.primary_owner_id = primary_owner_id
        self.project_organization = project_organization
        self.project_primary_owner = project_primary_owner
        self.project_volume = project_volume
        self.type = type
        self.updated_dt = updated_dt
        self.volume_id = volume_id

    @property
    def cached_git_default_branch(self):
        """Gets the cached_git_default_branch of this ResponseProject.  # noqa: E501


        :return: The cached_git_default_branch of this ResponseProject.  # noqa: E501
        :rtype: str
        """
        return self._cached_git_default_branch

    @cached_git_default_branch.setter
    def cached_git_default_branch(self, cached_git_default_branch):
        """Sets the cached_git_default_branch of this ResponseProject.


        :param cached_git_default_branch: The cached_git_default_branch of this ResponseProject.  # noqa: E501
        :type cached_git_default_branch: str
        """
        if self.local_vars_configuration.client_side_validation and cached_git_default_branch is None:  # noqa: E501
            raise ValueError("Invalid value for `cached_git_default_branch`, must not be `None`")  # noqa: E501

        self._cached_git_default_branch = cached_git_default_branch

    @property
    def cached_git_http_url_to_repo(self):
        """Gets the cached_git_http_url_to_repo of this ResponseProject.  # noqa: E501


        :return: The cached_git_http_url_to_repo of this ResponseProject.  # noqa: E501
        :rtype: str
        """
        return self._cached_git_http_url_to_repo

    @cached_git_http_url_to_repo.setter
    def cached_git_http_url_to_repo(self, cached_git_http_url_to_repo):
        """Sets the cached_git_http_url_to_repo of this ResponseProject.


        :param cached_git_http_url_to_repo: The cached_git_http_url_to_repo of this ResponseProject.  # noqa: E501
        :type cached_git_http_url_to_repo: str
        """

        self._cached_git_http_url_to_repo = cached_git_http_url_to_repo

    @property
    def cached_git_owner_slug(self):
        """Gets the cached_git_owner_slug of this ResponseProject.  # noqa: E501


        :return: The cached_git_owner_slug of this ResponseProject.  # noqa: E501
        :rtype: str
        """
        return self._cached_git_owner_slug

    @cached_git_owner_slug.setter
    def cached_git_owner_slug(self, cached_git_owner_slug):
        """Sets the cached_git_owner_slug of this ResponseProject.


        :param cached_git_owner_slug: The cached_git_owner_slug of this ResponseProject.  # noqa: E501
        :type cached_git_owner_slug: str
        """
        if self.local_vars_configuration.client_side_validation and cached_git_owner_slug is None:  # noqa: E501
            raise ValueError("Invalid value for `cached_git_owner_slug`, must not be `None`")  # noqa: E501

        self._cached_git_owner_slug = cached_git_owner_slug

    @property
    def cached_git_repo_slug(self):
        """Gets the cached_git_repo_slug of this ResponseProject.  # noqa: E501


        :return: The cached_git_repo_slug of this ResponseProject.  # noqa: E501
        :rtype: str
        """
        return self._cached_git_repo_slug

    @cached_git_repo_slug.setter
    def cached_git_repo_slug(self, cached_git_repo_slug):
        """Sets the cached_git_repo_slug of this ResponseProject.


        :param cached_git_repo_slug: The cached_git_repo_slug of this ResponseProject.  # noqa: E501
        :type cached_git_repo_slug: str
        """
        if self.local_vars_configuration.client_side_validation and cached_git_repo_slug is None:  # noqa: E501
            raise ValueError("Invalid value for `cached_git_repo_slug`, must not be `None`")  # noqa: E501

        self._cached_git_repo_slug = cached_git_repo_slug

    @property
    def cached_git_ssh_url_to_repo(self):
        """Gets the cached_git_ssh_url_to_repo of this ResponseProject.  # noqa: E501


        :return: The cached_git_ssh_url_to_repo of this ResponseProject.  # noqa: E501
        :rtype: str
        """
        return self._cached_git_ssh_url_to_repo

    @cached_git_ssh_url_to_repo.setter
    def cached_git_ssh_url_to_repo(self, cached_git_ssh_url_to_repo):
        """Sets the cached_git_ssh_url_to_repo of this ResponseProject.


        :param cached_git_ssh_url_to_repo: The cached_git_ssh_url_to_repo of this ResponseProject.  # noqa: E501
        :type cached_git_ssh_url_to_repo: str
        """

        self._cached_git_ssh_url_to_repo = cached_git_ssh_url_to_repo

    @property
    def created_dt(self):
        """Gets the created_dt of this ResponseProject.  # noqa: E501


        :return: The created_dt of this ResponseProject.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this ResponseProject.


        :param created_dt: The created_dt of this ResponseProject.  # noqa: E501
        :type created_dt: datetime
        """

        self._created_dt = created_dt

    @property
    def description(self):
        """Gets the description of this ResponseProject.  # noqa: E501


        :return: The description of this ResponseProject.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ResponseProject.


        :param description: The description of this ResponseProject.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def git_provider(self):
        """Gets the git_provider of this ResponseProject.  # noqa: E501


        :return: The git_provider of this ResponseProject.  # noqa: E501
        :rtype: str
        """
        return self._git_provider

    @git_provider.setter
    def git_provider(self, git_provider):
        """Sets the git_provider of this ResponseProject.


        :param git_provider: The git_provider of this ResponseProject.  # noqa: E501
        :type git_provider: str
        """
        if self.local_vars_configuration.client_side_validation and git_provider is None:  # noqa: E501
            raise ValueError("Invalid value for `git_provider`, must not be `None`")  # noqa: E501

        self._git_provider = git_provider

    @property
    def id(self):
        """Gets the id of this ResponseProject.  # noqa: E501


        :return: The id of this ResponseProject.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResponseProject.


        :param id: The id of this ResponseProject.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def immutable_slug(self):
        """Gets the immutable_slug of this ResponseProject.  # noqa: E501


        :return: The immutable_slug of this ResponseProject.  # noqa: E501
        :rtype: str
        """
        return self._immutable_slug

    @immutable_slug.setter
    def immutable_slug(self, immutable_slug):
        """Sets the immutable_slug of this ResponseProject.


        :param immutable_slug: The immutable_slug of this ResponseProject.  # noqa: E501
        :type immutable_slug: str
        """
        if self.local_vars_configuration.client_side_validation and immutable_slug is None:  # noqa: E501
            raise ValueError("Invalid value for `immutable_slug`, must not be `None`")  # noqa: E501

        self._immutable_slug = immutable_slug

    @property
    def is_public(self):
        """Gets the is_public of this ResponseProject.  # noqa: E501


        :return: The is_public of this ResponseProject.  # noqa: E501
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """Sets the is_public of this ResponseProject.


        :param is_public: The is_public of this ResponseProject.  # noqa: E501
        :type is_public: bool
        """
        if self.local_vars_configuration.client_side_validation and is_public is None:  # noqa: E501
            raise ValueError("Invalid value for `is_public`, must not be `None`")  # noqa: E501

        self._is_public = is_public

    @property
    def name(self):
        """Gets the name of this ResponseProject.  # noqa: E501


        :return: The name of this ResponseProject.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ResponseProject.


        :param name: The name of this ResponseProject.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def organization_id(self):
        """Gets the organization_id of this ResponseProject.  # noqa: E501


        :return: The organization_id of this ResponseProject.  # noqa: E501
        :rtype: int
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this ResponseProject.


        :param organization_id: The organization_id of this ResponseProject.  # noqa: E501
        :type organization_id: int
        """
        if self.local_vars_configuration.client_side_validation and organization_id is None:  # noqa: E501
            raise ValueError("Invalid value for `organization_id`, must not be `None`")  # noqa: E501

        self._organization_id = organization_id

    @property
    def primary_owner_id(self):
        """Gets the primary_owner_id of this ResponseProject.  # noqa: E501


        :return: The primary_owner_id of this ResponseProject.  # noqa: E501
        :rtype: int
        """
        return self._primary_owner_id

    @primary_owner_id.setter
    def primary_owner_id(self, primary_owner_id):
        """Sets the primary_owner_id of this ResponseProject.


        :param primary_owner_id: The primary_owner_id of this ResponseProject.  # noqa: E501
        :type primary_owner_id: int
        """
        if self.local_vars_configuration.client_side_validation and primary_owner_id is None:  # noqa: E501
            raise ValueError("Invalid value for `primary_owner_id`, must not be `None`")  # noqa: E501

        self._primary_owner_id = primary_owner_id

    @property
    def project_organization(self):
        """Gets the project_organization of this ResponseProject.  # noqa: E501


        :return: The project_organization of this ResponseProject.  # noqa: E501
        :rtype: int
        """
        return self._project_organization

    @project_organization.setter
    def project_organization(self, project_organization):
        """Sets the project_organization of this ResponseProject.


        :param project_organization: The project_organization of this ResponseProject.  # noqa: E501
        :type project_organization: int
        """
        if self.local_vars_configuration.client_side_validation and project_organization is None:  # noqa: E501
            raise ValueError("Invalid value for `project_organization`, must not be `None`")  # noqa: E501

        self._project_organization = project_organization

    @property
    def project_primary_owner(self):
        """Gets the project_primary_owner of this ResponseProject.  # noqa: E501


        :return: The project_primary_owner of this ResponseProject.  # noqa: E501
        :rtype: int
        """
        return self._project_primary_owner

    @project_primary_owner.setter
    def project_primary_owner(self, project_primary_owner):
        """Sets the project_primary_owner of this ResponseProject.


        :param project_primary_owner: The project_primary_owner of this ResponseProject.  # noqa: E501
        :type project_primary_owner: int
        """
        if self.local_vars_configuration.client_side_validation and project_primary_owner is None:  # noqa: E501
            raise ValueError("Invalid value for `project_primary_owner`, must not be `None`")  # noqa: E501

        self._project_primary_owner = project_primary_owner

    @property
    def project_volume(self):
        """Gets the project_volume of this ResponseProject.  # noqa: E501


        :return: The project_volume of this ResponseProject.  # noqa: E501
        :rtype: int
        """
        return self._project_volume

    @project_volume.setter
    def project_volume(self, project_volume):
        """Sets the project_volume of this ResponseProject.


        :param project_volume: The project_volume of this ResponseProject.  # noqa: E501
        :type project_volume: int
        """
        if self.local_vars_configuration.client_side_validation and project_volume is None:  # noqa: E501
            raise ValueError("Invalid value for `project_volume`, must not be `None`")  # noqa: E501

        self._project_volume = project_volume

    @property
    def type(self):
        """Gets the type of this ResponseProject.  # noqa: E501


        :return: The type of this ResponseProject.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ResponseProject.


        :param type: The type of this ResponseProject.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def updated_dt(self):
        """Gets the updated_dt of this ResponseProject.  # noqa: E501


        :return: The updated_dt of this ResponseProject.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_dt

    @updated_dt.setter
    def updated_dt(self, updated_dt):
        """Sets the updated_dt of this ResponseProject.


        :param updated_dt: The updated_dt of this ResponseProject.  # noqa: E501
        :type updated_dt: datetime
        """

        self._updated_dt = updated_dt

    @property
    def volume_id(self):
        """Gets the volume_id of this ResponseProject.  # noqa: E501


        :return: The volume_id of this ResponseProject.  # noqa: E501
        :rtype: int
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """Sets the volume_id of this ResponseProject.


        :param volume_id: The volume_id of this ResponseProject.  # noqa: E501
        :type volume_id: int
        """
        if self.local_vars_configuration.client_side_validation and volume_id is None:  # noqa: E501
            raise ValueError("Invalid value for `volume_id`, must not be `None`")  # noqa: E501

        self._volume_id = volume_id

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
        if not isinstance(other, ResponseProject):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResponseProject):
            return True

        return self.to_dict() != other.to_dict()
