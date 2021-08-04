# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['JobArgs', 'Job']

@pulumi.input_type
class JobArgs:
    def __init__(__self__, *,
                 job_id: pulumi.Input[str],
                 etag: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 prediction_input: Optional[pulumi.Input['GoogleCloudMlV1__PredictionInputArgs']] = None,
                 prediction_output: Optional[pulumi.Input['GoogleCloudMlV1__PredictionOutputArgs']] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 training_input: Optional[pulumi.Input['GoogleCloudMlV1__TrainingInputArgs']] = None,
                 training_output: Optional[pulumi.Input['GoogleCloudMlV1__TrainingOutputArgs']] = None):
        """
        The set of arguments for constructing a Job resource.
        :param pulumi.Input[str] job_id: The user-specified id of the job.
        :param pulumi.Input[str] etag: `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a job from overwriting each other. It is strongly suggested that systems make use of the `etag` in the read-modify-write cycle to perform job updates in order to avoid race conditions: An `etag` is returned in the response to `GetJob`, and systems are expected to put that etag in the request to `UpdateJob` to ensure that their change will be applied to the same version of the job.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Optional. One or more labels that you can add, to organize your jobs. Each label is a key-value pair, where both the key and the value are arbitrary strings that you supply. For more information, see the documentation on using labels.
        :param pulumi.Input['GoogleCloudMlV1__PredictionInputArgs'] prediction_input: Input parameters to create a prediction job.
        :param pulumi.Input['GoogleCloudMlV1__PredictionOutputArgs'] prediction_output: The current prediction job result.
        :param pulumi.Input['GoogleCloudMlV1__TrainingInputArgs'] training_input: Input parameters to create a training job.
        :param pulumi.Input['GoogleCloudMlV1__TrainingOutputArgs'] training_output: The current training job result.
        """
        pulumi.set(__self__, "job_id", job_id)
        if etag is not None:
            pulumi.set(__self__, "etag", etag)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if prediction_input is not None:
            pulumi.set(__self__, "prediction_input", prediction_input)
        if prediction_output is not None:
            pulumi.set(__self__, "prediction_output", prediction_output)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if training_input is not None:
            pulumi.set(__self__, "training_input", training_input)
        if training_output is not None:
            pulumi.set(__self__, "training_output", training_output)

    @property
    @pulumi.getter(name="jobId")
    def job_id(self) -> pulumi.Input[str]:
        """
        The user-specified id of the job.
        """
        return pulumi.get(self, "job_id")

    @job_id.setter
    def job_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "job_id", value)

    @property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[str]]:
        """
        `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a job from overwriting each other. It is strongly suggested that systems make use of the `etag` in the read-modify-write cycle to perform job updates in order to avoid race conditions: An `etag` is returned in the response to `GetJob`, and systems are expected to put that etag in the request to `UpdateJob` to ensure that their change will be applied to the same version of the job.
        """
        return pulumi.get(self, "etag")

    @etag.setter
    def etag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "etag", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Optional. One or more labels that you can add, to organize your jobs. Each label is a key-value pair, where both the key and the value are arbitrary strings that you supply. For more information, see the documentation on using labels.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter(name="predictionInput")
    def prediction_input(self) -> Optional[pulumi.Input['GoogleCloudMlV1__PredictionInputArgs']]:
        """
        Input parameters to create a prediction job.
        """
        return pulumi.get(self, "prediction_input")

    @prediction_input.setter
    def prediction_input(self, value: Optional[pulumi.Input['GoogleCloudMlV1__PredictionInputArgs']]):
        pulumi.set(self, "prediction_input", value)

    @property
    @pulumi.getter(name="predictionOutput")
    def prediction_output(self) -> Optional[pulumi.Input['GoogleCloudMlV1__PredictionOutputArgs']]:
        """
        The current prediction job result.
        """
        return pulumi.get(self, "prediction_output")

    @prediction_output.setter
    def prediction_output(self, value: Optional[pulumi.Input['GoogleCloudMlV1__PredictionOutputArgs']]):
        pulumi.set(self, "prediction_output", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter(name="trainingInput")
    def training_input(self) -> Optional[pulumi.Input['GoogleCloudMlV1__TrainingInputArgs']]:
        """
        Input parameters to create a training job.
        """
        return pulumi.get(self, "training_input")

    @training_input.setter
    def training_input(self, value: Optional[pulumi.Input['GoogleCloudMlV1__TrainingInputArgs']]):
        pulumi.set(self, "training_input", value)

    @property
    @pulumi.getter(name="trainingOutput")
    def training_output(self) -> Optional[pulumi.Input['GoogleCloudMlV1__TrainingOutputArgs']]:
        """
        The current training job result.
        """
        return pulumi.get(self, "training_output")

    @training_output.setter
    def training_output(self, value: Optional[pulumi.Input['GoogleCloudMlV1__TrainingOutputArgs']]):
        pulumi.set(self, "training_output", value)


class Job(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 job_id: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 prediction_input: Optional[pulumi.Input[pulumi.InputType['GoogleCloudMlV1__PredictionInputArgs']]] = None,
                 prediction_output: Optional[pulumi.Input[pulumi.InputType['GoogleCloudMlV1__PredictionOutputArgs']]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 training_input: Optional[pulumi.Input[pulumi.InputType['GoogleCloudMlV1__TrainingInputArgs']]] = None,
                 training_output: Optional[pulumi.Input[pulumi.InputType['GoogleCloudMlV1__TrainingOutputArgs']]] = None,
                 __props__=None):
        """
        Creates a training or a batch prediction job.
        Auto-naming is currently not supported for this resource.
        Note - this resource's API doesn't support deletion. When deleted, the resource will persist
        on Google Cloud even though it will be deleted from Pulumi state.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] etag: `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a job from overwriting each other. It is strongly suggested that systems make use of the `etag` in the read-modify-write cycle to perform job updates in order to avoid race conditions: An `etag` is returned in the response to `GetJob`, and systems are expected to put that etag in the request to `UpdateJob` to ensure that their change will be applied to the same version of the job.
        :param pulumi.Input[str] job_id: The user-specified id of the job.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Optional. One or more labels that you can add, to organize your jobs. Each label is a key-value pair, where both the key and the value are arbitrary strings that you supply. For more information, see the documentation on using labels.
        :param pulumi.Input[pulumi.InputType['GoogleCloudMlV1__PredictionInputArgs']] prediction_input: Input parameters to create a prediction job.
        :param pulumi.Input[pulumi.InputType['GoogleCloudMlV1__PredictionOutputArgs']] prediction_output: The current prediction job result.
        :param pulumi.Input[pulumi.InputType['GoogleCloudMlV1__TrainingInputArgs']] training_input: Input parameters to create a training job.
        :param pulumi.Input[pulumi.InputType['GoogleCloudMlV1__TrainingOutputArgs']] training_output: The current training job result.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: JobArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a training or a batch prediction job.
        Auto-naming is currently not supported for this resource.
        Note - this resource's API doesn't support deletion. When deleted, the resource will persist
        on Google Cloud even though it will be deleted from Pulumi state.

        :param str resource_name: The name of the resource.
        :param JobArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(JobArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 job_id: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 prediction_input: Optional[pulumi.Input[pulumi.InputType['GoogleCloudMlV1__PredictionInputArgs']]] = None,
                 prediction_output: Optional[pulumi.Input[pulumi.InputType['GoogleCloudMlV1__PredictionOutputArgs']]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 training_input: Optional[pulumi.Input[pulumi.InputType['GoogleCloudMlV1__TrainingInputArgs']]] = None,
                 training_output: Optional[pulumi.Input[pulumi.InputType['GoogleCloudMlV1__TrainingOutputArgs']]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = JobArgs.__new__(JobArgs)

            __props__.__dict__["etag"] = etag
            if job_id is None and not opts.urn:
                raise TypeError("Missing required property 'job_id'")
            __props__.__dict__["job_id"] = job_id
            __props__.__dict__["labels"] = labels
            __props__.__dict__["prediction_input"] = prediction_input
            __props__.__dict__["prediction_output"] = prediction_output
            __props__.__dict__["project"] = project
            __props__.__dict__["training_input"] = training_input
            __props__.__dict__["training_output"] = training_output
            __props__.__dict__["create_time"] = None
            __props__.__dict__["end_time"] = None
            __props__.__dict__["error_message"] = None
            __props__.__dict__["start_time"] = None
            __props__.__dict__["state"] = None
        super(Job, __self__).__init__(
            'google-native:ml/v1:Job',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Job':
        """
        Get an existing Job resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = JobArgs.__new__(JobArgs)

        __props__.__dict__["create_time"] = None
        __props__.__dict__["end_time"] = None
        __props__.__dict__["error_message"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["job_id"] = None
        __props__.__dict__["labels"] = None
        __props__.__dict__["prediction_input"] = None
        __props__.__dict__["prediction_output"] = None
        __props__.__dict__["start_time"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["training_input"] = None
        __props__.__dict__["training_output"] = None
        return Job(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        When the job was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="endTime")
    def end_time(self) -> pulumi.Output[str]:
        """
        When the job processing was completed.
        """
        return pulumi.get(self, "end_time")

    @property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> pulumi.Output[str]:
        """
        The details of a failure or a cancellation.
        """
        return pulumi.get(self, "error_message")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a job from overwriting each other. It is strongly suggested that systems make use of the `etag` in the read-modify-write cycle to perform job updates in order to avoid race conditions: An `etag` is returned in the response to `GetJob`, and systems are expected to put that etag in the request to `UpdateJob` to ensure that their change will be applied to the same version of the job.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="jobId")
    def job_id(self) -> pulumi.Output[str]:
        """
        The user-specified id of the job.
        """
        return pulumi.get(self, "job_id")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Optional. One or more labels that you can add, to organize your jobs. Each label is a key-value pair, where both the key and the value are arbitrary strings that you supply. For more information, see the documentation on using labels.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter(name="predictionInput")
    def prediction_input(self) -> pulumi.Output['outputs.GoogleCloudMlV1__PredictionInputResponse']:
        """
        Input parameters to create a prediction job.
        """
        return pulumi.get(self, "prediction_input")

    @property
    @pulumi.getter(name="predictionOutput")
    def prediction_output(self) -> pulumi.Output['outputs.GoogleCloudMlV1__PredictionOutputResponse']:
        """
        The current prediction job result.
        """
        return pulumi.get(self, "prediction_output")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> pulumi.Output[str]:
        """
        When the job processing was started.
        """
        return pulumi.get(self, "start_time")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The detailed state of a job.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="trainingInput")
    def training_input(self) -> pulumi.Output['outputs.GoogleCloudMlV1__TrainingInputResponse']:
        """
        Input parameters to create a training job.
        """
        return pulumi.get(self, "training_input")

    @property
    @pulumi.getter(name="trainingOutput")
    def training_output(self) -> pulumi.Output['outputs.GoogleCloudMlV1__TrainingOutputResponse']:
        """
        The current training job result.
        """
        return pulumi.get(self, "training_output")

