# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: osm.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='osm.proto',
  package='osm',
  syntax='proto3',
  serialized_options=b'Z(github.com/aicdev/osm_poly_harvester/osm',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\tosm.proto\x12\x03osm\"\x93\x01\n\tNominatim\x12\x0c\n\x04type\x18\x01 \x01(\t\x12,\n\nproperties\x18\x02 \x01(\x0b\x32\x18.osm.NominatimProperties\x12 \n\x04\x62\x62ox\x18\x03 \x01(\x0b\x32\x12.osm.NominatimBbox\x12(\n\x08geometry\x18\x04 \x03(\x0b\x32\x16.osm.NominatimGeometry\"\x8e\x01\n\x13NominatimProperties\x12\x0f\n\x07placeId\x18\x01 \x01(\x03\x12\r\n\x05osmId\x18\x02 \x01(\x05\x12\x13\n\x0b\x64isplayName\x18\x03 \x01(\t\x12\x11\n\tplaceRank\x18\x04 \x01(\x05\x12\x10\n\x08\x63\x61tegory\x18\x05 \x01(\t\x12\x0c\n\x04type\x18\x06 \x01(\t\x12\x0f\n\x07osmType\x18\x07 \x01(\t\"\x1e\n\rNominatimBbox\x12\r\n\x05\x65ntry\x18\x01 \x03(\x02\"Q\n\x11NominatimGeometry\x12\x0c\n\x04type\x18\x01 \x01(\t\x12.\n\x0b\x63oordinates\x18\x02 \x03(\x0b\x32\x19.osm.NominatimCoordinates\"0\n\x14NominatimCoordinates\x12\x0b\n\x03lat\x18\x01 \x01(\x02\x12\x0b\n\x03lon\x18\x02 \x01(\x02\x42*Z(github.com/aicdev/osm_poly_harvester/osmb\x06proto3'
)




_NOMINATIM = _descriptor.Descriptor(
  name='Nominatim',
  full_name='osm.Nominatim',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='osm.Nominatim.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='properties', full_name='osm.Nominatim.properties', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bbox', full_name='osm.Nominatim.bbox', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='geometry', full_name='osm.Nominatim.geometry', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=19,
  serialized_end=166,
)


_NOMINATIMPROPERTIES = _descriptor.Descriptor(
  name='NominatimProperties',
  full_name='osm.NominatimProperties',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='placeId', full_name='osm.NominatimProperties.placeId', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='osmId', full_name='osm.NominatimProperties.osmId', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='displayName', full_name='osm.NominatimProperties.displayName', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='placeRank', full_name='osm.NominatimProperties.placeRank', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='category', full_name='osm.NominatimProperties.category', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='osm.NominatimProperties.type', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='osmType', full_name='osm.NominatimProperties.osmType', index=6,
      number=7, type=9, cpp_type=9, label=1,
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
  serialized_start=169,
  serialized_end=311,
)


_NOMINATIMBBOX = _descriptor.Descriptor(
  name='NominatimBbox',
  full_name='osm.NominatimBbox',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='entry', full_name='osm.NominatimBbox.entry', index=0,
      number=1, type=2, cpp_type=6, label=3,
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
  serialized_start=313,
  serialized_end=343,
)


_NOMINATIMGEOMETRY = _descriptor.Descriptor(
  name='NominatimGeometry',
  full_name='osm.NominatimGeometry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='osm.NominatimGeometry.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='coordinates', full_name='osm.NominatimGeometry.coordinates', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=345,
  serialized_end=426,
)


_NOMINATIMCOORDINATES = _descriptor.Descriptor(
  name='NominatimCoordinates',
  full_name='osm.NominatimCoordinates',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='lat', full_name='osm.NominatimCoordinates.lat', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lon', full_name='osm.NominatimCoordinates.lon', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=428,
  serialized_end=476,
)

_NOMINATIM.fields_by_name['properties'].message_type = _NOMINATIMPROPERTIES
_NOMINATIM.fields_by_name['bbox'].message_type = _NOMINATIMBBOX
_NOMINATIM.fields_by_name['geometry'].message_type = _NOMINATIMGEOMETRY
_NOMINATIMGEOMETRY.fields_by_name['coordinates'].message_type = _NOMINATIMCOORDINATES
DESCRIPTOR.message_types_by_name['Nominatim'] = _NOMINATIM
DESCRIPTOR.message_types_by_name['NominatimProperties'] = _NOMINATIMPROPERTIES
DESCRIPTOR.message_types_by_name['NominatimBbox'] = _NOMINATIMBBOX
DESCRIPTOR.message_types_by_name['NominatimGeometry'] = _NOMINATIMGEOMETRY
DESCRIPTOR.message_types_by_name['NominatimCoordinates'] = _NOMINATIMCOORDINATES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Nominatim = _reflection.GeneratedProtocolMessageType('Nominatim', (_message.Message,), {
  'DESCRIPTOR' : _NOMINATIM,
  '__module__' : 'osm_pb2'
  # @@protoc_insertion_point(class_scope:osm.Nominatim)
  })
_sym_db.RegisterMessage(Nominatim)

NominatimProperties = _reflection.GeneratedProtocolMessageType('NominatimProperties', (_message.Message,), {
  'DESCRIPTOR' : _NOMINATIMPROPERTIES,
  '__module__' : 'osm_pb2'
  # @@protoc_insertion_point(class_scope:osm.NominatimProperties)
  })
_sym_db.RegisterMessage(NominatimProperties)

NominatimBbox = _reflection.GeneratedProtocolMessageType('NominatimBbox', (_message.Message,), {
  'DESCRIPTOR' : _NOMINATIMBBOX,
  '__module__' : 'osm_pb2'
  # @@protoc_insertion_point(class_scope:osm.NominatimBbox)
  })
_sym_db.RegisterMessage(NominatimBbox)

NominatimGeometry = _reflection.GeneratedProtocolMessageType('NominatimGeometry', (_message.Message,), {
  'DESCRIPTOR' : _NOMINATIMGEOMETRY,
  '__module__' : 'osm_pb2'
  # @@protoc_insertion_point(class_scope:osm.NominatimGeometry)
  })
_sym_db.RegisterMessage(NominatimGeometry)

NominatimCoordinates = _reflection.GeneratedProtocolMessageType('NominatimCoordinates', (_message.Message,), {
  'DESCRIPTOR' : _NOMINATIMCOORDINATES,
  '__module__' : 'osm_pb2'
  # @@protoc_insertion_point(class_scope:osm.NominatimCoordinates)
  })
_sym_db.RegisterMessage(NominatimCoordinates)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
