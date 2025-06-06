# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: k8s.io/apimachinery/pkg/apis/meta/v1/generated.proto
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
    'k8s.io/apimachinery/pkg/apis/meta/v1/generated.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from k8s.io.apimachinery.pkg.runtime import generated_pb2 as k8s_dot_io_dot_apimachinery_dot_pkg_dot_runtime_dot_generated__pb2
from k8s.io.apimachinery.pkg.runtime.schema import generated_pb2 as k8s_dot_io_dot_apimachinery_dot_pkg_dot_runtime_dot_schema_dot_generated__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4k8s.io/apimachinery/pkg/apis/meta/v1/generated.proto\x12$k8s.io.apimachinery.pkg.apis.meta.v1\x1a/k8s.io/apimachinery/pkg/runtime/generated.proto\x1a\x36k8s.io/apimachinery/pkg/runtime/schema/generated.proto\"\xa9\x02\n\x08\x41PIGroup\x12\x0c\n\x04name\x18\x01 \x01(\t\x12P\n\x08versions\x18\x02 \x03(\x0b\x32>.k8s.io.apimachinery.pkg.apis.meta.v1.GroupVersionForDiscovery\x12X\n\x10preferredVersion\x18\x03 \x01(\x0b\x32>.k8s.io.apimachinery.pkg.apis.meta.v1.GroupVersionForDiscovery\x12\x63\n\x1aserverAddressByClientCIDRs\x18\x04 \x03(\x0b\x32?.k8s.io.apimachinery.pkg.apis.meta.v1.ServerAddressByClientCIDR\"N\n\x0c\x41PIGroupList\x12>\n\x06groups\x18\x01 \x03(\x0b\x32..k8s.io.apimachinery.pkg.apis.meta.v1.APIGroup\"\xf3\x01\n\x0b\x41PIResource\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0csingularName\x18\x06 \x01(\t\x12\x12\n\nnamespaced\x18\x02 \x01(\x08\x12\r\n\x05group\x18\x08 \x01(\t\x12\x0f\n\x07version\x18\t \x01(\t\x12\x0c\n\x04kind\x18\x03 \x01(\t\x12:\n\x05verbs\x18\x04 \x01(\x0b\x32+.k8s.io.apimachinery.pkg.apis.meta.v1.Verbs\x12\x12\n\nshortNames\x18\x05 \x03(\t\x12\x12\n\ncategories\x18\x07 \x03(\t\x12\x1a\n\x12storageVersionHash\x18\n \x01(\t\"m\n\x0f\x41PIResourceList\x12\x14\n\x0cgroupVersion\x18\x01 \x01(\t\x12\x44\n\tresources\x18\x02 \x03(\x0b\x32\x31.k8s.io.apimachinery.pkg.apis.meta.v1.APIResource\"\x84\x01\n\x0b\x41PIVersions\x12\x10\n\x08versions\x18\x01 \x03(\t\x12\x63\n\x1aserverAddressByClientCIDRs\x18\x02 \x03(\x0b\x32?.k8s.io.apimachinery.pkg.apis.meta.v1.ServerAddressByClientCIDR\"C\n\x0c\x41pplyOptions\x12\x0e\n\x06\x64ryRun\x18\x01 \x03(\t\x12\r\n\x05\x66orce\x18\x02 \x01(\x08\x12\x14\n\x0c\x66ieldManager\x18\x03 \x01(\t\"\xae\x01\n\tCondition\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t\x12\x1a\n\x12observedGeneration\x18\x03 \x01(\x03\x12\x46\n\x12lastTransitionTime\x18\x04 \x01(\x0b\x32*.k8s.io.apimachinery.pkg.apis.meta.v1.Time\x12\x0e\n\x06reason\x18\x05 \x01(\t\x12\x0f\n\x07message\x18\x06 \x01(\t\"N\n\rCreateOptions\x12\x0e\n\x06\x64ryRun\x18\x01 \x03(\t\x12\x14\n\x0c\x66ieldManager\x18\x03 \x01(\t\x12\x17\n\x0f\x66ieldValidation\x18\x04 \x01(\t\"\xf6\x01\n\rDeleteOptions\x12\x1a\n\x12gracePeriodSeconds\x18\x01 \x01(\x03\x12J\n\rpreconditions\x18\x02 \x01(\x0b\x32\x33.k8s.io.apimachinery.pkg.apis.meta.v1.Preconditions\x12\x18\n\x10orphanDependents\x18\x03 \x01(\x08\x12\x19\n\x11propagationPolicy\x18\x04 \x01(\t\x12\x0e\n\x06\x64ryRun\x18\x05 \x03(\t\x12\x38\n0ignoreStoreReadErrorWithClusterBreakingPotential\x18\x06 \x01(\x08\"\x1c\n\x08\x44uration\x12\x10\n\x08\x64uration\x18\x01 \x01(\x03\"I\n\x18\x46ieldSelectorRequirement\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x10\n\x08operator\x18\x02 \x01(\t\x12\x0e\n\x06values\x18\x03 \x03(\t\"\x17\n\x08\x46ieldsV1\x12\x0b\n\x03Raw\x18\x01 \x01(\x0c\"%\n\nGetOptions\x12\x17\n\x0fresourceVersion\x18\x01 \x01(\t\"(\n\tGroupKind\x12\r\n\x05group\x18\x01 \x01(\t\x12\x0c\n\x04kind\x18\x02 \x01(\t\"0\n\rGroupResource\x12\r\n\x05group\x18\x01 \x01(\t\x12\x10\n\x08resource\x18\x02 \x01(\t\".\n\x0cGroupVersion\x12\r\n\x05group\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\"A\n\x18GroupVersionForDiscovery\x12\x14\n\x0cgroupVersion\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\"@\n\x10GroupVersionKind\x12\r\n\x05group\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x0c\n\x04kind\x18\x03 \x01(\t\"H\n\x14GroupVersionResource\x12\r\n\x05group\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x10\n\x08resource\x18\x03 \x01(\t\"\xf8\x01\n\rLabelSelector\x12Y\n\x0bmatchLabels\x18\x01 \x03(\x0b\x32\x44.k8s.io.apimachinery.pkg.apis.meta.v1.LabelSelector.MatchLabelsEntry\x12X\n\x10matchExpressions\x18\x02 \x03(\x0b\x32>.k8s.io.apimachinery.pkg.apis.meta.v1.LabelSelectorRequirement\x1a\x32\n\x10MatchLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"I\n\x18LabelSelectorRequirement\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x10\n\x08operator\x18\x02 \x01(\t\x12\x0e\n\x06values\x18\x03 \x03(\t\"\x86\x01\n\x04List\x12@\n\x08metadata\x18\x01 \x01(\x0b\x32..k8s.io.apimachinery.pkg.apis.meta.v1.ListMeta\x12<\n\x05items\x18\x02 \x03(\x0b\x32-.k8s.io.apimachinery.pkg.runtime.RawExtension\"c\n\x08ListMeta\x12\x10\n\x08selfLink\x18\x01 \x01(\t\x12\x17\n\x0fresourceVersion\x18\x02 \x01(\t\x12\x10\n\x08\x63ontinue\x18\x03 \x01(\t\x12\x1a\n\x12remainingItemCount\x18\x04 \x01(\x03\"\xf2\x01\n\x0bListOptions\x12\x15\n\rlabelSelector\x18\x01 \x01(\t\x12\x15\n\rfieldSelector\x18\x02 \x01(\t\x12\r\n\x05watch\x18\x03 \x01(\x08\x12\x1b\n\x13\x61llowWatchBookmarks\x18\t \x01(\x08\x12\x17\n\x0fresourceVersion\x18\x04 \x01(\t\x12\x1c\n\x14resourceVersionMatch\x18\n \x01(\t\x12\x16\n\x0etimeoutSeconds\x18\x05 \x01(\x03\x12\r\n\x05limit\x18\x07 \x01(\x03\x12\x10\n\x08\x63ontinue\x18\x08 \x01(\t\x12\x19\n\x11sendInitialEvents\x18\x0b \x01(\x08\"\xf1\x01\n\x12ManagedFieldsEntry\x12\x0f\n\x07manager\x18\x01 \x01(\t\x12\x11\n\toperation\x18\x02 \x01(\t\x12\x12\n\napiVersion\x18\x03 \x01(\t\x12\x38\n\x04time\x18\x04 \x01(\x0b\x32*.k8s.io.apimachinery.pkg.apis.meta.v1.Time\x12\x12\n\nfieldsType\x18\x06 \x01(\t\x12@\n\x08\x66ieldsV1\x18\x07 \x01(\x0b\x32..k8s.io.apimachinery.pkg.apis.meta.v1.FieldsV1\x12\x13\n\x0bsubresource\x18\x08 \x01(\t\"+\n\tMicroTime\x12\x0f\n\x07seconds\x18\x01 \x01(\x03\x12\r\n\x05nanos\x18\x02 \x01(\x05\"\xfe\x05\n\nObjectMeta\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cgenerateName\x18\x02 \x01(\t\x12\x11\n\tnamespace\x18\x03 \x01(\t\x12\x10\n\x08selfLink\x18\x04 \x01(\t\x12\x0b\n\x03uid\x18\x05 \x01(\t\x12\x17\n\x0fresourceVersion\x18\x06 \x01(\t\x12\x12\n\ngeneration\x18\x07 \x01(\x03\x12\x45\n\x11\x63reationTimestamp\x18\x08 \x01(\x0b\x32*.k8s.io.apimachinery.pkg.apis.meta.v1.Time\x12\x45\n\x11\x64\x65letionTimestamp\x18\t \x01(\x0b\x32*.k8s.io.apimachinery.pkg.apis.meta.v1.Time\x12\"\n\x1a\x64\x65letionGracePeriodSeconds\x18\n \x01(\x03\x12L\n\x06labels\x18\x0b \x03(\x0b\x32<.k8s.io.apimachinery.pkg.apis.meta.v1.ObjectMeta.LabelsEntry\x12V\n\x0b\x61nnotations\x18\x0c \x03(\x0b\x32\x41.k8s.io.apimachinery.pkg.apis.meta.v1.ObjectMeta.AnnotationsEntry\x12M\n\x0fownerReferences\x18\r \x03(\x0b\x32\x34.k8s.io.apimachinery.pkg.apis.meta.v1.OwnerReference\x12\x12\n\nfinalizers\x18\x0e \x03(\t\x12O\n\rmanagedFields\x18\x11 \x03(\x0b\x32\x38.k8s.io.apimachinery.pkg.apis.meta.v1.ManagedFieldsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x32\n\x10\x41nnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"}\n\x0eOwnerReference\x12\x12\n\napiVersion\x18\x05 \x01(\t\x12\x0c\n\x04kind\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0b\n\x03uid\x18\x04 \x01(\t\x12\x12\n\ncontroller\x18\x06 \x01(\x08\x12\x1a\n\x12\x62lockOwnerDeletion\x18\x07 \x01(\x08\"[\n\x15PartialObjectMetadata\x12\x42\n\x08metadata\x18\x01 \x01(\x0b\x32\x30.k8s.io.apimachinery.pkg.apis.meta.v1.ObjectMeta\"\xa9\x01\n\x19PartialObjectMetadataList\x12@\n\x08metadata\x18\x01 \x01(\x0b\x32..k8s.io.apimachinery.pkg.apis.meta.v1.ListMeta\x12J\n\x05items\x18\x02 \x03(\x0b\x32;.k8s.io.apimachinery.pkg.apis.meta.v1.PartialObjectMetadata\"\x07\n\x05Patch\"\\\n\x0cPatchOptions\x12\x0e\n\x06\x64ryRun\x18\x01 \x03(\t\x12\r\n\x05\x66orce\x18\x02 \x01(\x08\x12\x14\n\x0c\x66ieldManager\x18\x03 \x01(\t\x12\x17\n\x0f\x66ieldValidation\x18\x04 \x01(\t\"5\n\rPreconditions\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12\x17\n\x0fresourceVersion\x18\x02 \x01(\t\"\x1a\n\tRootPaths\x12\r\n\x05paths\x18\x01 \x03(\t\"F\n\x19ServerAddressByClientCIDR\x12\x12\n\nclientCIDR\x18\x01 \x01(\t\x12\x15\n\rserverAddress\x18\x02 \x01(\t\"\xcf\x01\n\x06Status\x12@\n\x08metadata\x18\x01 \x01(\x0b\x32..k8s.io.apimachinery.pkg.apis.meta.v1.ListMeta\x12\x0e\n\x06status\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\t\x12\x0e\n\x06reason\x18\x04 \x01(\t\x12\x44\n\x07\x64\x65tails\x18\x05 \x01(\x0b\x32\x33.k8s.io.apimachinery.pkg.apis.meta.v1.StatusDetails\x12\x0c\n\x04\x63ode\x18\x06 \x01(\x05\"=\n\x0bStatusCause\x12\x0e\n\x06reason\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\r\n\x05\x66ield\x18\x03 \x01(\t\"\xa5\x01\n\rStatusDetails\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05group\x18\x02 \x01(\t\x12\x0c\n\x04kind\x18\x03 \x01(\t\x12\x0b\n\x03uid\x18\x06 \x01(\t\x12\x41\n\x06\x63\x61uses\x18\x04 \x03(\x0b\x32\x31.k8s.io.apimachinery.pkg.apis.meta.v1.StatusCause\x12\x19\n\x11retryAfterSeconds\x18\x05 \x01(\x05\"%\n\x0cTableOptions\x12\x15\n\rincludeObject\x18\x01 \x01(\t\"&\n\x04Time\x12\x0f\n\x07seconds\x18\x01 \x01(\x03\x12\r\n\x05nanos\x18\x02 \x01(\x05\"+\n\tTimestamp\x12\x0f\n\x07seconds\x18\x01 \x01(\x03\x12\r\n\x05nanos\x18\x02 \x01(\x05\",\n\x08TypeMeta\x12\x0c\n\x04kind\x18\x01 \x01(\t\x12\x12\n\napiVersion\x18\x02 \x01(\t\"N\n\rUpdateOptions\x12\x0e\n\x06\x64ryRun\x18\x01 \x03(\t\x12\x14\n\x0c\x66ieldManager\x18\x02 \x01(\t\x12\x17\n\x0f\x66ieldValidation\x18\x03 \x01(\t\"\x16\n\x05Verbs\x12\r\n\x05items\x18\x01 \x03(\t\"Y\n\nWatchEvent\x12\x0c\n\x04type\x18\x01 \x01(\t\x12=\n\x06object\x18\x02 \x01(\x0b\x32-.k8s.io.apimachinery.pkg.runtime.RawExtensionB&Z$k8s.io/apimachinery/pkg/apis/meta/v1')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'k8s.io.apimachinery.pkg.apis.meta.v1.generated_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z$k8s.io/apimachinery/pkg/apis/meta/v1'
  _globals['_LABELSELECTOR_MATCHLABELSENTRY']._loaded_options = None
  _globals['_LABELSELECTOR_MATCHLABELSENTRY']._serialized_options = b'8\001'
  _globals['_OBJECTMETA_LABELSENTRY']._loaded_options = None
  _globals['_OBJECTMETA_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_OBJECTMETA_ANNOTATIONSENTRY']._loaded_options = None
  _globals['_OBJECTMETA_ANNOTATIONSENTRY']._serialized_options = b'8\001'
  _globals['_APIGROUP']._serialized_start=200
  _globals['_APIGROUP']._serialized_end=497
  _globals['_APIGROUPLIST']._serialized_start=499
  _globals['_APIGROUPLIST']._serialized_end=577
  _globals['_APIRESOURCE']._serialized_start=580
  _globals['_APIRESOURCE']._serialized_end=823
  _globals['_APIRESOURCELIST']._serialized_start=825
  _globals['_APIRESOURCELIST']._serialized_end=934
  _globals['_APIVERSIONS']._serialized_start=937
  _globals['_APIVERSIONS']._serialized_end=1069
  _globals['_APPLYOPTIONS']._serialized_start=1071
  _globals['_APPLYOPTIONS']._serialized_end=1138
  _globals['_CONDITION']._serialized_start=1141
  _globals['_CONDITION']._serialized_end=1315
  _globals['_CREATEOPTIONS']._serialized_start=1317
  _globals['_CREATEOPTIONS']._serialized_end=1395
  _globals['_DELETEOPTIONS']._serialized_start=1398
  _globals['_DELETEOPTIONS']._serialized_end=1644
  _globals['_DURATION']._serialized_start=1646
  _globals['_DURATION']._serialized_end=1674
  _globals['_FIELDSELECTORREQUIREMENT']._serialized_start=1676
  _globals['_FIELDSELECTORREQUIREMENT']._serialized_end=1749
  _globals['_FIELDSV1']._serialized_start=1751
  _globals['_FIELDSV1']._serialized_end=1774
  _globals['_GETOPTIONS']._serialized_start=1776
  _globals['_GETOPTIONS']._serialized_end=1813
  _globals['_GROUPKIND']._serialized_start=1815
  _globals['_GROUPKIND']._serialized_end=1855
  _globals['_GROUPRESOURCE']._serialized_start=1857
  _globals['_GROUPRESOURCE']._serialized_end=1905
  _globals['_GROUPVERSION']._serialized_start=1907
  _globals['_GROUPVERSION']._serialized_end=1953
  _globals['_GROUPVERSIONFORDISCOVERY']._serialized_start=1955
  _globals['_GROUPVERSIONFORDISCOVERY']._serialized_end=2020
  _globals['_GROUPVERSIONKIND']._serialized_start=2022
  _globals['_GROUPVERSIONKIND']._serialized_end=2086
  _globals['_GROUPVERSIONRESOURCE']._serialized_start=2088
  _globals['_GROUPVERSIONRESOURCE']._serialized_end=2160
  _globals['_LABELSELECTOR']._serialized_start=2163
  _globals['_LABELSELECTOR']._serialized_end=2411
  _globals['_LABELSELECTOR_MATCHLABELSENTRY']._serialized_start=2361
  _globals['_LABELSELECTOR_MATCHLABELSENTRY']._serialized_end=2411
  _globals['_LABELSELECTORREQUIREMENT']._serialized_start=2413
  _globals['_LABELSELECTORREQUIREMENT']._serialized_end=2486
  _globals['_LIST']._serialized_start=2489
  _globals['_LIST']._serialized_end=2623
  _globals['_LISTMETA']._serialized_start=2625
  _globals['_LISTMETA']._serialized_end=2724
  _globals['_LISTOPTIONS']._serialized_start=2727
  _globals['_LISTOPTIONS']._serialized_end=2969
  _globals['_MANAGEDFIELDSENTRY']._serialized_start=2972
  _globals['_MANAGEDFIELDSENTRY']._serialized_end=3213
  _globals['_MICROTIME']._serialized_start=3215
  _globals['_MICROTIME']._serialized_end=3258
  _globals['_OBJECTMETA']._serialized_start=3261
  _globals['_OBJECTMETA']._serialized_end=4027
  _globals['_OBJECTMETA_LABELSENTRY']._serialized_start=3930
  _globals['_OBJECTMETA_LABELSENTRY']._serialized_end=3975
  _globals['_OBJECTMETA_ANNOTATIONSENTRY']._serialized_start=3977
  _globals['_OBJECTMETA_ANNOTATIONSENTRY']._serialized_end=4027
  _globals['_OWNERREFERENCE']._serialized_start=4029
  _globals['_OWNERREFERENCE']._serialized_end=4154
  _globals['_PARTIALOBJECTMETADATA']._serialized_start=4156
  _globals['_PARTIALOBJECTMETADATA']._serialized_end=4247
  _globals['_PARTIALOBJECTMETADATALIST']._serialized_start=4250
  _globals['_PARTIALOBJECTMETADATALIST']._serialized_end=4419
  _globals['_PATCH']._serialized_start=4421
  _globals['_PATCH']._serialized_end=4428
  _globals['_PATCHOPTIONS']._serialized_start=4430
  _globals['_PATCHOPTIONS']._serialized_end=4522
  _globals['_PRECONDITIONS']._serialized_start=4524
  _globals['_PRECONDITIONS']._serialized_end=4577
  _globals['_ROOTPATHS']._serialized_start=4579
  _globals['_ROOTPATHS']._serialized_end=4605
  _globals['_SERVERADDRESSBYCLIENTCIDR']._serialized_start=4607
  _globals['_SERVERADDRESSBYCLIENTCIDR']._serialized_end=4677
  _globals['_STATUS']._serialized_start=4680
  _globals['_STATUS']._serialized_end=4887
  _globals['_STATUSCAUSE']._serialized_start=4889
  _globals['_STATUSCAUSE']._serialized_end=4950
  _globals['_STATUSDETAILS']._serialized_start=4953
  _globals['_STATUSDETAILS']._serialized_end=5118
  _globals['_TABLEOPTIONS']._serialized_start=5120
  _globals['_TABLEOPTIONS']._serialized_end=5157
  _globals['_TIME']._serialized_start=5159
  _globals['_TIME']._serialized_end=5197
  _globals['_TIMESTAMP']._serialized_start=5199
  _globals['_TIMESTAMP']._serialized_end=5242
  _globals['_TYPEMETA']._serialized_start=5244
  _globals['_TYPEMETA']._serialized_end=5288
  _globals['_UPDATEOPTIONS']._serialized_start=5290
  _globals['_UPDATEOPTIONS']._serialized_end=5368
  _globals['_VERBS']._serialized_start=5370
  _globals['_VERBS']._serialized_end=5392
  _globals['_WATCHEVENT']._serialized_start=5394
  _globals['_WATCHEVENT']._serialized_end=5483
# @@protoc_insertion_point(module_scope)
