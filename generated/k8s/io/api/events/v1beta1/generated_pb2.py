# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: k8s.io/api/events/v1beta1/generated.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'k8s.io/api/events/v1beta1/generated.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from k8s.io.api.core.v1 import generated_pb2 as k8s_dot_io_dot_api_dot_core_dot_v1_dot_generated__pb2
from k8s.io.apimachinery.pkg.apis.meta.v1 import generated_pb2 as k8s_dot_io_dot_apimachinery_dot_pkg_dot_apis_dot_meta_dot_v1_dot_generated__pb2
from k8s.io.apimachinery.pkg.runtime import generated_pb2 as k8s_dot_io_dot_apimachinery_dot_pkg_dot_runtime_dot_generated__pb2
from k8s.io.apimachinery.pkg.runtime.schema import generated_pb2 as k8s_dot_io_dot_apimachinery_dot_pkg_dot_runtime_dot_schema_dot_generated__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)k8s.io/api/events/v1beta1/generated.proto\x12\x19k8s.io.api.events.v1beta1\x1a\"k8s.io/api/core/v1/generated.proto\x1a\x34k8s.io/apimachinery/pkg/apis/meta/v1/generated.proto\x1a/k8s.io/apimachinery/pkg/runtime/generated.proto\x1a\x36k8s.io/apimachinery/pkg/runtime/schema/generated.proto\"\x98\x05\n\x05\x45vent\x12\x42\n\x08metadata\x18\x01 \x01(\x0b\x32\x30.k8s.io.apimachinery.pkg.apis.meta.v1.ObjectMeta\x12\x42\n\teventTime\x18\x02 \x01(\x0b\x32/.k8s.io.apimachinery.pkg.apis.meta.v1.MicroTime\x12\x36\n\x06series\x18\x03 \x01(\x0b\x32&.k8s.io.api.events.v1beta1.EventSeries\x12\x1b\n\x13reportingController\x18\x04 \x01(\t\x12\x19\n\x11reportingInstance\x18\x05 \x01(\t\x12\x0e\n\x06\x61\x63tion\x18\x06 \x01(\t\x12\x0e\n\x06reason\x18\x07 \x01(\t\x12\x36\n\tregarding\x18\x08 \x01(\x0b\x32#.k8s.io.api.core.v1.ObjectReference\x12\x34\n\x07related\x18\t \x01(\x0b\x32#.k8s.io.api.core.v1.ObjectReference\x12\x0c\n\x04note\x18\n \x01(\t\x12\x0c\n\x04type\x18\x0b \x01(\t\x12\x39\n\x10\x64\x65precatedSource\x18\x0c \x01(\x0b\x32\x1f.k8s.io.api.core.v1.EventSource\x12L\n\x18\x64\x65precatedFirstTimestamp\x18\r \x01(\x0b\x32*.k8s.io.apimachinery.pkg.apis.meta.v1.Time\x12K\n\x17\x64\x65precatedLastTimestamp\x18\x0e \x01(\x0b\x32*.k8s.io.apimachinery.pkg.apis.meta.v1.Time\x12\x17\n\x0f\x64\x65precatedCount\x18\x0f \x01(\x05\"~\n\tEventList\x12@\n\x08metadata\x18\x01 \x01(\x0b\x32..k8s.io.apimachinery.pkg.apis.meta.v1.ListMeta\x12/\n\x05items\x18\x02 \x03(\x0b\x32 .k8s.io.api.events.v1beta1.Event\"g\n\x0b\x45ventSeries\x12\r\n\x05\x63ount\x18\x01 \x01(\x05\x12I\n\x10lastObservedTime\x18\x02 \x01(\x0b\x32/.k8s.io.apimachinery.pkg.apis.meta.v1.MicroTimeB\x1bZ\x19k8s.io/api/events/v1beta1')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'k8s.io.api.events.v1beta1.generated_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\031k8s.io/api/events/v1beta1'
  _globals['_EVENT']._serialized_start=268
  _globals['_EVENT']._serialized_end=932
  _globals['_EVENTLIST']._serialized_start=934
  _globals['_EVENTLIST']._serialized_end=1060
  _globals['_EVENTSERIES']._serialized_start=1062
  _globals['_EVENTSERIES']._serialized_end=1165
# @@protoc_insertion_point(module_scope)
