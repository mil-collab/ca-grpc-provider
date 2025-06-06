# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: k8s.io/api/resource/v1alpha3/generated.proto
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
    'k8s.io/api/resource/v1alpha3/generated.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from k8s.io.api.core.v1 import generated_pb2 as k8s_dot_io_dot_api_dot_core_dot_v1_dot_generated__pb2
from k8s.io.apimachinery.pkg.api.resource import generated_pb2 as k8s_dot_io_dot_apimachinery_dot_pkg_dot_api_dot_resource_dot_generated__pb2
from k8s.io.apimachinery.pkg.apis.meta.v1 import generated_pb2 as k8s_dot_io_dot_apimachinery_dot_pkg_dot_apis_dot_meta_dot_v1_dot_generated__pb2
from k8s.io.apimachinery.pkg.runtime import generated_pb2 as k8s_dot_io_dot_apimachinery_dot_pkg_dot_runtime_dot_generated__pb2
from k8s.io.apimachinery.pkg.runtime.schema import generated_pb2 as k8s_dot_io_dot_apimachinery_dot_pkg_dot_runtime_dot_schema_dot_generated__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,k8s.io/api/resource/v1alpha3/generated.proto\x12\x1ck8s.io.api.resource.v1alpha3\x1a\"k8s.io/api/core/v1/generated.proto\x1a\x34k8s.io/apimachinery/pkg/api/resource/generated.proto\x1a\x34k8s.io/apimachinery/pkg/apis/meta/v1/generated.proto\x1a/k8s.io/apimachinery/pkg/runtime/generated.proto\x1a\x36k8s.io/apimachinery/pkg/runtime/schema/generated.proto\"\x8d\x02\n\x15\x41llocatedDeviceStatus\x12\x0e\n\x06\x64river\x18\x01 \x01(\t\x12\x0c\n\x04pool\x18\x02 \x01(\t\x12\x0e\n\x06\x64\x65vice\x18\x03 \x01(\t\x12\x43\n\nconditions\x18\x04 \x03(\x0b\x32/.k8s.io.apimachinery.pkg.apis.meta.v1.Condition\x12;\n\x04\x64\x61ta\x18\x05 \x01(\x0b\x32-.k8s.io.apimachinery.pkg.runtime.RawExtension\x12\x44\n\x0bnetworkData\x18\x06 \x01(\x0b\x32/.k8s.io.api.resource.v1alpha3.NetworkDeviceData\"\x91\x01\n\x10\x41llocationResult\x12\x45\n\x07\x64\x65vices\x18\x01 \x01(\x0b\x32\x34.k8s.io.api.resource.v1alpha3.DeviceAllocationResult\x12\x36\n\x0cnodeSelector\x18\x03 \x01(\x0b\x32 .k8s.io.api.core.v1.NodeSelector\"\xd3\x04\n\x0b\x42\x61sicDevice\x12M\n\nattributes\x18\x01 \x03(\x0b\x32\x39.k8s.io.api.resource.v1alpha3.BasicDevice.AttributesEntry\x12I\n\x08\x63\x61pacity\x18\x02 \x03(\x0b\x32\x37.k8s.io.api.resource.v1alpha3.BasicDevice.CapacityEntry\x12P\n\x10\x63onsumesCounters\x18\x03 \x03(\x0b\x32\x36.k8s.io.api.resource.v1alpha3.DeviceCounterConsumption\x12\x10\n\x08nodeName\x18\x04 \x01(\t\x12\x36\n\x0cnodeSelector\x18\x05 \x01(\x0b\x32 .k8s.io.api.core.v1.NodeSelector\x12\x10\n\x08\x61llNodes\x18\x06 \x01(\x08\x12\x39\n\x06taints\x18\x07 \x03(\x0b\x32).k8s.io.api.resource.v1alpha3.DeviceTaint\x1a`\n\x0f\x41ttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12<\n\x05value\x18\x02 \x01(\x0b\x32-.k8s.io.api.resource.v1alpha3.DeviceAttribute:\x02\x38\x01\x1a_\n\rCapacityEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12=\n\x05value\x18\x02 \x01(\x0b\x32..k8s.io.apimachinery.pkg.api.resource.Quantity:\x02\x38\x01\"\'\n\x11\x43\x45LDeviceSelector\x12\x12\n\nexpression\x18\x01 \x01(\t\"H\n\x07\x43ounter\x12=\n\x05value\x18\x01 \x01(\x0b\x32..k8s.io.apimachinery.pkg.api.resource.Quantity\"\xbc\x01\n\nCounterSet\x12\x0c\n\x04name\x18\x01 \x01(\t\x12H\n\x08\x63ounters\x18\x02 \x03(\x0b\x32\x36.k8s.io.api.resource.v1alpha3.CounterSet.CountersEntry\x1aV\n\rCountersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x34\n\x05value\x18\x02 \x01(\x0b\x32%.k8s.io.api.resource.v1alpha3.Counter:\x02\x38\x01\"P\n\x06\x44\x65vice\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x38\n\x05\x62\x61sic\x18\x02 \x01(\x0b\x32).k8s.io.api.resource.v1alpha3.BasicDevice\"\x91\x01\n\x1d\x44\x65viceAllocationConfiguration\x12\x0e\n\x06source\x18\x01 \x01(\t\x12\x10\n\x08requests\x18\x02 \x03(\t\x12N\n\x13\x64\x65viceConfiguration\x18\x03 \x01(\x0b\x32\x31.k8s.io.api.resource.v1alpha3.DeviceConfiguration\"\xb3\x01\n\x16\x44\x65viceAllocationResult\x12L\n\x07results\x18\x01 \x03(\x0b\x32;.k8s.io.api.resource.v1alpha3.DeviceRequestAllocationResult\x12K\n\x06\x63onfig\x18\x02 \x03(\x0b\x32;.k8s.io.api.resource.v1alpha3.DeviceAllocationConfiguration\"M\n\x0f\x44\x65viceAttribute\x12\x0b\n\x03int\x18\x02 \x01(\x03\x12\x0c\n\x04\x62ool\x18\x03 \x01(\x08\x12\x0e\n\x06string\x18\x04 \x01(\t\x12\x0f\n\x07version\x18\x05 \x01(\t\"\xd9\x01\n\x0b\x44\x65viceClaim\x12=\n\x08requests\x18\x01 \x03(\x0b\x32+.k8s.io.api.resource.v1alpha3.DeviceRequest\x12\x43\n\x0b\x63onstraints\x18\x02 \x03(\x0b\x32..k8s.io.api.resource.v1alpha3.DeviceConstraint\x12\x46\n\x06\x63onfig\x18\x03 \x03(\x0b\x32\x36.k8s.io.api.resource.v1alpha3.DeviceClaimConfiguration\"|\n\x18\x44\x65viceClaimConfiguration\x12\x10\n\x08requests\x18\x01 \x03(\t\x12N\n\x13\x64\x65viceConfiguration\x18\x02 \x01(\x0b\x32\x31.k8s.io.api.resource.v1alpha3.DeviceConfiguration\"\x8e\x01\n\x0b\x44\x65viceClass\x12\x42\n\x08metadata\x18\x01 \x01(\x0b\x32\x30.k8s.io.apimachinery.pkg.apis.meta.v1.ObjectMeta\x12;\n\x04spec\x18\x02 \x01(\x0b\x32-.k8s.io.api.resource.v1alpha3.DeviceClassSpec\"j\n\x18\x44\x65viceClassConfiguration\x12N\n\x13\x64\x65viceConfiguration\x18\x01 \x01(\x0b\x32\x31.k8s.io.api.resource.v1alpha3.DeviceConfiguration\"\x8d\x01\n\x0f\x44\x65viceClassList\x12@\n\x08metadata\x18\x01 \x01(\x0b\x32..k8s.io.apimachinery.pkg.apis.meta.v1.ListMeta\x12\x38\n\x05items\x18\x02 \x03(\x0b\x32).k8s.io.api.resource.v1alpha3.DeviceClass\"\x9a\x01\n\x0f\x44\x65viceClassSpec\x12?\n\tselectors\x18\x01 \x03(\x0b\x32,.k8s.io.api.resource.v1alpha3.DeviceSelector\x12\x46\n\x06\x63onfig\x18\x02 \x03(\x0b\x32\x36.k8s.io.api.resource.v1alpha3.DeviceClassConfiguration\"^\n\x13\x44\x65viceConfiguration\x12G\n\x06opaque\x18\x01 \x01(\x0b\x32\x37.k8s.io.api.resource.v1alpha3.OpaqueDeviceConfiguration\"<\n\x10\x44\x65viceConstraint\x12\x10\n\x08requests\x18\x01 \x03(\t\x12\x16\n\x0ematchAttribute\x18\x02 \x01(\t\"\xde\x01\n\x18\x44\x65viceCounterConsumption\x12\x12\n\ncounterSet\x18\x01 \x01(\t\x12V\n\x08\x63ounters\x18\x02 \x03(\x0b\x32\x44.k8s.io.api.resource.v1alpha3.DeviceCounterConsumption.CountersEntry\x1aV\n\rCountersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x34\n\x05value\x18\x02 \x01(\x0b\x32%.k8s.io.api.resource.v1alpha3.Counter:\x02\x38\x01\"\xc0\x02\n\rDeviceRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x17\n\x0f\x64\x65viceClassName\x18\x02 \x01(\t\x12?\n\tselectors\x18\x03 \x03(\x0b\x32,.k8s.io.api.resource.v1alpha3.DeviceSelector\x12\x16\n\x0e\x61llocationMode\x18\x04 \x01(\t\x12\r\n\x05\x63ount\x18\x05 \x01(\x03\x12\x13\n\x0b\x61\x64minAccess\x18\x06 \x01(\x08\x12\x46\n\x0e\x66irstAvailable\x18\x07 \x03(\x0b\x32..k8s.io.api.resource.v1alpha3.DeviceSubRequest\x12\x43\n\x0btolerations\x18\x08 \x03(\x0b\x32..k8s.io.api.resource.v1alpha3.DeviceToleration\"\xb8\x01\n\x1d\x44\x65viceRequestAllocationResult\x12\x0f\n\x07request\x18\x01 \x01(\t\x12\x0e\n\x06\x64river\x18\x02 \x01(\t\x12\x0c\n\x04pool\x18\x03 \x01(\t\x12\x0e\n\x06\x64\x65vice\x18\x04 \x01(\t\x12\x13\n\x0b\x61\x64minAccess\x18\x05 \x01(\x08\x12\x43\n\x0btolerations\x18\x06 \x03(\x0b\x32..k8s.io.api.resource.v1alpha3.DeviceToleration\"N\n\x0e\x44\x65viceSelector\x12<\n\x03\x63\x65l\x18\x01 \x01(\x0b\x32/.k8s.io.api.resource.v1alpha3.CELDeviceSelector\"\xe6\x01\n\x10\x44\x65viceSubRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x17\n\x0f\x64\x65viceClassName\x18\x02 \x01(\t\x12?\n\tselectors\x18\x03 \x03(\x0b\x32,.k8s.io.api.resource.v1alpha3.DeviceSelector\x12\x16\n\x0e\x61llocationMode\x18\x04 \x01(\t\x12\r\n\x05\x63ount\x18\x05 \x01(\x03\x12\x43\n\x0btolerations\x18\x07 \x03(\x0b\x32..k8s.io.api.resource.v1alpha3.DeviceToleration\"x\n\x0b\x44\x65viceTaint\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\x0e\n\x06\x65\x66\x66\x65\x63t\x18\x03 \x01(\t\x12=\n\ttimeAdded\x18\x04 \x01(\x0b\x32*.k8s.io.apimachinery.pkg.apis.meta.v1.Time\"\x96\x01\n\x0f\x44\x65viceTaintRule\x12\x42\n\x08metadata\x18\x01 \x01(\x0b\x32\x30.k8s.io.apimachinery.pkg.apis.meta.v1.ObjectMeta\x12?\n\x04spec\x18\x02 \x01(\x0b\x32\x31.k8s.io.api.resource.v1alpha3.DeviceTaintRuleSpec\"\x95\x01\n\x13\x44\x65viceTaintRuleList\x12@\n\x08metadata\x18\x01 \x01(\x0b\x32..k8s.io.apimachinery.pkg.apis.meta.v1.ListMeta\x12<\n\x05items\x18\x02 \x03(\x0b\x32-.k8s.io.api.resource.v1alpha3.DeviceTaintRule\"\x9a\x01\n\x13\x44\x65viceTaintRuleSpec\x12I\n\x0e\x64\x65viceSelector\x18\x01 \x01(\x0b\x32\x31.k8s.io.api.resource.v1alpha3.DeviceTaintSelector\x12\x38\n\x05taint\x18\x02 \x01(\x0b\x32).k8s.io.api.resource.v1alpha3.DeviceTaint\"\x9d\x01\n\x13\x44\x65viceTaintSelector\x12\x17\n\x0f\x64\x65viceClassName\x18\x01 \x01(\t\x12\x0e\n\x06\x64river\x18\x02 \x01(\t\x12\x0c\n\x04pool\x18\x03 \x01(\t\x12\x0e\n\x06\x64\x65vice\x18\x04 \x01(\t\x12?\n\tselectors\x18\x05 \x03(\x0b\x32,.k8s.io.api.resource.v1alpha3.DeviceSelector\"k\n\x10\x44\x65viceToleration\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x10\n\x08operator\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\x12\x0e\n\x06\x65\x66\x66\x65\x63t\x18\x04 \x01(\t\x12\x19\n\x11tolerationSeconds\x18\x05 \x01(\x03\"P\n\x11NetworkDeviceData\x12\x15\n\rinterfaceName\x18\x01 \x01(\t\x12\x0b\n\x03ips\x18\x02 \x03(\t\x12\x17\n\x0fhardwareAddress\x18\x03 \x01(\t\"n\n\x19OpaqueDeviceConfiguration\x12\x0e\n\x06\x64river\x18\x01 \x01(\t\x12\x41\n\nparameters\x18\x02 \x01(\x0b\x32-.k8s.io.apimachinery.pkg.runtime.RawExtension\"\xd5\x01\n\rResourceClaim\x12\x42\n\x08metadata\x18\x01 \x01(\x0b\x32\x30.k8s.io.apimachinery.pkg.apis.meta.v1.ObjectMeta\x12=\n\x04spec\x18\x02 \x01(\x0b\x32/.k8s.io.api.resource.v1alpha3.ResourceClaimSpec\x12\x41\n\x06status\x18\x03 \x01(\x0b\x32\x31.k8s.io.api.resource.v1alpha3.ResourceClaimStatus\"_\n\x1eResourceClaimConsumerReference\x12\x10\n\x08\x61piGroup\x18\x01 \x01(\t\x12\x10\n\x08resource\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x0b\n\x03uid\x18\x05 \x01(\t\"\x91\x01\n\x11ResourceClaimList\x12@\n\x08metadata\x18\x01 \x01(\x0b\x32..k8s.io.apimachinery.pkg.apis.meta.v1.ListMeta\x12:\n\x05items\x18\x02 \x03(\x0b\x32+.k8s.io.api.resource.v1alpha3.ResourceClaim\"O\n\x11ResourceClaimSpec\x12:\n\x07\x64\x65vices\x18\x01 \x01(\x0b\x32).k8s.io.api.resource.v1alpha3.DeviceClaim\"\xf2\x01\n\x13ResourceClaimStatus\x12\x42\n\nallocation\x18\x01 \x01(\x0b\x32..k8s.io.api.resource.v1alpha3.AllocationResult\x12Q\n\x0breservedFor\x18\x02 \x03(\x0b\x32<.k8s.io.api.resource.v1alpha3.ResourceClaimConsumerReference\x12\x44\n\x07\x64\x65vices\x18\x04 \x03(\x0b\x32\x33.k8s.io.api.resource.v1alpha3.AllocatedDeviceStatus\"\xa2\x01\n\x15ResourceClaimTemplate\x12\x42\n\x08metadata\x18\x01 \x01(\x0b\x32\x30.k8s.io.apimachinery.pkg.apis.meta.v1.ObjectMeta\x12\x45\n\x04spec\x18\x02 \x01(\x0b\x32\x37.k8s.io.api.resource.v1alpha3.ResourceClaimTemplateSpec\"\xa1\x01\n\x19ResourceClaimTemplateList\x12@\n\x08metadata\x18\x01 \x01(\x0b\x32..k8s.io.apimachinery.pkg.apis.meta.v1.ListMeta\x12\x42\n\x05items\x18\x02 \x03(\x0b\x32\x33.k8s.io.api.resource.v1alpha3.ResourceClaimTemplate\"\x9e\x01\n\x19ResourceClaimTemplateSpec\x12\x42\n\x08metadata\x18\x01 \x01(\x0b\x32\x30.k8s.io.apimachinery.pkg.apis.meta.v1.ObjectMeta\x12=\n\x04spec\x18\x02 \x01(\x0b\x32/.k8s.io.api.resource.v1alpha3.ResourceClaimSpec\"L\n\x0cResourcePool\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\ngeneration\x18\x02 \x01(\x03\x12\x1a\n\x12resourceSliceCount\x18\x03 \x01(\x03\"\x92\x01\n\rResourceSlice\x12\x42\n\x08metadata\x18\x01 \x01(\x0b\x32\x30.k8s.io.apimachinery.pkg.apis.meta.v1.ObjectMeta\x12=\n\x04spec\x18\x02 \x01(\x0b\x32/.k8s.io.api.resource.v1alpha3.ResourceSliceSpec\"\x91\x01\n\x11ResourceSliceList\x12@\n\x08metadata\x18\x01 \x01(\x0b\x32..k8s.io.apimachinery.pkg.apis.meta.v1.ListMeta\x12:\n\x05items\x18\x02 \x03(\x0b\x32+.k8s.io.api.resource.v1alpha3.ResourceSlice\"\xd2\x02\n\x11ResourceSliceSpec\x12\x0e\n\x06\x64river\x18\x01 \x01(\t\x12\x38\n\x04pool\x18\x02 \x01(\x0b\x32*.k8s.io.api.resource.v1alpha3.ResourcePool\x12\x10\n\x08nodeName\x18\x03 \x01(\t\x12\x36\n\x0cnodeSelector\x18\x04 \x01(\x0b\x32 .k8s.io.api.core.v1.NodeSelector\x12\x10\n\x08\x61llNodes\x18\x05 \x01(\x08\x12\x35\n\x07\x64\x65vices\x18\x06 \x03(\x0b\x32$.k8s.io.api.resource.v1alpha3.Device\x12\x1e\n\x16perDeviceNodeSelection\x18\x07 \x01(\x08\x12@\n\x0esharedCounters\x18\x08 \x03(\x0b\x32(.k8s.io.api.resource.v1alpha3.CounterSetB\x1eZ\x1ck8s.io/api/resource/v1alpha3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'k8s.io.api.resource.v1alpha3.generated_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\034k8s.io/api/resource/v1alpha3'
  _globals['_BASICDEVICE_ATTRIBUTESENTRY']._loaded_options = None
  _globals['_BASICDEVICE_ATTRIBUTESENTRY']._serialized_options = b'8\001'
  _globals['_BASICDEVICE_CAPACITYENTRY']._loaded_options = None
  _globals['_BASICDEVICE_CAPACITYENTRY']._serialized_options = b'8\001'
  _globals['_COUNTERSET_COUNTERSENTRY']._loaded_options = None
  _globals['_COUNTERSET_COUNTERSENTRY']._serialized_options = b'8\001'
  _globals['_DEVICECOUNTERCONSUMPTION_COUNTERSENTRY']._loaded_options = None
  _globals['_DEVICECOUNTERCONSUMPTION_COUNTERSENTRY']._serialized_options = b'8\001'
  _globals['_ALLOCATEDDEVICESTATUS']._serialized_start=328
  _globals['_ALLOCATEDDEVICESTATUS']._serialized_end=597
  _globals['_ALLOCATIONRESULT']._serialized_start=600
  _globals['_ALLOCATIONRESULT']._serialized_end=745
  _globals['_BASICDEVICE']._serialized_start=748
  _globals['_BASICDEVICE']._serialized_end=1343
  _globals['_BASICDEVICE_ATTRIBUTESENTRY']._serialized_start=1150
  _globals['_BASICDEVICE_ATTRIBUTESENTRY']._serialized_end=1246
  _globals['_BASICDEVICE_CAPACITYENTRY']._serialized_start=1248
  _globals['_BASICDEVICE_CAPACITYENTRY']._serialized_end=1343
  _globals['_CELDEVICESELECTOR']._serialized_start=1345
  _globals['_CELDEVICESELECTOR']._serialized_end=1384
  _globals['_COUNTER']._serialized_start=1386
  _globals['_COUNTER']._serialized_end=1458
  _globals['_COUNTERSET']._serialized_start=1461
  _globals['_COUNTERSET']._serialized_end=1649
  _globals['_COUNTERSET_COUNTERSENTRY']._serialized_start=1563
  _globals['_COUNTERSET_COUNTERSENTRY']._serialized_end=1649
  _globals['_DEVICE']._serialized_start=1651
  _globals['_DEVICE']._serialized_end=1731
  _globals['_DEVICEALLOCATIONCONFIGURATION']._serialized_start=1734
  _globals['_DEVICEALLOCATIONCONFIGURATION']._serialized_end=1879
  _globals['_DEVICEALLOCATIONRESULT']._serialized_start=1882
  _globals['_DEVICEALLOCATIONRESULT']._serialized_end=2061
  _globals['_DEVICEATTRIBUTE']._serialized_start=2063
  _globals['_DEVICEATTRIBUTE']._serialized_end=2140
  _globals['_DEVICECLAIM']._serialized_start=2143
  _globals['_DEVICECLAIM']._serialized_end=2360
  _globals['_DEVICECLAIMCONFIGURATION']._serialized_start=2362
  _globals['_DEVICECLAIMCONFIGURATION']._serialized_end=2486
  _globals['_DEVICECLASS']._serialized_start=2489
  _globals['_DEVICECLASS']._serialized_end=2631
  _globals['_DEVICECLASSCONFIGURATION']._serialized_start=2633
  _globals['_DEVICECLASSCONFIGURATION']._serialized_end=2739
  _globals['_DEVICECLASSLIST']._serialized_start=2742
  _globals['_DEVICECLASSLIST']._serialized_end=2883
  _globals['_DEVICECLASSSPEC']._serialized_start=2886
  _globals['_DEVICECLASSSPEC']._serialized_end=3040
  _globals['_DEVICECONFIGURATION']._serialized_start=3042
  _globals['_DEVICECONFIGURATION']._serialized_end=3136
  _globals['_DEVICECONSTRAINT']._serialized_start=3138
  _globals['_DEVICECONSTRAINT']._serialized_end=3198
  _globals['_DEVICECOUNTERCONSUMPTION']._serialized_start=3201
  _globals['_DEVICECOUNTERCONSUMPTION']._serialized_end=3423
  _globals['_DEVICECOUNTERCONSUMPTION_COUNTERSENTRY']._serialized_start=1563
  _globals['_DEVICECOUNTERCONSUMPTION_COUNTERSENTRY']._serialized_end=1649
  _globals['_DEVICEREQUEST']._serialized_start=3426
  _globals['_DEVICEREQUEST']._serialized_end=3746
  _globals['_DEVICEREQUESTALLOCATIONRESULT']._serialized_start=3749
  _globals['_DEVICEREQUESTALLOCATIONRESULT']._serialized_end=3933
  _globals['_DEVICESELECTOR']._serialized_start=3935
  _globals['_DEVICESELECTOR']._serialized_end=4013
  _globals['_DEVICESUBREQUEST']._serialized_start=4016
  _globals['_DEVICESUBREQUEST']._serialized_end=4246
  _globals['_DEVICETAINT']._serialized_start=4248
  _globals['_DEVICETAINT']._serialized_end=4368
  _globals['_DEVICETAINTRULE']._serialized_start=4371
  _globals['_DEVICETAINTRULE']._serialized_end=4521
  _globals['_DEVICETAINTRULELIST']._serialized_start=4524
  _globals['_DEVICETAINTRULELIST']._serialized_end=4673
  _globals['_DEVICETAINTRULESPEC']._serialized_start=4676
  _globals['_DEVICETAINTRULESPEC']._serialized_end=4830
  _globals['_DEVICETAINTSELECTOR']._serialized_start=4833
  _globals['_DEVICETAINTSELECTOR']._serialized_end=4990
  _globals['_DEVICETOLERATION']._serialized_start=4992
  _globals['_DEVICETOLERATION']._serialized_end=5099
  _globals['_NETWORKDEVICEDATA']._serialized_start=5101
  _globals['_NETWORKDEVICEDATA']._serialized_end=5181
  _globals['_OPAQUEDEVICECONFIGURATION']._serialized_start=5183
  _globals['_OPAQUEDEVICECONFIGURATION']._serialized_end=5293
  _globals['_RESOURCECLAIM']._serialized_start=5296
  _globals['_RESOURCECLAIM']._serialized_end=5509
  _globals['_RESOURCECLAIMCONSUMERREFERENCE']._serialized_start=5511
  _globals['_RESOURCECLAIMCONSUMERREFERENCE']._serialized_end=5606
  _globals['_RESOURCECLAIMLIST']._serialized_start=5609
  _globals['_RESOURCECLAIMLIST']._serialized_end=5754
  _globals['_RESOURCECLAIMSPEC']._serialized_start=5756
  _globals['_RESOURCECLAIMSPEC']._serialized_end=5835
  _globals['_RESOURCECLAIMSTATUS']._serialized_start=5838
  _globals['_RESOURCECLAIMSTATUS']._serialized_end=6080
  _globals['_RESOURCECLAIMTEMPLATE']._serialized_start=6083
  _globals['_RESOURCECLAIMTEMPLATE']._serialized_end=6245
  _globals['_RESOURCECLAIMTEMPLATELIST']._serialized_start=6248
  _globals['_RESOURCECLAIMTEMPLATELIST']._serialized_end=6409
  _globals['_RESOURCECLAIMTEMPLATESPEC']._serialized_start=6412
  _globals['_RESOURCECLAIMTEMPLATESPEC']._serialized_end=6570
  _globals['_RESOURCEPOOL']._serialized_start=6572
  _globals['_RESOURCEPOOL']._serialized_end=6648
  _globals['_RESOURCESLICE']._serialized_start=6651
  _globals['_RESOURCESLICE']._serialized_end=6797
  _globals['_RESOURCESLICELIST']._serialized_start=6800
  _globals['_RESOURCESLICELIST']._serialized_end=6945
  _globals['_RESOURCESLICESPEC']._serialized_start=6948
  _globals['_RESOURCESLICESPEC']._serialized_end=7286
# @@protoc_insertion_point(module_scope)
