# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import vector3d_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='road.proto',
  package='gazebo.msgs',
  serialized_pb='\n\nroad.proto\x12\x0bgazebo.msgs\x1a\x0evector3d.proto\"I\n\x04Road\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\r\n\x05width\x18\x02 \x02(\x01\x12$\n\x05point\x18\x03 \x03(\x0b\x32\x15.gazebo.msgs.Vector3d')




_ROAD = descriptor.Descriptor(
  name='Road',
  full_name='gazebo.msgs.Road',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='gazebo.msgs.Road.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='width', full_name='gazebo.msgs.Road.width', index=1,
      number=2, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='point', full_name='gazebo.msgs.Road.point', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=43,
  serialized_end=116,
)

_ROAD.fields_by_name['point'].message_type = vector3d_pb2._VECTOR3D
DESCRIPTOR.message_types_by_name['Road'] = _ROAD

class Road(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ROAD
  
  # @@protoc_insertion_point(class_scope:gazebo.msgs.Road)

# @@protoc_insertion_point(module_scope)