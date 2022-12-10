# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import service.inventoryObject_pb2 as inventoryObject__pb2

class InventoryServiceStub(object):
    """Interface exported by the server.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateBook = channel.unary_unary(
                '/InventoryService/CreateBook',
                request_serializer=inventoryObject__pb2.Book.SerializeToString,
                response_deserializer=inventoryObject__pb2.CreateBookResponse.FromString,
                )
        self.GetBook = channel.unary_unary(
                '/InventoryService/GetBook',
                request_serializer=inventoryObject__pb2.GetBookRequest.SerializeToString,
                response_deserializer=inventoryObject__pb2.GetBookReponse.FromString,
                )


class InventoryServiceServicer(object):
    """Interface exported by the server.
    """

    def CreateBook(self, request, context):
        """Add a book into inventory service. Require details of new book as
        input arguments.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBook(self, request, context):
        """Search a book from inventory service by ISBN.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InventoryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateBook': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateBook,
                    request_deserializer=inventoryObject__pb2.Book.FromString,
                    response_serializer=inventoryObject__pb2.CreateBookResponse.SerializeToString,
            ),
            'GetBook': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBook,
                    request_deserializer=inventoryObject__pb2.GetBookRequest.FromString,
                    response_serializer=inventoryObject__pb2.GetBookReponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'InventoryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class InventoryService(object):
    """Interface exported by the server.
    """

    @staticmethod
    def CreateBook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/InventoryService/CreateBook',
            inventoryObject__pb2.Book.SerializeToString,
            inventoryObject__pb2.CreateBookResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/InventoryService/GetBook',
            inventoryObject__pb2.GetBookRequest.SerializeToString,
            inventoryObject__pb2.GetBookReponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
