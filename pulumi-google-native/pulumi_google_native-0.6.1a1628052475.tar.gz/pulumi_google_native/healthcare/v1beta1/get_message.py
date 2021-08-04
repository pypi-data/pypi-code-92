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
    'GetMessageResult',
    'AwaitableGetMessageResult',
    'get_message',
]

@pulumi.output_type
class GetMessageResult:
    def __init__(__self__, create_time=None, data=None, labels=None, message_type=None, name=None, parsed_data=None, patient_ids=None, schematized_data=None, send_facility=None, send_time=None):
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if data and not isinstance(data, str):
            raise TypeError("Expected argument 'data' to be a str")
        pulumi.set(__self__, "data", data)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if message_type and not isinstance(message_type, str):
            raise TypeError("Expected argument 'message_type' to be a str")
        pulumi.set(__self__, "message_type", message_type)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if parsed_data and not isinstance(parsed_data, dict):
            raise TypeError("Expected argument 'parsed_data' to be a dict")
        pulumi.set(__self__, "parsed_data", parsed_data)
        if patient_ids and not isinstance(patient_ids, list):
            raise TypeError("Expected argument 'patient_ids' to be a list")
        pulumi.set(__self__, "patient_ids", patient_ids)
        if schematized_data and not isinstance(schematized_data, dict):
            raise TypeError("Expected argument 'schematized_data' to be a dict")
        pulumi.set(__self__, "schematized_data", schematized_data)
        if send_facility and not isinstance(send_facility, str):
            raise TypeError("Expected argument 'send_facility' to be a str")
        pulumi.set(__self__, "send_facility", send_facility)
        if send_time and not isinstance(send_time, str):
            raise TypeError("Expected argument 'send_time' to be a str")
        pulumi.set(__self__, "send_time", send_time)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        The datetime when the message was created. Set by the server.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def data(self) -> str:
        """
        Raw message bytes.
        """
        return pulumi.get(self, "data")

    @property
    @pulumi.getter
    def labels(self) -> Mapping[str, str]:
        """
        User-supplied key-value pairs used to organize HL7v2 stores. Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: \p{Ll}\p{Lo}{0,62} Label values are optional, must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: [\p{Ll}\p{Lo}\p{N}_-]{0,63} No more than 64 labels can be associated with a given store.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter(name="messageType")
    def message_type(self) -> str:
        """
        The message type for this message. MSH-9.1.
        """
        return pulumi.get(self, "message_type")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name of the Message, of the form `projects/{project_id}/datasets/{dataset_id}/hl7V2Stores/{hl7_v2_store_id}/messages/{message_id}`. Assigned by the server.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="parsedData")
    def parsed_data(self) -> 'outputs.ParsedDataResponse':
        """
        The parsed version of the raw message data.
        """
        return pulumi.get(self, "parsed_data")

    @property
    @pulumi.getter(name="patientIds")
    def patient_ids(self) -> Sequence['outputs.PatientIdResponse']:
        """
        All patient IDs listed in the PID-2, PID-3, and PID-4 segments of this message.
        """
        return pulumi.get(self, "patient_ids")

    @property
    @pulumi.getter(name="schematizedData")
    def schematized_data(self) -> 'outputs.SchematizedDataResponse':
        """
        The parsed version of the raw message data schematized according to this store's schemas and type definitions.
        """
        return pulumi.get(self, "schematized_data")

    @property
    @pulumi.getter(name="sendFacility")
    def send_facility(self) -> str:
        """
        The hospital that this message came from. MSH-4.
        """
        return pulumi.get(self, "send_facility")

    @property
    @pulumi.getter(name="sendTime")
    def send_time(self) -> str:
        """
        The datetime the sending application sent this message. MSH-7.
        """
        return pulumi.get(self, "send_time")


class AwaitableGetMessageResult(GetMessageResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMessageResult(
            create_time=self.create_time,
            data=self.data,
            labels=self.labels,
            message_type=self.message_type,
            name=self.name,
            parsed_data=self.parsed_data,
            patient_ids=self.patient_ids,
            schematized_data=self.schematized_data,
            send_facility=self.send_facility,
            send_time=self.send_time)


def get_message(dataset_id: Optional[str] = None,
                hl7_v2_store_id: Optional[str] = None,
                location: Optional[str] = None,
                message_id: Optional[str] = None,
                project: Optional[str] = None,
                view: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMessageResult:
    """
    Gets an HL7v2 message.
    """
    __args__ = dict()
    __args__['datasetId'] = dataset_id
    __args__['hl7V2StoreId'] = hl7_v2_store_id
    __args__['location'] = location
    __args__['messageId'] = message_id
    __args__['project'] = project
    __args__['view'] = view
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:healthcare/v1beta1:getMessage', __args__, opts=opts, typ=GetMessageResult).value

    return AwaitableGetMessageResult(
        create_time=__ret__.create_time,
        data=__ret__.data,
        labels=__ret__.labels,
        message_type=__ret__.message_type,
        name=__ret__.name,
        parsed_data=__ret__.parsed_data,
        patient_ids=__ret__.patient_ids,
        schematized_data=__ret__.schematized_data,
        send_facility=__ret__.send_facility,
        send_time=__ret__.send_time)
