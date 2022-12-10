from service import inventoryService_server
import logging

if __name__ == '__main__':
    logging.basicConfig()
    inventoryService_server.serve()
