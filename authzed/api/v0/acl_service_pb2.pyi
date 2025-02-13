"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import authzed.api.v0.core_pb2
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class RelationTupleFilter(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class Filter(metaclass=_Filter):
        V = typing.NewType('V', builtins.int)

    UNKNOWN = RelationTupleFilter.Filter.V(0)
    OBJECT_ID = RelationTupleFilter.Filter.V(1)
    RELATION = RelationTupleFilter.Filter.V(2)
    USERSET = RelationTupleFilter.Filter.V(4)

    class _Filter(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Filter.V], builtins.type):  # type: ignore
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNKNOWN = RelationTupleFilter.Filter.V(0)
        OBJECT_ID = RelationTupleFilter.Filter.V(1)
        RELATION = RelationTupleFilter.Filter.V(2)
        USERSET = RelationTupleFilter.Filter.V(4)

    NAMESPACE_FIELD_NUMBER: builtins.int
    OBJECT_ID_FIELD_NUMBER: builtins.int
    RELATION_FIELD_NUMBER: builtins.int
    USERSET_FIELD_NUMBER: builtins.int
    FILTERS_FIELD_NUMBER: builtins.int
    namespace: typing.Text = ...
    object_id: typing.Text = ...
    relation: typing.Text = ...

    @property
    def filters(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[global___RelationTupleFilter.Filter.V]: ...

    @property
    def userset(self) -> authzed.api.v0.core_pb2.ObjectAndRelation: ...

    def __init__(self,
        *,
        namespace : typing.Text = ...,
        object_id : typing.Text = ...,
        relation : typing.Text = ...,
        userset : typing.Optional[authzed.api.v0.core_pb2.ObjectAndRelation] = ...,
        filters : typing.Optional[typing.Iterable[global___RelationTupleFilter.Filter.V]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"userset",b"userset"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"filters",b"filters",u"namespace",b"namespace",u"object_id",b"object_id",u"relation",b"relation",u"userset",b"userset"]) -> None: ...
global___RelationTupleFilter = RelationTupleFilter

class ReadRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TUPLESETS_FIELD_NUMBER: builtins.int
    AT_REVISION_FIELD_NUMBER: builtins.int

    @property
    def tuplesets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___RelationTupleFilter]: ...

    @property
    def at_revision(self) -> authzed.api.v0.core_pb2.Zookie: ...

    def __init__(self,
        *,
        tuplesets : typing.Optional[typing.Iterable[global___RelationTupleFilter]] = ...,
        at_revision : typing.Optional[authzed.api.v0.core_pb2.Zookie] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"at_revision",b"at_revision"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"at_revision",b"at_revision",u"tuplesets",b"tuplesets"]) -> None: ...
global___ReadRequest = ReadRequest

class ReadResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class Tupleset(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        TUPLES_FIELD_NUMBER: builtins.int

        @property
        def tuples(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[authzed.api.v0.core_pb2.RelationTuple]: ...

        def __init__(self,
            *,
            tuples : typing.Optional[typing.Iterable[authzed.api.v0.core_pb2.RelationTuple]] = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"tuples",b"tuples"]) -> None: ...

    TUPLESETS_FIELD_NUMBER: builtins.int
    REVISION_FIELD_NUMBER: builtins.int

    @property
    def tuplesets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ReadResponse.Tupleset]: ...

    @property
    def revision(self) -> authzed.api.v0.core_pb2.Zookie: ...

    def __init__(self,
        *,
        tuplesets : typing.Optional[typing.Iterable[global___ReadResponse.Tupleset]] = ...,
        revision : typing.Optional[authzed.api.v0.core_pb2.Zookie] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"revision",b"revision"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"revision",b"revision",u"tuplesets",b"tuplesets"]) -> None: ...
global___ReadResponse = ReadResponse

class WriteRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    WRITE_CONDITIONS_FIELD_NUMBER: builtins.int
    UPDATES_FIELD_NUMBER: builtins.int

    @property
    def write_conditions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[authzed.api.v0.core_pb2.RelationTuple]: ...

    @property
    def updates(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[authzed.api.v0.core_pb2.RelationTupleUpdate]: ...

    def __init__(self,
        *,
        write_conditions : typing.Optional[typing.Iterable[authzed.api.v0.core_pb2.RelationTuple]] = ...,
        updates : typing.Optional[typing.Iterable[authzed.api.v0.core_pb2.RelationTupleUpdate]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"updates",b"updates",u"write_conditions",b"write_conditions"]) -> None: ...
global___WriteRequest = WriteRequest

class WriteResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    REVISION_FIELD_NUMBER: builtins.int

    @property
    def revision(self) -> authzed.api.v0.core_pb2.Zookie: ...

    def __init__(self,
        *,
        revision : typing.Optional[authzed.api.v0.core_pb2.Zookie] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"revision",b"revision"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"revision",b"revision"]) -> None: ...
global___WriteResponse = WriteResponse

class CheckRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TEST_USERSET_FIELD_NUMBER: builtins.int
    USER_FIELD_NUMBER: builtins.int
    AT_REVISION_FIELD_NUMBER: builtins.int

    @property
    def test_userset(self) -> authzed.api.v0.core_pb2.ObjectAndRelation: ...

    @property
    def user(self) -> authzed.api.v0.core_pb2.User: ...

    @property
    def at_revision(self) -> authzed.api.v0.core_pb2.Zookie: ...

    def __init__(self,
        *,
        test_userset : typing.Optional[authzed.api.v0.core_pb2.ObjectAndRelation] = ...,
        user : typing.Optional[authzed.api.v0.core_pb2.User] = ...,
        at_revision : typing.Optional[authzed.api.v0.core_pb2.Zookie] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"at_revision",b"at_revision",u"test_userset",b"test_userset",u"user",b"user"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"at_revision",b"at_revision",u"test_userset",b"test_userset",u"user",b"user"]) -> None: ...
global___CheckRequest = CheckRequest

class ContentChangeCheckRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TEST_USERSET_FIELD_NUMBER: builtins.int
    USER_FIELD_NUMBER: builtins.int

    @property
    def test_userset(self) -> authzed.api.v0.core_pb2.ObjectAndRelation: ...

    @property
    def user(self) -> authzed.api.v0.core_pb2.User: ...

    def __init__(self,
        *,
        test_userset : typing.Optional[authzed.api.v0.core_pb2.ObjectAndRelation] = ...,
        user : typing.Optional[authzed.api.v0.core_pb2.User] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"test_userset",b"test_userset",u"user",b"user"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"test_userset",b"test_userset",u"user",b"user"]) -> None: ...
global___ContentChangeCheckRequest = ContentChangeCheckRequest

class CheckResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class Membership(metaclass=_Membership):
        V = typing.NewType('V', builtins.int)

    UNKNOWN = CheckResponse.Membership.V(0)
    NOT_MEMBER = CheckResponse.Membership.V(1)
    MEMBER = CheckResponse.Membership.V(2)

    class _Membership(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Membership.V], builtins.type):  # type: ignore
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNKNOWN = CheckResponse.Membership.V(0)
        NOT_MEMBER = CheckResponse.Membership.V(1)
        MEMBER = CheckResponse.Membership.V(2)

    IS_MEMBER_FIELD_NUMBER: builtins.int
    REVISION_FIELD_NUMBER: builtins.int
    MEMBERSHIP_FIELD_NUMBER: builtins.int
    is_member: builtins.bool = ...
    membership: global___CheckResponse.Membership.V = ...

    @property
    def revision(self) -> authzed.api.v0.core_pb2.Zookie: ...

    def __init__(self,
        *,
        is_member : builtins.bool = ...,
        revision : typing.Optional[authzed.api.v0.core_pb2.Zookie] = ...,
        membership : global___CheckResponse.Membership.V = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"revision",b"revision"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"is_member",b"is_member",u"membership",b"membership",u"revision",b"revision"]) -> None: ...
global___CheckResponse = CheckResponse

class ExpandRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    USERSET_FIELD_NUMBER: builtins.int
    AT_REVISION_FIELD_NUMBER: builtins.int

    @property
    def userset(self) -> authzed.api.v0.core_pb2.ObjectAndRelation: ...

    @property
    def at_revision(self) -> authzed.api.v0.core_pb2.Zookie: ...

    def __init__(self,
        *,
        userset : typing.Optional[authzed.api.v0.core_pb2.ObjectAndRelation] = ...,
        at_revision : typing.Optional[authzed.api.v0.core_pb2.Zookie] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"at_revision",b"at_revision",u"userset",b"userset"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"at_revision",b"at_revision",u"userset",b"userset"]) -> None: ...
global___ExpandRequest = ExpandRequest

class ExpandResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TREE_NODE_FIELD_NUMBER: builtins.int
    REVISION_FIELD_NUMBER: builtins.int

    @property
    def tree_node(self) -> authzed.api.v0.core_pb2.RelationTupleTreeNode: ...

    @property
    def revision(self) -> authzed.api.v0.core_pb2.Zookie: ...

    def __init__(self,
        *,
        tree_node : typing.Optional[authzed.api.v0.core_pb2.RelationTupleTreeNode] = ...,
        revision : typing.Optional[authzed.api.v0.core_pb2.Zookie] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"revision",b"revision",u"tree_node",b"tree_node"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"revision",b"revision",u"tree_node",b"tree_node"]) -> None: ...
global___ExpandResponse = ExpandResponse

class LookupRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    OBJECT_RELATION_FIELD_NUMBER: builtins.int
    USER_FIELD_NUMBER: builtins.int
    AT_REVISION_FIELD_NUMBER: builtins.int
    PAGE_REFERENCE_FIELD_NUMBER: builtins.int
    LIMIT_FIELD_NUMBER: builtins.int
    page_reference: typing.Text = ...
    limit: builtins.int = ...

    @property
    def object_relation(self) -> authzed.api.v0.core_pb2.RelationReference: ...

    @property
    def user(self) -> authzed.api.v0.core_pb2.ObjectAndRelation: ...

    @property
    def at_revision(self) -> authzed.api.v0.core_pb2.Zookie: ...

    def __init__(self,
        *,
        object_relation : typing.Optional[authzed.api.v0.core_pb2.RelationReference] = ...,
        user : typing.Optional[authzed.api.v0.core_pb2.ObjectAndRelation] = ...,
        at_revision : typing.Optional[authzed.api.v0.core_pb2.Zookie] = ...,
        page_reference : typing.Text = ...,
        limit : builtins.int = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"at_revision",b"at_revision",u"object_relation",b"object_relation",u"user",b"user"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"at_revision",b"at_revision",u"limit",b"limit",u"object_relation",b"object_relation",u"page_reference",b"page_reference",u"user",b"user"]) -> None: ...
global___LookupRequest = LookupRequest

class LookupResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOLVED_OBJECT_IDS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_REFERENCE_FIELD_NUMBER: builtins.int
    REVISION_FIELD_NUMBER: builtins.int

    @property
    def resolved_object_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    next_page_reference: typing.Text = ...

    @property
    def revision(self) -> authzed.api.v0.core_pb2.Zookie: ...

    def __init__(self,
        *,
        resolved_object_ids : typing.Optional[typing.Iterable[typing.Text]] = ...,
        next_page_reference : typing.Text = ...,
        revision : typing.Optional[authzed.api.v0.core_pb2.Zookie] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"revision",b"revision"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"next_page_reference",b"next_page_reference",u"resolved_object_ids",b"resolved_object_ids",u"revision",b"revision"]) -> None: ...
global___LookupResponse = LookupResponse
