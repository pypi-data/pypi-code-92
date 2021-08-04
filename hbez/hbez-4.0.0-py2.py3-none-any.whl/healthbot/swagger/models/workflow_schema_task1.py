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


class WorkflowSchemaTask1(object):
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
        'parallel': 'list[object]',
        'step': 'list[WorkflowSchemaStep]',
        'task_name': 'str'
    }

    attribute_map = {
        'parallel': 'parallel',
        'step': 'step',
        'task_name': 'task-name'
    }

    def __init__(self, parallel=None, step=None, task_name=None):  # noqa: E501
        """WorkflowSchemaTask1 - a model defined in Swagger"""  # noqa: E501

        self._parallel = None
        self._step = None
        self._task_name = None
        self.discriminator = None

        if parallel is not None:
            self.parallel = parallel
        if step is not None:
            self.step = step
        self.task_name = task_name

    @property
    def parallel(self):
        """Gets the parallel of this WorkflowSchemaTask1.  # noqa: E501

        Run all steps in this task in parallel to one another  # noqa: E501

        :return: The parallel of this WorkflowSchemaTask1.  # noqa: E501
        :rtype: list[object]
        """
        return self._parallel

    @parallel.setter
    def parallel(self, parallel):
        """Sets the parallel of this WorkflowSchemaTask1.

        Run all steps in this task in parallel to one another  # noqa: E501

        :param parallel: The parallel of this WorkflowSchemaTask1.  # noqa: E501
        :type: list[object]
        """

        self._parallel = parallel

    @property
    def step(self):
        """Gets the step of this WorkflowSchemaTask1.  # noqa: E501

        Workflow step configuration  # noqa: E501

        :return: The step of this WorkflowSchemaTask1.  # noqa: E501
        :rtype: list[WorkflowSchemaStep]
        """
        return self._step

    @step.setter
    def step(self, step):
        """Sets the step of this WorkflowSchemaTask1.

        Workflow step configuration  # noqa: E501

        :param step: The step of this WorkflowSchemaTask1.  # noqa: E501
        :type: list[WorkflowSchemaStep]
        """

        self._step = step

    @property
    def task_name(self):
        """Gets the task_name of this WorkflowSchemaTask1.  # noqa: E501

        Name of the task being called. Should be of pattern [a-zA-Z][a-zA-Z0-9_-]*  # noqa: E501

        :return: The task_name of this WorkflowSchemaTask1.  # noqa: E501
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this WorkflowSchemaTask1.

        Name of the task being called. Should be of pattern [a-zA-Z][a-zA-Z0-9_-]*  # noqa: E501

        :param task_name: The task_name of this WorkflowSchemaTask1.  # noqa: E501
        :type: str
        """
        if task_name is None:
            raise ValueError("Invalid value for `task_name`, must not be `None`")  # noqa: E501
        if task_name is not None and len(task_name) > 64:
            raise ValueError("Invalid value for `task_name`, length must be less than or equal to `64`")  # noqa: E501
        if task_name is not None and len(task_name) < 1:
            raise ValueError("Invalid value for `task_name`, length must be greater than or equal to `1`")  # noqa: E501
        if task_name is not None and not re.search(r'^[a-zA-Z][a-zA-Z0-9_-]*$', task_name):  # noqa: E501
            raise ValueError(r"Invalid value for `task_name`, must be a follow pattern or equal to `/^[a-zA-Z][a-zA-Z0-9_-]*$/`")  # noqa: E501

        self._task_name = task_name

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
        if issubclass(WorkflowSchemaTask1, dict):
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
        if not isinstance(other, WorkflowSchemaTask1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
