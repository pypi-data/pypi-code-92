# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flyteidl/admin/task_execution.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from flyteidl.admin import common_pb2 as flyteidl_dot_admin_dot_common__pb2
from flyteidl.core import execution_pb2 as flyteidl_dot_core_dot_execution__pb2
from flyteidl.core import identifier_pb2 as flyteidl_dot_core_dot_identifier__pb2
from flyteidl.core import literals_pb2 as flyteidl_dot_core_dot_literals__pb2
from flyteidl.event import event_pb2 as flyteidl_dot_event_dot_event__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='flyteidl/admin/task_execution.proto',
  package='flyteidl.admin',
  syntax='proto3',
  serialized_options=_b('Z5github.com/flyteorg/flyteidl/gen/pb-go/flyteidl/admin'),
  serialized_pb=_b('\n#flyteidl/admin/task_execution.proto\x12\x0e\x66lyteidl.admin\x1a\x1b\x66lyteidl/admin/common.proto\x1a\x1d\x66lyteidl/core/execution.proto\x1a\x1e\x66lyteidl/core/identifier.proto\x1a\x1c\x66lyteidl/core/literals.proto\x1a\x1a\x66lyteidl/event/event.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1cgoogle/protobuf/struct.proto\"M\n\x17TaskExecutionGetRequest\x12\x32\n\x02id\x18\x01 \x01(\x0b\x32&.flyteidl.core.TaskExecutionIdentifier\"\xb3\x01\n\x18TaskExecutionListRequest\x12\x41\n\x11node_execution_id\x18\x01 \x01(\x0b\x32&.flyteidl.core.NodeExecutionIdentifier\x12\r\n\x05limit\x18\x02 \x01(\r\x12\r\n\x05token\x18\x03 \x01(\t\x12\x0f\n\x07\x66ilters\x18\x04 \x01(\t\x12%\n\x07sort_by\x18\x05 \x01(\x0b\x32\x14.flyteidl.admin.Sort\"\xa0\x01\n\rTaskExecution\x12\x32\n\x02id\x18\x01 \x01(\x0b\x32&.flyteidl.core.TaskExecutionIdentifier\x12\x11\n\tinput_uri\x18\x02 \x01(\t\x12\x35\n\x07\x63losure\x18\x03 \x01(\x0b\x32$.flyteidl.admin.TaskExecutionClosure\x12\x11\n\tis_parent\x18\x04 \x01(\x08\"Z\n\x11TaskExecutionList\x12\x36\n\x0ftask_executions\x18\x01 \x03(\x0b\x32\x1d.flyteidl.admin.TaskExecution\x12\r\n\x05token\x18\x02 \x01(\t\"\x8d\x04\n\x14TaskExecutionClosure\x12\x14\n\noutput_uri\x18\x01 \x01(\tH\x00\x12.\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x1d.flyteidl.core.ExecutionErrorH\x00\x12\x31\n\x05phase\x18\x03 \x01(\x0e\x32\".flyteidl.core.TaskExecution.Phase\x12$\n\x04logs\x18\x04 \x03(\x0b\x32\x16.flyteidl.core.TaskLog\x12.\n\nstarted_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\x08\x64uration\x18\x06 \x01(\x0b\x32\x19.google.protobuf.Duration\x12.\n\ncreated_at\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x0b\x63ustom_info\x18\t \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x0e\n\x06reason\x18\n \x01(\t\x12\x11\n\ttask_type\x18\x0b \x01(\t\x12\x37\n\x08metadata\x18\x10 \x01(\x0b\x32%.flyteidl.event.TaskExecutionMetadataB\x0f\n\routput_result\"Q\n\x1bTaskExecutionGetDataRequest\x12\x32\n\x02id\x18\x01 \x01(\x0b\x32&.flyteidl.core.TaskExecutionIdentifier\"\xda\x01\n\x1cTaskExecutionGetDataResponse\x12+\n\x06inputs\x18\x01 \x01(\x0b\x32\x17.flyteidl.admin.UrlBlobB\x02\x18\x01\x12,\n\x07outputs\x18\x02 \x01(\x0b\x32\x17.flyteidl.admin.UrlBlobB\x02\x18\x01\x12.\n\x0b\x66ull_inputs\x18\x03 \x01(\x0b\x32\x19.flyteidl.core.LiteralMap\x12/\n\x0c\x66ull_outputs\x18\x04 \x01(\x0b\x32\x19.flyteidl.core.LiteralMapB7Z5github.com/flyteorg/flyteidl/gen/pb-go/flyteidl/adminb\x06proto3')
  ,
  dependencies=[flyteidl_dot_admin_dot_common__pb2.DESCRIPTOR,flyteidl_dot_core_dot_execution__pb2.DESCRIPTOR,flyteidl_dot_core_dot_identifier__pb2.DESCRIPTOR,flyteidl_dot_core_dot_literals__pb2.DESCRIPTOR,flyteidl_dot_event_dot_event__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_TASKEXECUTIONGETREQUEST = _descriptor.Descriptor(
  name='TaskExecutionGetRequest',
  full_name='flyteidl.admin.TaskExecutionGetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='flyteidl.admin.TaskExecutionGetRequest.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=300,
  serialized_end=377,
)


_TASKEXECUTIONLISTREQUEST = _descriptor.Descriptor(
  name='TaskExecutionListRequest',
  full_name='flyteidl.admin.TaskExecutionListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node_execution_id', full_name='flyteidl.admin.TaskExecutionListRequest.node_execution_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limit', full_name='flyteidl.admin.TaskExecutionListRequest.limit', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='token', full_name='flyteidl.admin.TaskExecutionListRequest.token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filters', full_name='flyteidl.admin.TaskExecutionListRequest.filters', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sort_by', full_name='flyteidl.admin.TaskExecutionListRequest.sort_by', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=380,
  serialized_end=559,
)


_TASKEXECUTION = _descriptor.Descriptor(
  name='TaskExecution',
  full_name='flyteidl.admin.TaskExecution',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='flyteidl.admin.TaskExecution.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='input_uri', full_name='flyteidl.admin.TaskExecution.input_uri', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='closure', full_name='flyteidl.admin.TaskExecution.closure', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_parent', full_name='flyteidl.admin.TaskExecution.is_parent', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=562,
  serialized_end=722,
)


_TASKEXECUTIONLIST = _descriptor.Descriptor(
  name='TaskExecutionList',
  full_name='flyteidl.admin.TaskExecutionList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_executions', full_name='flyteidl.admin.TaskExecutionList.task_executions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='token', full_name='flyteidl.admin.TaskExecutionList.token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=724,
  serialized_end=814,
)


_TASKEXECUTIONCLOSURE = _descriptor.Descriptor(
  name='TaskExecutionClosure',
  full_name='flyteidl.admin.TaskExecutionClosure',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='output_uri', full_name='flyteidl.admin.TaskExecutionClosure.output_uri', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='flyteidl.admin.TaskExecutionClosure.error', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='phase', full_name='flyteidl.admin.TaskExecutionClosure.phase', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='logs', full_name='flyteidl.admin.TaskExecutionClosure.logs', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='started_at', full_name='flyteidl.admin.TaskExecutionClosure.started_at', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='duration', full_name='flyteidl.admin.TaskExecutionClosure.duration', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='flyteidl.admin.TaskExecutionClosure.created_at', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updated_at', full_name='flyteidl.admin.TaskExecutionClosure.updated_at', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='custom_info', full_name='flyteidl.admin.TaskExecutionClosure.custom_info', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reason', full_name='flyteidl.admin.TaskExecutionClosure.reason', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='task_type', full_name='flyteidl.admin.TaskExecutionClosure.task_type', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='flyteidl.admin.TaskExecutionClosure.metadata', index=11,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='output_result', full_name='flyteidl.admin.TaskExecutionClosure.output_result',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=817,
  serialized_end=1342,
)


_TASKEXECUTIONGETDATAREQUEST = _descriptor.Descriptor(
  name='TaskExecutionGetDataRequest',
  full_name='flyteidl.admin.TaskExecutionGetDataRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='flyteidl.admin.TaskExecutionGetDataRequest.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1344,
  serialized_end=1425,
)


_TASKEXECUTIONGETDATARESPONSE = _descriptor.Descriptor(
  name='TaskExecutionGetDataResponse',
  full_name='flyteidl.admin.TaskExecutionGetDataResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='inputs', full_name='flyteidl.admin.TaskExecutionGetDataResponse.inputs', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='outputs', full_name='flyteidl.admin.TaskExecutionGetDataResponse.outputs', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='full_inputs', full_name='flyteidl.admin.TaskExecutionGetDataResponse.full_inputs', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='full_outputs', full_name='flyteidl.admin.TaskExecutionGetDataResponse.full_outputs', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1428,
  serialized_end=1646,
)

_TASKEXECUTIONGETREQUEST.fields_by_name['id'].message_type = flyteidl_dot_core_dot_identifier__pb2._TASKEXECUTIONIDENTIFIER
_TASKEXECUTIONLISTREQUEST.fields_by_name['node_execution_id'].message_type = flyteidl_dot_core_dot_identifier__pb2._NODEEXECUTIONIDENTIFIER
_TASKEXECUTIONLISTREQUEST.fields_by_name['sort_by'].message_type = flyteidl_dot_admin_dot_common__pb2._SORT
_TASKEXECUTION.fields_by_name['id'].message_type = flyteidl_dot_core_dot_identifier__pb2._TASKEXECUTIONIDENTIFIER
_TASKEXECUTION.fields_by_name['closure'].message_type = _TASKEXECUTIONCLOSURE
_TASKEXECUTIONLIST.fields_by_name['task_executions'].message_type = _TASKEXECUTION
_TASKEXECUTIONCLOSURE.fields_by_name['error'].message_type = flyteidl_dot_core_dot_execution__pb2._EXECUTIONERROR
_TASKEXECUTIONCLOSURE.fields_by_name['phase'].enum_type = flyteidl_dot_core_dot_execution__pb2._TASKEXECUTION_PHASE
_TASKEXECUTIONCLOSURE.fields_by_name['logs'].message_type = flyteidl_dot_core_dot_execution__pb2._TASKLOG
_TASKEXECUTIONCLOSURE.fields_by_name['started_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TASKEXECUTIONCLOSURE.fields_by_name['duration'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_TASKEXECUTIONCLOSURE.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TASKEXECUTIONCLOSURE.fields_by_name['updated_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TASKEXECUTIONCLOSURE.fields_by_name['custom_info'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_TASKEXECUTIONCLOSURE.fields_by_name['metadata'].message_type = flyteidl_dot_event_dot_event__pb2._TASKEXECUTIONMETADATA
_TASKEXECUTIONCLOSURE.oneofs_by_name['output_result'].fields.append(
  _TASKEXECUTIONCLOSURE.fields_by_name['output_uri'])
_TASKEXECUTIONCLOSURE.fields_by_name['output_uri'].containing_oneof = _TASKEXECUTIONCLOSURE.oneofs_by_name['output_result']
_TASKEXECUTIONCLOSURE.oneofs_by_name['output_result'].fields.append(
  _TASKEXECUTIONCLOSURE.fields_by_name['error'])
_TASKEXECUTIONCLOSURE.fields_by_name['error'].containing_oneof = _TASKEXECUTIONCLOSURE.oneofs_by_name['output_result']
_TASKEXECUTIONGETDATAREQUEST.fields_by_name['id'].message_type = flyteidl_dot_core_dot_identifier__pb2._TASKEXECUTIONIDENTIFIER
_TASKEXECUTIONGETDATARESPONSE.fields_by_name['inputs'].message_type = flyteidl_dot_admin_dot_common__pb2._URLBLOB
_TASKEXECUTIONGETDATARESPONSE.fields_by_name['outputs'].message_type = flyteidl_dot_admin_dot_common__pb2._URLBLOB
_TASKEXECUTIONGETDATARESPONSE.fields_by_name['full_inputs'].message_type = flyteidl_dot_core_dot_literals__pb2._LITERALMAP
_TASKEXECUTIONGETDATARESPONSE.fields_by_name['full_outputs'].message_type = flyteidl_dot_core_dot_literals__pb2._LITERALMAP
DESCRIPTOR.message_types_by_name['TaskExecutionGetRequest'] = _TASKEXECUTIONGETREQUEST
DESCRIPTOR.message_types_by_name['TaskExecutionListRequest'] = _TASKEXECUTIONLISTREQUEST
DESCRIPTOR.message_types_by_name['TaskExecution'] = _TASKEXECUTION
DESCRIPTOR.message_types_by_name['TaskExecutionList'] = _TASKEXECUTIONLIST
DESCRIPTOR.message_types_by_name['TaskExecutionClosure'] = _TASKEXECUTIONCLOSURE
DESCRIPTOR.message_types_by_name['TaskExecutionGetDataRequest'] = _TASKEXECUTIONGETDATAREQUEST
DESCRIPTOR.message_types_by_name['TaskExecutionGetDataResponse'] = _TASKEXECUTIONGETDATARESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TaskExecutionGetRequest = _reflection.GeneratedProtocolMessageType('TaskExecutionGetRequest', (_message.Message,), dict(
  DESCRIPTOR = _TASKEXECUTIONGETREQUEST,
  __module__ = 'flyteidl.admin.task_execution_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.TaskExecutionGetRequest)
  ))
_sym_db.RegisterMessage(TaskExecutionGetRequest)

TaskExecutionListRequest = _reflection.GeneratedProtocolMessageType('TaskExecutionListRequest', (_message.Message,), dict(
  DESCRIPTOR = _TASKEXECUTIONLISTREQUEST,
  __module__ = 'flyteidl.admin.task_execution_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.TaskExecutionListRequest)
  ))
_sym_db.RegisterMessage(TaskExecutionListRequest)

TaskExecution = _reflection.GeneratedProtocolMessageType('TaskExecution', (_message.Message,), dict(
  DESCRIPTOR = _TASKEXECUTION,
  __module__ = 'flyteidl.admin.task_execution_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.TaskExecution)
  ))
_sym_db.RegisterMessage(TaskExecution)

TaskExecutionList = _reflection.GeneratedProtocolMessageType('TaskExecutionList', (_message.Message,), dict(
  DESCRIPTOR = _TASKEXECUTIONLIST,
  __module__ = 'flyteidl.admin.task_execution_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.TaskExecutionList)
  ))
_sym_db.RegisterMessage(TaskExecutionList)

TaskExecutionClosure = _reflection.GeneratedProtocolMessageType('TaskExecutionClosure', (_message.Message,), dict(
  DESCRIPTOR = _TASKEXECUTIONCLOSURE,
  __module__ = 'flyteidl.admin.task_execution_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.TaskExecutionClosure)
  ))
_sym_db.RegisterMessage(TaskExecutionClosure)

TaskExecutionGetDataRequest = _reflection.GeneratedProtocolMessageType('TaskExecutionGetDataRequest', (_message.Message,), dict(
  DESCRIPTOR = _TASKEXECUTIONGETDATAREQUEST,
  __module__ = 'flyteidl.admin.task_execution_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.TaskExecutionGetDataRequest)
  ))
_sym_db.RegisterMessage(TaskExecutionGetDataRequest)

TaskExecutionGetDataResponse = _reflection.GeneratedProtocolMessageType('TaskExecutionGetDataResponse', (_message.Message,), dict(
  DESCRIPTOR = _TASKEXECUTIONGETDATARESPONSE,
  __module__ = 'flyteidl.admin.task_execution_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.TaskExecutionGetDataResponse)
  ))
_sym_db.RegisterMessage(TaskExecutionGetDataResponse)


DESCRIPTOR._options = None
_TASKEXECUTIONGETDATARESPONSE.fields_by_name['inputs']._options = None
_TASKEXECUTIONGETDATARESPONSE.fields_by_name['outputs']._options = None
# @@protoc_insertion_point(module_scope)
