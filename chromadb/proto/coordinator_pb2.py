# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromadb/proto/coordinator.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chromadb.proto import chroma_pb2 as chromadb_dot_proto_dot_chroma__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n chromadb/proto/coordinator.proto\x12\x06\x63hroma\x1a\x1b\x63hromadb/proto/chroma.proto\x1a\x1bgoogle/protobuf/empty.proto\"A\n\x15\x43reateDatabaseRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06tenant\x18\x03 \x01(\t\"&\n\x16\x43reateDatabaseResponseJ\x04\x08\x01\x10\x02R\x06status\"2\n\x12GetDatabaseRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06tenant\x18\x02 \x01(\t\"G\n\x13GetDatabaseResponse\x12\"\n\x08\x64\x61tabase\x18\x01 \x01(\x0b\x32\x10.chroma.DatabaseJ\x04\x08\x02\x10\x03R\x06status\"#\n\x13\x43reateTenantRequest\x12\x0c\n\x04name\x18\x02 \x01(\t\"$\n\x14\x43reateTenantResponseJ\x04\x08\x01\x10\x02R\x06status\" \n\x10GetTenantRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"A\n\x11GetTenantResponse\x12\x1e\n\x06tenant\x18\x01 \x01(\x0b\x32\x0e.chroma.TenantJ\x04\x08\x02\x10\x03R\x06status\"8\n\x14\x43reateSegmentRequest\x12 \n\x07segment\x18\x01 \x01(\x0b\x32\x0f.chroma.Segment\"%\n\x15\x43reateSegmentResponseJ\x04\x08\x01\x10\x02R\x06status\"6\n\x14\x44\x65leteSegmentRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\ncollection\x18\x02 \x01(\t\"%\n\x15\x44\x65leteSegmentResponseJ\x04\x08\x01\x10\x02R\x06status\"\x90\x01\n\x12GetSegmentsRequest\x12\x0f\n\x02id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x11\n\x04type\x18\x02 \x01(\tH\x01\x88\x01\x01\x12(\n\x05scope\x18\x03 \x01(\x0e\x32\x14.chroma.SegmentScopeH\x02\x88\x01\x01\x12\x12\n\ncollection\x18\x04 \x01(\tB\x05\n\x03_idB\x07\n\x05_typeB\x08\n\x06_scope\"F\n\x13GetSegmentsResponse\x12!\n\x08segments\x18\x01 \x03(\x0b\x32\x0f.chroma.SegmentJ\x04\x08\x02\x10\x03R\x06status\"\x8f\x01\n\x14UpdateSegmentRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\ncollection\x18\x04 \x01(\t\x12*\n\x08metadata\x18\x06 \x01(\x0b\x32\x16.chroma.UpdateMetadataH\x00\x12\x18\n\x0ereset_metadata\x18\x07 \x01(\x08H\x00\x42\x11\n\x0fmetadata_update\"%\n\x15UpdateSegmentResponseJ\x04\x08\x01\x10\x02R\x06status\"\xa8\x02\n\x17\x43reateCollectionRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x1e\n\x16\x63onfiguration_json_str\x18\x03 \x01(\t\x12-\n\x08metadata\x18\x04 \x01(\x0b\x32\x16.chroma.UpdateMetadataH\x00\x88\x01\x01\x12\x16\n\tdimension\x18\x05 \x01(\x05H\x01\x88\x01\x01\x12\x1a\n\rget_or_create\x18\x06 \x01(\x08H\x02\x88\x01\x01\x12\x0e\n\x06tenant\x18\x07 \x01(\t\x12\x10\n\x08\x64\x61tabase\x18\x08 \x01(\t\x12!\n\x08segments\x18\t \x03(\x0b\x32\x0f.chroma.SegmentB\x0b\n\t_metadataB\x0c\n\n_dimensionB\x10\n\x0e_get_or_create\"a\n\x18\x43reateCollectionResponse\x12&\n\ncollection\x18\x01 \x01(\x0b\x32\x12.chroma.Collection\x12\x0f\n\x07\x63reated\x18\x02 \x01(\x08J\x04\x08\x03\x10\x04R\x06status\"\\\n\x17\x44\x65leteCollectionRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06tenant\x18\x02 \x01(\t\x12\x10\n\x08\x64\x61tabase\x18\x03 \x01(\t\x12\x13\n\x0bsegment_ids\x18\x04 \x03(\t\"(\n\x18\x44\x65leteCollectionResponseJ\x04\x08\x01\x10\x02R\x06status\"\xab\x01\n\x15GetCollectionsRequest\x12\x0f\n\x02id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x11\n\x04name\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x0e\n\x06tenant\x18\x04 \x01(\t\x12\x10\n\x08\x64\x61tabase\x18\x05 \x01(\t\x12\x12\n\x05limit\x18\x06 \x01(\x05H\x02\x88\x01\x01\x12\x13\n\x06offset\x18\x07 \x01(\x05H\x03\x88\x01\x01\x42\x05\n\x03_idB\x07\n\x05_nameB\x08\n\x06_limitB\t\n\x07_offset\"O\n\x16GetCollectionsResponse\x12\'\n\x0b\x63ollections\x18\x01 \x03(\x0b\x32\x12.chroma.CollectionJ\x04\x08\x02\x10\x03R\x06status\"\xc0\x01\n\x17UpdateCollectionRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\x04name\x18\x03 \x01(\tH\x01\x88\x01\x01\x12\x16\n\tdimension\x18\x04 \x01(\x05H\x02\x88\x01\x01\x12*\n\x08metadata\x18\x05 \x01(\x0b\x32\x16.chroma.UpdateMetadataH\x00\x12\x18\n\x0ereset_metadata\x18\x06 \x01(\x08H\x00\x42\x11\n\x0fmetadata_updateB\x07\n\x05_nameB\x0c\n\n_dimension\"(\n\x18UpdateCollectionResponseJ\x04\x08\x01\x10\x02R\x06status\"\"\n\x12ResetStateResponseJ\x04\x08\x01\x10\x02R\x06status\":\n%GetLastCompactionTimeForTenantRequest\x12\x11\n\ttenant_id\x18\x01 \x03(\t\"K\n\x18TenantLastCompactionTime\x12\x11\n\ttenant_id\x18\x01 \x01(\t\x12\x1c\n\x14last_compaction_time\x18\x02 \x01(\x03\"o\n&GetLastCompactionTimeForTenantResponse\x12\x45\n\x1btenant_last_compaction_time\x18\x01 \x03(\x0b\x32 .chroma.TenantLastCompactionTime\"n\n%SetLastCompactionTimeForTenantRequest\x12\x45\n\x1btenant_last_compaction_time\x18\x01 \x01(\x0b\x32 .chroma.TenantLastCompactionTime\"\xbc\x01\n\x1a\x46lushSegmentCompactionInfo\x12\x12\n\nsegment_id\x18\x01 \x01(\t\x12\x45\n\nfile_paths\x18\x02 \x03(\x0b\x32\x31.chroma.FlushSegmentCompactionInfo.FilePathsEntry\x1a\x43\n\x0e\x46ilePathsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12 \n\x05value\x18\x02 \x01(\x0b\x32\x11.chroma.FilePaths:\x02\x38\x01\"\xc3\x01\n FlushCollectionCompactionRequest\x12\x11\n\ttenant_id\x18\x01 \x01(\t\x12\x15\n\rcollection_id\x18\x02 \x01(\t\x12\x14\n\x0clog_position\x18\x03 \x01(\x03\x12\x1a\n\x12\x63ollection_version\x18\x04 \x01(\x05\x12\x43\n\x17segment_compaction_info\x18\x05 \x03(\x0b\x32\".chroma.FlushSegmentCompactionInfo\"t\n!FlushCollectionCompactionResponse\x12\x15\n\rcollection_id\x18\x01 \x01(\t\x12\x1a\n\x12\x63ollection_version\x18\x02 \x01(\x05\x12\x1c\n\x14last_compaction_time\x18\x03 \x01(\x03\x32\xf4\n\n\x05SysDB\x12Q\n\x0e\x43reateDatabase\x12\x1d.chroma.CreateDatabaseRequest\x1a\x1e.chroma.CreateDatabaseResponse\"\x00\x12H\n\x0bGetDatabase\x12\x1a.chroma.GetDatabaseRequest\x1a\x1b.chroma.GetDatabaseResponse\"\x00\x12K\n\x0c\x43reateTenant\x12\x1b.chroma.CreateTenantRequest\x1a\x1c.chroma.CreateTenantResponse\"\x00\x12\x42\n\tGetTenant\x12\x18.chroma.GetTenantRequest\x1a\x19.chroma.GetTenantResponse\"\x00\x12N\n\rCreateSegment\x12\x1c.chroma.CreateSegmentRequest\x1a\x1d.chroma.CreateSegmentResponse\"\x00\x12N\n\rDeleteSegment\x12\x1c.chroma.DeleteSegmentRequest\x1a\x1d.chroma.DeleteSegmentResponse\"\x00\x12H\n\x0bGetSegments\x12\x1a.chroma.GetSegmentsRequest\x1a\x1b.chroma.GetSegmentsResponse\"\x00\x12N\n\rUpdateSegment\x12\x1c.chroma.UpdateSegmentRequest\x1a\x1d.chroma.UpdateSegmentResponse\"\x00\x12W\n\x10\x43reateCollection\x12\x1f.chroma.CreateCollectionRequest\x1a .chroma.CreateCollectionResponse\"\x00\x12W\n\x10\x44\x65leteCollection\x12\x1f.chroma.DeleteCollectionRequest\x1a .chroma.DeleteCollectionResponse\"\x00\x12Q\n\x0eGetCollections\x12\x1d.chroma.GetCollectionsRequest\x1a\x1e.chroma.GetCollectionsResponse\"\x00\x12W\n\x10UpdateCollection\x12\x1f.chroma.UpdateCollectionRequest\x1a .chroma.UpdateCollectionResponse\"\x00\x12\x42\n\nResetState\x12\x16.google.protobuf.Empty\x1a\x1a.chroma.ResetStateResponse\"\x00\x12\x81\x01\n\x1eGetLastCompactionTimeForTenant\x12-.chroma.GetLastCompactionTimeForTenantRequest\x1a..chroma.GetLastCompactionTimeForTenantResponse\"\x00\x12i\n\x1eSetLastCompactionTimeForTenant\x12-.chroma.SetLastCompactionTimeForTenantRequest\x1a\x16.google.protobuf.Empty\"\x00\x12r\n\x19\x46lushCollectionCompaction\x12(.chroma.FlushCollectionCompactionRequest\x1a).chroma.FlushCollectionCompactionResponse\"\x00\x42:Z8github.com/chroma-core/chroma/go/pkg/proto/coordinatorpbb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chromadb.proto.coordinator_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z8github.com/chroma-core/chroma/go/pkg/proto/coordinatorpb'
  _globals['_FLUSHSEGMENTCOMPACTIONINFO_FILEPATHSENTRY']._loaded_options = None
  _globals['_FLUSHSEGMENTCOMPACTIONINFO_FILEPATHSENTRY']._serialized_options = b'8\001'
  _globals['_CREATEDATABASEREQUEST']._serialized_start=102
  _globals['_CREATEDATABASEREQUEST']._serialized_end=167
  _globals['_CREATEDATABASERESPONSE']._serialized_start=169
  _globals['_CREATEDATABASERESPONSE']._serialized_end=207
  _globals['_GETDATABASEREQUEST']._serialized_start=209
  _globals['_GETDATABASEREQUEST']._serialized_end=259
  _globals['_GETDATABASERESPONSE']._serialized_start=261
  _globals['_GETDATABASERESPONSE']._serialized_end=332
  _globals['_CREATETENANTREQUEST']._serialized_start=334
  _globals['_CREATETENANTREQUEST']._serialized_end=369
  _globals['_CREATETENANTRESPONSE']._serialized_start=371
  _globals['_CREATETENANTRESPONSE']._serialized_end=407
  _globals['_GETTENANTREQUEST']._serialized_start=409
  _globals['_GETTENANTREQUEST']._serialized_end=441
  _globals['_GETTENANTRESPONSE']._serialized_start=443
  _globals['_GETTENANTRESPONSE']._serialized_end=508
  _globals['_CREATESEGMENTREQUEST']._serialized_start=510
  _globals['_CREATESEGMENTREQUEST']._serialized_end=566
  _globals['_CREATESEGMENTRESPONSE']._serialized_start=568
  _globals['_CREATESEGMENTRESPONSE']._serialized_end=605
  _globals['_DELETESEGMENTREQUEST']._serialized_start=607
  _globals['_DELETESEGMENTREQUEST']._serialized_end=661
  _globals['_DELETESEGMENTRESPONSE']._serialized_start=663
  _globals['_DELETESEGMENTRESPONSE']._serialized_end=700
  _globals['_GETSEGMENTSREQUEST']._serialized_start=703
  _globals['_GETSEGMENTSREQUEST']._serialized_end=847
  _globals['_GETSEGMENTSRESPONSE']._serialized_start=849
  _globals['_GETSEGMENTSRESPONSE']._serialized_end=919
  _globals['_UPDATESEGMENTREQUEST']._serialized_start=922
  _globals['_UPDATESEGMENTREQUEST']._serialized_end=1065
  _globals['_UPDATESEGMENTRESPONSE']._serialized_start=1067
  _globals['_UPDATESEGMENTRESPONSE']._serialized_end=1104
  _globals['_CREATECOLLECTIONREQUEST']._serialized_start=1107
  _globals['_CREATECOLLECTIONREQUEST']._serialized_end=1403
  _globals['_CREATECOLLECTIONRESPONSE']._serialized_start=1405
  _globals['_CREATECOLLECTIONRESPONSE']._serialized_end=1502
  _globals['_DELETECOLLECTIONREQUEST']._serialized_start=1504
  _globals['_DELETECOLLECTIONREQUEST']._serialized_end=1596
  _globals['_DELETECOLLECTIONRESPONSE']._serialized_start=1598
  _globals['_DELETECOLLECTIONRESPONSE']._serialized_end=1638
  _globals['_GETCOLLECTIONSREQUEST']._serialized_start=1641
  _globals['_GETCOLLECTIONSREQUEST']._serialized_end=1812
  _globals['_GETCOLLECTIONSRESPONSE']._serialized_start=1814
  _globals['_GETCOLLECTIONSRESPONSE']._serialized_end=1893
  _globals['_UPDATECOLLECTIONREQUEST']._serialized_start=1896
  _globals['_UPDATECOLLECTIONREQUEST']._serialized_end=2088
  _globals['_UPDATECOLLECTIONRESPONSE']._serialized_start=2090
  _globals['_UPDATECOLLECTIONRESPONSE']._serialized_end=2130
  _globals['_RESETSTATERESPONSE']._serialized_start=2132
  _globals['_RESETSTATERESPONSE']._serialized_end=2166
  _globals['_GETLASTCOMPACTIONTIMEFORTENANTREQUEST']._serialized_start=2168
  _globals['_GETLASTCOMPACTIONTIMEFORTENANTREQUEST']._serialized_end=2226
  _globals['_TENANTLASTCOMPACTIONTIME']._serialized_start=2228
  _globals['_TENANTLASTCOMPACTIONTIME']._serialized_end=2303
  _globals['_GETLASTCOMPACTIONTIMEFORTENANTRESPONSE']._serialized_start=2305
  _globals['_GETLASTCOMPACTIONTIMEFORTENANTRESPONSE']._serialized_end=2416
  _globals['_SETLASTCOMPACTIONTIMEFORTENANTREQUEST']._serialized_start=2418
  _globals['_SETLASTCOMPACTIONTIMEFORTENANTREQUEST']._serialized_end=2528
  _globals['_FLUSHSEGMENTCOMPACTIONINFO']._serialized_start=2531
  _globals['_FLUSHSEGMENTCOMPACTIONINFO']._serialized_end=2719
  _globals['_FLUSHSEGMENTCOMPACTIONINFO_FILEPATHSENTRY']._serialized_start=2652
  _globals['_FLUSHSEGMENTCOMPACTIONINFO_FILEPATHSENTRY']._serialized_end=2719
  _globals['_FLUSHCOLLECTIONCOMPACTIONREQUEST']._serialized_start=2722
  _globals['_FLUSHCOLLECTIONCOMPACTIONREQUEST']._serialized_end=2917
  _globals['_FLUSHCOLLECTIONCOMPACTIONRESPONSE']._serialized_start=2919
  _globals['_FLUSHCOLLECTIONCOMPACTIONRESPONSE']._serialized_end=3035
  _globals['_SYSDB']._serialized_start=3038
  _globals['_SYSDB']._serialized_end=4434
# @@protoc_insertion_point(module_scope)
