# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from kikimr.public.api.protos import ydb_experimental_pb2 as kikimr_dot_public_dot_api_dot_protos_dot_ydb__experimental__pb2


class ExperimentalServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.UploadRows = channel.unary_unary(
        '/Ydb.Experimental.V1.ExperimentalService/UploadRows',
        request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__experimental__pb2.UploadRowsRequest.SerializeToString,
        response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__experimental__pb2.UploadRowsResponse.FromString,
        )
    self.ExecuteStreamQuery = channel.unary_stream(
        '/Ydb.Experimental.V1.ExperimentalService/ExecuteStreamQuery',
        request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__experimental__pb2.ExecuteStreamQueryRequest.SerializeToString,
        response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__experimental__pb2.ExecuteStreamQueryResponse.FromString,
        )
    self.GetDiskSpaceUsage = channel.unary_unary(
        '/Ydb.Experimental.V1.ExperimentalService/GetDiskSpaceUsage',
        request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__experimental__pb2.GetDiskSpaceUsageRequest.SerializeToString,
        response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__experimental__pb2.GetDiskSpaceUsageResponse.FromString,
        )


class ExperimentalServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def UploadRows(self, request, context):
    """Fast bulk load rows to a table bypassing transaction logic.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ExecuteStreamQuery(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetDiskSpaceUsage(self, request, context):
    """Returns disk space usage by database
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ExperimentalServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'UploadRows': grpc.unary_unary_rpc_method_handler(
          servicer.UploadRows,
          request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__experimental__pb2.UploadRowsRequest.FromString,
          response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__experimental__pb2.UploadRowsResponse.SerializeToString,
      ),
      'ExecuteStreamQuery': grpc.unary_stream_rpc_method_handler(
          servicer.ExecuteStreamQuery,
          request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__experimental__pb2.ExecuteStreamQueryRequest.FromString,
          response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__experimental__pb2.ExecuteStreamQueryResponse.SerializeToString,
      ),
      'GetDiskSpaceUsage': grpc.unary_unary_rpc_method_handler(
          servicer.GetDiskSpaceUsage,
          request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__experimental__pb2.GetDiskSpaceUsageRequest.FromString,
          response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__experimental__pb2.GetDiskSpaceUsageResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Ydb.Experimental.V1.ExperimentalService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
