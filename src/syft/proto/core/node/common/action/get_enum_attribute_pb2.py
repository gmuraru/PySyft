# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/core/node/common/action/get_enum_attribute.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from syft.proto.core.common import (
    common_object_pb2 as proto_dot_core_dot_common_dot_common__object__pb2,
)
from syft.proto.core.io import address_pb2 as proto_dot_core_dot_io_dot_address__pb2
from syft.proto.core.pointer import (
    pointer_pb2 as proto_dot_core_dot_pointer_dot_pointer__pb2,
)


DESCRIPTOR = _descriptor.FileDescriptor(
    name="proto/core/node/common/action/get_enum_attribute.proto",
    package="syft.core.node.common.action",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n6proto/core/node/common/action/get_enum_attribute.proto\x12\x1csyft.core.node.common.action\x1a%proto/core/common/common_object.proto\x1a\x1bproto/core/io/address.proto\x1a proto/core/pointer/pointer.proto"\xa4\x01\n\x16GetEnumAttributeAction\x12\x0c\n\x04path\x18\x01 \x01(\t\x12-\n\x0eid_at_location\x18\x02 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x03 \x01(\x0b\x32\x15.syft.core.io.Address\x12%\n\x06msg_id\x18\x04 \x01(\x0b\x32\x15.syft.core.common.UIDb\x06proto3',
    dependencies=[
        proto_dot_core_dot_common_dot_common__object__pb2.DESCRIPTOR,
        proto_dot_core_dot_io_dot_address__pb2.DESCRIPTOR,
        proto_dot_core_dot_pointer_dot_pointer__pb2.DESCRIPTOR,
    ],
)


_GETENUMATTRIBUTEACTION = _descriptor.Descriptor(
    name="GetEnumAttributeAction",
    full_name="syft.core.node.common.action.GetEnumAttributeAction",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="path",
            full_name="syft.core.node.common.action.GetEnumAttributeAction.path",
            index=0,
            number=1,
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
            name="id_at_location",
            full_name="syft.core.node.common.action.GetEnumAttributeAction.id_at_location",
            index=1,
            number=2,
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
            name="address",
            full_name="syft.core.node.common.action.GetEnumAttributeAction.address",
            index=2,
            number=3,
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
            name="msg_id",
            full_name="syft.core.node.common.action.GetEnumAttributeAction.msg_id",
            index=3,
            number=4,
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=191,
    serialized_end=355,
)

_GETENUMATTRIBUTEACTION.fields_by_name[
    "id_at_location"
].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
_GETENUMATTRIBUTEACTION.fields_by_name[
    "address"
].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
_GETENUMATTRIBUTEACTION.fields_by_name[
    "msg_id"
].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
DESCRIPTOR.message_types_by_name["GetEnumAttributeAction"] = _GETENUMATTRIBUTEACTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetEnumAttributeAction = _reflection.GeneratedProtocolMessageType(
    "GetEnumAttributeAction",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETENUMATTRIBUTEACTION,
        "__module__": "proto.core.node.common.action.get_enum_attribute_pb2"
        # @@protoc_insertion_point(class_scope:syft.core.node.common.action.GetEnumAttributeAction)
    },
)
_sym_db.RegisterMessage(GetEnumAttributeAction)


# @@protoc_insertion_point(module_scope)
