# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetParticipantResult',
    'AwaitableGetParticipantResult',
    'get_participant',
]

@pulumi.output_type
class GetParticipantResult:
    def __init__(__self__, name=None, obfuscated_external_user_id=None, role=None):
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if obfuscated_external_user_id and not isinstance(obfuscated_external_user_id, str):
            raise TypeError("Expected argument 'obfuscated_external_user_id' to be a str")
        pulumi.set(__self__, "obfuscated_external_user_id", obfuscated_external_user_id)
        if role and not isinstance(role, str):
            raise TypeError("Expected argument 'role' to be a str")
        pulumi.set(__self__, "role", role)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Optional. The unique identifier of this participant. Format: `projects//locations//conversations//participants/`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="obfuscatedExternalUserId")
    def obfuscated_external_user_id(self) -> str:
        """
        Optional. Obfuscated user id that should be associated with the created participant. You can specify a user id as follows: 1. If you set this field in CreateParticipantRequest or UpdateParticipantRequest, Dialogflow adds the obfuscated user id with the participant. 2. If you set this field in AnalyzeContent or StreamingAnalyzeContent, Dialogflow will update Participant.obfuscated_external_user_id. Dialogflow uses this user id for following purposes: 1) Billing and measurement. If user with the same obfuscated_external_user_id is created in a later conversation, dialogflow will know it's the same user. 2) Agent assist suggestion personalization. For example, Dialogflow can use it to provide personalized smart reply suggestions for this user. Note: * Please never pass raw user ids to Dialogflow. Always obfuscate your user id first. * Dialogflow only accepts a UTF-8 encoded string, e.g., a hex digest of a hash function like SHA-512. * The length of the user id must be <= 256 characters.
        """
        return pulumi.get(self, "obfuscated_external_user_id")

    @property
    @pulumi.getter
    def role(self) -> str:
        """
        Immutable. The role this participant plays in the conversation. This field must be set during participant creation and is then immutable.
        """
        return pulumi.get(self, "role")


class AwaitableGetParticipantResult(GetParticipantResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetParticipantResult(
            name=self.name,
            obfuscated_external_user_id=self.obfuscated_external_user_id,
            role=self.role)


def get_participant(conversation_id: Optional[str] = None,
                    location: Optional[str] = None,
                    participant_id: Optional[str] = None,
                    project: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetParticipantResult:
    """
    Retrieves a conversation participant.
    """
    __args__ = dict()
    __args__['conversationId'] = conversation_id
    __args__['location'] = location
    __args__['participantId'] = participant_id
    __args__['project'] = project
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:dialogflow/v2beta1:getParticipant', __args__, opts=opts, typ=GetParticipantResult).value

    return AwaitableGetParticipantResult(
        name=__ret__.name,
        obfuscated_external_user_id=__ret__.obfuscated_external_user_id,
        role=__ret__.role)
