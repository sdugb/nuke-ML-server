# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='message.proto',
  package='dlserver',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\rmessage.proto\x12\x08\x64lserver\"i\n\x0eRequestWrapper\x12\x0c\n\x04info\x18\x01 \x01(\x08\x12!\n\x02r1\x18\x02 \x01(\x0b\x32\x15.dlserver.RequestInfo\x12&\n\x02r2\x18\x03 \x01(\x0b\x32\x1a.dlserver.RequestInference\"\x89\x01\n\x0eRespondWrapper\x12\x0c\n\x04info\x18\x01 \x01(\x08\x12!\n\x02r1\x18\x02 \x01(\x0b\x32\x15.dlserver.RespondInfo\x12&\n\x02r2\x18\x03 \x01(\x0b\x32\x1a.dlserver.RespondInference\x12\x1e\n\x05\x65rror\x18\x04 \x01(\x0b\x32\x0f.dlserver.Error\"\x1b\n\x0bRequestInfo\x12\x0c\n\x04info\x18\x01 \x01(\x08\"B\n\x0bRespondInfo\x12\x12\n\nnum_models\x18\x01 \x01(\x05\x12\x1f\n\x06models\x18\x02 \x03(\x0b\x32\x0f.dlserver.Model\"\x8f\x03\n\x05Model\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t\x12(\n\x06inputs\x18\x03 \x03(\x0b\x32\x18.dlserver.ImagePrototype\x12)\n\x07outputs\x18\x04 \x03(\x0b\x32\x18.dlserver.ImagePrototype\x12*\n\x0c\x62ool_options\x18\x05 \x03(\x0b\x32\x14.dlserver.BoolAttrib\x12(\n\x0bint_options\x18\x06 \x03(\x0b\x32\x13.dlserver.IntAttrib\x12,\n\rfloat_options\x18\x07 \x03(\x0b\x32\x15.dlserver.FloatAttrib\x12.\n\x0estring_options\x18\x08 \x03(\x0b\x32\x16.dlserver.StringAttrib\x12,\n\x0e\x62utton_options\x18\t \x03(\x0b\x32\x14.dlserver.BoolAttrib\x12\x32\n\nmc_options\x18\n \x03(\x0b\x32\x1e.dlserver.MultipleChoiceOption\"D\n\x14MultipleChoiceOption\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\x0f\n\x07\x63hoices\x18\x03 \x03(\t\"0\n\x0eImagePrototype\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08\x63hannels\x18\x02 \x01(\x05\"\x14\n\x05\x45rror\x12\x0b\n\x03msg\x18\x01 \x01(\t\"S\n\x10RequestInference\x12\x1e\n\x05model\x18\x01 \x01(\x0b\x32\x0f.dlserver.Model\x12\x1f\n\x06images\x18\x02 \x03(\x0b\x32\x0f.dlserver.Image\"\x8d\x01\n\x10RespondInference\x12\x12\n\nnum_images\x18\x01 \x01(\x05\x12\x1f\n\x06images\x18\x02 \x03(\x0b\x32\x0f.dlserver.Image\x12\x13\n\x0bnum_objects\x18\x03 \x01(\x05\x12/\n\x07objects\x18\x04 \x03(\x0b\x32\x1e.dlserver.FieldValuePairAttrib\"G\n\x05Image\x12\r\n\x05width\x18\x01 \x01(\x05\x12\x0e\n\x06height\x18\x02 \x01(\x05\x12\x10\n\x08\x63hannels\x18\x03 \x01(\x05\x12\r\n\x05image\x18\x04 \x01(\x0c\".\n\nBoolAttrib\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\x06values\x18\x02 \x03(\x08\x42\x02\x10\x01\"-\n\tIntAttrib\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\x06values\x18\x02 \x03(\x05\x42\x02\x10\x01\"/\n\x0b\x46loatAttrib\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\x06values\x18\x02 \x03(\x02\x42\x02\x10\x01\",\n\x0cStringAttrib\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06values\x18\x02 \x03(\t\"N\n\x14\x46ieldValuePairAttrib\x12\x0c\n\x04name\x18\x01 \x01(\t\x12(\n\x06values\x18\x02 \x03(\x0b\x32\x18.dlserver.FieldValuePair\"\xd3\x01\n\x0e\x46ieldValuePair\x12+\n\x0eint_attributes\x18\x01 \x03(\x0b\x32\x13.dlserver.IntAttrib\x12/\n\x10\x66loat_attributes\x18\x02 \x03(\x0b\x32\x15.dlserver.FloatAttrib\x12\x31\n\x11string_attributes\x18\x03 \x03(\x0b\x32\x16.dlserver.StringAttrib\x12\x30\n\x08\x63hildren\x18\x04 \x03(\x0b\x32\x1e.dlserver.FieldValuePairAttrib')
)




_REQUESTWRAPPER = _descriptor.Descriptor(
  name='RequestWrapper',
  full_name='dlserver.RequestWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='info', full_name='dlserver.RequestWrapper.info', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='r1', full_name='dlserver.RequestWrapper.r1', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='r2', full_name='dlserver.RequestWrapper.r2', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=27,
  serialized_end=132,
)


_RESPONDWRAPPER = _descriptor.Descriptor(
  name='RespondWrapper',
  full_name='dlserver.RespondWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='info', full_name='dlserver.RespondWrapper.info', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='r1', full_name='dlserver.RespondWrapper.r1', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='r2', full_name='dlserver.RespondWrapper.r2', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='dlserver.RespondWrapper.error', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=135,
  serialized_end=272,
)


_REQUESTINFO = _descriptor.Descriptor(
  name='RequestInfo',
  full_name='dlserver.RequestInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='info', full_name='dlserver.RequestInfo.info', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=274,
  serialized_end=301,
)


_RESPONDINFO = _descriptor.Descriptor(
  name='RespondInfo',
  full_name='dlserver.RespondInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_models', full_name='dlserver.RespondInfo.num_models', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='models', full_name='dlserver.RespondInfo.models', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=303,
  serialized_end=369,
)


_MODEL = _descriptor.Descriptor(
  name='Model',
  full_name='dlserver.Model',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='dlserver.Model.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='label', full_name='dlserver.Model.label', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inputs', full_name='dlserver.Model.inputs', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='outputs', full_name='dlserver.Model.outputs', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bool_options', full_name='dlserver.Model.bool_options', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='int_options', full_name='dlserver.Model.int_options', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='float_options', full_name='dlserver.Model.float_options', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='string_options', full_name='dlserver.Model.string_options', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='button_options', full_name='dlserver.Model.button_options', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mc_options', full_name='dlserver.Model.mc_options', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=372,
  serialized_end=771,
)


_MULTIPLECHOICEOPTION = _descriptor.Descriptor(
  name='MultipleChoiceOption',
  full_name='dlserver.MultipleChoiceOption',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='dlserver.MultipleChoiceOption.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='dlserver.MultipleChoiceOption.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='choices', full_name='dlserver.MultipleChoiceOption.choices', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=773,
  serialized_end=841,
)


_IMAGEPROTOTYPE = _descriptor.Descriptor(
  name='ImagePrototype',
  full_name='dlserver.ImagePrototype',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='dlserver.ImagePrototype.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='channels', full_name='dlserver.ImagePrototype.channels', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=843,
  serialized_end=891,
)


_ERROR = _descriptor.Descriptor(
  name='Error',
  full_name='dlserver.Error',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg', full_name='dlserver.Error.msg', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=893,
  serialized_end=913,
)


_REQUESTINFERENCE = _descriptor.Descriptor(
  name='RequestInference',
  full_name='dlserver.RequestInference',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='model', full_name='dlserver.RequestInference.model', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='images', full_name='dlserver.RequestInference.images', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=915,
  serialized_end=998,
)


_RESPONDINFERENCE = _descriptor.Descriptor(
  name='RespondInference',
  full_name='dlserver.RespondInference',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_images', full_name='dlserver.RespondInference.num_images', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='images', full_name='dlserver.RespondInference.images', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_objects', full_name='dlserver.RespondInference.num_objects', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='objects', full_name='dlserver.RespondInference.objects', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1001,
  serialized_end=1142,
)


_IMAGE = _descriptor.Descriptor(
  name='Image',
  full_name='dlserver.Image',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='width', full_name='dlserver.Image.width', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='dlserver.Image.height', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='channels', full_name='dlserver.Image.channels', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='image', full_name='dlserver.Image.image', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1144,
  serialized_end=1215,
)


_BOOLATTRIB = _descriptor.Descriptor(
  name='BoolAttrib',
  full_name='dlserver.BoolAttrib',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='dlserver.BoolAttrib.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='values', full_name='dlserver.BoolAttrib.values', index=1,
      number=2, type=8, cpp_type=7, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1217,
  serialized_end=1263,
)


_INTATTRIB = _descriptor.Descriptor(
  name='IntAttrib',
  full_name='dlserver.IntAttrib',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='dlserver.IntAttrib.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='values', full_name='dlserver.IntAttrib.values', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1265,
  serialized_end=1310,
)


_FLOATATTRIB = _descriptor.Descriptor(
  name='FloatAttrib',
  full_name='dlserver.FloatAttrib',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='dlserver.FloatAttrib.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='values', full_name='dlserver.FloatAttrib.values', index=1,
      number=2, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1312,
  serialized_end=1359,
)


_STRINGATTRIB = _descriptor.Descriptor(
  name='StringAttrib',
  full_name='dlserver.StringAttrib',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='dlserver.StringAttrib.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='values', full_name='dlserver.StringAttrib.values', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1361,
  serialized_end=1405,
)


_FIELDVALUEPAIRATTRIB = _descriptor.Descriptor(
  name='FieldValuePairAttrib',
  full_name='dlserver.FieldValuePairAttrib',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='dlserver.FieldValuePairAttrib.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='values', full_name='dlserver.FieldValuePairAttrib.values', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1407,
  serialized_end=1485,
)


_FIELDVALUEPAIR = _descriptor.Descriptor(
  name='FieldValuePair',
  full_name='dlserver.FieldValuePair',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='int_attributes', full_name='dlserver.FieldValuePair.int_attributes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='float_attributes', full_name='dlserver.FieldValuePair.float_attributes', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='string_attributes', full_name='dlserver.FieldValuePair.string_attributes', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='children', full_name='dlserver.FieldValuePair.children', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1488,
  serialized_end=1699,
)

_REQUESTWRAPPER.fields_by_name['r1'].message_type = _REQUESTINFO
_REQUESTWRAPPER.fields_by_name['r2'].message_type = _REQUESTINFERENCE
_RESPONDWRAPPER.fields_by_name['r1'].message_type = _RESPONDINFO
_RESPONDWRAPPER.fields_by_name['r2'].message_type = _RESPONDINFERENCE
_RESPONDWRAPPER.fields_by_name['error'].message_type = _ERROR
_RESPONDINFO.fields_by_name['models'].message_type = _MODEL
_MODEL.fields_by_name['inputs'].message_type = _IMAGEPROTOTYPE
_MODEL.fields_by_name['outputs'].message_type = _IMAGEPROTOTYPE
_MODEL.fields_by_name['bool_options'].message_type = _BOOLATTRIB
_MODEL.fields_by_name['int_options'].message_type = _INTATTRIB
_MODEL.fields_by_name['float_options'].message_type = _FLOATATTRIB
_MODEL.fields_by_name['string_options'].message_type = _STRINGATTRIB
_MODEL.fields_by_name['button_options'].message_type = _BOOLATTRIB
_MODEL.fields_by_name['mc_options'].message_type = _MULTIPLECHOICEOPTION
_REQUESTINFERENCE.fields_by_name['model'].message_type = _MODEL
_REQUESTINFERENCE.fields_by_name['images'].message_type = _IMAGE
_RESPONDINFERENCE.fields_by_name['images'].message_type = _IMAGE
_RESPONDINFERENCE.fields_by_name['objects'].message_type = _FIELDVALUEPAIRATTRIB
_FIELDVALUEPAIRATTRIB.fields_by_name['values'].message_type = _FIELDVALUEPAIR
_FIELDVALUEPAIR.fields_by_name['int_attributes'].message_type = _INTATTRIB
_FIELDVALUEPAIR.fields_by_name['float_attributes'].message_type = _FLOATATTRIB
_FIELDVALUEPAIR.fields_by_name['string_attributes'].message_type = _STRINGATTRIB
_FIELDVALUEPAIR.fields_by_name['children'].message_type = _FIELDVALUEPAIRATTRIB
DESCRIPTOR.message_types_by_name['RequestWrapper'] = _REQUESTWRAPPER
DESCRIPTOR.message_types_by_name['RespondWrapper'] = _RESPONDWRAPPER
DESCRIPTOR.message_types_by_name['RequestInfo'] = _REQUESTINFO
DESCRIPTOR.message_types_by_name['RespondInfo'] = _RESPONDINFO
DESCRIPTOR.message_types_by_name['Model'] = _MODEL
DESCRIPTOR.message_types_by_name['MultipleChoiceOption'] = _MULTIPLECHOICEOPTION
DESCRIPTOR.message_types_by_name['ImagePrototype'] = _IMAGEPROTOTYPE
DESCRIPTOR.message_types_by_name['Error'] = _ERROR
DESCRIPTOR.message_types_by_name['RequestInference'] = _REQUESTINFERENCE
DESCRIPTOR.message_types_by_name['RespondInference'] = _RESPONDINFERENCE
DESCRIPTOR.message_types_by_name['Image'] = _IMAGE
DESCRIPTOR.message_types_by_name['BoolAttrib'] = _BOOLATTRIB
DESCRIPTOR.message_types_by_name['IntAttrib'] = _INTATTRIB
DESCRIPTOR.message_types_by_name['FloatAttrib'] = _FLOATATTRIB
DESCRIPTOR.message_types_by_name['StringAttrib'] = _STRINGATTRIB
DESCRIPTOR.message_types_by_name['FieldValuePairAttrib'] = _FIELDVALUEPAIRATTRIB
DESCRIPTOR.message_types_by_name['FieldValuePair'] = _FIELDVALUEPAIR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RequestWrapper = _reflection.GeneratedProtocolMessageType('RequestWrapper', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTWRAPPER,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:dlserver.RequestWrapper)
  ))
_sym_db.RegisterMessage(RequestWrapper)

RespondWrapper = _reflection.GeneratedProtocolMessageType('RespondWrapper', (_message.Message,), dict(
  DESCRIPTOR = _RESPONDWRAPPER,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:dlserver.RespondWrapper)
  ))
_sym_db.RegisterMessage(RespondWrapper)

RequestInfo = _reflection.GeneratedProtocolMessageType('RequestInfo', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTINFO,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:dlserver.RequestInfo)
  ))
_sym_db.RegisterMessage(RequestInfo)

RespondInfo = _reflection.GeneratedProtocolMessageType('RespondInfo', (_message.Message,), dict(
  DESCRIPTOR = _RESPONDINFO,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:dlserver.RespondInfo)
  ))
_sym_db.RegisterMessage(RespondInfo)

Model = _reflection.GeneratedProtocolMessageType('Model', (_message.Message,), dict(
  DESCRIPTOR = _MODEL,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:dlserver.Model)
  ))
_sym_db.RegisterMessage(Model)

MultipleChoiceOption = _reflection.GeneratedProtocolMessageType('MultipleChoiceOption', (_message.Message,), dict(
  DESCRIPTOR = _MULTIPLECHOICEOPTION,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:dlserver.MultipleChoiceOption)
  ))
_sym_db.RegisterMessage(MultipleChoiceOption)

ImagePrototype = _reflection.GeneratedProtocolMessageType('ImagePrototype', (_message.Message,), dict(
  DESCRIPTOR = _IMAGEPROTOTYPE,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:dlserver.ImagePrototype)
  ))
_sym_db.RegisterMessage(ImagePrototype)

Error = _reflection.GeneratedProtocolMessageType('Error', (_message.Message,), dict(
  DESCRIPTOR = _ERROR,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:dlserver.Error)
  ))
_sym_db.RegisterMessage(Error)

RequestInference = _reflection.GeneratedProtocolMessageType('RequestInference', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTINFERENCE,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:dlserver.RequestInference)
  ))
_sym_db.RegisterMessage(RequestInference)

RespondInference = _reflection.GeneratedProtocolMessageType('RespondInference', (_message.Message,), dict(
  DESCRIPTOR = _RESPONDINFERENCE,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:dlserver.RespondInference)
  ))
_sym_db.RegisterMessage(RespondInference)

Image = _reflection.GeneratedProtocolMessageType('Image', (_message.Message,), dict(
  DESCRIPTOR = _IMAGE,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:dlserver.Image)
  ))
_sym_db.RegisterMessage(Image)

BoolAttrib = _reflection.GeneratedProtocolMessageType('BoolAttrib', (_message.Message,), dict(
  DESCRIPTOR = _BOOLATTRIB,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:dlserver.BoolAttrib)
  ))
_sym_db.RegisterMessage(BoolAttrib)

IntAttrib = _reflection.GeneratedProtocolMessageType('IntAttrib', (_message.Message,), dict(
  DESCRIPTOR = _INTATTRIB,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:dlserver.IntAttrib)
  ))
_sym_db.RegisterMessage(IntAttrib)

FloatAttrib = _reflection.GeneratedProtocolMessageType('FloatAttrib', (_message.Message,), dict(
  DESCRIPTOR = _FLOATATTRIB,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:dlserver.FloatAttrib)
  ))
_sym_db.RegisterMessage(FloatAttrib)

StringAttrib = _reflection.GeneratedProtocolMessageType('StringAttrib', (_message.Message,), dict(
  DESCRIPTOR = _STRINGATTRIB,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:dlserver.StringAttrib)
  ))
_sym_db.RegisterMessage(StringAttrib)

FieldValuePairAttrib = _reflection.GeneratedProtocolMessageType('FieldValuePairAttrib', (_message.Message,), dict(
  DESCRIPTOR = _FIELDVALUEPAIRATTRIB,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:dlserver.FieldValuePairAttrib)
  ))
_sym_db.RegisterMessage(FieldValuePairAttrib)

FieldValuePair = _reflection.GeneratedProtocolMessageType('FieldValuePair', (_message.Message,), dict(
  DESCRIPTOR = _FIELDVALUEPAIR,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:dlserver.FieldValuePair)
  ))
_sym_db.RegisterMessage(FieldValuePair)


_BOOLATTRIB.fields_by_name['values']._options = None
_INTATTRIB.fields_by_name['values']._options = None
_FLOATATTRIB.fields_by_name['values']._options = None
# @@protoc_insertion_point(module_scope)
