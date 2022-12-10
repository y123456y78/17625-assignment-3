import grpc
from service import inventoryService_pb2_grpc as service
from service import inventoryObject_pb2 as object
from service import inventoryService_server as server

"""Client for inventory service which encapsulate the connection configuration."""
class InventoryClient:
    def __init__(self):
        channel = grpc.insecure_channel(server.ADDRESS)
        self.stub = service.InventoryServiceStub(channel)

"""GetBookTitle functionality interface.
    Get book's title by ISBN number from server.
        
    Args:
        client: Inventory service client.
        ISBNs: List of ISBN for query.

    Returns:
        List of book titles.
"""
def getBookTitlesFromServer(client, ISBNs):
    titles = []
    for ISBN in ISBNs:
        request = object.GetBookRequest(ISBN=ISBN)
        response = client.stub.GetBook(request)
        if response.found:
            titles.append(response.book.title)
    return titles