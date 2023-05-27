# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import books_shared.protopy.book_pb2 as book__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class BookServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetBookList = channel.unary_unary(
                '/BookService/GetBookList',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=book__pb2.GetBookListResponse.FromString,
                )
        self.GetBook = channel.unary_unary(
                '/BookService/GetBook',
                request_serializer=book__pb2.GetBookRequest.SerializeToString,
                response_deserializer=book__pb2.GetBookResponse.FromString,
                )
        self.UpdateBookCount = channel.unary_unary(
                '/BookService/UpdateBookCount',
                request_serializer=book__pb2.UpdateBookCountRequest.SerializeToString,
                response_deserializer=book__pb2.UpdateBookCountResponse.FromString,
                )
        self.AddBook = channel.unary_unary(
                '/BookService/AddBook',
                request_serializer=book__pb2.AddBookRequest.SerializeToString,
                response_deserializer=book__pb2.AddBookResponse.FromString,
                )


class BookServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetBookList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBook(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateBookCount(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddBook(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BookServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetBookList': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBookList,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=book__pb2.GetBookListResponse.SerializeToString,
            ),
            'GetBook': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBook,
                    request_deserializer=book__pb2.GetBookRequest.FromString,
                    response_serializer=book__pb2.GetBookResponse.SerializeToString,
            ),
            'UpdateBookCount': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateBookCount,
                    request_deserializer=book__pb2.UpdateBookCountRequest.FromString,
                    response_serializer=book__pb2.UpdateBookCountResponse.SerializeToString,
            ),
            'AddBook': grpc.unary_unary_rpc_method_handler(
                    servicer.AddBook,
                    request_deserializer=book__pb2.AddBookRequest.FromString,
                    response_serializer=book__pb2.AddBookResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'BookService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class BookService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetBookList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BookService/GetBookList',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            book__pb2.GetBookListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BookService/GetBook',
            book__pb2.GetBookRequest.SerializeToString,
            book__pb2.GetBookResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateBookCount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BookService/UpdateBookCount',
            book__pb2.UpdateBookCountRequest.SerializeToString,
            book__pb2.UpdateBookCountResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddBook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BookService/AddBook',
            book__pb2.AddBookRequest.SerializeToString,
            book__pb2.AddBookResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
