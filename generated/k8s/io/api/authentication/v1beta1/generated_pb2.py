# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: k8s.io/api/authentication/v1beta1/generated.proto
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
    'k8s.io/api/authentication/v1beta1/generated.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from k8s.io.api.authentication.v1 import generated_pb2 as k8s_dot_io_dot_api_dot_authentication_dot_v1_dot_generated__pb2
from k8s.io.apimachinery.pkg.apis.meta.v1 import generated_pb2 as k8s_dot_io_dot_apimachinery_dot_pkg_dot_apis_dot_meta_dot_v1_dot_generated__pb2
from k8s.io.apimachinery.pkg.runtime import generated_pb2 as k8s_dot_io_dot_apimachinery_dot_pkg_dot_runtime_dot_generated__pb2
from k8s.io.apimachinery.pkg.runtime.schema import generated_pb2 as k8s_dot_io_dot_apimachinery_dot_pkg_dot_runtime_dot_schema_dot_generated__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1k8s.io/api/authentication/v1beta1/generated.proto\x12!k8s.io.api.authentication.v1beta1\x1a,k8s.io/api/authentication/v1/generated.proto\x1a\x34k8s.io/apimachinery/pkg/apis/meta/v1/generated.proto\x1a/k8s.io/apimachinery/pkg/runtime/generated.proto\x1a\x36k8s.io/apimachinery/pkg/runtime/schema/generated.proto\"\x1b\n\nExtraValue\x12\r\n\x05items\x18\x01 \x03(\t\"\xa3\x01\n\x11SelfSubjectReview\x12\x42\n\x08metadata\x18\x01 \x01(\x0b\x32\x30.k8s.io.apimachinery.pkg.apis.meta.v1.ObjectMeta\x12J\n\x06status\x18\x02 \x01(\x0b\x32:.k8s.io.api.authentication.v1beta1.SelfSubjectReviewStatus\"S\n\x17SelfSubjectReviewStatus\x12\x38\n\x08userInfo\x18\x01 \x01(\x0b\x32&.k8s.io.api.authentication.v1.UserInfo\"\xd9\x01\n\x0bTokenReview\x12\x42\n\x08metadata\x18\x01 \x01(\x0b\x32\x30.k8s.io.apimachinery.pkg.apis.meta.v1.ObjectMeta\x12@\n\x04spec\x18\x02 \x01(\x0b\x32\x32.k8s.io.api.authentication.v1beta1.TokenReviewSpec\x12\x44\n\x06status\x18\x03 \x01(\x0b\x32\x34.k8s.io.api.authentication.v1beta1.TokenReviewStatus\"3\n\x0fTokenReviewSpec\x12\r\n\x05token\x18\x01 \x01(\t\x12\x11\n\taudiences\x18\x02 \x03(\t\"\x87\x01\n\x11TokenReviewStatus\x12\x15\n\rauthenticated\x18\x01 \x01(\x08\x12\x39\n\x04user\x18\x02 \x01(\x0b\x32+.k8s.io.api.authentication.v1beta1.UserInfo\x12\x11\n\taudiences\x18\x04 \x03(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\"\xdd\x01\n\x08UserInfo\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x0b\n\x03uid\x18\x02 \x01(\t\x12\x0e\n\x06groups\x18\x03 \x03(\t\x12\x45\n\x05\x65xtra\x18\x04 \x03(\x0b\x32\x36.k8s.io.api.authentication.v1beta1.UserInfo.ExtraEntry\x1a[\n\nExtraEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12<\n\x05value\x18\x02 \x01(\x0b\x32-.k8s.io.api.authentication.v1beta1.ExtraValue:\x02\x38\x01\x42#Z!k8s.io/api/authentication/v1beta1')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'k8s.io.api.authentication.v1beta1.generated_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z!k8s.io/api/authentication/v1beta1'
  _globals['_USERINFO_EXTRAENTRY']._loaded_options = None
  _globals['_USERINFO_EXTRAENTRY']._serialized_options = b'8\001'
  _globals['_EXTRAVALUE']._serialized_start=293
  _globals['_EXTRAVALUE']._serialized_end=320
  _globals['_SELFSUBJECTREVIEW']._serialized_start=323
  _globals['_SELFSUBJECTREVIEW']._serialized_end=486
  _globals['_SELFSUBJECTREVIEWSTATUS']._serialized_start=488
  _globals['_SELFSUBJECTREVIEWSTATUS']._serialized_end=571
  _globals['_TOKENREVIEW']._serialized_start=574
  _globals['_TOKENREVIEW']._serialized_end=791
  _globals['_TOKENREVIEWSPEC']._serialized_start=793
  _globals['_TOKENREVIEWSPEC']._serialized_end=844
  _globals['_TOKENREVIEWSTATUS']._serialized_start=847
  _globals['_TOKENREVIEWSTATUS']._serialized_end=982
  _globals['_USERINFO']._serialized_start=985
  _globals['_USERINFO']._serialized_end=1206
  _globals['_USERINFO_EXTRAENTRY']._serialized_start=1115
  _globals['_USERINFO_EXTRAENTRY']._serialized_end=1206
# @@protoc_insertion_point(module_scope)
