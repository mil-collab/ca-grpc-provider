# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: k8s.io/api/storage/v1beta1/generated.proto
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
    'k8s.io/api/storage/v1beta1/generated.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from k8s.io.api.core.v1 import generated_pb2 as k8s_dot_io_dot_api_dot_core_dot_v1_dot_generated__pb2
from k8s.io.apimachinery.pkg.api.resource import generated_pb2 as k8s_dot_io_dot_apimachinery_dot_pkg_dot_api_dot_resource_dot_generated__pb2
from k8s.io.apimachinery.pkg.apis.meta.v1 import generated_pb2 as k8s_dot_io_dot_apimachinery_dot_pkg_dot_apis_dot_meta_dot_v1_dot_generated__pb2
from k8s.io.apimachinery.pkg.runtime import generated_pb2 as k8s_dot_io_dot_apimachinery_dot_pkg_dot_runtime_dot_generated__pb2
from k8s.io.apimachinery.pkg.runtime.schema import generated_pb2 as k8s_dot_io_dot_apimachinery_dot_pkg_dot_runtime_dot_schema_dot_generated__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*k8s.io/api/storage/v1beta1/generated.proto\x12\x1ak8s.io.api.storage.v1beta1\x1a\"k8s.io/api/core/v1/generated.proto\x1a\x34k8s.io/apimachinery/pkg/api/resource/generated.proto\x1a\x34k8s.io/apimachinery/pkg/apis/meta/v1/generated.proto\x1a/k8s.io/apimachinery/pkg/runtime/generated.proto\x1a\x36k8s.io/apimachinery/pkg/runtime/schema/generated.proto\"\x88\x01\n\tCSIDriver\x12\x42\n\x08metadata\x18\x01 \x01(\x0b\x32\x30.k8s.io.apimachinery.pkg.apis.meta.v1.ObjectMeta\x12\x37\n\x04spec\x18\x02 \x01(\x0b\x32).k8s.io.api.storage.v1beta1.CSIDriverSpec\"\x87\x01\n\rCSIDriverList\x12@\n\x08metadata\x18\x01 \x01(\x0b\x32..k8s.io.apimachinery.pkg.apis.meta.v1.ListMeta\x12\x34\n\x05items\x18\x02 \x03(\x0b\x32%.k8s.io.api.storage.v1beta1.CSIDriver\"\xab\x02\n\rCSIDriverSpec\x12\x16\n\x0e\x61ttachRequired\x18\x01 \x01(\x08\x12\x16\n\x0epodInfoOnMount\x18\x02 \x01(\x08\x12\x1c\n\x14volumeLifecycleModes\x18\x03 \x03(\t\x12\x17\n\x0fstorageCapacity\x18\x04 \x01(\x08\x12\x15\n\rfsGroupPolicy\x18\x05 \x01(\t\x12?\n\rtokenRequests\x18\x06 \x03(\x0b\x32(.k8s.io.api.storage.v1beta1.TokenRequest\x12\x19\n\x11requiresRepublish\x18\x07 \x01(\x08\x12\x14\n\x0cseLinuxMount\x18\x08 \x01(\x08\x12*\n\"nodeAllocatableUpdatePeriodSeconds\x18\t \x01(\x03\"\x84\x01\n\x07\x43SINode\x12\x42\n\x08metadata\x18\x01 \x01(\x0b\x32\x30.k8s.io.apimachinery.pkg.apis.meta.v1.ObjectMeta\x12\x35\n\x04spec\x18\x02 \x01(\x0b\x32\'.k8s.io.api.storage.v1beta1.CSINodeSpec\"\x89\x01\n\rCSINodeDriver\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06nodeID\x18\x02 \x01(\t\x12\x14\n\x0ctopologyKeys\x18\x03 \x03(\t\x12\x44\n\x0b\x61llocatable\x18\x04 \x01(\x0b\x32/.k8s.io.api.storage.v1beta1.VolumeNodeResources\"\x83\x01\n\x0b\x43SINodeList\x12@\n\x08metadata\x18\x01 \x01(\x0b\x32..k8s.io.apimachinery.pkg.apis.meta.v1.ListMeta\x12\x32\n\x05items\x18\x02 \x03(\x0b\x32#.k8s.io.api.storage.v1beta1.CSINode\"I\n\x0b\x43SINodeSpec\x12:\n\x07\x64rivers\x18\x01 \x03(\x0b\x32).k8s.io.api.storage.v1beta1.CSINodeDriver\"\xca\x02\n\x12\x43SIStorageCapacity\x12\x42\n\x08metadata\x18\x01 \x01(\x0b\x32\x30.k8s.io.apimachinery.pkg.apis.meta.v1.ObjectMeta\x12I\n\x0cnodeTopology\x18\x02 \x01(\x0b\x32\x33.k8s.io.apimachinery.pkg.apis.meta.v1.LabelSelector\x12\x18\n\x10storageClassName\x18\x03 \x01(\t\x12@\n\x08\x63\x61pacity\x18\x04 \x01(\x0b\x32..k8s.io.apimachinery.pkg.api.resource.Quantity\x12I\n\x11maximumVolumeSize\x18\x05 \x01(\x0b\x32..k8s.io.apimachinery.pkg.api.resource.Quantity\"\x99\x01\n\x16\x43SIStorageCapacityList\x12@\n\x08metadata\x18\x01 \x01(\x0b\x32..k8s.io.apimachinery.pkg.apis.meta.v1.ListMeta\x12=\n\x05items\x18\x02 \x03(\x0b\x32..k8s.io.api.storage.v1beta1.CSIStorageCapacity\"\x93\x03\n\x0cStorageClass\x12\x42\n\x08metadata\x18\x01 \x01(\x0b\x32\x30.k8s.io.apimachinery.pkg.apis.meta.v1.ObjectMeta\x12\x13\n\x0bprovisioner\x18\x02 \x01(\t\x12L\n\nparameters\x18\x03 \x03(\x0b\x32\x38.k8s.io.api.storage.v1beta1.StorageClass.ParametersEntry\x12\x15\n\rreclaimPolicy\x18\x04 \x01(\t\x12\x14\n\x0cmountOptions\x18\x05 \x03(\t\x12\x1c\n\x14\x61llowVolumeExpansion\x18\x06 \x01(\x08\x12\x19\n\x11volumeBindingMode\x18\x07 \x01(\t\x12\x43\n\x11\x61llowedTopologies\x18\x08 \x03(\x0b\x32(.k8s.io.api.core.v1.TopologySelectorTerm\x1a\x31\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x8d\x01\n\x10StorageClassList\x12@\n\x08metadata\x18\x01 \x01(\x0b\x32..k8s.io.apimachinery.pkg.apis.meta.v1.ListMeta\x12\x37\n\x05items\x18\x02 \x03(\x0b\x32(.k8s.io.api.storage.v1beta1.StorageClass\";\n\x0cTokenRequest\x12\x10\n\x08\x61udience\x18\x01 \x01(\t\x12\x19\n\x11\x65xpirationSeconds\x18\x02 \x01(\x03\"\xda\x01\n\x10VolumeAttachment\x12\x42\n\x08metadata\x18\x01 \x01(\x0b\x32\x30.k8s.io.apimachinery.pkg.apis.meta.v1.ObjectMeta\x12>\n\x04spec\x18\x02 \x01(\x0b\x32\x30.k8s.io.api.storage.v1beta1.VolumeAttachmentSpec\x12\x42\n\x06status\x18\x03 \x01(\x0b\x32\x32.k8s.io.api.storage.v1beta1.VolumeAttachmentStatus\"\x95\x01\n\x14VolumeAttachmentList\x12@\n\x08metadata\x18\x01 \x01(\x0b\x32..k8s.io.apimachinery.pkg.apis.meta.v1.ListMeta\x12;\n\x05items\x18\x02 \x03(\x0b\x32,.k8s.io.api.storage.v1beta1.VolumeAttachment\"z\n\x16VolumeAttachmentSource\x12\x1c\n\x14persistentVolumeName\x18\x01 \x01(\t\x12\x42\n\x10inlineVolumeSpec\x18\x02 \x01(\x0b\x32(.k8s.io.api.core.v1.PersistentVolumeSpec\"~\n\x14VolumeAttachmentSpec\x12\x10\n\x08\x61ttacher\x18\x01 \x01(\t\x12\x42\n\x06source\x18\x02 \x01(\x0b\x32\x32.k8s.io.api.storage.v1beta1.VolumeAttachmentSource\x12\x10\n\x08nodeName\x18\x03 \x01(\t\"\xc9\x02\n\x16VolumeAttachmentStatus\x12\x10\n\x08\x61ttached\x18\x01 \x01(\x08\x12\x66\n\x12\x61ttachmentMetadata\x18\x02 \x03(\x0b\x32J.k8s.io.api.storage.v1beta1.VolumeAttachmentStatus.AttachmentMetadataEntry\x12<\n\x0b\x61ttachError\x18\x03 \x01(\x0b\x32\'.k8s.io.api.storage.v1beta1.VolumeError\x12<\n\x0b\x64\x65tachError\x18\x04 \x01(\x0b\x32\'.k8s.io.api.storage.v1beta1.VolumeError\x1a\x39\n\x17\x41ttachmentMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xf9\x01\n\x15VolumeAttributesClass\x12\x42\n\x08metadata\x18\x01 \x01(\x0b\x32\x30.k8s.io.apimachinery.pkg.apis.meta.v1.ObjectMeta\x12\x12\n\ndriverName\x18\x02 \x01(\t\x12U\n\nparameters\x18\x03 \x03(\x0b\x32\x41.k8s.io.api.storage.v1beta1.VolumeAttributesClass.ParametersEntry\x1a\x31\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x9f\x01\n\x19VolumeAttributesClassList\x12@\n\x08metadata\x18\x01 \x01(\x0b\x32..k8s.io.apimachinery.pkg.apis.meta.v1.ListMeta\x12@\n\x05items\x18\x02 \x03(\x0b\x32\x31.k8s.io.api.storage.v1beta1.VolumeAttributesClass\"k\n\x0bVolumeError\x12\x38\n\x04time\x18\x01 \x01(\x0b\x32*.k8s.io.apimachinery.pkg.apis.meta.v1.Time\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x11\n\terrorCode\x18\x03 \x01(\x05\"$\n\x13VolumeNodeResources\x12\r\n\x05\x63ount\x18\x01 \x01(\x05\x42\x1cZ\x1ak8s.io/api/storage/v1beta1')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'k8s.io.api.storage.v1beta1.generated_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\032k8s.io/api/storage/v1beta1'
  _globals['_STORAGECLASS_PARAMETERSENTRY']._loaded_options = None
  _globals['_STORAGECLASS_PARAMETERSENTRY']._serialized_options = b'8\001'
  _globals['_VOLUMEATTACHMENTSTATUS_ATTACHMENTMETADATAENTRY']._loaded_options = None
  _globals['_VOLUMEATTACHMENTSTATUS_ATTACHMENTMETADATAENTRY']._serialized_options = b'8\001'
  _globals['_VOLUMEATTRIBUTESCLASS_PARAMETERSENTRY']._loaded_options = None
  _globals['_VOLUMEATTRIBUTESCLASS_PARAMETERSENTRY']._serialized_options = b'8\001'
  _globals['_CSIDRIVER']._serialized_start=324
  _globals['_CSIDRIVER']._serialized_end=460
  _globals['_CSIDRIVERLIST']._serialized_start=463
  _globals['_CSIDRIVERLIST']._serialized_end=598
  _globals['_CSIDRIVERSPEC']._serialized_start=601
  _globals['_CSIDRIVERSPEC']._serialized_end=900
  _globals['_CSINODE']._serialized_start=903
  _globals['_CSINODE']._serialized_end=1035
  _globals['_CSINODEDRIVER']._serialized_start=1038
  _globals['_CSINODEDRIVER']._serialized_end=1175
  _globals['_CSINODELIST']._serialized_start=1178
  _globals['_CSINODELIST']._serialized_end=1309
  _globals['_CSINODESPEC']._serialized_start=1311
  _globals['_CSINODESPEC']._serialized_end=1384
  _globals['_CSISTORAGECAPACITY']._serialized_start=1387
  _globals['_CSISTORAGECAPACITY']._serialized_end=1717
  _globals['_CSISTORAGECAPACITYLIST']._serialized_start=1720
  _globals['_CSISTORAGECAPACITYLIST']._serialized_end=1873
  _globals['_STORAGECLASS']._serialized_start=1876
  _globals['_STORAGECLASS']._serialized_end=2279
  _globals['_STORAGECLASS_PARAMETERSENTRY']._serialized_start=2230
  _globals['_STORAGECLASS_PARAMETERSENTRY']._serialized_end=2279
  _globals['_STORAGECLASSLIST']._serialized_start=2282
  _globals['_STORAGECLASSLIST']._serialized_end=2423
  _globals['_TOKENREQUEST']._serialized_start=2425
  _globals['_TOKENREQUEST']._serialized_end=2484
  _globals['_VOLUMEATTACHMENT']._serialized_start=2487
  _globals['_VOLUMEATTACHMENT']._serialized_end=2705
  _globals['_VOLUMEATTACHMENTLIST']._serialized_start=2708
  _globals['_VOLUMEATTACHMENTLIST']._serialized_end=2857
  _globals['_VOLUMEATTACHMENTSOURCE']._serialized_start=2859
  _globals['_VOLUMEATTACHMENTSOURCE']._serialized_end=2981
  _globals['_VOLUMEATTACHMENTSPEC']._serialized_start=2983
  _globals['_VOLUMEATTACHMENTSPEC']._serialized_end=3109
  _globals['_VOLUMEATTACHMENTSTATUS']._serialized_start=3112
  _globals['_VOLUMEATTACHMENTSTATUS']._serialized_end=3441
  _globals['_VOLUMEATTACHMENTSTATUS_ATTACHMENTMETADATAENTRY']._serialized_start=3384
  _globals['_VOLUMEATTACHMENTSTATUS_ATTACHMENTMETADATAENTRY']._serialized_end=3441
  _globals['_VOLUMEATTRIBUTESCLASS']._serialized_start=3444
  _globals['_VOLUMEATTRIBUTESCLASS']._serialized_end=3693
  _globals['_VOLUMEATTRIBUTESCLASS_PARAMETERSENTRY']._serialized_start=2230
  _globals['_VOLUMEATTRIBUTESCLASS_PARAMETERSENTRY']._serialized_end=2279
  _globals['_VOLUMEATTRIBUTESCLASSLIST']._serialized_start=3696
  _globals['_VOLUMEATTRIBUTESCLASSLIST']._serialized_end=3855
  _globals['_VOLUMEERROR']._serialized_start=3857
  _globals['_VOLUMEERROR']._serialized_end=3964
  _globals['_VOLUMENODERESOURCES']._serialized_start=3966
  _globals['_VOLUMENODERESOURCES']._serialized_end=4002
# @@protoc_insertion_point(module_scope)
