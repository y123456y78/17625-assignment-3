# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: inventoryObject.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15inventoryObject.proto\"b\n\x04\x42ook\x12\x0c\n\x04ISBN\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x03 \x01(\t\x12\x15\n\x05genre\x18\x04 \x01(\x0e\x32\x06.Genre\x12\x16\n\x0epublishingYear\x18\x05 \x01(\x05\"`\n\rInventoryItem\x12\x17\n\x0finventoryNumber\x18\x01 \x01(\x05\x12\x15\n\x04\x62ook\x18\x02 \x01(\x0b\x32\x05.BookH\x00\x12\x17\n\x06status\x18\x03 \x01(\x0e\x32\x07.StatusB\x06\n\x04item\"6\n\x12\x43reateBookResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x1e\n\x0eGetBookRequest\x12\x0c\n\x04ISBN\x18\x01 \x01(\t\"4\n\x0eGetBookReponse\x12\r\n\x05\x66ound\x18\x01 \x01(\x08\x12\x13\n\x04\x62ook\x18\x02 \x01(\x0b\x32\x05.Book*u\n\x05Genre\x12\x15\n\x11GENRE_UNSPECIFIED\x10\x00\x12\x19\n\x15GENRE_SCIENCE_FICTION\x10\x01\x12\x11\n\rGENRE_FANTASY\x10\x02\x12\x11\n\rGENRE_MYSTERY\x10\x03\x12\x14\n\x10GENRE_HISTORICAL\x10\x04*H\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x14\n\x10STATUS_AVAILABLE\x10\x01\x12\x10\n\x0cSTATUS_TAKEN\x10\x02\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'inventoryObject_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GENRE._serialized_start=365
  _GENRE._serialized_end=482
  _STATUS._serialized_start=484
  _STATUS._serialized_end=556
  _BOOK._serialized_start=25
  _BOOK._serialized_end=123
  _INVENTORYITEM._serialized_start=125
  _INVENTORYITEM._serialized_end=221
  _CREATEBOOKRESPONSE._serialized_start=223
  _CREATEBOOKRESPONSE._serialized_end=277
  _GETBOOKREQUEST._serialized_start=279
  _GETBOOKREQUEST._serialized_end=309
  _GETBOOKREPONSE._serialized_start=311
  _GETBOOKREPONSE._serialized_end=363
# @@protoc_insertion_point(module_scope)