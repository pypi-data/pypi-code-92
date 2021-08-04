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

from pulpcore.client.pulp_ansible.configuration import Configuration


class AnsibleCollectionVersion(object):
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
        'artifact': 'str',
        'id': 'str',
        'authors': 'list[str]',
        'contents': 'object',
        'dependencies': 'object',
        'description': 'str',
        'docs_blob': 'object',
        'manifest': 'object',
        'files': 'object',
        'documentation': 'str',
        'homepage': 'str',
        'issues': 'str',
        'license': 'list[str]',
        'name': 'str',
        'namespace': 'str',
        'repository': 'str',
        'version': 'str',
        'requires_ansible': 'str'
    }

    attribute_map = {
        'artifact': 'artifact',
        'id': 'id',
        'authors': 'authors',
        'contents': 'contents',
        'dependencies': 'dependencies',
        'description': 'description',
        'docs_blob': 'docs_blob',
        'manifest': 'manifest',
        'files': 'files',
        'documentation': 'documentation',
        'homepage': 'homepage',
        'issues': 'issues',
        'license': 'license',
        'name': 'name',
        'namespace': 'namespace',
        'repository': 'repository',
        'version': 'version',
        'requires_ansible': 'requires_ansible'
    }

    def __init__(self, artifact=None, id=None, authors=None, contents=None, dependencies=None, description=None, docs_blob=None, manifest=None, files=None, documentation=None, homepage=None, issues=None, license=None, name=None, namespace=None, repository=None, version=None, requires_ansible=None, local_vars_configuration=None):  # noqa: E501
        """AnsibleCollectionVersion - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._artifact = None
        self._id = None
        self._authors = None
        self._contents = None
        self._dependencies = None
        self._description = None
        self._docs_blob = None
        self._manifest = None
        self._files = None
        self._documentation = None
        self._homepage = None
        self._issues = None
        self._license = None
        self._name = None
        self._namespace = None
        self._repository = None
        self._version = None
        self._requires_ansible = None
        self.discriminator = None

        self.artifact = artifact
        self.id = id
        self.authors = authors
        self.contents = contents
        self.dependencies = dependencies
        self.description = description
        self.docs_blob = docs_blob
        self.manifest = manifest
        self.files = files
        self.documentation = documentation
        self.homepage = homepage
        self.issues = issues
        self.license = license
        self.name = name
        self.namespace = namespace
        self.repository = repository
        self.version = version
        self.requires_ansible = requires_ansible

    @property
    def artifact(self):
        """Gets the artifact of this AnsibleCollectionVersion.  # noqa: E501

        Artifact file representing the physical content  # noqa: E501

        :return: The artifact of this AnsibleCollectionVersion.  # noqa: E501
        :rtype: str
        """
        return self._artifact

    @artifact.setter
    def artifact(self, artifact):
        """Sets the artifact of this AnsibleCollectionVersion.

        Artifact file representing the physical content  # noqa: E501

        :param artifact: The artifact of this AnsibleCollectionVersion.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and artifact is None:  # noqa: E501
            raise ValueError("Invalid value for `artifact`, must not be `None`")  # noqa: E501

        self._artifact = artifact

    @property
    def id(self):
        """Gets the id of this AnsibleCollectionVersion.  # noqa: E501

        A collection identifier.  # noqa: E501

        :return: The id of this AnsibleCollectionVersion.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AnsibleCollectionVersion.

        A collection identifier.  # noqa: E501

        :param id: The id of this AnsibleCollectionVersion.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def authors(self):
        """Gets the authors of this AnsibleCollectionVersion.  # noqa: E501

        A list of the CollectionVersion content's authors.  # noqa: E501

        :return: The authors of this AnsibleCollectionVersion.  # noqa: E501
        :rtype: list[str]
        """
        return self._authors

    @authors.setter
    def authors(self, authors):
        """Sets the authors of this AnsibleCollectionVersion.

        A list of the CollectionVersion content's authors.  # noqa: E501

        :param authors: The authors of this AnsibleCollectionVersion.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and authors is None:  # noqa: E501
            raise ValueError("Invalid value for `authors`, must not be `None`")  # noqa: E501

        self._authors = authors

    @property
    def contents(self):
        """Gets the contents of this AnsibleCollectionVersion.  # noqa: E501

        A JSON field with data about the contents.  # noqa: E501

        :return: The contents of this AnsibleCollectionVersion.  # noqa: E501
        :rtype: object
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        """Sets the contents of this AnsibleCollectionVersion.

        A JSON field with data about the contents.  # noqa: E501

        :param contents: The contents of this AnsibleCollectionVersion.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and contents is None:  # noqa: E501
            raise ValueError("Invalid value for `contents`, must not be `None`")  # noqa: E501

        self._contents = contents

    @property
    def dependencies(self):
        """Gets the dependencies of this AnsibleCollectionVersion.  # noqa: E501

        A dict declaring Collections that this collection requires to be installed for it to be usable.  # noqa: E501

        :return: The dependencies of this AnsibleCollectionVersion.  # noqa: E501
        :rtype: object
        """
        return self._dependencies

    @dependencies.setter
    def dependencies(self, dependencies):
        """Sets the dependencies of this AnsibleCollectionVersion.

        A dict declaring Collections that this collection requires to be installed for it to be usable.  # noqa: E501

        :param dependencies: The dependencies of this AnsibleCollectionVersion.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and dependencies is None:  # noqa: E501
            raise ValueError("Invalid value for `dependencies`, must not be `None`")  # noqa: E501

        self._dependencies = dependencies

    @property
    def description(self):
        """Gets the description of this AnsibleCollectionVersion.  # noqa: E501

        A short summary description of the collection.  # noqa: E501

        :return: The description of this AnsibleCollectionVersion.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AnsibleCollectionVersion.

        A short summary description of the collection.  # noqa: E501

        :param description: The description of this AnsibleCollectionVersion.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def docs_blob(self):
        """Gets the docs_blob of this AnsibleCollectionVersion.  # noqa: E501

        A JSON field holding the various documentation blobs in the collection.  # noqa: E501

        :return: The docs_blob of this AnsibleCollectionVersion.  # noqa: E501
        :rtype: object
        """
        return self._docs_blob

    @docs_blob.setter
    def docs_blob(self, docs_blob):
        """Sets the docs_blob of this AnsibleCollectionVersion.

        A JSON field holding the various documentation blobs in the collection.  # noqa: E501

        :param docs_blob: The docs_blob of this AnsibleCollectionVersion.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and docs_blob is None:  # noqa: E501
            raise ValueError("Invalid value for `docs_blob`, must not be `None`")  # noqa: E501

        self._docs_blob = docs_blob

    @property
    def manifest(self):
        """Gets the manifest of this AnsibleCollectionVersion.  # noqa: E501

        A JSON field holding MANIFEST.json data.  # noqa: E501

        :return: The manifest of this AnsibleCollectionVersion.  # noqa: E501
        :rtype: object
        """
        return self._manifest

    @manifest.setter
    def manifest(self, manifest):
        """Sets the manifest of this AnsibleCollectionVersion.

        A JSON field holding MANIFEST.json data.  # noqa: E501

        :param manifest: The manifest of this AnsibleCollectionVersion.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and manifest is None:  # noqa: E501
            raise ValueError("Invalid value for `manifest`, must not be `None`")  # noqa: E501

        self._manifest = manifest

    @property
    def files(self):
        """Gets the files of this AnsibleCollectionVersion.  # noqa: E501

        A JSON field holding FILES.json data.  # noqa: E501

        :return: The files of this AnsibleCollectionVersion.  # noqa: E501
        :rtype: object
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this AnsibleCollectionVersion.

        A JSON field holding FILES.json data.  # noqa: E501

        :param files: The files of this AnsibleCollectionVersion.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and files is None:  # noqa: E501
            raise ValueError("Invalid value for `files`, must not be `None`")  # noqa: E501

        self._files = files

    @property
    def documentation(self):
        """Gets the documentation of this AnsibleCollectionVersion.  # noqa: E501

        The URL to any online docs.  # noqa: E501

        :return: The documentation of this AnsibleCollectionVersion.  # noqa: E501
        :rtype: str
        """
        return self._documentation

    @documentation.setter
    def documentation(self, documentation):
        """Sets the documentation of this AnsibleCollectionVersion.

        The URL to any online docs.  # noqa: E501

        :param documentation: The documentation of this AnsibleCollectionVersion.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and documentation is None:  # noqa: E501
            raise ValueError("Invalid value for `documentation`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                documentation is not None and len(documentation) > 2000):
            raise ValueError("Invalid value for `documentation`, length must be less than or equal to `2000`")  # noqa: E501

        self._documentation = documentation

    @property
    def homepage(self):
        """Gets the homepage of this AnsibleCollectionVersion.  # noqa: E501

        The URL to the homepage of the collection/project.  # noqa: E501

        :return: The homepage of this AnsibleCollectionVersion.  # noqa: E501
        :rtype: str
        """
        return self._homepage

    @homepage.setter
    def homepage(self, homepage):
        """Sets the homepage of this AnsibleCollectionVersion.

        The URL to the homepage of the collection/project.  # noqa: E501

        :param homepage: The homepage of this AnsibleCollectionVersion.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and homepage is None:  # noqa: E501
            raise ValueError("Invalid value for `homepage`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                homepage is not None and len(homepage) > 2000):
            raise ValueError("Invalid value for `homepage`, length must be less than or equal to `2000`")  # noqa: E501

        self._homepage = homepage

    @property
    def issues(self):
        """Gets the issues of this AnsibleCollectionVersion.  # noqa: E501

        The URL to the collection issue tracker.  # noqa: E501

        :return: The issues of this AnsibleCollectionVersion.  # noqa: E501
        :rtype: str
        """
        return self._issues

    @issues.setter
    def issues(self, issues):
        """Sets the issues of this AnsibleCollectionVersion.

        The URL to the collection issue tracker.  # noqa: E501

        :param issues: The issues of this AnsibleCollectionVersion.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and issues is None:  # noqa: E501
            raise ValueError("Invalid value for `issues`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                issues is not None and len(issues) > 2000):
            raise ValueError("Invalid value for `issues`, length must be less than or equal to `2000`")  # noqa: E501

        self._issues = issues

    @property
    def license(self):
        """Gets the license of this AnsibleCollectionVersion.  # noqa: E501

        A list of licenses for content inside of a collection.  # noqa: E501

        :return: The license of this AnsibleCollectionVersion.  # noqa: E501
        :rtype: list[str]
        """
        return self._license

    @license.setter
    def license(self, license):
        """Sets the license of this AnsibleCollectionVersion.

        A list of licenses for content inside of a collection.  # noqa: E501

        :param license: The license of this AnsibleCollectionVersion.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and license is None:  # noqa: E501
            raise ValueError("Invalid value for `license`, must not be `None`")  # noqa: E501

        self._license = license

    @property
    def name(self):
        """Gets the name of this AnsibleCollectionVersion.  # noqa: E501

        The name of the collection.  # noqa: E501

        :return: The name of this AnsibleCollectionVersion.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AnsibleCollectionVersion.

        The name of the collection.  # noqa: E501

        :param name: The name of this AnsibleCollectionVersion.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 64):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `64`")  # noqa: E501

        self._name = name

    @property
    def namespace(self):
        """Gets the namespace of this AnsibleCollectionVersion.  # noqa: E501

        The namespace of the collection.  # noqa: E501

        :return: The namespace of this AnsibleCollectionVersion.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this AnsibleCollectionVersion.

        The namespace of the collection.  # noqa: E501

        :param namespace: The namespace of this AnsibleCollectionVersion.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and namespace is None:  # noqa: E501
            raise ValueError("Invalid value for `namespace`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                namespace is not None and len(namespace) > 64):
            raise ValueError("Invalid value for `namespace`, length must be less than or equal to `64`")  # noqa: E501

        self._namespace = namespace

    @property
    def repository(self):
        """Gets the repository of this AnsibleCollectionVersion.  # noqa: E501

        The URL of the originating SCM repository.  # noqa: E501

        :return: The repository of this AnsibleCollectionVersion.  # noqa: E501
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        """Sets the repository of this AnsibleCollectionVersion.

        The URL of the originating SCM repository.  # noqa: E501

        :param repository: The repository of this AnsibleCollectionVersion.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and repository is None:  # noqa: E501
            raise ValueError("Invalid value for `repository`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                repository is not None and len(repository) > 2000):
            raise ValueError("Invalid value for `repository`, length must be less than or equal to `2000`")  # noqa: E501

        self._repository = repository

    @property
    def version(self):
        """Gets the version of this AnsibleCollectionVersion.  # noqa: E501

        The version of the collection.  # noqa: E501

        :return: The version of this AnsibleCollectionVersion.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this AnsibleCollectionVersion.

        The version of the collection.  # noqa: E501

        :param version: The version of this AnsibleCollectionVersion.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and version is None:  # noqa: E501
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                version is not None and len(version) > 128):
            raise ValueError("Invalid value for `version`, length must be less than or equal to `128`")  # noqa: E501

        self._version = version

    @property
    def requires_ansible(self):
        """Gets the requires_ansible of this AnsibleCollectionVersion.  # noqa: E501

        The version of Ansible required to use the collection. Multiple versions can be separated with a comma.  # noqa: E501

        :return: The requires_ansible of this AnsibleCollectionVersion.  # noqa: E501
        :rtype: str
        """
        return self._requires_ansible

    @requires_ansible.setter
    def requires_ansible(self, requires_ansible):
        """Sets the requires_ansible of this AnsibleCollectionVersion.

        The version of Ansible required to use the collection. Multiple versions can be separated with a comma.  # noqa: E501

        :param requires_ansible: The requires_ansible of this AnsibleCollectionVersion.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                requires_ansible is not None and len(requires_ansible) > 255):
            raise ValueError("Invalid value for `requires_ansible`, length must be less than or equal to `255`")  # noqa: E501

        self._requires_ansible = requires_ansible

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
        if not isinstance(other, AnsibleCollectionVersion):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AnsibleCollectionVersion):
            return True

        return self.to_dict() != other.to_dict()
