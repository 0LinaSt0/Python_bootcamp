# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceships.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10spaceships.proto\">\n\x07Officer\x12\x12\n\nfirst_name\x18\x01 \x01(\t\x12\x11\n\tlast_name\x18\x02 \x01(\t\x12\x0c\n\x04rank\x18\x03 \x01(\t\"\'\n\x10SpaceshipRequest\x12\x13\n\x0b\x63oordinates\x18\x01 \x01(\t\"\x89\x02\n\tSpaceship\x12\"\n\talignment\x18\x01 \x01(\x0e\x32\n.AlignmentH\x00\x88\x01\x01\x12\x11\n\x04name\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x1f\n\nship_class\x18\x04 \x01(\x0e\x32\x06.ClassH\x02\x88\x01\x01\x12\x13\n\x06length\x18\x03 \x01(\x02H\x03\x88\x01\x01\x12\x16\n\tcrew_size\x18\x05 \x01(\x05H\x04\x88\x01\x01\x12\x12\n\x05\x61rmed\x18\x06 \x01(\x08H\x05\x88\x01\x01\x12\x1a\n\x08officers\x18\x07 \x03(\x0b\x32\x08.OfficerB\x0c\n\n_alignmentB\x07\n\x05_nameB\r\n\x0b_ship_classB\t\n\x07_lengthB\x0c\n\n_crew_sizeB\x08\n\x06_armed\"6\n\x11SpaceshipResponse\x12!\n\rrespons_ships\x18\x01 \x01(\x0b\x32\n.Spaceship* \n\tAlignment\x12\x08\n\x04\x41lly\x10\x00\x12\t\n\x05\x45nemy\x10\x01*W\n\x05\x43lass\x12\x0c\n\x08\x43orvette\x10\x00\x12\x0b\n\x07\x46rigate\x10\x01\x12\x0b\n\x07\x43ruiser\x10\x02\x12\x0c\n\x08\x44\x65stroye\x10\x03\x12\x0b\n\x07\x43\x61rrier\x10\x04\x12\x0b\n\x07\x44readno\x10\x05\x32\x46\n\nSpaceships\x12\x38\n\rSendSpaceship\x12\x11.SpaceshipRequest\x1a\x12.SpaceshipResponse0\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'spaceships_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ALIGNMENT._serialized_start=449
  _ALIGNMENT._serialized_end=481
  _CLASS._serialized_start=483
  _CLASS._serialized_end=570
  _OFFICER._serialized_start=20
  _OFFICER._serialized_end=82
  _SPACESHIPREQUEST._serialized_start=84
  _SPACESHIPREQUEST._serialized_end=123
  _SPACESHIP._serialized_start=126
  _SPACESHIP._serialized_end=391
  _SPACESHIPRESPONSE._serialized_start=393
  _SPACESHIPRESPONSE._serialized_end=447
  _SPACESHIPS._serialized_start=572
  _SPACESHIPS._serialized_end=642
# @@protoc_insertion_point(module_scope)