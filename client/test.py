from unittest.mock import Mock
from service import inventoryObject_pb2 as object
from client.inventory_client import InventoryClient, getBookTitlesFromServer
from service.db import db
import unittest
import os

TEST_WITH_SERVER = (os.getenv('SERVER_TEST') == 'True')

class TestGetBookTitles(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestGetBookTitles, self).__init__(*args, **kwargs)
        self.testData = db.readInvetoryData()[:2] # take first two instances as test data
        self.testResponse = [object.GetBookReponse(found=True, book=book) for book in self.testData]
        self.input = [book.ISBN for book in self.testData]
        self.expectedResult = [book.title for book in self.testData]

    """Test GetBookTitles with a mock client"""
    def testWithMockServer(self):
        clientMock = Mock()
        clientMock.stub.GetBook.side_effect = self.testResponse
        titles = getBookTitlesFromServer(clientMock, self.input)
        self.assertEqual(titles, self.expectedResult)

    """Test GetBookTitles with a mock client under empty data condition"""
    def testWithMockEmptyData(self):
        clientMock = Mock()
        clientMock.stub.GetBook.return_value = object.GetBookReponse(found=False)
        titles = getBookTitlesFromServer(clientMock, self.input)
        assert(len(titles)==0)

    """Test GetBookTitles with a real client"""
    @unittest.skipIf(not TEST_WITH_SERVER, "Test with real server")
    def testWithServer(self):
        client = InventoryClient()
        titles = getBookTitlesFromServer(client, self.input)
        self.assertEqual(titles, self.expectedResult)

if __name__ == '__main__':
    unittest.main()