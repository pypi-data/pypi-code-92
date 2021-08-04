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
    'GetModelResult',
    'AwaitableGetModelResult',
    'get_model',
]

@pulumi.output_type
class GetModelResult:
    def __init__(__self__, active_operations=None, create_time=None, display_name=None, etag=None, model_hash=None, name=None, state=None, tags=None, tflite_model=None, update_time=None):
        if active_operations and not isinstance(active_operations, list):
            raise TypeError("Expected argument 'active_operations' to be a list")
        pulumi.set(__self__, "active_operations", active_operations)
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if model_hash and not isinstance(model_hash, str):
            raise TypeError("Expected argument 'model_hash' to be a str")
        pulumi.set(__self__, "model_hash", model_hash)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if state and not isinstance(state, dict):
            raise TypeError("Expected argument 'state' to be a dict")
        pulumi.set(__self__, "state", state)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if tflite_model and not isinstance(tflite_model, dict):
            raise TypeError("Expected argument 'tflite_model' to be a dict")
        pulumi.set(__self__, "tflite_model", tflite_model)
        if update_time and not isinstance(update_time, str):
            raise TypeError("Expected argument 'update_time' to be a str")
        pulumi.set(__self__, "update_time", update_time)

    @property
    @pulumi.getter(name="activeOperations")
    def active_operations(self) -> Sequence['outputs.OperationResponse']:
        """
        Lists operation ids associated with this model whose status is NOT done.
        """
        return pulumi.get(self, "active_operations")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        Timestamp when this model was created in Firebase ML.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The name of the model to create. The name can be up to 32 characters long and can consist only of ASCII Latin letters A-Z and a-z, underscores(_) and ASCII digits 0-9. It must start with a letter.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        See RFC7232 https://tools.ietf.org/html/rfc7232#section-2.3
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="modelHash")
    def model_hash(self) -> str:
        """
        The model_hash will change if a new file is available for download.
        """
        return pulumi.get(self, "model_hash")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The resource name of the Model. Model names have the form `projects/{project_id}/models/{model_id}` The name is ignored when creating a model.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def state(self) -> 'outputs.ModelStateResponse':
        """
        State common to all model types. Includes publishing and validation information.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def tags(self) -> Sequence[str]:
        """
        User defined tags which can be used to group/filter models during listing
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tfliteModel")
    def tflite_model(self) -> 'outputs.TfLiteModelResponse':
        """
        A TFLite Model
        """
        return pulumi.get(self, "tflite_model")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> str:
        """
        Timestamp when this model was updated in Firebase ML.
        """
        return pulumi.get(self, "update_time")


class AwaitableGetModelResult(GetModelResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetModelResult(
            active_operations=self.active_operations,
            create_time=self.create_time,
            display_name=self.display_name,
            etag=self.etag,
            model_hash=self.model_hash,
            name=self.name,
            state=self.state,
            tags=self.tags,
            tflite_model=self.tflite_model,
            update_time=self.update_time)


def get_model(model_id: Optional[str] = None,
              project: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetModelResult:
    """
    Gets a model resource.
    """
    __args__ = dict()
    __args__['modelId'] = model_id
    __args__['project'] = project
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:firebaseml/v1beta2:getModel', __args__, opts=opts, typ=GetModelResult).value

    return AwaitableGetModelResult(
        active_operations=__ret__.active_operations,
        create_time=__ret__.create_time,
        display_name=__ret__.display_name,
        etag=__ret__.etag,
        model_hash=__ret__.model_hash,
        name=__ret__.name,
        state=__ret__.state,
        tags=__ret__.tags,
        tflite_model=__ret__.tflite_model,
        update_time=__ret__.update_time)
