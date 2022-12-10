from concurrent import futures

import grpc
import service.inventoryObject_pb2 as object
import service.inventoryService_pb2_grpc as service
from service.db import db

ADDRESS = '[::]:50051'

"""Provides methods that implement functionality of inventory service server."""
class InventoryServiceServicer(service.InventoryServiceServicer):
    def __init__(self):
        self.db = db.readInvetoryDB()

    """Implement create book funcitonality.
        Handle create book request and add a new book into the database.
        
        Args:
            request: gRPC request contains deatils of new book.
            context: gRPC context.

        Returns:
            Sccessful status and message of the request.
    """
    def CreateBook(self, request, context):
        try:
            haveBook = self.GetBookByISBN(request.ISBN)
            if haveBook:
                return object.CreateBookResponse(
                    success=False,
                    message="There book is already existed."
                )
            else:
                book = object.Book(
                    ISBN=request.ISBN,
                    title=request.title,
                    author=request.author,
                    genre=request.genre,
                    publishingYear=request.publishingYear
                )
                self.db.append(book)
                return object.CreateBookResponse(
                    success=True,
                    message="The book was successfully added."
                )
        except Exception:
            context.set_code(grpc.StatusCode.UNKNOWN)
            return object.CreateBookResponse(
                success=False,
                message="There is an unknown error."
            )

    """Implement get book funcitonality.
        
        Args:
            request: gRPC request containts ISBN used for searching.
            context: gRPC context.

        Returns:
            Searching result and the book's detail if found.
    """
    def GetBook(self, request, context):
        book = self.GetBookByISBN(request.ISBN)
        if book:
            return object.GetBookReponse(
                found=True,
                book=book
            )
        else:
            return object.GetBookReponse(
                found=False
            )

    """Search a book by ISBN in the database
        
        Args:
            ISBN: Unique identifier of the book
        Returns:
            Target book if found, otherwise null
    """
    def GetBookByISBN(self, ISBN):
        for book in self.db:
            if book.ISBN == ISBN:
                return book
        return None

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service.add_InventoryServiceServicer_to_server(
        InventoryServiceServicer(), server)
        
    server.add_insecure_port(ADDRESS)
    server.start()
    server.wait_for_termination()


