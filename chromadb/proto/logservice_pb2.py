# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromadb/proto/logservice.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chromadb.proto import chroma_pb2 as chromadb_dot_proto_dot_chroma__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1f\x63hromadb/proto/logservice.proto\x12\x06\x63hroma\x1a\x1b\x63hromadb/proto/chroma.proto"X\n\x0fPushLogsRequest\x12\x15\n\rcollection_id\x18\x01 \x01(\t\x12.\n\x07records\x18\x02 \x03(\x0b\x32\x1d.chroma.SubmitEmbeddingRecord"(\n\x10PushLogsResponse\x12\x14\n\x0crecord_count\x18\x01 \x01(\x05"S\n\x0fPullLogsRequest\x12\x15\n\rcollection_id\x18\x01 \x01(\t\x12\x15\n\rstart_from_id\x18\x02 \x01(\x03\x12\x12\n\nbatch_size\x18\x03 \x01(\x05"B\n\x10PullLogsResponse\x12.\n\x07records\x18\x01 \x03(\x0b\x32\x1d.chroma.SubmitEmbeddingRecord2\x8e\x01\n\nLogService\x12?\n\x08PushLogs\x12\x17.chroma.PushLogsRequest\x1a\x18.chroma.PushLogsResponse"\x00\x12?\n\x08PullLogs\x12\x17.chroma.PullLogsRequest\x1a\x18.chroma.PullLogsResponse"\x00\x42\x42Z@github.com/chroma/chroma-coordinator/internal/proto/logservicepbb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "chromadb.proto.logservice_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = (
        b"Z@github.com/chroma/chroma-coordinator/internal/proto/logservicepb"
    )
    _globals["_PUSHLOGSREQUEST"]._serialized_start = 72
    _globals["_PUSHLOGSREQUEST"]._serialized_end = 160
    _globals["_PUSHLOGSRESPONSE"]._serialized_start = 162
    _globals["_PUSHLOGSRESPONSE"]._serialized_end = 202
    _globals["_PULLLOGSREQUEST"]._serialized_start = 204
    _globals["_PULLLOGSREQUEST"]._serialized_end = 287
    _globals["_PULLLOGSRESPONSE"]._serialized_start = 289
    _globals["_PULLLOGSRESPONSE"]._serialized_end = 355
    _globals["_LOGSERVICE"]._serialized_start = 358
    _globals["_LOGSERVICE"]._serialized_end = 500
# @@protoc_insertion_point(module_scope)
