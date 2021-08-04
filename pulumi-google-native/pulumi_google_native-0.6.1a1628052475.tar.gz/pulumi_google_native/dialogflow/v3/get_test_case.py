# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = [
    'GetTestCaseResult',
    'AwaitableGetTestCaseResult',
    'get_test_case',
]

@pulumi.output_type
class GetTestCaseResult:
    def __init__(__self__, creation_time=None, display_name=None, last_test_result=None, name=None, notes=None, tags=None, test_case_conversation_turns=None, test_config=None):
        if creation_time and not isinstance(creation_time, str):
            raise TypeError("Expected argument 'creation_time' to be a str")
        pulumi.set(__self__, "creation_time", creation_time)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if last_test_result and not isinstance(last_test_result, dict):
            raise TypeError("Expected argument 'last_test_result' to be a dict")
        pulumi.set(__self__, "last_test_result", last_test_result)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if notes and not isinstance(notes, str):
            raise TypeError("Expected argument 'notes' to be a str")
        pulumi.set(__self__, "notes", notes)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if test_case_conversation_turns and not isinstance(test_case_conversation_turns, list):
            raise TypeError("Expected argument 'test_case_conversation_turns' to be a list")
        pulumi.set(__self__, "test_case_conversation_turns", test_case_conversation_turns)
        if test_config and not isinstance(test_config, dict):
            raise TypeError("Expected argument 'test_config' to be a dict")
        pulumi.set(__self__, "test_config", test_config)

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> str:
        """
        When the test was created.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The human-readable name of the test case, unique within the agent. Limit of 200 characters.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="lastTestResult")
    def last_test_result(self) -> 'outputs.GoogleCloudDialogflowCxV3TestCaseResultResponse':
        """
        The latest test result.
        """
        return pulumi.get(self, "last_test_result")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The unique identifier of the test case. TestCases.CreateTestCase will populate the name automatically. Otherwise use format: `projects//locations//agents/ /testCases/`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def notes(self) -> str:
        """
        Additional freeform notes about the test case. Limit of 400 characters.
        """
        return pulumi.get(self, "notes")

    @property
    @pulumi.getter
    def tags(self) -> Sequence[str]:
        """
        Tags are short descriptions that users may apply to test cases for organizational and filtering purposes. Each tag should start with "#" and has a limit of 30 characters.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="testCaseConversationTurns")
    def test_case_conversation_turns(self) -> Sequence['outputs.GoogleCloudDialogflowCxV3ConversationTurnResponse']:
        """
        The conversation turns uttered when the test case was created, in chronological order. These include the canonical set of agent utterances that should occur when the agent is working properly.
        """
        return pulumi.get(self, "test_case_conversation_turns")

    @property
    @pulumi.getter(name="testConfig")
    def test_config(self) -> 'outputs.GoogleCloudDialogflowCxV3TestConfigResponse':
        """
        Config for the test case.
        """
        return pulumi.get(self, "test_config")


class AwaitableGetTestCaseResult(GetTestCaseResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTestCaseResult(
            creation_time=self.creation_time,
            display_name=self.display_name,
            last_test_result=self.last_test_result,
            name=self.name,
            notes=self.notes,
            tags=self.tags,
            test_case_conversation_turns=self.test_case_conversation_turns,
            test_config=self.test_config)


def get_test_case(agent_id: Optional[str] = None,
                  location: Optional[str] = None,
                  project: Optional[str] = None,
                  test_case_id: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTestCaseResult:
    """
    Gets a test case.
    """
    __args__ = dict()
    __args__['agentId'] = agent_id
    __args__['location'] = location
    __args__['project'] = project
    __args__['testCaseId'] = test_case_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:dialogflow/v3:getTestCase', __args__, opts=opts, typ=GetTestCaseResult).value

    return AwaitableGetTestCaseResult(
        creation_time=__ret__.creation_time,
        display_name=__ret__.display_name,
        last_test_result=__ret__.last_test_result,
        name=__ret__.name,
        notes=__ret__.notes,
        tags=__ret__.tags,
        test_case_conversation_turns=__ret__.test_case_conversation_turns,
        test_config=__ret__.test_config)
