# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/lib/tenseal/vector.proto

# third party
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


# syft absolute
from syft.proto.core.common import (
    common_object_pb2 as proto_dot_core_dot_common_dot_common__object__pb2,
)

DESCRIPTOR = _descriptor.FileDescriptor(
    name="proto/lib/tenseal/vector.proto",
    package="syft.lib.tenseal",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x1eproto/lib/tenseal/vector.proto\x12\x10syft.lib.tenseal\x1a%proto/core/common/common_object.proto"e\n\rTenSEALVector\x12!\n\x02id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12\x10\n\x08obj_type\x18\x02 \x01(\t\x12\x0f\n\x07\x63ontext\x18\x03 \x01(\x0c\x12\x0e\n\x06vector\x18\x04 \x01(\x0c\x62\x06proto3',
    dependencies=[
        proto_dot_core_dot_common_dot_common__object__pb2.DESCRIPTOR,
    ],
)


_TENSEALVECTOR = _descriptor.Descriptor(
    name="TenSEALVector",
    full_name="syft.lib.tenseal.TenSEALVector",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="syft.lib.tenseal.TenSEALVector.id",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="obj_type",
            full_name="syft.lib.tenseal.TenSEALVector.obj_type",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="context",
            full_name="syft.lib.tenseal.TenSEALVector.context",
            index=2,
            number=3,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="vector",
            full_name="syft.lib.tenseal.TenSEALVector.vector",
            index=3,
            number=4,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=91,
    serialized_end=192,
)

_TENSEALVECTOR.fields_by_name[
    "id"
].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
DESCRIPTOR.message_types_by_name["TenSEALVector"] = _TENSEALVECTOR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TenSEALVector = _reflection.GeneratedProtocolMessageType(
    "TenSEALVector",
    (_message.Message,),
    {
        "DESCRIPTOR": _TENSEALVECTOR,
        "__module__": "proto.lib.tenseal.vector_pb2"
        # @@protoc_insertion_point(class_scope:syft.lib.tenseal.TenSEALVector)
    },
)
_sym_db.RegisterMessage(TenSEALVector)


# @@protoc_insertion_point(module_scope)
