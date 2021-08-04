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


class ReportSchemaGraphcanvas(object):
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
        'canvas_panel': 'list[ReportSchemaCanvaspanel]',
        'name': 'str'
    }

    attribute_map = {
        'canvas_panel': 'canvas-panel',
        'name': 'name'
    }

    def __init__(self, canvas_panel=None, name=None):  # noqa: E501
        """ReportSchemaGraphcanvas - a model defined in Swagger"""  # noqa: E501

        self._canvas_panel = None
        self._name = None
        self.discriminator = None

        if canvas_panel is not None:
            self.canvas_panel = canvas_panel
        self.name = name

    @property
    def canvas_panel(self):
        """Gets the canvas_panel of this ReportSchemaGraphcanvas.  # noqa: E501

        Canvas panel  # noqa: E501

        :return: The canvas_panel of this ReportSchemaGraphcanvas.  # noqa: E501
        :rtype: list[ReportSchemaCanvaspanel]
        """
        return self._canvas_panel

    @canvas_panel.setter
    def canvas_panel(self, canvas_panel):
        """Sets the canvas_panel of this ReportSchemaGraphcanvas.

        Canvas panel  # noqa: E501

        :param canvas_panel: The canvas_panel of this ReportSchemaGraphcanvas.  # noqa: E501
        :type: list[ReportSchemaCanvaspanel]
        """

        self._canvas_panel = canvas_panel

    @property
    def name(self):
        """Gets the name of this ReportSchemaGraphcanvas.  # noqa: E501

        Name of the canvas.  # noqa: E501

        :return: The name of this ReportSchemaGraphcanvas.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ReportSchemaGraphcanvas.

        Name of the canvas.  # noqa: E501

        :param name: The name of this ReportSchemaGraphcanvas.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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
        if issubclass(ReportSchemaGraphcanvas, dict):
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
        if not isinstance(other, ReportSchemaGraphcanvas):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
