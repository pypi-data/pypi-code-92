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


class WorkflowSchemaStep(object):
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
        'cli_command': 'list[WorkflowCommandSchema]',
        'executable': 'list[WorkflowCommandSchema]',
        'netconf_command': 'list[WorkflowCommandSchema]',
        'notification': 'list[WorkflowNotificationSchema]',
        'condition': 'list[str]',
        'condition_description': 'str',
        'condition_type': 'str',
        'dependencies': 'list[str]',
        'description': 'str',
        'input': 'list[WorkflowSchemaInput]',
        'output': 'list[WorkflowSchemaOutput]',
        'step_name': 'str',
        'suspend': 'WorkflowSchemaSuspend',
        'task': 'WorkflowSchemaTask',
        'workflow': 'WorkflowSchemaWorkflow'
    }

    attribute_map = {
        'cli_command': 'cli-command',
        'executable': 'executable',
        'netconf_command': 'netconf-command',
        'notification': 'notification',
        'condition': 'condition',
        'condition_description': 'condition-description',
        'condition_type': 'condition-type',
        'dependencies': 'dependencies',
        'description': 'description',
        'input': 'input',
        'output': 'output',
        'step_name': 'step-name',
        'suspend': 'suspend',
        'task': 'task',
        'workflow': 'workflow'
    }

    def __init__(self, cli_command=None, executable=None, netconf_command=None, notification=None, condition=None, condition_description=None, condition_type=None, dependencies=None, description=None, input=None, output=None, step_name=None, suspend=None, task=None, workflow=None):  # noqa: E501
        """WorkflowSchemaStep - a model defined in Swagger"""  # noqa: E501

        self._cli_command = None
        self._executable = None
        self._netconf_command = None
        self._notification = None
        self._condition = None
        self._condition_description = None
        self._condition_type = None
        self._dependencies = None
        self._description = None
        self._input = None
        self._output = None
        self._step_name = None
        self._suspend = None
        self._task = None
        self._workflow = None
        self.discriminator = None

        if cli_command is not None:
            self.cli_command = cli_command
        if executable is not None:
            self.executable = executable
        if netconf_command is not None:
            self.netconf_command = netconf_command
        if notification is not None:
            self.notification = notification
        if condition is not None:
            self.condition = condition
        if condition_description is not None:
            self.condition_description = condition_description
        if condition_type is not None:
            self.condition_type = condition_type
        if dependencies is not None:
            self.dependencies = dependencies
        if description is not None:
            self.description = description
        if input is not None:
            self.input = input
        if output is not None:
            self.output = output
        self.step_name = step_name
        if suspend is not None:
            self.suspend = suspend
        if task is not None:
            self.task = task
        if workflow is not None:
            self.workflow = workflow

    @property
    def cli_command(self):
        """Gets the cli_command of this WorkflowSchemaStep.  # noqa: E501

        Run CLI command(s)  # noqa: E501

        :return: The cli_command of this WorkflowSchemaStep.  # noqa: E501
        :rtype: list[WorkflowCommandSchema]
        """
        return self._cli_command

    @cli_command.setter
    def cli_command(self, cli_command):
        """Sets the cli_command of this WorkflowSchemaStep.

        Run CLI command(s)  # noqa: E501

        :param cli_command: The cli_command of this WorkflowSchemaStep.  # noqa: E501
        :type: list[WorkflowCommandSchema]
        """

        self._cli_command = cli_command

    @property
    def executable(self):
        """Gets the executable of this WorkflowSchemaStep.  # noqa: E501

        Run an arbitrary executable file such as bash, python, ruby, etc.  # noqa: E501

        :return: The executable of this WorkflowSchemaStep.  # noqa: E501
        :rtype: list[WorkflowCommandSchema]
        """
        return self._executable

    @executable.setter
    def executable(self, executable):
        """Sets the executable of this WorkflowSchemaStep.

        Run an arbitrary executable file such as bash, python, ruby, etc.  # noqa: E501

        :param executable: The executable of this WorkflowSchemaStep.  # noqa: E501
        :type: list[WorkflowCommandSchema]
        """

        self._executable = executable

    @property
    def netconf_command(self):
        """Gets the netconf_command of this WorkflowSchemaStep.  # noqa: E501

        Run netconf command(s)  # noqa: E501

        :return: The netconf_command of this WorkflowSchemaStep.  # noqa: E501
        :rtype: list[WorkflowCommandSchema]
        """
        return self._netconf_command

    @netconf_command.setter
    def netconf_command(self, netconf_command):
        """Sets the netconf_command of this WorkflowSchemaStep.

        Run netconf command(s)  # noqa: E501

        :param netconf_command: The netconf_command of this WorkflowSchemaStep.  # noqa: E501
        :type: list[WorkflowCommandSchema]
        """

        self._netconf_command = netconf_command

    @property
    def notification(self):
        """Gets the notification of this WorkflowSchemaStep.  # noqa: E501

        Send a notification message (configured under notification section)  # noqa: E501

        :return: The notification of this WorkflowSchemaStep.  # noqa: E501
        :rtype: list[WorkflowNotificationSchema]
        """
        return self._notification

    @notification.setter
    def notification(self, notification):
        """Sets the notification of this WorkflowSchemaStep.

        Send a notification message (configured under notification section)  # noqa: E501

        :param notification: The notification of this WorkflowSchemaStep.  # noqa: E501
        :type: list[WorkflowNotificationSchema]
        """

        self._notification = notification

    @property
    def condition(self):
        """Gets the condition of this WorkflowSchemaStep.  # noqa: E501


        :return: The condition of this WorkflowSchemaStep.  # noqa: E501
        :rtype: list[str]
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this WorkflowSchemaStep.


        :param condition: The condition of this WorkflowSchemaStep.  # noqa: E501
        :type: list[str]
        """

        self._condition = condition

    @property
    def condition_description(self):
        """Gets the condition_description of this WorkflowSchemaStep.  # noqa: E501

        Description of the configured conditions  # noqa: E501

        :return: The condition_description of this WorkflowSchemaStep.  # noqa: E501
        :rtype: str
        """
        return self._condition_description

    @condition_description.setter
    def condition_description(self, condition_description):
        """Sets the condition_description of this WorkflowSchemaStep.

        Description of the configured conditions  # noqa: E501

        :param condition_description: The condition_description of this WorkflowSchemaStep.  # noqa: E501
        :type: str
        """

        self._condition_description = condition_description

    @property
    def condition_type(self):
        """Gets the condition_type of this WorkflowSchemaStep.  # noqa: E501

        Call the step if any of the conditions evaluates to true or all of the conditions evaluate to true (default any)  # noqa: E501

        :return: The condition_type of this WorkflowSchemaStep.  # noqa: E501
        :rtype: str
        """
        return self._condition_type

    @condition_type.setter
    def condition_type(self, condition_type):
        """Sets the condition_type of this WorkflowSchemaStep.

        Call the step if any of the conditions evaluates to true or all of the conditions evaluate to true (default any)  # noqa: E501

        :param condition_type: The condition_type of this WorkflowSchemaStep.  # noqa: E501
        :type: str
        """
        allowed_values = ["any", "all"]  # noqa: E501
        if condition_type not in allowed_values:
            raise ValueError(
                "Invalid value for `condition_type` ({0}), must be one of {1}"  # noqa: E501
                .format(condition_type, allowed_values)
            )

        self._condition_type = condition_type

    @property
    def dependencies(self):
        """Gets the dependencies of this WorkflowSchemaStep.  # noqa: E501


        :return: The dependencies of this WorkflowSchemaStep.  # noqa: E501
        :rtype: list[str]
        """
        return self._dependencies

    @dependencies.setter
    def dependencies(self, dependencies):
        """Sets the dependencies of this WorkflowSchemaStep.


        :param dependencies: The dependencies of this WorkflowSchemaStep.  # noqa: E501
        :type: list[str]
        """

        self._dependencies = dependencies

    @property
    def description(self):
        """Gets the description of this WorkflowSchemaStep.  # noqa: E501

        Description about the step being called  # noqa: E501

        :return: The description of this WorkflowSchemaStep.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this WorkflowSchemaStep.

        Description about the step being called  # noqa: E501

        :param description: The description of this WorkflowSchemaStep.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def input(self):
        """Gets the input of this WorkflowSchemaStep.  # noqa: E501

        Workflow input parameters configuration  # noqa: E501

        :return: The input of this WorkflowSchemaStep.  # noqa: E501
        :rtype: list[WorkflowSchemaInput]
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this WorkflowSchemaStep.

        Workflow input parameters configuration  # noqa: E501

        :param input: The input of this WorkflowSchemaStep.  # noqa: E501
        :type: list[WorkflowSchemaInput]
        """

        self._input = input

    @property
    def output(self):
        """Gets the output of this WorkflowSchemaStep.  # noqa: E501

        Workflow output parameters configuration  # noqa: E501

        :return: The output of this WorkflowSchemaStep.  # noqa: E501
        :rtype: list[WorkflowSchemaOutput]
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this WorkflowSchemaStep.

        Workflow output parameters configuration  # noqa: E501

        :param output: The output of this WorkflowSchemaStep.  # noqa: E501
        :type: list[WorkflowSchemaOutput]
        """

        self._output = output

    @property
    def step_name(self):
        """Gets the step_name of this WorkflowSchemaStep.  # noqa: E501

        Name of the step being called. Should be of pattern [a-zA-Z][a-zA-Z0-9_-]*  # noqa: E501

        :return: The step_name of this WorkflowSchemaStep.  # noqa: E501
        :rtype: str
        """
        return self._step_name

    @step_name.setter
    def step_name(self, step_name):
        """Sets the step_name of this WorkflowSchemaStep.

        Name of the step being called. Should be of pattern [a-zA-Z][a-zA-Z0-9_-]*  # noqa: E501

        :param step_name: The step_name of this WorkflowSchemaStep.  # noqa: E501
        :type: str
        """
        if step_name is None:
            raise ValueError("Invalid value for `step_name`, must not be `None`")  # noqa: E501
        if step_name is not None and len(step_name) > 64:
            raise ValueError("Invalid value for `step_name`, length must be less than or equal to `64`")  # noqa: E501
        if step_name is not None and len(step_name) < 1:
            raise ValueError("Invalid value for `step_name`, length must be greater than or equal to `1`")  # noqa: E501
        if step_name is not None and not re.search(r'^[a-zA-Z][a-zA-Z0-9_-]*$', step_name):  # noqa: E501
            raise ValueError(r"Invalid value for `step_name`, must be a follow pattern or equal to `/^[a-zA-Z][a-zA-Z0-9_-]*$/`")  # noqa: E501

        self._step_name = step_name

    @property
    def suspend(self):
        """Gets the suspend of this WorkflowSchemaStep.  # noqa: E501


        :return: The suspend of this WorkflowSchemaStep.  # noqa: E501
        :rtype: WorkflowSchemaSuspend
        """
        return self._suspend

    @suspend.setter
    def suspend(self, suspend):
        """Sets the suspend of this WorkflowSchemaStep.


        :param suspend: The suspend of this WorkflowSchemaStep.  # noqa: E501
        :type: WorkflowSchemaSuspend
        """

        self._suspend = suspend

    @property
    def task(self):
        """Gets the task of this WorkflowSchemaStep.  # noqa: E501


        :return: The task of this WorkflowSchemaStep.  # noqa: E501
        :rtype: WorkflowSchemaTask
        """
        return self._task

    @task.setter
    def task(self, task):
        """Sets the task of this WorkflowSchemaStep.


        :param task: The task of this WorkflowSchemaStep.  # noqa: E501
        :type: WorkflowSchemaTask
        """

        self._task = task

    @property
    def workflow(self):
        """Gets the workflow of this WorkflowSchemaStep.  # noqa: E501


        :return: The workflow of this WorkflowSchemaStep.  # noqa: E501
        :rtype: WorkflowSchemaWorkflow
        """
        return self._workflow

    @workflow.setter
    def workflow(self, workflow):
        """Sets the workflow of this WorkflowSchemaStep.


        :param workflow: The workflow of this WorkflowSchemaStep.  # noqa: E501
        :type: WorkflowSchemaWorkflow
        """

        self._workflow = workflow

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
        if issubclass(WorkflowSchemaStep, dict):
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
        if not isinstance(other, WorkflowSchemaStep):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
