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
    'GetSessionEntityTypeResult',
    'AwaitableGetSessionEntityTypeResult',
    'get_session_entity_type',
]

@pulumi.output_type
class GetSessionEntityTypeResult:
    def __init__(__self__, entities=None, entity_override_mode=None, name=None):
        if entities and not isinstance(entities, list):
            raise TypeError("Expected argument 'entities' to be a list")
        pulumi.set(__self__, "entities", entities)
        if entity_override_mode and not isinstance(entity_override_mode, str):
            raise TypeError("Expected argument 'entity_override_mode' to be a str")
        pulumi.set(__self__, "entity_override_mode", entity_override_mode)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def entities(self) -> Sequence['outputs.GoogleCloudDialogflowV2EntityTypeEntityResponse']:
        """
        The collection of entities associated with this session entity type.
        """
        return pulumi.get(self, "entities")

    @property
    @pulumi.getter(name="entityOverrideMode")
    def entity_override_mode(self) -> str:
        """
        Indicates whether the additional data should override or supplement the custom entity type definition.
        """
        return pulumi.get(self, "entity_override_mode")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The unique identifier of this session entity type. Format: `projects//agent/sessions//entityTypes/`, or `projects//agent/environments//users//sessions//entityTypes/`. If `Environment ID` is not specified, we assume default 'draft' environment. If `User ID` is not specified, we assume default '-' user. `` must be the display name of an existing entity type in the same agent that will be overridden or supplemented.
        """
        return pulumi.get(self, "name")


class AwaitableGetSessionEntityTypeResult(GetSessionEntityTypeResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSessionEntityTypeResult(
            entities=self.entities,
            entity_override_mode=self.entity_override_mode,
            name=self.name)


def get_session_entity_type(entity_type_id: Optional[str] = None,
                            environment_id: Optional[str] = None,
                            location: Optional[str] = None,
                            project: Optional[str] = None,
                            session_id: Optional[str] = None,
                            user_id: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSessionEntityTypeResult:
    """
    Retrieves the specified session entity type. This method doesn't work with Google Assistant integration. Contact Dialogflow support if you need to use session entities with Google Assistant integration.
    """
    __args__ = dict()
    __args__['entityTypeId'] = entity_type_id
    __args__['environmentId'] = environment_id
    __args__['location'] = location
    __args__['project'] = project
    __args__['sessionId'] = session_id
    __args__['userId'] = user_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:dialogflow/v2:getSessionEntityType', __args__, opts=opts, typ=GetSessionEntityTypeResult).value

    return AwaitableGetSessionEntityTypeResult(
        entities=__ret__.entities,
        entity_override_mode=__ret__.entity_override_mode,
        name=__ret__.name)
