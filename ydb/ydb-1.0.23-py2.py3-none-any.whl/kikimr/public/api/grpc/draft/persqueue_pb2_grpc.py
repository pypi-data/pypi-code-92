# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from kikimr.public.api.protos.draft import persqueue_pb2 as kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_persqueue__pb2


class PersQueueServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.WriteSession = channel.stream_stream(
        '/NPersQueue.PersQueueService/WriteSession',
        request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_persqueue__pb2.WriteRequest.SerializeToString,
        response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_persqueue__pb2.WriteResponse.FromString,
        )
    self.ReadSession = channel.stream_stream(
        '/NPersQueue.PersQueueService/ReadSession',
        request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_persqueue__pb2.ReadRequest.SerializeToString,
        response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_persqueue__pb2.ReadResponse.FromString,
        )


class PersQueueServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def WriteSession(self, request_iterator, context):
    """*
    Creates Write Session
    Pipeline:
    client                  server
    Init(Topic, SourceId, ...)
    ---------------->
    Init(Partition, MaxSeqNo, ...)
    <----------------
    write(data1, seqNo1)
    ---------------->
    write(data2, seqNo2)
    ---------------->
    ack(seqNo1, offset1, ...)
    <----------------
    write(data3, seqNo3)
    ---------------->
    ack(seqNo2, offset2, ...)
    <----------------
    error(description, errorCode)
    <----------------

    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReadSession(self, request_iterator, context):
    """*
    Creates Read Session
    Pipeline:
    client                  server
    Init(Topics, ClientId, ...)
    ---------------->
    Init(SessionId)
    <----------------
    read1
    ---------------->
    read2
    ---------------->
    lock(Topic1,Partition1, ...) - locks and releases are optional
    <----------------
    lock(Topic2, Partition2, ...)
    <----------------
    release(Topic1, Partition1, ...)
    <----------------
    locked(Topic2, Partition2, ...) - client must respond to lock request with this message. Only after this client will start recieving messages from this partition
    ---------------->
    read result(data, ...)
    <----------------
    commit(cookie1)
    ---------------->
    commit result(cookie1)
    <----------------
    error(description, errorCode)
    <----------------

    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PersQueueServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'WriteSession': grpc.stream_stream_rpc_method_handler(
          servicer.WriteSession,
          request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_persqueue__pb2.WriteRequest.FromString,
          response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_persqueue__pb2.WriteResponse.SerializeToString,
      ),
      'ReadSession': grpc.stream_stream_rpc_method_handler(
          servicer.ReadSession,
          request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_persqueue__pb2.ReadRequest.FromString,
          response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_persqueue__pb2.ReadResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'NPersQueue.PersQueueService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
