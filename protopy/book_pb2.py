# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: book.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='book.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nbook.proto\"K\n\x04\x42ook\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x19\n\x05genre\x18\x02 \x01(\x0e\x32\n.BookGenre\x12\r\n\x05title\x18\x03 \x01(\t\x12\r\n\x05\x63ount\x18\x04 \x01(\x05\"\x1f\n\x0eGetBookRequest\x12\r\n\x05title\x18\x01 \x01(\t\"&\n\x0fGetBookResponse\x12\x13\n\x04\x62ook\x18\x01 \x01(\x0b\x32\x05.Book\"3\n\x16UpdateBookCountRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05\x63ount\x18\x02 \x01(\x05\".\n\x17UpdateBookCountResponse\x12\x13\n\x04\x62ook\x18\x01 \x01(\x0b\x32\x05.Book\"I\n\x0e\x41\x64\x64\x42ookRequest\x12\x19\n\x05genre\x18\x01 \x01(\x0e\x32\n.BookGenre\x12\r\n\x05title\x18\x02 \x01(\t\x12\r\n\x05\x63ount\x18\x03 \x01(\x05\"&\n\x0f\x41\x64\x64\x42ookResponse\x12\x13\n\x04\x62ook\x18\x01 \x01(\x0b\x32\x05.Book*A\n\tBookGenre\x12\x0b\n\x07\x46ICTION\x10\x00\x12\x0b\n\x07MYSTERY\x10\x01\x12\x0b\n\x07SCIENCE\x10\x02\x12\r\n\tSELF_HELP\x10\x03\x32\xb5\x01\n\x0b\x42ookService\x12.\n\x07GetBook\x12\x0f.GetBookRequest\x1a\x10.GetBookResponse\"\x00\x12\x46\n\x0fUpdateBookCount\x12\x17.UpdateBookCountRequest\x1a\x18.UpdateBookCountResponse\"\x00\x12.\n\x07\x41\x64\x64\x42ook\x12\x0f.AddBookRequest\x1a\x10.AddBookResponse\"\x00\x62\x06proto3'
)

_BOOKGENRE = _descriptor.EnumDescriptor(
  name='BookGenre',
  full_name='BookGenre',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FICTION', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MYSTERY', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SCIENCE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SELF_HELP', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=380,
  serialized_end=445,
)
_sym_db.RegisterEnumDescriptor(_BOOKGENRE)

BookGenre = enum_type_wrapper.EnumTypeWrapper(_BOOKGENRE)
FICTION = 0
MYSTERY = 1
SCIENCE = 2
SELF_HELP = 3



_BOOK = _descriptor.Descriptor(
  name='Book',
  full_name='Book',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Book.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='genre', full_name='Book.genre', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='title', full_name='Book.title', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='count', full_name='Book.count', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=14,
  serialized_end=89,
)


_GETBOOKREQUEST = _descriptor.Descriptor(
  name='GetBookRequest',
  full_name='GetBookRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='GetBookRequest.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=91,
  serialized_end=122,
)


_GETBOOKRESPONSE = _descriptor.Descriptor(
  name='GetBookResponse',
  full_name='GetBookResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='book', full_name='GetBookResponse.book', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=124,
  serialized_end=162,
)


_UPDATEBOOKCOUNTREQUEST = _descriptor.Descriptor(
  name='UpdateBookCountRequest',
  full_name='UpdateBookCountRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='UpdateBookCountRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='count', full_name='UpdateBookCountRequest.count', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=164,
  serialized_end=215,
)


_UPDATEBOOKCOUNTRESPONSE = _descriptor.Descriptor(
  name='UpdateBookCountResponse',
  full_name='UpdateBookCountResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='book', full_name='UpdateBookCountResponse.book', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=217,
  serialized_end=263,
)


_ADDBOOKREQUEST = _descriptor.Descriptor(
  name='AddBookRequest',
  full_name='AddBookRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='genre', full_name='AddBookRequest.genre', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='title', full_name='AddBookRequest.title', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='count', full_name='AddBookRequest.count', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=265,
  serialized_end=338,
)


_ADDBOOKRESPONSE = _descriptor.Descriptor(
  name='AddBookResponse',
  full_name='AddBookResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='book', full_name='AddBookResponse.book', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=340,
  serialized_end=378,
)

_BOOK.fields_by_name['genre'].enum_type = _BOOKGENRE
_GETBOOKRESPONSE.fields_by_name['book'].message_type = _BOOK
_UPDATEBOOKCOUNTRESPONSE.fields_by_name['book'].message_type = _BOOK
_ADDBOOKREQUEST.fields_by_name['genre'].enum_type = _BOOKGENRE
_ADDBOOKRESPONSE.fields_by_name['book'].message_type = _BOOK
DESCRIPTOR.message_types_by_name['Book'] = _BOOK
DESCRIPTOR.message_types_by_name['GetBookRequest'] = _GETBOOKREQUEST
DESCRIPTOR.message_types_by_name['GetBookResponse'] = _GETBOOKRESPONSE
DESCRIPTOR.message_types_by_name['UpdateBookCountRequest'] = _UPDATEBOOKCOUNTREQUEST
DESCRIPTOR.message_types_by_name['UpdateBookCountResponse'] = _UPDATEBOOKCOUNTRESPONSE
DESCRIPTOR.message_types_by_name['AddBookRequest'] = _ADDBOOKREQUEST
DESCRIPTOR.message_types_by_name['AddBookResponse'] = _ADDBOOKRESPONSE
DESCRIPTOR.enum_types_by_name['BookGenre'] = _BOOKGENRE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Book = _reflection.GeneratedProtocolMessageType('Book', (_message.Message,), {
  'DESCRIPTOR' : _BOOK,
  '__module__' : 'book_pb2'
  # @@protoc_insertion_point(class_scope:Book)
  })
_sym_db.RegisterMessage(Book)

GetBookRequest = _reflection.GeneratedProtocolMessageType('GetBookRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETBOOKREQUEST,
  '__module__' : 'book_pb2'
  # @@protoc_insertion_point(class_scope:GetBookRequest)
  })
_sym_db.RegisterMessage(GetBookRequest)

GetBookResponse = _reflection.GeneratedProtocolMessageType('GetBookResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETBOOKRESPONSE,
  '__module__' : 'book_pb2'
  # @@protoc_insertion_point(class_scope:GetBookResponse)
  })
_sym_db.RegisterMessage(GetBookResponse)

UpdateBookCountRequest = _reflection.GeneratedProtocolMessageType('UpdateBookCountRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEBOOKCOUNTREQUEST,
  '__module__' : 'book_pb2'
  # @@protoc_insertion_point(class_scope:UpdateBookCountRequest)
  })
_sym_db.RegisterMessage(UpdateBookCountRequest)

UpdateBookCountResponse = _reflection.GeneratedProtocolMessageType('UpdateBookCountResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEBOOKCOUNTRESPONSE,
  '__module__' : 'book_pb2'
  # @@protoc_insertion_point(class_scope:UpdateBookCountResponse)
  })
_sym_db.RegisterMessage(UpdateBookCountResponse)

AddBookRequest = _reflection.GeneratedProtocolMessageType('AddBookRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDBOOKREQUEST,
  '__module__' : 'book_pb2'
  # @@protoc_insertion_point(class_scope:AddBookRequest)
  })
_sym_db.RegisterMessage(AddBookRequest)

AddBookResponse = _reflection.GeneratedProtocolMessageType('AddBookResponse', (_message.Message,), {
  'DESCRIPTOR' : _ADDBOOKRESPONSE,
  '__module__' : 'book_pb2'
  # @@protoc_insertion_point(class_scope:AddBookResponse)
  })
_sym_db.RegisterMessage(AddBookResponse)



_BOOKSERVICE = _descriptor.ServiceDescriptor(
  name='BookService',
  full_name='BookService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=448,
  serialized_end=629,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetBook',
    full_name='BookService.GetBook',
    index=0,
    containing_service=None,
    input_type=_GETBOOKREQUEST,
    output_type=_GETBOOKRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateBookCount',
    full_name='BookService.UpdateBookCount',
    index=1,
    containing_service=None,
    input_type=_UPDATEBOOKCOUNTREQUEST,
    output_type=_UPDATEBOOKCOUNTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='AddBook',
    full_name='BookService.AddBook',
    index=2,
    containing_service=None,
    input_type=_ADDBOOKREQUEST,
    output_type=_ADDBOOKRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_BOOKSERVICE)

DESCRIPTOR.services_by_name['BookService'] = _BOOKSERVICE

# @@protoc_insertion_point(module_scope)
