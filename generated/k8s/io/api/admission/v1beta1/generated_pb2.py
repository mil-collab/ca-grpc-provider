# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: k8s.io/api/admission/v1beta1/generated.proto
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
    'k8s.io/api/admission/v1beta1/generated.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from k8s.io.api.authentication.v1 import generated_pb2 as k8s_dot_io_dot_api_dot_authentication_dot_v1_dot_generated__pb2
from k8s.io.apimachinery.pkg.apis.meta.v1 import generated_pb2 as k8s_dot_io_dot_apimachinery_dot_pkg_dot_apis_dot_meta_dot_v1_dot_generated__pb2
from k8s.io.apimachinery.pkg.runtime import generated_pb2 as k8s_dot_io_dot_apimachinery_dot_pkg_dot_runtime_dot_generated__pb2
from k8s.io.apimachinery.pkg.runtime.schema import generated_pb2 as k8s_dot_io_dot_apimachinery_dot_pkg_dot_runtime_dot_schema_dot_generated__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,k8s.io/api/admission/v1beta1/generated.proto\x12\x1ck8s.io.api.admission.v1beta1\x1a,k8s.io/api/authentication/v1/generated.proto\x1a\x34k8s.io/apimachinery/pkg/apis/meta/v1/generated.proto\x1a/k8s.io/apimachinery/pkg/runtime/generated.proto\x1a\x36k8s.io/apimachinery/pkg/runtime/schema/generated.proto\"\xc5\x05\n\x10\x41\x64missionRequest\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12\x44\n\x04kind\x18\x02 \x01(\x0b\x32\x36.k8s.io.apimachinery.pkg.apis.meta.v1.GroupVersionKind\x12L\n\x08resource\x18\x03 \x01(\x0b\x32:.k8s.io.apimachinery.pkg.apis.meta.v1.GroupVersionResource\x12\x13\n\x0bsubResource\x18\x04 \x01(\t\x12K\n\x0brequestKind\x18\r \x01(\x0b\x32\x36.k8s.io.apimachinery.pkg.apis.meta.v1.GroupVersionKind\x12S\n\x0frequestResource\x18\x0e \x01(\x0b\x32:.k8s.io.apimachinery.pkg.apis.meta.v1.GroupVersionResource\x12\x1a\n\x12requestSubResource\x18\x0f \x01(\t\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x11\n\tnamespace\x18\x06 \x01(\t\x12\x11\n\toperation\x18\x07 \x01(\t\x12\x38\n\x08userInfo\x18\x08 \x01(\x0b\x32&.k8s.io.api.authentication.v1.UserInfo\x12=\n\x06object\x18\t \x01(\x0b\x32-.k8s.io.apimachinery.pkg.runtime.RawExtension\x12@\n\toldObject\x18\n \x01(\x0b\x32-.k8s.io.apimachinery.pkg.runtime.RawExtension\x12\x0e\n\x06\x64ryRun\x18\x0b \x01(\x08\x12>\n\x07options\x18\x0c \x01(\x0b\x32-.k8s.io.apimachinery.pkg.runtime.RawExtension\"\xbd\x02\n\x11\x41\x64missionResponse\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12\x0f\n\x07\x61llowed\x18\x02 \x01(\x08\x12<\n\x06status\x18\x03 \x01(\x0b\x32,.k8s.io.apimachinery.pkg.apis.meta.v1.Status\x12\r\n\x05patch\x18\x04 \x01(\x0c\x12\x11\n\tpatchType\x18\x05 \x01(\t\x12_\n\x10\x61uditAnnotations\x18\x06 \x03(\x0b\x32\x45.k8s.io.api.admission.v1beta1.AdmissionResponse.AuditAnnotationsEntry\x12\x10\n\x08warnings\x18\x07 \x03(\t\x1a\x37\n\x15\x41uditAnnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x95\x01\n\x0f\x41\x64missionReview\x12?\n\x07request\x18\x01 \x01(\x0b\x32..k8s.io.api.admission.v1beta1.AdmissionRequest\x12\x41\n\x08response\x18\x02 \x01(\x0b\x32/.k8s.io.api.admission.v1beta1.AdmissionResponseB\x1eZ\x1ck8s.io/api/admission/v1beta1')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'k8s.io.api.admission.v1beta1.generated_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\034k8s.io/api/admission/v1beta1'
  _globals['_ADMISSIONRESPONSE_AUDITANNOTATIONSENTRY']._loaded_options = None
  _globals['_ADMISSIONRESPONSE_AUDITANNOTATIONSENTRY']._serialized_options = b'8\001'
  _globals['_ADMISSIONREQUEST']._serialized_start=284
  _globals['_ADMISSIONREQUEST']._serialized_end=993
  _globals['_ADMISSIONRESPONSE']._serialized_start=996
  _globals['_ADMISSIONRESPONSE']._serialized_end=1313
  _globals['_ADMISSIONRESPONSE_AUDITANNOTATIONSENTRY']._serialized_start=1258
  _globals['_ADMISSIONRESPONSE_AUDITANNOTATIONSENTRY']._serialized_end=1313
  _globals['_ADMISSIONREVIEW']._serialized_start=1316
  _globals['_ADMISSIONREVIEW']._serialized_end=1465
# @@protoc_insertion_point(module_scope)
