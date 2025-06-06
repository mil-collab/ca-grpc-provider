# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: k8s.io/api/admissionregistration/v1beta1/generated.proto
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
    'k8s.io/api/admissionregistration/v1beta1/generated.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from k8s.io.api.admissionregistration.v1 import generated_pb2 as k8s_dot_io_dot_api_dot_admissionregistration_dot_v1_dot_generated__pb2
from k8s.io.apimachinery.pkg.apis.meta.v1 import generated_pb2 as k8s_dot_io_dot_apimachinery_dot_pkg_dot_apis_dot_meta_dot_v1_dot_generated__pb2
from k8s.io.apimachinery.pkg.runtime import generated_pb2 as k8s_dot_io_dot_apimachinery_dot_pkg_dot_runtime_dot_generated__pb2
from k8s.io.apimachinery.pkg.runtime.schema import generated_pb2 as k8s_dot_io_dot_apimachinery_dot_pkg_dot_runtime_dot_schema_dot_generated__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8k8s.io/api/admissionregistration/v1beta1/generated.proto\x12(k8s.io.api.admissionregistration.v1beta1\x1a\x33k8s.io/api/admissionregistration/v1/generated.proto\x1a\x34k8s.io/apimachinery/pkg/apis/meta/v1/generated.proto\x1a/k8s.io/apimachinery/pkg/runtime/generated.proto\x1a\x36k8s.io/apimachinery/pkg/runtime/schema/generated.proto\"7\n\x0f\x41uditAnnotation\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x17\n\x0fvalueExpression\x18\x02 \x01(\t\"6\n\x11\x45xpressionWarning\x12\x10\n\x08\x66ieldRef\x18\x02 \x01(\t\x12\x0f\n\x07warning\x18\x03 \x01(\t\"2\n\x0eMatchCondition\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nexpression\x18\x02 \x01(\t\"\xfd\x02\n\x0eMatchResources\x12N\n\x11namespaceSelector\x18\x01 \x01(\x0b\x32\x33.k8s.io.apimachinery.pkg.apis.meta.v1.LabelSelector\x12K\n\x0eobjectSelector\x18\x02 \x01(\x0b\x32\x33.k8s.io.apimachinery.pkg.apis.meta.v1.LabelSelector\x12X\n\rresourceRules\x18\x03 \x03(\x0b\x32\x41.k8s.io.api.admissionregistration.v1beta1.NamedRuleWithOperations\x12_\n\x14\x65xcludeResourceRules\x18\x04 \x03(\x0b\x32\x41.k8s.io.api.admissionregistration.v1beta1.NamedRuleWithOperations\x12\x13\n\x0bmatchPolicy\x18\x07 \x01(\t\"\xc2\x04\n\x0fMutatingWebhook\x12\x0c\n\x04name\x18\x01 \x01(\t\x12S\n\x0c\x63lientConfig\x18\x02 \x01(\x0b\x32=.k8s.io.api.admissionregistration.v1beta1.WebhookClientConfig\x12\x46\n\x05rules\x18\x03 \x03(\x0b\x32\x37.k8s.io.api.admissionregistration.v1.RuleWithOperations\x12\x15\n\rfailurePolicy\x18\x04 \x01(\t\x12\x13\n\x0bmatchPolicy\x18\t \x01(\t\x12N\n\x11namespaceSelector\x18\x05 \x01(\x0b\x32\x33.k8s.io.apimachinery.pkg.apis.meta.v1.LabelSelector\x12K\n\x0eobjectSelector\x18\x0b \x01(\x0b\x32\x33.k8s.io.apimachinery.pkg.apis.meta.v1.LabelSelector\x12\x13\n\x0bsideEffects\x18\x06 \x01(\t\x12\x16\n\x0etimeoutSeconds\x18\x07 \x01(\x05\x12\x1f\n\x17\x61\x64missionReviewVersions\x18\x08 \x03(\t\x12\x1a\n\x12reinvocationPolicy\x18\n \x01(\t\x12Q\n\x0fmatchConditions\x18\x0c \x03(\x0b\x32\x38.k8s.io.api.admissionregistration.v1beta1.MatchCondition\"\xaf\x01\n\x1cMutatingWebhookConfiguration\x12\x42\n\x08metadata\x18\x01 \x01(\x0b\x32\x30.k8s.io.apimachinery.pkg.apis.meta.v1.ObjectMeta\x12K\n\x08Webhooks\x18\x02 \x03(\x0b\x32\x39.k8s.io.api.admissionregistration.v1beta1.MutatingWebhook\"\xbb\x01\n MutatingWebhookConfigurationList\x12@\n\x08metadata\x18\x01 \x01(\x0b\x32..k8s.io.apimachinery.pkg.apis.meta.v1.ListMeta\x12U\n\x05items\x18\x02 \x03(\x0b\x32\x46.k8s.io.api.admissionregistration.v1beta1.MutatingWebhookConfiguration\"\x85\x01\n\x17NamedRuleWithOperations\x12\x15\n\rresourceNames\x18\x01 \x03(\t\x12S\n\x12ruleWithOperations\x18\x02 \x01(\x0b\x32\x37.k8s.io.api.admissionregistration.v1.RuleWithOperations\"-\n\tParamKind\x12\x12\n\napiVersion\x18\x01 \x01(\t\x12\x0c\n\x04kind\x18\x02 \x01(\t\"\x93\x01\n\x08ParamRef\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tnamespace\x18\x02 \x01(\t\x12\x45\n\x08selector\x18\x03 \x01(\x0b\x32\x33.k8s.io.apimachinery.pkg.apis.meta.v1.LabelSelector\x12\x1f\n\x17parameterNotFoundAction\x18\x04 \x01(\t\"O\n\x10ServiceReference\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04path\x18\x03 \x01(\t\x12\x0c\n\x04port\x18\x04 \x01(\x05\"g\n\x0cTypeChecking\x12W\n\x12\x65xpressionWarnings\x18\x01 \x03(\x0b\x32;.k8s.io.api.admissionregistration.v1beta1.ExpressionWarning\"\x91\x02\n\x19ValidatingAdmissionPolicy\x12\x42\n\x08metadata\x18\x01 \x01(\x0b\x32\x30.k8s.io.apimachinery.pkg.apis.meta.v1.ObjectMeta\x12U\n\x04spec\x18\x02 \x01(\x0b\x32G.k8s.io.api.admissionregistration.v1beta1.ValidatingAdmissionPolicySpec\x12Y\n\x06status\x18\x03 \x01(\x0b\x32I.k8s.io.api.admissionregistration.v1beta1.ValidatingAdmissionPolicyStatus\"\xc4\x01\n ValidatingAdmissionPolicyBinding\x12\x42\n\x08metadata\x18\x01 \x01(\x0b\x32\x30.k8s.io.apimachinery.pkg.apis.meta.v1.ObjectMeta\x12\\\n\x04spec\x18\x02 \x01(\x0b\x32N.k8s.io.api.admissionregistration.v1beta1.ValidatingAdmissionPolicyBindingSpec\"\xc3\x01\n$ValidatingAdmissionPolicyBindingList\x12@\n\x08metadata\x18\x01 \x01(\x0b\x32..k8s.io.apimachinery.pkg.apis.meta.v1.ListMeta\x12Y\n\x05items\x18\x02 \x03(\x0b\x32J.k8s.io.api.admissionregistration.v1beta1.ValidatingAdmissionPolicyBinding\"\xed\x01\n$ValidatingAdmissionPolicyBindingSpec\x12\x12\n\npolicyName\x18\x01 \x01(\t\x12\x44\n\x08paramRef\x18\x02 \x01(\x0b\x32\x32.k8s.io.api.admissionregistration.v1beta1.ParamRef\x12P\n\x0ematchResources\x18\x03 \x01(\x0b\x32\x38.k8s.io.api.admissionregistration.v1beta1.MatchResources\x12\x19\n\x11validationActions\x18\x04 \x03(\t\"\xb5\x01\n\x1dValidatingAdmissionPolicyList\x12@\n\x08metadata\x18\x01 \x01(\x0b\x32..k8s.io.apimachinery.pkg.apis.meta.v1.ListMeta\x12R\n\x05items\x18\x02 \x03(\x0b\x32\x43.k8s.io.api.admissionregistration.v1beta1.ValidatingAdmissionPolicy\"\x8c\x04\n\x1dValidatingAdmissionPolicySpec\x12\x46\n\tparamKind\x18\x01 \x01(\x0b\x32\x33.k8s.io.api.admissionregistration.v1beta1.ParamKind\x12R\n\x10matchConstraints\x18\x02 \x01(\x0b\x32\x38.k8s.io.api.admissionregistration.v1beta1.MatchResources\x12I\n\x0bvalidations\x18\x03 \x03(\x0b\x32\x34.k8s.io.api.admissionregistration.v1beta1.Validation\x12\x15\n\rfailurePolicy\x18\x04 \x01(\t\x12S\n\x10\x61uditAnnotations\x18\x05 \x03(\x0b\x32\x39.k8s.io.api.admissionregistration.v1beta1.AuditAnnotation\x12Q\n\x0fmatchConditions\x18\x06 \x03(\x0b\x32\x38.k8s.io.api.admissionregistration.v1beta1.MatchCondition\x12\x45\n\tvariables\x18\x07 \x03(\x0b\x32\x32.k8s.io.api.admissionregistration.v1beta1.Variable\"\xd0\x01\n\x1fValidatingAdmissionPolicyStatus\x12\x1a\n\x12observedGeneration\x18\x01 \x01(\x03\x12L\n\x0ctypeChecking\x18\x02 \x01(\x0b\x32\x36.k8s.io.api.admissionregistration.v1beta1.TypeChecking\x12\x43\n\nconditions\x18\x03 \x03(\x0b\x32/.k8s.io.apimachinery.pkg.apis.meta.v1.Condition\"\xa8\x04\n\x11ValidatingWebhook\x12\x0c\n\x04name\x18\x01 \x01(\t\x12S\n\x0c\x63lientConfig\x18\x02 \x01(\x0b\x32=.k8s.io.api.admissionregistration.v1beta1.WebhookClientConfig\x12\x46\n\x05rules\x18\x03 \x03(\x0b\x32\x37.k8s.io.api.admissionregistration.v1.RuleWithOperations\x12\x15\n\rfailurePolicy\x18\x04 \x01(\t\x12\x13\n\x0bmatchPolicy\x18\t \x01(\t\x12N\n\x11namespaceSelector\x18\x05 \x01(\x0b\x32\x33.k8s.io.apimachinery.pkg.apis.meta.v1.LabelSelector\x12K\n\x0eobjectSelector\x18\n \x01(\x0b\x32\x33.k8s.io.apimachinery.pkg.apis.meta.v1.LabelSelector\x12\x13\n\x0bsideEffects\x18\x06 \x01(\t\x12\x16\n\x0etimeoutSeconds\x18\x07 \x01(\x05\x12\x1f\n\x17\x61\x64missionReviewVersions\x18\x08 \x03(\t\x12Q\n\x0fmatchConditions\x18\x0b \x03(\x0b\x32\x38.k8s.io.api.admissionregistration.v1beta1.MatchCondition\"\xb3\x01\n\x1eValidatingWebhookConfiguration\x12\x42\n\x08metadata\x18\x01 \x01(\x0b\x32\x30.k8s.io.apimachinery.pkg.apis.meta.v1.ObjectMeta\x12M\n\x08Webhooks\x18\x02 \x03(\x0b\x32;.k8s.io.api.admissionregistration.v1beta1.ValidatingWebhook\"\xbf\x01\n\"ValidatingWebhookConfigurationList\x12@\n\x08metadata\x18\x01 \x01(\x0b\x32..k8s.io.apimachinery.pkg.apis.meta.v1.ListMeta\x12W\n\x05items\x18\x02 \x03(\x0b\x32H.k8s.io.api.admissionregistration.v1beta1.ValidatingWebhookConfiguration\"\\\n\nValidation\x12\x12\n\nExpression\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x0e\n\x06reason\x18\x03 \x01(\t\x12\x19\n\x11messageExpression\x18\x04 \x01(\t\",\n\x08Variable\x12\x0c\n\x04Name\x18\x01 \x01(\t\x12\x12\n\nExpression\x18\x02 \x01(\t\"\x81\x01\n\x13WebhookClientConfig\x12\x0b\n\x03url\x18\x03 \x01(\t\x12K\n\x07service\x18\x01 \x01(\x0b\x32:.k8s.io.api.admissionregistration.v1beta1.ServiceReference\x12\x10\n\x08\x63\x61\x42undle\x18\x02 \x01(\x0c\x42*Z(k8s.io/api/admissionregistration/v1beta1')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'k8s.io.api.admissionregistration.v1beta1.generated_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z(k8s.io/api/admissionregistration/v1beta1'
  _globals['_AUDITANNOTATION']._serialized_start=314
  _globals['_AUDITANNOTATION']._serialized_end=369
  _globals['_EXPRESSIONWARNING']._serialized_start=371
  _globals['_EXPRESSIONWARNING']._serialized_end=425
  _globals['_MATCHCONDITION']._serialized_start=427
  _globals['_MATCHCONDITION']._serialized_end=477
  _globals['_MATCHRESOURCES']._serialized_start=480
  _globals['_MATCHRESOURCES']._serialized_end=861
  _globals['_MUTATINGWEBHOOK']._serialized_start=864
  _globals['_MUTATINGWEBHOOK']._serialized_end=1442
  _globals['_MUTATINGWEBHOOKCONFIGURATION']._serialized_start=1445
  _globals['_MUTATINGWEBHOOKCONFIGURATION']._serialized_end=1620
  _globals['_MUTATINGWEBHOOKCONFIGURATIONLIST']._serialized_start=1623
  _globals['_MUTATINGWEBHOOKCONFIGURATIONLIST']._serialized_end=1810
  _globals['_NAMEDRULEWITHOPERATIONS']._serialized_start=1813
  _globals['_NAMEDRULEWITHOPERATIONS']._serialized_end=1946
  _globals['_PARAMKIND']._serialized_start=1948
  _globals['_PARAMKIND']._serialized_end=1993
  _globals['_PARAMREF']._serialized_start=1996
  _globals['_PARAMREF']._serialized_end=2143
  _globals['_SERVICEREFERENCE']._serialized_start=2145
  _globals['_SERVICEREFERENCE']._serialized_end=2224
  _globals['_TYPECHECKING']._serialized_start=2226
  _globals['_TYPECHECKING']._serialized_end=2329
  _globals['_VALIDATINGADMISSIONPOLICY']._serialized_start=2332
  _globals['_VALIDATINGADMISSIONPOLICY']._serialized_end=2605
  _globals['_VALIDATINGADMISSIONPOLICYBINDING']._serialized_start=2608
  _globals['_VALIDATINGADMISSIONPOLICYBINDING']._serialized_end=2804
  _globals['_VALIDATINGADMISSIONPOLICYBINDINGLIST']._serialized_start=2807
  _globals['_VALIDATINGADMISSIONPOLICYBINDINGLIST']._serialized_end=3002
  _globals['_VALIDATINGADMISSIONPOLICYBINDINGSPEC']._serialized_start=3005
  _globals['_VALIDATINGADMISSIONPOLICYBINDINGSPEC']._serialized_end=3242
  _globals['_VALIDATINGADMISSIONPOLICYLIST']._serialized_start=3245
  _globals['_VALIDATINGADMISSIONPOLICYLIST']._serialized_end=3426
  _globals['_VALIDATINGADMISSIONPOLICYSPEC']._serialized_start=3429
  _globals['_VALIDATINGADMISSIONPOLICYSPEC']._serialized_end=3953
  _globals['_VALIDATINGADMISSIONPOLICYSTATUS']._serialized_start=3956
  _globals['_VALIDATINGADMISSIONPOLICYSTATUS']._serialized_end=4164
  _globals['_VALIDATINGWEBHOOK']._serialized_start=4167
  _globals['_VALIDATINGWEBHOOK']._serialized_end=4719
  _globals['_VALIDATINGWEBHOOKCONFIGURATION']._serialized_start=4722
  _globals['_VALIDATINGWEBHOOKCONFIGURATION']._serialized_end=4901
  _globals['_VALIDATINGWEBHOOKCONFIGURATIONLIST']._serialized_start=4904
  _globals['_VALIDATINGWEBHOOKCONFIGURATIONLIST']._serialized_end=5095
  _globals['_VALIDATION']._serialized_start=5097
  _globals['_VALIDATION']._serialized_end=5189
  _globals['_VARIABLE']._serialized_start=5191
  _globals['_VARIABLE']._serialized_end=5235
  _globals['_WEBHOOKCLIENTCONFIG']._serialized_start=5238
  _globals['_WEBHOOKCLIENTCONFIG']._serialized_end=5367
# @@protoc_insertion_point(module_scope)
