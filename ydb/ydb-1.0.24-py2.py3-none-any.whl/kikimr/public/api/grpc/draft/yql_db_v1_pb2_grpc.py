# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from kikimr.public.api.protos.draft import yql_internal_pb2 as kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yql__internal__pb2


class YqlInternalTaskServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetTask = channel.unary_unary(
        '/Yql.Analytics.V1.YqlInternalTaskService/GetTask',
        request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yql__internal__pb2.GetTaskRequest.SerializeToString,
        response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yql__internal__pb2.GetTaskResponse.FromString,
        )
    self.PingTask = channel.unary_unary(
        '/Yql.Analytics.V1.YqlInternalTaskService/PingTask',
        request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yql__internal__pb2.PingTaskRequest.SerializeToString,
        response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yql__internal__pb2.PingTaskResponse.FromString,
        )
    self.WriteTaskResult = channel.unary_unary(
        '/Yql.Analytics.V1.YqlInternalTaskService/WriteTaskResult',
        request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yql__internal__pb2.WriteTaskResultRequest.SerializeToString,
        response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yql__internal__pb2.WriteTaskResultResponse.FromString,
        )


class YqlInternalTaskServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetTask(self, request, context):
    """gets new task
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PingTask(self, request, context):
    """pings new task (also can update metadata)
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def WriteTaskResult(self, request, context):
    """writes rows
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_YqlInternalTaskServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetTask': grpc.unary_unary_rpc_method_handler(
          servicer.GetTask,
          request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yql__internal__pb2.GetTaskRequest.FromString,
          response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yql__internal__pb2.GetTaskResponse.SerializeToString,
      ),
      'PingTask': grpc.unary_unary_rpc_method_handler(
          servicer.PingTask,
          request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yql__internal__pb2.PingTaskRequest.FromString,
          response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yql__internal__pb2.PingTaskResponse.SerializeToString,
      ),
      'WriteTaskResult': grpc.unary_unary_rpc_method_handler(
          servicer.WriteTaskResult,
          request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yql__internal__pb2.WriteTaskResultRequest.FromString,
          response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yql__internal__pb2.WriteTaskResultResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Yql.Analytics.V1.YqlInternalTaskService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
