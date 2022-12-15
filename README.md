# 17625-assignment-3

This is a gRPC service that provides library inventory service.

## CreateBook
  - Create a book in the inventory service
  
## GetBook
  - Search a book in the inventory service and get the book's details
  
## Usage
  Complie proto
  ```complie proto
 cd service/
 python -m grpc_tools.protoc -I../protos --python_out=. --pyi_out=. --grpc_python_out=. ../protos/inventoryService.proto ../protos/inventoryObject.proto
  ```
  
  Execute server
  ```execute server
  python runServer.py 
  ```
  
  Execute client
  ```execute client
  python runClient.py 
  ```
 
  Execute testing without a real server
  ```execute testing without a real server
  python runTest.py 
  ```
  
  Execute testing with a real server
  ```execute testing with a real server
  export SERVER_TEST="True"
  python runTest.py 
  ```
