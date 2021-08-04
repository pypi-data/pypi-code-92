# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

#  (C) Copyright IBM Corp. 2020.
#  #
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#  #
#       http://www.apache.org/licenses/LICENSE-2.0
#  #
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from pprint import pformat
from six import iteritems


class MetaObjectFunctionsMetadata(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        MetaObjectFunctionsMetadata - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'guid': 'str',
            'created_at': 'datetime',
            'modified_at': 'datetime',
            'url': 'str'
        }

        self.attribute_map = {
            'guid': 'guid',
            'created_at': 'created_at',
            'modified_at': 'modified_at',
            'url': 'url'
        }

        self._guid = None
        self._created_at = None
        self._modified_at = None
        self._url = None

    @property
    def guid(self):
        """
        Gets the guid of this MetaObjectFunctionsMetadata.


        :return: The guid of this MetaObjectFunctionsMetadata.
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """
        Sets the guid of this MetaObjectFunctionsMetadata.


        :param guid: The guid of this MetaObjectFunctionsMetadata.
        :type: str
        """
        self._guid = guid

    @property
    def created_at(self):
        """
        Gets the created_at of this MetaObjectFunctionsMetadata.


        :return: The created_at of this MetaObjectFunctionsMetadata.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this MetaObjectFunctionsMetadata.


        :param created_at: The created_at of this MetaObjectFunctionsMetadata.
        :type: datetime
        """
        self._created_at = created_at

    @property
    def modified_at(self):
        """
        Gets the modified_at of this MetaObjectFunctionsMetadata.


        :return: The modified_at of this MetaObjectFunctionsMetadata.
        :rtype: datetime
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """
        Sets the modified_at of this MetaObjectFunctionsMetadata.


        :param modified_at: The modified_at of this MetaObjectFunctionsMetadata.
        :type: datetime
        """
        self._modified_at = modified_at

    @property
    def url(self):
        """
        Gets the url of this MetaObjectFunctionsMetadata.


        :return: The url of this MetaObjectFunctionsMetadata.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this MetaObjectFunctionsMetadata.


        :param url: The url of this MetaObjectFunctionsMetadata.
        :type: str
        """
        self._url = url

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

