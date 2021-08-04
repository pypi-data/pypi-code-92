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


class ResponseKernelImage(object):
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
        'command': 'str',
        'created_dt': 'datetime',
        'description': 'str',
        'execute_type': 'str',
        'id': 'int',
        'image_pull_policy': 'str',
        'image_url': 'str',
        'immutable_slug': 'str',
        'is_public': 'bool',
        'is_savvihub_managed': 'bool',
        'kernel_image_organization': 'int',
        'kernel_image_organization_credentials': 'int',
        'language': 'str',
        'name': 'str',
        'organization_credentials_id': 'int',
        'organization_id': 'int',
        'packages': 'str',
        'processor_type': 'str',
        'updated_dt': 'datetime',
        'working_dir': 'str'
    }

    attribute_map = {
        'command': 'command',
        'created_dt': 'created_dt',
        'description': 'description',
        'execute_type': 'execute_type',
        'id': 'id',
        'image_pull_policy': 'image_pull_policy',
        'image_url': 'image_url',
        'immutable_slug': 'immutable_slug',
        'is_public': 'is_public',
        'is_savvihub_managed': 'is_savvihub_managed',
        'kernel_image_organization': 'kernel_image_organization',
        'kernel_image_organization_credentials': 'kernel_image_organization_credentials',
        'language': 'language',
        'name': 'name',
        'organization_credentials_id': 'organization_credentials_id',
        'organization_id': 'organization_id',
        'packages': 'packages',
        'processor_type': 'processor_type',
        'updated_dt': 'updated_dt',
        'working_dir': 'working_dir'
    }

    def __init__(self, command=None, created_dt=None, description=None, execute_type=None, id=None, image_pull_policy=None, image_url=None, immutable_slug=None, is_public=None, is_savvihub_managed=None, kernel_image_organization=None, kernel_image_organization_credentials=None, language=None, name=None, organization_credentials_id=None, organization_id=None, packages=None, processor_type=None, updated_dt=None, working_dir=None, local_vars_configuration=None):  # noqa: E501
        """ResponseKernelImage - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._command = None
        self._created_dt = None
        self._description = None
        self._execute_type = None
        self._id = None
        self._image_pull_policy = None
        self._image_url = None
        self._immutable_slug = None
        self._is_public = None
        self._is_savvihub_managed = None
        self._kernel_image_organization = None
        self._kernel_image_organization_credentials = None
        self._language = None
        self._name = None
        self._organization_credentials_id = None
        self._organization_id = None
        self._packages = None
        self._processor_type = None
        self._updated_dt = None
        self._working_dir = None
        self.discriminator = None

        self.command = command
        self.created_dt = created_dt
        self.description = description
        self.execute_type = execute_type
        self.id = id
        self.image_pull_policy = image_pull_policy
        self.image_url = image_url
        self.immutable_slug = immutable_slug
        self.is_public = is_public
        self.is_savvihub_managed = is_savvihub_managed
        self.kernel_image_organization = kernel_image_organization
        self.kernel_image_organization_credentials = kernel_image_organization_credentials
        self.language = language
        self.name = name
        self.organization_credentials_id = organization_credentials_id
        self.organization_id = organization_id
        self.packages = packages
        self.processor_type = processor_type
        self.updated_dt = updated_dt
        self.working_dir = working_dir

    @property
    def command(self):
        """Gets the command of this ResponseKernelImage.  # noqa: E501


        :return: The command of this ResponseKernelImage.  # noqa: E501
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this ResponseKernelImage.


        :param command: The command of this ResponseKernelImage.  # noqa: E501
        :type command: str
        """
        if self.local_vars_configuration.client_side_validation and command is None:  # noqa: E501
            raise ValueError("Invalid value for `command`, must not be `None`")  # noqa: E501

        self._command = command

    @property
    def created_dt(self):
        """Gets the created_dt of this ResponseKernelImage.  # noqa: E501


        :return: The created_dt of this ResponseKernelImage.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this ResponseKernelImage.


        :param created_dt: The created_dt of this ResponseKernelImage.  # noqa: E501
        :type created_dt: datetime
        """

        self._created_dt = created_dt

    @property
    def description(self):
        """Gets the description of this ResponseKernelImage.  # noqa: E501


        :return: The description of this ResponseKernelImage.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ResponseKernelImage.


        :param description: The description of this ResponseKernelImage.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def execute_type(self):
        """Gets the execute_type of this ResponseKernelImage.  # noqa: E501


        :return: The execute_type of this ResponseKernelImage.  # noqa: E501
        :rtype: str
        """
        return self._execute_type

    @execute_type.setter
    def execute_type(self, execute_type):
        """Sets the execute_type of this ResponseKernelImage.


        :param execute_type: The execute_type of this ResponseKernelImage.  # noqa: E501
        :type execute_type: str
        """

        self._execute_type = execute_type

    @property
    def id(self):
        """Gets the id of this ResponseKernelImage.  # noqa: E501


        :return: The id of this ResponseKernelImage.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResponseKernelImage.


        :param id: The id of this ResponseKernelImage.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def image_pull_policy(self):
        """Gets the image_pull_policy of this ResponseKernelImage.  # noqa: E501


        :return: The image_pull_policy of this ResponseKernelImage.  # noqa: E501
        :rtype: str
        """
        return self._image_pull_policy

    @image_pull_policy.setter
    def image_pull_policy(self, image_pull_policy):
        """Sets the image_pull_policy of this ResponseKernelImage.


        :param image_pull_policy: The image_pull_policy of this ResponseKernelImage.  # noqa: E501
        :type image_pull_policy: str
        """
        if self.local_vars_configuration.client_side_validation and image_pull_policy is None:  # noqa: E501
            raise ValueError("Invalid value for `image_pull_policy`, must not be `None`")  # noqa: E501

        self._image_pull_policy = image_pull_policy

    @property
    def image_url(self):
        """Gets the image_url of this ResponseKernelImage.  # noqa: E501


        :return: The image_url of this ResponseKernelImage.  # noqa: E501
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this ResponseKernelImage.


        :param image_url: The image_url of this ResponseKernelImage.  # noqa: E501
        :type image_url: str
        """
        if self.local_vars_configuration.client_side_validation and image_url is None:  # noqa: E501
            raise ValueError("Invalid value for `image_url`, must not be `None`")  # noqa: E501

        self._image_url = image_url

    @property
    def immutable_slug(self):
        """Gets the immutable_slug of this ResponseKernelImage.  # noqa: E501


        :return: The immutable_slug of this ResponseKernelImage.  # noqa: E501
        :rtype: str
        """
        return self._immutable_slug

    @immutable_slug.setter
    def immutable_slug(self, immutable_slug):
        """Sets the immutable_slug of this ResponseKernelImage.


        :param immutable_slug: The immutable_slug of this ResponseKernelImage.  # noqa: E501
        :type immutable_slug: str
        """
        if self.local_vars_configuration.client_side_validation and immutable_slug is None:  # noqa: E501
            raise ValueError("Invalid value for `immutable_slug`, must not be `None`")  # noqa: E501

        self._immutable_slug = immutable_slug

    @property
    def is_public(self):
        """Gets the is_public of this ResponseKernelImage.  # noqa: E501


        :return: The is_public of this ResponseKernelImage.  # noqa: E501
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """Sets the is_public of this ResponseKernelImage.


        :param is_public: The is_public of this ResponseKernelImage.  # noqa: E501
        :type is_public: bool
        """
        if self.local_vars_configuration.client_side_validation and is_public is None:  # noqa: E501
            raise ValueError("Invalid value for `is_public`, must not be `None`")  # noqa: E501

        self._is_public = is_public

    @property
    def is_savvihub_managed(self):
        """Gets the is_savvihub_managed of this ResponseKernelImage.  # noqa: E501


        :return: The is_savvihub_managed of this ResponseKernelImage.  # noqa: E501
        :rtype: bool
        """
        return self._is_savvihub_managed

    @is_savvihub_managed.setter
    def is_savvihub_managed(self, is_savvihub_managed):
        """Sets the is_savvihub_managed of this ResponseKernelImage.


        :param is_savvihub_managed: The is_savvihub_managed of this ResponseKernelImage.  # noqa: E501
        :type is_savvihub_managed: bool
        """
        if self.local_vars_configuration.client_side_validation and is_savvihub_managed is None:  # noqa: E501
            raise ValueError("Invalid value for `is_savvihub_managed`, must not be `None`")  # noqa: E501

        self._is_savvihub_managed = is_savvihub_managed

    @property
    def kernel_image_organization(self):
        """Gets the kernel_image_organization of this ResponseKernelImage.  # noqa: E501


        :return: The kernel_image_organization of this ResponseKernelImage.  # noqa: E501
        :rtype: int
        """
        return self._kernel_image_organization

    @kernel_image_organization.setter
    def kernel_image_organization(self, kernel_image_organization):
        """Sets the kernel_image_organization of this ResponseKernelImage.


        :param kernel_image_organization: The kernel_image_organization of this ResponseKernelImage.  # noqa: E501
        :type kernel_image_organization: int
        """
        if self.local_vars_configuration.client_side_validation and kernel_image_organization is None:  # noqa: E501
            raise ValueError("Invalid value for `kernel_image_organization`, must not be `None`")  # noqa: E501

        self._kernel_image_organization = kernel_image_organization

    @property
    def kernel_image_organization_credentials(self):
        """Gets the kernel_image_organization_credentials of this ResponseKernelImage.  # noqa: E501


        :return: The kernel_image_organization_credentials of this ResponseKernelImage.  # noqa: E501
        :rtype: int
        """
        return self._kernel_image_organization_credentials

    @kernel_image_organization_credentials.setter
    def kernel_image_organization_credentials(self, kernel_image_organization_credentials):
        """Sets the kernel_image_organization_credentials of this ResponseKernelImage.


        :param kernel_image_organization_credentials: The kernel_image_organization_credentials of this ResponseKernelImage.  # noqa: E501
        :type kernel_image_organization_credentials: int
        """

        self._kernel_image_organization_credentials = kernel_image_organization_credentials

    @property
    def language(self):
        """Gets the language of this ResponseKernelImage.  # noqa: E501


        :return: The language of this ResponseKernelImage.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this ResponseKernelImage.


        :param language: The language of this ResponseKernelImage.  # noqa: E501
        :type language: str
        """

        self._language = language

    @property
    def name(self):
        """Gets the name of this ResponseKernelImage.  # noqa: E501


        :return: The name of this ResponseKernelImage.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ResponseKernelImage.


        :param name: The name of this ResponseKernelImage.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def organization_credentials_id(self):
        """Gets the organization_credentials_id of this ResponseKernelImage.  # noqa: E501


        :return: The organization_credentials_id of this ResponseKernelImage.  # noqa: E501
        :rtype: int
        """
        return self._organization_credentials_id

    @organization_credentials_id.setter
    def organization_credentials_id(self, organization_credentials_id):
        """Sets the organization_credentials_id of this ResponseKernelImage.


        :param organization_credentials_id: The organization_credentials_id of this ResponseKernelImage.  # noqa: E501
        :type organization_credentials_id: int
        """

        self._organization_credentials_id = organization_credentials_id

    @property
    def organization_id(self):
        """Gets the organization_id of this ResponseKernelImage.  # noqa: E501


        :return: The organization_id of this ResponseKernelImage.  # noqa: E501
        :rtype: int
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this ResponseKernelImage.


        :param organization_id: The organization_id of this ResponseKernelImage.  # noqa: E501
        :type organization_id: int
        """
        if self.local_vars_configuration.client_side_validation and organization_id is None:  # noqa: E501
            raise ValueError("Invalid value for `organization_id`, must not be `None`")  # noqa: E501

        self._organization_id = organization_id

    @property
    def packages(self):
        """Gets the packages of this ResponseKernelImage.  # noqa: E501


        :return: The packages of this ResponseKernelImage.  # noqa: E501
        :rtype: str
        """
        return self._packages

    @packages.setter
    def packages(self, packages):
        """Sets the packages of this ResponseKernelImage.


        :param packages: The packages of this ResponseKernelImage.  # noqa: E501
        :type packages: str
        """
        if self.local_vars_configuration.client_side_validation and packages is None:  # noqa: E501
            raise ValueError("Invalid value for `packages`, must not be `None`")  # noqa: E501

        self._packages = packages

    @property
    def processor_type(self):
        """Gets the processor_type of this ResponseKernelImage.  # noqa: E501


        :return: The processor_type of this ResponseKernelImage.  # noqa: E501
        :rtype: str
        """
        return self._processor_type

    @processor_type.setter
    def processor_type(self, processor_type):
        """Sets the processor_type of this ResponseKernelImage.


        :param processor_type: The processor_type of this ResponseKernelImage.  # noqa: E501
        :type processor_type: str
        """

        self._processor_type = processor_type

    @property
    def updated_dt(self):
        """Gets the updated_dt of this ResponseKernelImage.  # noqa: E501


        :return: The updated_dt of this ResponseKernelImage.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_dt

    @updated_dt.setter
    def updated_dt(self, updated_dt):
        """Sets the updated_dt of this ResponseKernelImage.


        :param updated_dt: The updated_dt of this ResponseKernelImage.  # noqa: E501
        :type updated_dt: datetime
        """

        self._updated_dt = updated_dt

    @property
    def working_dir(self):
        """Gets the working_dir of this ResponseKernelImage.  # noqa: E501


        :return: The working_dir of this ResponseKernelImage.  # noqa: E501
        :rtype: str
        """
        return self._working_dir

    @working_dir.setter
    def working_dir(self, working_dir):
        """Sets the working_dir of this ResponseKernelImage.


        :param working_dir: The working_dir of this ResponseKernelImage.  # noqa: E501
        :type working_dir: str
        """

        self._working_dir = working_dir

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
        if not isinstance(other, ResponseKernelImage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResponseKernelImage):
            return True

        return self.to_dict() != other.to_dict()
