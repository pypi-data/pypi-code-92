# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kikimr/public/api/protos/draft/yql_internal.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from kikimr.public.api.protos import ydb_operation_pb2 as kikimr_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2
from kikimr.public.api.protos import ydb_value_pb2 as kikimr_dot_public_dot_api_dot_protos_dot_ydb__value__pb2
from kikimr.public.api.protos import ydb_issue_message_pb2 as kikimr_dot_public_dot_api_dot_protos_dot_ydb__issue__message__pb2
from kikimr.public.api.protos.draft import yql_analytics_pb2 as kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yql__analytics__pb2
from kikimr.public.api.protos import yq_pb2 as kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='kikimr/public/api/protos/draft/yql_internal.proto',
  package='Yql.Analytics',
  syntax='proto3',
  serialized_options=b'\n!com.yandex.yql.analytics.internalB\026AnalyticsIntenalProtos\370\001\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n1kikimr/public/api/protos/draft/yql_internal.proto\x12\rYql.Analytics\x1a,kikimr/public/api/protos/ydb_operation.proto\x1a(kikimr/public/api/protos/ydb_value.proto\x1a\x30kikimr/public/api/protos/ydb_issue_message.proto\x1a\x32kikimr/public/api/protos/draft/yql_analytics.proto\x1a!kikimr/public/api/protos/yq.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"@\n\x0eGetTaskRequest\x12\x0e\n\x06tenant\x18\x01 \x01(\t\x12\x10\n\x08owner_id\x18\x02 \x01(\t\x12\x0c\n\x04host\x18\x03 \x01(\t\"2\n\x0eSignedIdentity\x12\r\n\x05value\x18\x01 \x01(\t\x12\x11\n\tsignature\x18\x02 \x01(\t\"\x9b\x03\n\rGetTaskResult\x12\x10\n\x08has_task\x18\x01 \x01(\x08\x12\x30\n\tresult_id\x18\x02 \x01(\x0b\x32\x1d.Yql.Analytics.SignedIdentity\x12/\n\x08query_id\x18\x03 \x01(\x0b\x32\x1d.Yql.Analytics.SignedIdentity\x12-\n\x06job_id\x18\x04 \x01(\x0b\x32\x1d.Yql.Analytics.SignedIdentity\x12\x12\n\ngeneration\x18\x05 \x01(\x04\x12\x11\n\tstreaming\x18\x06 \x01(\x08\x12\x10\n\x08\x64q_graph\x18\x07 \x01(\t\x12\x0c\n\x04text\x18\x08 \x01(\t\x12+\n\nconnection\x18\t \x03(\x0b\x32\x17.YandexQuery.Connection\x12%\n\x07\x62inding\x18\n \x03(\x0b\x32\x14.YandexQuery.Binding\x12\x12\n\nuser_token\x18\x0b \x01(\t\x12\x37\n\x10service_accounts\x18\x0c \x03(\x0b\x32\x1d.Yql.Analytics.SignedIdentity\"?\n\x0fGetTaskResponse\x12,\n\toperation\x18\x01 \x01(\x0b\x32\x19.Ydb.Operations.Operation\"\x82\x04\n\x0fPingTaskRequest\x12\x10\n\x08owner_id\x18\x01 \x01(\t\x12/\n\x08query_id\x18\x02 \x01(\x0b\x32\x1d.Yql.Analytics.SignedIdentity\x12-\n\x06job_id\x18\x03 \x01(\x0b\x32\x1d.Yql.Analytics.SignedIdentity\x12\x30\n\tresult_id\x18\x04 \x01(\x0b\x32\x1d.Yql.Analytics.SignedIdentity\x12\x34\n\x06status\x18\x05 \x01(\x0e\x32$.YandexQuery.QueryMeta.ComputeStatus\x12\'\n\x06issues\x18\x06 \x03(\x0b\x32\x17.Ydb.Issue.IssueMessage\x12\x18\n\x10result_set_count\x18\x07 \x01(\r\x12\x12\n\nstatistics\x18\x08 \x01(\t\x12\x1a\n\x12serialized_headers\x18\t \x01(\x0c\x12\x15\n\rexecuter_info\x18\n \x01(\t\x12\x10\n\x08\x64q_graph\x18\x0b \x01(\t\x12\x0b\n\x03\x61st\x18\x0c \x01(\t\x12\x0c\n\x04plan\x18\r \x01(\t\x12\x14\n\x0cresign_query\x18\x0e \x01(\x08\x12\x39\n\x10operation_params\x18\x0f \x01(\x0b\x32\x1f.Ydb.Operations.OperationParams\x12\r\n\x05scope\x18\x64 \x01(\t\":\n\x0ePingTaskResult\x12(\n\x06\x61\x63tion\x18\x01 \x01(\x0e\x32\x18.YandexQuery.QueryAction\"@\n\x10PingTaskResponse\x12,\n\toperation\x18\x01 \x01(\x0b\x32\x19.Ydb.Operations.Operation\"\xa7\x01\n\x16WriteTaskResultRequest\x12\x10\n\x08owner_id\x18\x01 \x01(\t\x12\x30\n\tresult_id\x18\x02 \x01(\x0b\x32\x1d.Yql.Analytics.SignedIdentity\x12\"\n\nresult_set\x18\x03 \x01(\x0b\x32\x0e.Ydb.ResultSet\x12\x15\n\rresult_set_id\x18\x04 \x01(\r\x12\x0e\n\x06offset\x18\x05 \x01(\x04\"\x17\n\x15WriteTaskResultResult\"G\n\x17WriteTaskResultResponse\x12,\n\toperation\x18\x01 \x01(\x0b\x32\x19.Ydb.Operations.OperationB>\n!com.yandex.yql.analytics.internalB\x16\x41nalyticsIntenalProtos\xf8\x01\x01\x62\x06proto3'
  ,
  dependencies=[kikimr_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2.DESCRIPTOR,kikimr_dot_public_dot_api_dot_protos_dot_ydb__value__pb2.DESCRIPTOR,kikimr_dot_public_dot_api_dot_protos_dot_ydb__issue__message__pb2.DESCRIPTOR,kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yql__analytics__pb2.DESCRIPTOR,kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_GETTASKREQUEST = _descriptor.Descriptor(
  name='GetTaskRequest',
  full_name='Yql.Analytics.GetTaskRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tenant', full_name='Yql.Analytics.GetTaskRequest.tenant', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='owner_id', full_name='Yql.Analytics.GetTaskRequest.owner_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='host', full_name='Yql.Analytics.GetTaskRequest.host', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=326,
  serialized_end=390,
)


_SIGNEDIDENTITY = _descriptor.Descriptor(
  name='SignedIdentity',
  full_name='Yql.Analytics.SignedIdentity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='Yql.Analytics.SignedIdentity.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='signature', full_name='Yql.Analytics.SignedIdentity.signature', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=392,
  serialized_end=442,
)


_GETTASKRESULT = _descriptor.Descriptor(
  name='GetTaskResult',
  full_name='Yql.Analytics.GetTaskResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='has_task', full_name='Yql.Analytics.GetTaskResult.has_task', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result_id', full_name='Yql.Analytics.GetTaskResult.result_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='query_id', full_name='Yql.Analytics.GetTaskResult.query_id', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='job_id', full_name='Yql.Analytics.GetTaskResult.job_id', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='generation', full_name='Yql.Analytics.GetTaskResult.generation', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='streaming', full_name='Yql.Analytics.GetTaskResult.streaming', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dq_graph', full_name='Yql.Analytics.GetTaskResult.dq_graph', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='text', full_name='Yql.Analytics.GetTaskResult.text', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='connection', full_name='Yql.Analytics.GetTaskResult.connection', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='binding', full_name='Yql.Analytics.GetTaskResult.binding', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_token', full_name='Yql.Analytics.GetTaskResult.user_token', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='service_accounts', full_name='Yql.Analytics.GetTaskResult.service_accounts', index=11,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=445,
  serialized_end=856,
)


_GETTASKRESPONSE = _descriptor.Descriptor(
  name='GetTaskResponse',
  full_name='Yql.Analytics.GetTaskResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='operation', full_name='Yql.Analytics.GetTaskResponse.operation', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=858,
  serialized_end=921,
)


_PINGTASKREQUEST = _descriptor.Descriptor(
  name='PingTaskRequest',
  full_name='Yql.Analytics.PingTaskRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='owner_id', full_name='Yql.Analytics.PingTaskRequest.owner_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='query_id', full_name='Yql.Analytics.PingTaskRequest.query_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='job_id', full_name='Yql.Analytics.PingTaskRequest.job_id', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result_id', full_name='Yql.Analytics.PingTaskRequest.result_id', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='Yql.Analytics.PingTaskRequest.status', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='issues', full_name='Yql.Analytics.PingTaskRequest.issues', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result_set_count', full_name='Yql.Analytics.PingTaskRequest.result_set_count', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='statistics', full_name='Yql.Analytics.PingTaskRequest.statistics', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='serialized_headers', full_name='Yql.Analytics.PingTaskRequest.serialized_headers', index=8,
      number=9, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='executer_info', full_name='Yql.Analytics.PingTaskRequest.executer_info', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dq_graph', full_name='Yql.Analytics.PingTaskRequest.dq_graph', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ast', full_name='Yql.Analytics.PingTaskRequest.ast', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='plan', full_name='Yql.Analytics.PingTaskRequest.plan', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resign_query', full_name='Yql.Analytics.PingTaskRequest.resign_query', index=13,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='operation_params', full_name='Yql.Analytics.PingTaskRequest.operation_params', index=14,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='scope', full_name='Yql.Analytics.PingTaskRequest.scope', index=15,
      number=100, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=924,
  serialized_end=1438,
)


_PINGTASKRESULT = _descriptor.Descriptor(
  name='PingTaskResult',
  full_name='Yql.Analytics.PingTaskResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='action', full_name='Yql.Analytics.PingTaskResult.action', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1440,
  serialized_end=1498,
)


_PINGTASKRESPONSE = _descriptor.Descriptor(
  name='PingTaskResponse',
  full_name='Yql.Analytics.PingTaskResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='operation', full_name='Yql.Analytics.PingTaskResponse.operation', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1500,
  serialized_end=1564,
)


_WRITETASKRESULTREQUEST = _descriptor.Descriptor(
  name='WriteTaskResultRequest',
  full_name='Yql.Analytics.WriteTaskResultRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='owner_id', full_name='Yql.Analytics.WriteTaskResultRequest.owner_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result_id', full_name='Yql.Analytics.WriteTaskResultRequest.result_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result_set', full_name='Yql.Analytics.WriteTaskResultRequest.result_set', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result_set_id', full_name='Yql.Analytics.WriteTaskResultRequest.result_set_id', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='offset', full_name='Yql.Analytics.WriteTaskResultRequest.offset', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1567,
  serialized_end=1734,
)


_WRITETASKRESULTRESULT = _descriptor.Descriptor(
  name='WriteTaskResultResult',
  full_name='Yql.Analytics.WriteTaskResultResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=1736,
  serialized_end=1759,
)


_WRITETASKRESULTRESPONSE = _descriptor.Descriptor(
  name='WriteTaskResultResponse',
  full_name='Yql.Analytics.WriteTaskResultResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='operation', full_name='Yql.Analytics.WriteTaskResultResponse.operation', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1761,
  serialized_end=1832,
)

_GETTASKRESULT.fields_by_name['result_id'].message_type = _SIGNEDIDENTITY
_GETTASKRESULT.fields_by_name['query_id'].message_type = _SIGNEDIDENTITY
_GETTASKRESULT.fields_by_name['job_id'].message_type = _SIGNEDIDENTITY
_GETTASKRESULT.fields_by_name['connection'].message_type = kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2._CONNECTION
_GETTASKRESULT.fields_by_name['binding'].message_type = kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2._BINDING
_GETTASKRESULT.fields_by_name['service_accounts'].message_type = _SIGNEDIDENTITY
_GETTASKRESPONSE.fields_by_name['operation'].message_type = kikimr_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2._OPERATION
_PINGTASKREQUEST.fields_by_name['query_id'].message_type = _SIGNEDIDENTITY
_PINGTASKREQUEST.fields_by_name['job_id'].message_type = _SIGNEDIDENTITY
_PINGTASKREQUEST.fields_by_name['result_id'].message_type = _SIGNEDIDENTITY
_PINGTASKREQUEST.fields_by_name['status'].enum_type = kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2._QUERYMETA_COMPUTESTATUS
_PINGTASKREQUEST.fields_by_name['issues'].message_type = kikimr_dot_public_dot_api_dot_protos_dot_ydb__issue__message__pb2._ISSUEMESSAGE
_PINGTASKREQUEST.fields_by_name['operation_params'].message_type = kikimr_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2._OPERATIONPARAMS
_PINGTASKRESULT.fields_by_name['action'].enum_type = kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2._QUERYACTION
_PINGTASKRESPONSE.fields_by_name['operation'].message_type = kikimr_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2._OPERATION
_WRITETASKRESULTREQUEST.fields_by_name['result_id'].message_type = _SIGNEDIDENTITY
_WRITETASKRESULTREQUEST.fields_by_name['result_set'].message_type = kikimr_dot_public_dot_api_dot_protos_dot_ydb__value__pb2._RESULTSET
_WRITETASKRESULTRESPONSE.fields_by_name['operation'].message_type = kikimr_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2._OPERATION
DESCRIPTOR.message_types_by_name['GetTaskRequest'] = _GETTASKREQUEST
DESCRIPTOR.message_types_by_name['SignedIdentity'] = _SIGNEDIDENTITY
DESCRIPTOR.message_types_by_name['GetTaskResult'] = _GETTASKRESULT
DESCRIPTOR.message_types_by_name['GetTaskResponse'] = _GETTASKRESPONSE
DESCRIPTOR.message_types_by_name['PingTaskRequest'] = _PINGTASKREQUEST
DESCRIPTOR.message_types_by_name['PingTaskResult'] = _PINGTASKRESULT
DESCRIPTOR.message_types_by_name['PingTaskResponse'] = _PINGTASKRESPONSE
DESCRIPTOR.message_types_by_name['WriteTaskResultRequest'] = _WRITETASKRESULTREQUEST
DESCRIPTOR.message_types_by_name['WriteTaskResultResult'] = _WRITETASKRESULTRESULT
DESCRIPTOR.message_types_by_name['WriteTaskResultResponse'] = _WRITETASKRESULTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetTaskRequest = _reflection.GeneratedProtocolMessageType('GetTaskRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETTASKREQUEST,
  '__module__' : 'kikimr.public.api.protos.draft.yql_internal_pb2'
  # @@protoc_insertion_point(class_scope:Yql.Analytics.GetTaskRequest)
  })
_sym_db.RegisterMessage(GetTaskRequest)

SignedIdentity = _reflection.GeneratedProtocolMessageType('SignedIdentity', (_message.Message,), {
  'DESCRIPTOR' : _SIGNEDIDENTITY,
  '__module__' : 'kikimr.public.api.protos.draft.yql_internal_pb2'
  # @@protoc_insertion_point(class_scope:Yql.Analytics.SignedIdentity)
  })
_sym_db.RegisterMessage(SignedIdentity)

GetTaskResult = _reflection.GeneratedProtocolMessageType('GetTaskResult', (_message.Message,), {
  'DESCRIPTOR' : _GETTASKRESULT,
  '__module__' : 'kikimr.public.api.protos.draft.yql_internal_pb2'
  # @@protoc_insertion_point(class_scope:Yql.Analytics.GetTaskResult)
  })
_sym_db.RegisterMessage(GetTaskResult)

GetTaskResponse = _reflection.GeneratedProtocolMessageType('GetTaskResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETTASKRESPONSE,
  '__module__' : 'kikimr.public.api.protos.draft.yql_internal_pb2'
  # @@protoc_insertion_point(class_scope:Yql.Analytics.GetTaskResponse)
  })
_sym_db.RegisterMessage(GetTaskResponse)

PingTaskRequest = _reflection.GeneratedProtocolMessageType('PingTaskRequest', (_message.Message,), {
  'DESCRIPTOR' : _PINGTASKREQUEST,
  '__module__' : 'kikimr.public.api.protos.draft.yql_internal_pb2'
  # @@protoc_insertion_point(class_scope:Yql.Analytics.PingTaskRequest)
  })
_sym_db.RegisterMessage(PingTaskRequest)

PingTaskResult = _reflection.GeneratedProtocolMessageType('PingTaskResult', (_message.Message,), {
  'DESCRIPTOR' : _PINGTASKRESULT,
  '__module__' : 'kikimr.public.api.protos.draft.yql_internal_pb2'
  # @@protoc_insertion_point(class_scope:Yql.Analytics.PingTaskResult)
  })
_sym_db.RegisterMessage(PingTaskResult)

PingTaskResponse = _reflection.GeneratedProtocolMessageType('PingTaskResponse', (_message.Message,), {
  'DESCRIPTOR' : _PINGTASKRESPONSE,
  '__module__' : 'kikimr.public.api.protos.draft.yql_internal_pb2'
  # @@protoc_insertion_point(class_scope:Yql.Analytics.PingTaskResponse)
  })
_sym_db.RegisterMessage(PingTaskResponse)

WriteTaskResultRequest = _reflection.GeneratedProtocolMessageType('WriteTaskResultRequest', (_message.Message,), {
  'DESCRIPTOR' : _WRITETASKRESULTREQUEST,
  '__module__' : 'kikimr.public.api.protos.draft.yql_internal_pb2'
  # @@protoc_insertion_point(class_scope:Yql.Analytics.WriteTaskResultRequest)
  })
_sym_db.RegisterMessage(WriteTaskResultRequest)

WriteTaskResultResult = _reflection.GeneratedProtocolMessageType('WriteTaskResultResult', (_message.Message,), {
  'DESCRIPTOR' : _WRITETASKRESULTRESULT,
  '__module__' : 'kikimr.public.api.protos.draft.yql_internal_pb2'
  # @@protoc_insertion_point(class_scope:Yql.Analytics.WriteTaskResultResult)
  })
_sym_db.RegisterMessage(WriteTaskResultResult)

WriteTaskResultResponse = _reflection.GeneratedProtocolMessageType('WriteTaskResultResponse', (_message.Message,), {
  'DESCRIPTOR' : _WRITETASKRESULTRESPONSE,
  '__module__' : 'kikimr.public.api.protos.draft.yql_internal_pb2'
  # @@protoc_insertion_point(class_scope:Yql.Analytics.WriteTaskResultResponse)
  })
_sym_db.RegisterMessage(WriteTaskResultResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
