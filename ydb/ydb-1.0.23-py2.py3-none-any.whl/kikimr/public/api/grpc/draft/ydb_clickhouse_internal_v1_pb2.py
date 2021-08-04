# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kikimr/public/api/grpc/draft/ydb_clickhouse_internal_v1.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from kikimr.public.api.protos import ydb_clickhouse_internal_pb2 as kikimr_dot_public_dot_api_dot_protos_dot_ydb__clickhouse__internal__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='kikimr/public/api/grpc/draft/ydb_clickhouse_internal_v1.proto',
  package='Ydb.ClickhouseInternal.V1',
  syntax='proto3',
  serialized_options=b'\n\034com.yandex.ydb.clickhouse.v1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n=kikimr/public/api/grpc/draft/ydb_clickhouse_internal_v1.proto\x12\x19Ydb.ClickhouseInternal.V1\x1a\x36kikimr/public/api/protos/ydb_clickhouse_internal.proto2\xaf\x05\n\x19\x43lickhouseInternalService\x12Q\n\x04Scan\x12#.Ydb.ClickhouseInternal.ScanRequest\x1a$.Ydb.ClickhouseInternal.ScanResponse\x12x\n\x11GetShardLocations\x12\x30.Ydb.ClickhouseInternal.GetShardLocationsRequest\x1a\x31.Ydb.ClickhouseInternal.GetShardLocationsResponse\x12l\n\rDescribeTable\x12,.Ydb.ClickhouseInternal.DescribeTableRequest\x1a-.Ydb.ClickhouseInternal.DescribeTableResponse\x12o\n\x0e\x43reateSnapshot\x12-.Ydb.ClickhouseInternal.CreateSnapshotRequest\x1a..Ydb.ClickhouseInternal.CreateSnapshotResponse\x12r\n\x0fRefreshSnapshot\x12..Ydb.ClickhouseInternal.RefreshSnapshotRequest\x1a/.Ydb.ClickhouseInternal.RefreshSnapshotResponse\x12r\n\x0f\x44iscardSnapshot\x12..Ydb.ClickhouseInternal.DiscardSnapshotRequest\x1a/.Ydb.ClickhouseInternal.DiscardSnapshotResponseB\x1e\n\x1c\x63om.yandex.ydb.clickhouse.v1b\x06proto3'
  ,
  dependencies=[kikimr_dot_public_dot_api_dot_protos_dot_ydb__clickhouse__internal__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_CLICKHOUSEINTERNALSERVICE = _descriptor.ServiceDescriptor(
  name='ClickhouseInternalService',
  full_name='Ydb.ClickhouseInternal.V1.ClickhouseInternalService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=149,
  serialized_end=836,
  methods=[
  _descriptor.MethodDescriptor(
    name='Scan',
    full_name='Ydb.ClickhouseInternal.V1.ClickhouseInternalService.Scan',
    index=0,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__clickhouse__internal__pb2._SCANREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__clickhouse__internal__pb2._SCANRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetShardLocations',
    full_name='Ydb.ClickhouseInternal.V1.ClickhouseInternalService.GetShardLocations',
    index=1,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__clickhouse__internal__pb2._GETSHARDLOCATIONSREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__clickhouse__internal__pb2._GETSHARDLOCATIONSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DescribeTable',
    full_name='Ydb.ClickhouseInternal.V1.ClickhouseInternalService.DescribeTable',
    index=2,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__clickhouse__internal__pb2._DESCRIBETABLEREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__clickhouse__internal__pb2._DESCRIBETABLERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CreateSnapshot',
    full_name='Ydb.ClickhouseInternal.V1.ClickhouseInternalService.CreateSnapshot',
    index=3,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__clickhouse__internal__pb2._CREATESNAPSHOTREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__clickhouse__internal__pb2._CREATESNAPSHOTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RefreshSnapshot',
    full_name='Ydb.ClickhouseInternal.V1.ClickhouseInternalService.RefreshSnapshot',
    index=4,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__clickhouse__internal__pb2._REFRESHSNAPSHOTREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__clickhouse__internal__pb2._REFRESHSNAPSHOTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DiscardSnapshot',
    full_name='Ydb.ClickhouseInternal.V1.ClickhouseInternalService.DiscardSnapshot',
    index=5,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__clickhouse__internal__pb2._DISCARDSNAPSHOTREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__clickhouse__internal__pb2._DISCARDSNAPSHOTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CLICKHOUSEINTERNALSERVICE)

DESCRIPTOR.services_by_name['ClickhouseInternalService'] = _CLICKHOUSEINTERNALSERVICE

# @@protoc_insertion_point(module_scope)
