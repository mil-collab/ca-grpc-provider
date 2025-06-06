# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: k8s.io/apimachinery/pkg/apis/testapigroup/v1/generated.proto
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
    'k8s.io/apimachinery/pkg/apis/testapigroup/v1/generated.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from k8s.io.apimachinery.pkg.apis.meta.v1 import generated_pb2 as k8s_dot_io_dot_apimachinery_dot_pkg_dot_apis_dot_meta_dot_v1_dot_generated__pb2
from k8s.io.apimachinery.pkg.runtime import generated_pb2 as k8s_dot_io_dot_apimachinery_dot_pkg_dot_runtime_dot_generated__pb2
from k8s.io.apimachinery.pkg.runtime.schema import generated_pb2 as k8s_dot_io_dot_apimachinery_dot_pkg_dot_runtime_dot_schema_dot_generated__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<k8s.io/apimachinery/pkg/apis/testapigroup/v1/generated.proto\x12,k8s.io.apimachinery.pkg.apis.testapigroup.v1\x1a\x34k8s.io/apimachinery/pkg/apis/meta/v1/generated.proto\x1a/k8s.io/apimachinery/pkg/runtime/generated.proto\x1a\x36k8s.io/apimachinery/pkg/runtime/schema/generated.proto\"\xda\x01\n\x04\x43\x61rp\x12\x42\n\x08metadata\x18\x01 \x01(\x0b\x32\x30.k8s.io.apimachinery.pkg.apis.meta.v1.ObjectMeta\x12\x44\n\x04spec\x18\x02 \x01(\x0b\x32\x36.k8s.io.apimachinery.pkg.apis.testapigroup.v1.CarpSpec\x12H\n\x06status\x18\x03 \x01(\x0b\x32\x38.k8s.io.apimachinery.pkg.apis.testapigroup.v1.CarpStatus\"\xd9\x01\n\rCarpCondition\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t\x12\x41\n\rlastProbeTime\x18\x03 \x01(\x0b\x32*.k8s.io.apimachinery.pkg.apis.meta.v1.Time\x12\x46\n\x12lastTransitionTime\x18\x04 \x01(\x0b\x32*.k8s.io.apimachinery.pkg.apis.meta.v1.Time\x12\x0e\n\x06reason\x18\x05 \x01(\t\x12\x0f\n\x07message\x18\x06 \x01(\t\"\x8f\x01\n\x08\x43\x61rpList\x12@\n\x08metadata\x18\x01 \x01(\x0b\x32..k8s.io.apimachinery.pkg.apis.meta.v1.ListMeta\x12\x41\n\x05items\x18\x02 \x03(\x0b\x32\x32.k8s.io.apimachinery.pkg.apis.testapigroup.v1.Carp\"\xb5\x03\n\x08\x43\x61rpSpec\x12\x15\n\rrestartPolicy\x18\x03 \x01(\t\x12%\n\x1dterminationGracePeriodSeconds\x18\x04 \x01(\x03\x12\x1d\n\x15\x61\x63tiveDeadlineSeconds\x18\x05 \x01(\x03\x12^\n\x0cnodeSelector\x18\x07 \x03(\x0b\x32H.k8s.io.apimachinery.pkg.apis.testapigroup.v1.CarpSpec.NodeSelectorEntry\x12\x1a\n\x12serviceAccountName\x18\x08 \x01(\t\x12\x16\n\x0eserviceAccount\x18\t \x01(\t\x12\x10\n\x08nodeName\x18\n \x01(\t\x12\x13\n\x0bhostNetwork\x18\x0b \x01(\x08\x12\x0f\n\x07hostPID\x18\x0c \x01(\x08\x12\x0f\n\x07hostIPC\x18\r \x01(\x08\x12\x10\n\x08hostname\x18\x10 \x01(\t\x12\x11\n\tsubdomain\x18\x11 \x01(\t\x12\x15\n\rschedulername\x18\x13 \x01(\t\x1a\x33\n\x11NodeSelectorEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xec\x01\n\nCarpStatus\x12\r\n\x05phase\x18\x01 \x01(\t\x12O\n\nconditions\x18\x02 \x03(\x0b\x32;.k8s.io.apimachinery.pkg.apis.testapigroup.v1.CarpCondition\x12\x0f\n\x07message\x18\x03 \x01(\t\x12\x0e\n\x06reason\x18\x04 \x01(\t\x12\x0e\n\x06hostIP\x18\x05 \x01(\t\x12\x0e\n\x06\x63\x61rpIP\x18\x06 \x01(\t\x12=\n\tstartTime\x18\x07 \x01(\x0b\x32*.k8s.io.apimachinery.pkg.apis.meta.v1.TimeB.Z,k8s.io/apimachinery/pkg/apis/testapigroup/v1')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'k8s.io.apimachinery.pkg.apis.testapigroup.v1.generated_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z,k8s.io/apimachinery/pkg/apis/testapigroup/v1'
  _globals['_CARPSPEC_NODESELECTORENTRY']._loaded_options = None
  _globals['_CARPSPEC_NODESELECTORENTRY']._serialized_options = b'8\001'
  _globals['_CARP']._serialized_start=270
  _globals['_CARP']._serialized_end=488
  _globals['_CARPCONDITION']._serialized_start=491
  _globals['_CARPCONDITION']._serialized_end=708
  _globals['_CARPLIST']._serialized_start=711
  _globals['_CARPLIST']._serialized_end=854
  _globals['_CARPSPEC']._serialized_start=857
  _globals['_CARPSPEC']._serialized_end=1294
  _globals['_CARPSPEC_NODESELECTORENTRY']._serialized_start=1243
  _globals['_CARPSPEC_NODESELECTORENTRY']._serialized_end=1294
  _globals['_CARPSTATUS']._serialized_start=1297
  _globals['_CARPSTATUS']._serialized_end=1533
# @@protoc_insertion_point(module_scope)
