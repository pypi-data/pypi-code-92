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
    'GetStudyResult',
    'AwaitableGetStudyResult',
    'get_study',
]

@pulumi.output_type
class GetStudyResult:
    def __init__(__self__, create_time=None, inactive_reason=None, name=None, state=None, study_config=None):
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if inactive_reason and not isinstance(inactive_reason, str):
            raise TypeError("Expected argument 'inactive_reason' to be a str")
        pulumi.set(__self__, "inactive_reason", inactive_reason)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if study_config and not isinstance(study_config, dict):
            raise TypeError("Expected argument 'study_config' to be a dict")
        pulumi.set(__self__, "study_config", study_config)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        Time at which the study was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="inactiveReason")
    def inactive_reason(self) -> str:
        """
        A human readable reason why the Study is inactive. This should be empty if a study is ACTIVE or COMPLETED.
        """
        return pulumi.get(self, "inactive_reason")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of a study.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The detailed state of a study.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="studyConfig")
    def study_config(self) -> 'outputs.GoogleCloudMlV1__StudyConfigResponse':
        """
        Configuration of the study.
        """
        return pulumi.get(self, "study_config")


class AwaitableGetStudyResult(GetStudyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetStudyResult(
            create_time=self.create_time,
            inactive_reason=self.inactive_reason,
            name=self.name,
            state=self.state,
            study_config=self.study_config)


def get_study(location: Optional[str] = None,
              project: Optional[str] = None,
              study_id: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetStudyResult:
    """
    Gets a study.
    """
    __args__ = dict()
    __args__['location'] = location
    __args__['project'] = project
    __args__['studyId'] = study_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:ml/v1:getStudy', __args__, opts=opts, typ=GetStudyResult).value

    return AwaitableGetStudyResult(
        create_time=__ret__.create_time,
        inactive_reason=__ret__.inactive_reason,
        name=__ret__.name,
        state=__ret__.state,
        study_config=__ret__.study_config)
