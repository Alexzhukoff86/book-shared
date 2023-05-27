# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: account.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='account.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\raccount.proto\x1a\x1bgoogle/protobuf/empty.proto\"2\n\x07\x41\x63\x63ount\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\"\x1f\n\x11GetAccountRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"/\n\x12GetAccountResponse\x12\x19\n\x07\x61\x63\x63ount\x18\x01 \x01(\x0b\x32\x08.Account\"3\n\x14\x43reateAccountRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\"#\n\x15\x43reateAccountResponse\x12\n\n\x02id\x18\x01 \x01(\x05\"4\n\x16GetAccountListResponse\x12\x1a\n\x08\x61\x63\x63ounts\x18\x01 \x03(\x0b\x32\x08.Account2\xd0\x01\n\x0e\x41\x63\x63ountService\x12\x43\n\x0eGetAccountList\x12\x16.google.protobuf.Empty\x1a\x17.GetAccountListResponse\"\x00\x12\x37\n\nGetAccount\x12\x12.GetAccountRequest\x1a\x13.GetAccountResponse\"\x00\x12@\n\rCreateAccount\x12\x15.CreateAccountRequest\x1a\x16.CreateAccountResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_ACCOUNT = _descriptor.Descriptor(
  name='Account',
  full_name='Account',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Account.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='Account.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='email', full_name='Account.email', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=46,
  serialized_end=96,
)


_GETACCOUNTREQUEST = _descriptor.Descriptor(
  name='GetAccountRequest',
  full_name='GetAccountRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='GetAccountRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=98,
  serialized_end=129,
)


_GETACCOUNTRESPONSE = _descriptor.Descriptor(
  name='GetAccountResponse',
  full_name='GetAccountResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='account', full_name='GetAccountResponse.account', index=0,
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
  serialized_start=131,
  serialized_end=178,
)


_CREATEACCOUNTREQUEST = _descriptor.Descriptor(
  name='CreateAccountRequest',
  full_name='CreateAccountRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='CreateAccountRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='email', full_name='CreateAccountRequest.email', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=180,
  serialized_end=231,
)


_CREATEACCOUNTRESPONSE = _descriptor.Descriptor(
  name='CreateAccountResponse',
  full_name='CreateAccountResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='CreateAccountResponse.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=233,
  serialized_end=268,
)


_GETACCOUNTLISTRESPONSE = _descriptor.Descriptor(
  name='GetAccountListResponse',
  full_name='GetAccountListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='accounts', full_name='GetAccountListResponse.accounts', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=270,
  serialized_end=322,
)

_GETACCOUNTRESPONSE.fields_by_name['account'].message_type = _ACCOUNT
_GETACCOUNTLISTRESPONSE.fields_by_name['accounts'].message_type = _ACCOUNT
DESCRIPTOR.message_types_by_name['Account'] = _ACCOUNT
DESCRIPTOR.message_types_by_name['GetAccountRequest'] = _GETACCOUNTREQUEST
DESCRIPTOR.message_types_by_name['GetAccountResponse'] = _GETACCOUNTRESPONSE
DESCRIPTOR.message_types_by_name['CreateAccountRequest'] = _CREATEACCOUNTREQUEST
DESCRIPTOR.message_types_by_name['CreateAccountResponse'] = _CREATEACCOUNTRESPONSE
DESCRIPTOR.message_types_by_name['GetAccountListResponse'] = _GETACCOUNTLISTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Account = _reflection.GeneratedProtocolMessageType('Account', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNT,
  '__module__' : 'account_pb2'
  # @@protoc_insertion_point(class_scope:Account)
  })
_sym_db.RegisterMessage(Account)

GetAccountRequest = _reflection.GeneratedProtocolMessageType('GetAccountRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETACCOUNTREQUEST,
  '__module__' : 'account_pb2'
  # @@protoc_insertion_point(class_scope:GetAccountRequest)
  })
_sym_db.RegisterMessage(GetAccountRequest)

GetAccountResponse = _reflection.GeneratedProtocolMessageType('GetAccountResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETACCOUNTRESPONSE,
  '__module__' : 'account_pb2'
  # @@protoc_insertion_point(class_scope:GetAccountResponse)
  })
_sym_db.RegisterMessage(GetAccountResponse)

CreateAccountRequest = _reflection.GeneratedProtocolMessageType('CreateAccountRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEACCOUNTREQUEST,
  '__module__' : 'account_pb2'
  # @@protoc_insertion_point(class_scope:CreateAccountRequest)
  })
_sym_db.RegisterMessage(CreateAccountRequest)

CreateAccountResponse = _reflection.GeneratedProtocolMessageType('CreateAccountResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEACCOUNTRESPONSE,
  '__module__' : 'account_pb2'
  # @@protoc_insertion_point(class_scope:CreateAccountResponse)
  })
_sym_db.RegisterMessage(CreateAccountResponse)

GetAccountListResponse = _reflection.GeneratedProtocolMessageType('GetAccountListResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETACCOUNTLISTRESPONSE,
  '__module__' : 'account_pb2'
  # @@protoc_insertion_point(class_scope:GetAccountListResponse)
  })
_sym_db.RegisterMessage(GetAccountListResponse)



_ACCOUNTSERVICE = _descriptor.ServiceDescriptor(
  name='AccountService',
  full_name='AccountService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=325,
  serialized_end=533,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetAccountList',
    full_name='AccountService.GetAccountList',
    index=0,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_GETACCOUNTLISTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetAccount',
    full_name='AccountService.GetAccount',
    index=1,
    containing_service=None,
    input_type=_GETACCOUNTREQUEST,
    output_type=_GETACCOUNTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CreateAccount',
    full_name='AccountService.CreateAccount',
    index=2,
    containing_service=None,
    input_type=_CREATEACCOUNTREQUEST,
    output_type=_CREATEACCOUNTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ACCOUNTSERVICE)

DESCRIPTOR.services_by_name['AccountService'] = _ACCOUNTSERVICE

# @@protoc_insertion_point(module_scope)
