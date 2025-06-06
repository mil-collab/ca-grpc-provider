# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: k8s.io/api/autoscaling/v2beta2/generated.proto
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
    'k8s.io/api/autoscaling/v2beta2/generated.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from k8s.io.api.core.v1 import generated_pb2 as k8s_dot_io_dot_api_dot_core_dot_v1_dot_generated__pb2
from k8s.io.apimachinery.pkg.api.resource import generated_pb2 as k8s_dot_io_dot_apimachinery_dot_pkg_dot_api_dot_resource_dot_generated__pb2
from k8s.io.apimachinery.pkg.apis.meta.v1 import generated_pb2 as k8s_dot_io_dot_apimachinery_dot_pkg_dot_apis_dot_meta_dot_v1_dot_generated__pb2
from k8s.io.apimachinery.pkg.runtime import generated_pb2 as k8s_dot_io_dot_apimachinery_dot_pkg_dot_runtime_dot_generated__pb2
from k8s.io.apimachinery.pkg.runtime.schema import generated_pb2 as k8s_dot_io_dot_apimachinery_dot_pkg_dot_runtime_dot_schema_dot_generated__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.k8s.io/api/autoscaling/v2beta2/generated.proto\x12\x1ek8s.io.api.autoscaling.v2beta2\x1a\"k8s.io/api/core/v1/generated.proto\x1a\x34k8s.io/apimachinery/pkg/api/resource/generated.proto\x1a\x34k8s.io/apimachinery/pkg/apis/meta/v1/generated.proto\x1a/k8s.io/apimachinery/pkg/runtime/generated.proto\x1a\x36k8s.io/apimachinery/pkg/runtime/schema/generated.proto\"~\n\x1d\x43ontainerResourceMetricSource\x12\x0c\n\x04name\x18\x01 \x01(\t\x12<\n\x06target\x18\x02 \x01(\x0b\x32,.k8s.io.api.autoscaling.v2beta2.MetricTarget\x12\x11\n\tcontainer\x18\x03 \x01(\t\"\x84\x01\n\x1d\x43ontainerResourceMetricStatus\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x42\n\x07\x63urrent\x18\x02 \x01(\x0b\x32\x31.k8s.io.api.autoscaling.v2beta2.MetricValueStatus\x12\x11\n\tcontainer\x18\x03 \x01(\t\"M\n\x1b\x43rossVersionObjectReference\x12\x0c\n\x04kind\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x12\n\napiVersion\x18\x03 \x01(\t\"\x96\x01\n\x14\x45xternalMetricSource\x12@\n\x06metric\x18\x01 \x01(\x0b\x32\x30.k8s.io.api.autoscaling.v2beta2.MetricIdentifier\x12<\n\x06target\x18\x02 \x01(\x0b\x32,.k8s.io.api.autoscaling.v2beta2.MetricTarget\"\x9c\x01\n\x14\x45xternalMetricStatus\x12@\n\x06metric\x18\x01 \x01(\x0b\x32\x30.k8s.io.api.autoscaling.v2beta2.MetricIdentifier\x12\x42\n\x07\x63urrent\x18\x02 \x01(\x0b\x32\x31.k8s.io.api.autoscaling.v2beta2.MetricValueStatus\"F\n\x10HPAScalingPolicy\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05\x12\x15\n\rperiodSeconds\x18\x03 \x01(\x05\"\x8f\x01\n\x0fHPAScalingRules\x12\"\n\x1astabilizationWindowSeconds\x18\x03 \x01(\x05\x12\x14\n\x0cselectPolicy\x18\x01 \x01(\t\x12\x42\n\x08policies\x18\x02 \x03(\x0b\x32\x30.k8s.io.api.autoscaling.v2beta2.HPAScalingPolicy\"\xf7\x01\n\x17HorizontalPodAutoscaler\x12\x42\n\x08metadata\x18\x01 \x01(\x0b\x32\x30.k8s.io.apimachinery.pkg.apis.meta.v1.ObjectMeta\x12I\n\x04spec\x18\x02 \x01(\x0b\x32;.k8s.io.api.autoscaling.v2beta2.HorizontalPodAutoscalerSpec\x12M\n\x06status\x18\x03 \x01(\x0b\x32=.k8s.io.api.autoscaling.v2beta2.HorizontalPodAutoscalerStatus\"\xa7\x01\n\x1fHorizontalPodAutoscalerBehavior\x12@\n\x07scaleUp\x18\x01 \x01(\x0b\x32/.k8s.io.api.autoscaling.v2beta2.HPAScalingRules\x12\x42\n\tscaleDown\x18\x02 \x01(\x0b\x32/.k8s.io.api.autoscaling.v2beta2.HPAScalingRules\"\xa9\x01\n HorizontalPodAutoscalerCondition\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t\x12\x46\n\x12lastTransitionTime\x18\x03 \x01(\x0b\x32*.k8s.io.apimachinery.pkg.apis.meta.v1.Time\x12\x0e\n\x06reason\x18\x04 \x01(\t\x12\x0f\n\x07message\x18\x05 \x01(\t\"\xa7\x01\n\x1bHorizontalPodAutoscalerList\x12@\n\x08metadata\x18\x01 \x01(\x0b\x32..k8s.io.apimachinery.pkg.apis.meta.v1.ListMeta\x12\x46\n\x05items\x18\x02 \x03(\x0b\x32\x37.k8s.io.api.autoscaling.v2beta2.HorizontalPodAutoscaler\"\xac\x02\n\x1bHorizontalPodAutoscalerSpec\x12S\n\x0escaleTargetRef\x18\x01 \x01(\x0b\x32;.k8s.io.api.autoscaling.v2beta2.CrossVersionObjectReference\x12\x13\n\x0bminReplicas\x18\x02 \x01(\x05\x12\x13\n\x0bmaxReplicas\x18\x03 \x01(\x05\x12;\n\x07metrics\x18\x04 \x03(\x0b\x32*.k8s.io.api.autoscaling.v2beta2.MetricSpec\x12Q\n\x08\x62\x65havior\x18\x05 \x01(\x0b\x32?.k8s.io.api.autoscaling.v2beta2.HorizontalPodAutoscalerBehavior\"\xcc\x02\n\x1dHorizontalPodAutoscalerStatus\x12\x1a\n\x12observedGeneration\x18\x01 \x01(\x03\x12\x41\n\rlastScaleTime\x18\x02 \x01(\x0b\x32*.k8s.io.apimachinery.pkg.apis.meta.v1.Time\x12\x17\n\x0f\x63urrentReplicas\x18\x03 \x01(\x05\x12\x17\n\x0f\x64\x65siredReplicas\x18\x04 \x01(\x05\x12\x44\n\x0e\x63urrentMetrics\x18\x05 \x03(\x0b\x32,.k8s.io.api.autoscaling.v2beta2.MetricStatus\x12T\n\nconditions\x18\x06 \x03(\x0b\x32@.k8s.io.api.autoscaling.v2beta2.HorizontalPodAutoscalerCondition\"g\n\x10MetricIdentifier\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x45\n\x08selector\x18\x02 \x01(\x0b\x32\x33.k8s.io.apimachinery.pkg.apis.meta.v1.LabelSelector\"\x88\x03\n\nMetricSpec\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x42\n\x06object\x18\x02 \x01(\x0b\x32\x32.k8s.io.api.autoscaling.v2beta2.ObjectMetricSource\x12>\n\x04pods\x18\x03 \x01(\x0b\x32\x30.k8s.io.api.autoscaling.v2beta2.PodsMetricSource\x12\x46\n\x08resource\x18\x04 \x01(\x0b\x32\x34.k8s.io.api.autoscaling.v2beta2.ResourceMetricSource\x12X\n\x11\x63ontainerResource\x18\x07 \x01(\x0b\x32=.k8s.io.api.autoscaling.v2beta2.ContainerResourceMetricSource\x12\x46\n\x08\x65xternal\x18\x05 \x01(\x0b\x32\x34.k8s.io.api.autoscaling.v2beta2.ExternalMetricSource\"\x8a\x03\n\x0cMetricStatus\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x42\n\x06object\x18\x02 \x01(\x0b\x32\x32.k8s.io.api.autoscaling.v2beta2.ObjectMetricStatus\x12>\n\x04pods\x18\x03 \x01(\x0b\x32\x30.k8s.io.api.autoscaling.v2beta2.PodsMetricStatus\x12\x46\n\x08resource\x18\x04 \x01(\x0b\x32\x34.k8s.io.api.autoscaling.v2beta2.ResourceMetricStatus\x12X\n\x11\x63ontainerResource\x18\x07 \x01(\x0b\x32=.k8s.io.api.autoscaling.v2beta2.ContainerResourceMetricStatus\x12\x46\n\x08\x65xternal\x18\x05 \x01(\x0b\x32\x34.k8s.io.api.autoscaling.v2beta2.ExternalMetricStatus\"\xbd\x01\n\x0cMetricTarget\x12\x0c\n\x04type\x18\x01 \x01(\t\x12=\n\x05value\x18\x02 \x01(\x0b\x32..k8s.io.apimachinery.pkg.api.resource.Quantity\x12\x44\n\x0c\x61verageValue\x18\x03 \x01(\x0b\x32..k8s.io.apimachinery.pkg.api.resource.Quantity\x12\x1a\n\x12\x61verageUtilization\x18\x04 \x01(\x05\"\xb4\x01\n\x11MetricValueStatus\x12=\n\x05value\x18\x01 \x01(\x0b\x32..k8s.io.apimachinery.pkg.api.resource.Quantity\x12\x44\n\x0c\x61verageValue\x18\x02 \x01(\x0b\x32..k8s.io.apimachinery.pkg.api.resource.Quantity\x12\x1a\n\x12\x61verageUtilization\x18\x03 \x01(\x05\"\xea\x01\n\x12ObjectMetricSource\x12T\n\x0f\x64\x65scribedObject\x18\x01 \x01(\x0b\x32;.k8s.io.api.autoscaling.v2beta2.CrossVersionObjectReference\x12<\n\x06target\x18\x02 \x01(\x0b\x32,.k8s.io.api.autoscaling.v2beta2.MetricTarget\x12@\n\x06metric\x18\x03 \x01(\x0b\x32\x30.k8s.io.api.autoscaling.v2beta2.MetricIdentifier\"\xf0\x01\n\x12ObjectMetricStatus\x12@\n\x06metric\x18\x01 \x01(\x0b\x32\x30.k8s.io.api.autoscaling.v2beta2.MetricIdentifier\x12\x42\n\x07\x63urrent\x18\x02 \x01(\x0b\x32\x31.k8s.io.api.autoscaling.v2beta2.MetricValueStatus\x12T\n\x0f\x64\x65scribedObject\x18\x03 \x01(\x0b\x32;.k8s.io.api.autoscaling.v2beta2.CrossVersionObjectReference\"\x92\x01\n\x10PodsMetricSource\x12@\n\x06metric\x18\x01 \x01(\x0b\x32\x30.k8s.io.api.autoscaling.v2beta2.MetricIdentifier\x12<\n\x06target\x18\x02 \x01(\x0b\x32,.k8s.io.api.autoscaling.v2beta2.MetricTarget\"\x98\x01\n\x10PodsMetricStatus\x12@\n\x06metric\x18\x01 \x01(\x0b\x32\x30.k8s.io.api.autoscaling.v2beta2.MetricIdentifier\x12\x42\n\x07\x63urrent\x18\x02 \x01(\x0b\x32\x31.k8s.io.api.autoscaling.v2beta2.MetricValueStatus\"b\n\x14ResourceMetricSource\x12\x0c\n\x04name\x18\x01 \x01(\t\x12<\n\x06target\x18\x02 \x01(\x0b\x32,.k8s.io.api.autoscaling.v2beta2.MetricTarget\"h\n\x14ResourceMetricStatus\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x42\n\x07\x63urrent\x18\x02 \x01(\x0b\x32\x31.k8s.io.api.autoscaling.v2beta2.MetricValueStatusB Z\x1ek8s.io/api/autoscaling/v2beta2')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'k8s.io.api.autoscaling.v2beta2.generated_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\036k8s.io/api/autoscaling/v2beta2'
  _globals['_CONTAINERRESOURCEMETRICSOURCE']._serialized_start=331
  _globals['_CONTAINERRESOURCEMETRICSOURCE']._serialized_end=457
  _globals['_CONTAINERRESOURCEMETRICSTATUS']._serialized_start=460
  _globals['_CONTAINERRESOURCEMETRICSTATUS']._serialized_end=592
  _globals['_CROSSVERSIONOBJECTREFERENCE']._serialized_start=594
  _globals['_CROSSVERSIONOBJECTREFERENCE']._serialized_end=671
  _globals['_EXTERNALMETRICSOURCE']._serialized_start=674
  _globals['_EXTERNALMETRICSOURCE']._serialized_end=824
  _globals['_EXTERNALMETRICSTATUS']._serialized_start=827
  _globals['_EXTERNALMETRICSTATUS']._serialized_end=983
  _globals['_HPASCALINGPOLICY']._serialized_start=985
  _globals['_HPASCALINGPOLICY']._serialized_end=1055
  _globals['_HPASCALINGRULES']._serialized_start=1058
  _globals['_HPASCALINGRULES']._serialized_end=1201
  _globals['_HORIZONTALPODAUTOSCALER']._serialized_start=1204
  _globals['_HORIZONTALPODAUTOSCALER']._serialized_end=1451
  _globals['_HORIZONTALPODAUTOSCALERBEHAVIOR']._serialized_start=1454
  _globals['_HORIZONTALPODAUTOSCALERBEHAVIOR']._serialized_end=1621
  _globals['_HORIZONTALPODAUTOSCALERCONDITION']._serialized_start=1624
  _globals['_HORIZONTALPODAUTOSCALERCONDITION']._serialized_end=1793
  _globals['_HORIZONTALPODAUTOSCALERLIST']._serialized_start=1796
  _globals['_HORIZONTALPODAUTOSCALERLIST']._serialized_end=1963
  _globals['_HORIZONTALPODAUTOSCALERSPEC']._serialized_start=1966
  _globals['_HORIZONTALPODAUTOSCALERSPEC']._serialized_end=2266
  _globals['_HORIZONTALPODAUTOSCALERSTATUS']._serialized_start=2269
  _globals['_HORIZONTALPODAUTOSCALERSTATUS']._serialized_end=2601
  _globals['_METRICIDENTIFIER']._serialized_start=2603
  _globals['_METRICIDENTIFIER']._serialized_end=2706
  _globals['_METRICSPEC']._serialized_start=2709
  _globals['_METRICSPEC']._serialized_end=3101
  _globals['_METRICSTATUS']._serialized_start=3104
  _globals['_METRICSTATUS']._serialized_end=3498
  _globals['_METRICTARGET']._serialized_start=3501
  _globals['_METRICTARGET']._serialized_end=3690
  _globals['_METRICVALUESTATUS']._serialized_start=3693
  _globals['_METRICVALUESTATUS']._serialized_end=3873
  _globals['_OBJECTMETRICSOURCE']._serialized_start=3876
  _globals['_OBJECTMETRICSOURCE']._serialized_end=4110
  _globals['_OBJECTMETRICSTATUS']._serialized_start=4113
  _globals['_OBJECTMETRICSTATUS']._serialized_end=4353
  _globals['_PODSMETRICSOURCE']._serialized_start=4356
  _globals['_PODSMETRICSOURCE']._serialized_end=4502
  _globals['_PODSMETRICSTATUS']._serialized_start=4505
  _globals['_PODSMETRICSTATUS']._serialized_end=4657
  _globals['_RESOURCEMETRICSOURCE']._serialized_start=4659
  _globals['_RESOURCEMETRICSOURCE']._serialized_end=4757
  _globals['_RESOURCEMETRICSTATUS']._serialized_start=4759
  _globals['_RESOURCEMETRICSTATUS']._serialized_end=4863
# @@protoc_insertion_point(module_scope)
