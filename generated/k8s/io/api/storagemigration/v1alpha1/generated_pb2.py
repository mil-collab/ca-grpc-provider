# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: k8s.io/api/storagemigration/v1alpha1/generated.proto
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
    'k8s.io/api/storagemigration/v1alpha1/generated.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from k8s.io.api.core.v1 import generated_pb2 as k8s_dot_io_dot_api_dot_core_dot_v1_dot_generated__pb2
from k8s.io.apimachinery.pkg.apis.meta.v1 import generated_pb2 as k8s_dot_io_dot_apimachinery_dot_pkg_dot_apis_dot_meta_dot_v1_dot_generated__pb2
from k8s.io.apimachinery.pkg.runtime import generated_pb2 as k8s_dot_io_dot_apimachinery_dot_pkg_dot_runtime_dot_generated__pb2
from k8s.io.apimachinery.pkg.runtime.schema import generated_pb2 as k8s_dot_io_dot_apimachinery_dot_pkg_dot_runtime_dot_schema_dot_generated__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4k8s.io/api/storagemigration/v1alpha1/generated.proto\x12$k8s.io.api.storagemigration.v1alpha1\x1a\"k8s.io/api/core/v1/generated.proto\x1a\x34k8s.io/apimachinery/pkg/apis/meta/v1/generated.proto\x1a/k8s.io/apimachinery/pkg/runtime/generated.proto\x1a\x36k8s.io/apimachinery/pkg/runtime/schema/generated.proto\"H\n\x14GroupVersionResource\x12\r\n\x05group\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x10\n\x08resource\x18\x03 \x01(\t\"\x97\x01\n\x12MigrationCondition\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t\x12\x42\n\x0elastUpdateTime\x18\x03 \x01(\x0b\x32*.k8s.io.apimachinery.pkg.apis.meta.v1.Time\x12\x0e\n\x06reason\x18\x04 \x01(\t\x12\x0f\n\x07message\x18\x05 \x01(\t\"\x83\x02\n\x17StorageVersionMigration\x12\x42\n\x08metadata\x18\x01 \x01(\x0b\x32\x30.k8s.io.apimachinery.pkg.apis.meta.v1.ObjectMeta\x12O\n\x04spec\x18\x02 \x01(\x0b\x32\x41.k8s.io.api.storagemigration.v1alpha1.StorageVersionMigrationSpec\x12S\n\x06status\x18\x03 \x01(\x0b\x32\x43.k8s.io.api.storagemigration.v1alpha1.StorageVersionMigrationStatus\"\xad\x01\n\x1bStorageVersionMigrationList\x12@\n\x08metadata\x18\x01 \x01(\x0b\x32..k8s.io.apimachinery.pkg.apis.meta.v1.ListMeta\x12L\n\x05items\x18\x02 \x03(\x0b\x32=.k8s.io.api.storagemigration.v1alpha1.StorageVersionMigration\"\x82\x01\n\x1bStorageVersionMigrationSpec\x12L\n\x08resource\x18\x01 \x01(\x0b\x32:.k8s.io.api.storagemigration.v1alpha1.GroupVersionResource\x12\x15\n\rcontinueToken\x18\x02 \x01(\t\"\x86\x01\n\x1dStorageVersionMigrationStatus\x12L\n\nconditions\x18\x01 \x03(\x0b\x32\x38.k8s.io.api.storagemigration.v1alpha1.MigrationCondition\x12\x17\n\x0fresourceVersion\x18\x02 \x01(\tB&Z$k8s.io/api/storagemigration/v1alpha1')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'k8s.io.api.storagemigration.v1alpha1.generated_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z$k8s.io/api/storagemigration/v1alpha1'
  _globals['_GROUPVERSIONRESOURCE']._serialized_start=289
  _globals['_GROUPVERSIONRESOURCE']._serialized_end=361
  _globals['_MIGRATIONCONDITION']._serialized_start=364
  _globals['_MIGRATIONCONDITION']._serialized_end=515
  _globals['_STORAGEVERSIONMIGRATION']._serialized_start=518
  _globals['_STORAGEVERSIONMIGRATION']._serialized_end=777
  _globals['_STORAGEVERSIONMIGRATIONLIST']._serialized_start=780
  _globals['_STORAGEVERSIONMIGRATIONLIST']._serialized_end=953
  _globals['_STORAGEVERSIONMIGRATIONSPEC']._serialized_start=956
  _globals['_STORAGEVERSIONMIGRATIONSPEC']._serialized_end=1086
  _globals['_STORAGEVERSIONMIGRATIONSTATUS']._serialized_start=1089
  _globals['_STORAGEVERSIONMIGRATIONSTATUS']._serialized_end=1223
# @@protoc_insertion_point(module_scope)
