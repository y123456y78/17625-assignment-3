"""Database used in inventory service."""

import json

import service.inventoryObject_pb2 as object


"""Reads the inventory database.
    Retrieve pre-defined data for executing inventory service.

    Returns:
        The full contents of the inventory database as a sequence of 
        inventoryObject_pb2.Book.
"""
def readInvetoryData():
    books = []
    with open("./service/db/inventoryDB.json") as inventoryDB:
        for item in json.load(inventoryDB):
            book = object.Book(
                ISBN=item["ISBN"],
                title=item["title"],
                author=item["author"],
                genre=item["genre"],
                publishingYear=item["publishingYear"]
            )
            books.append(book)
    return books
