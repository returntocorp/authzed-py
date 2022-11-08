"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import authzed.api.v1.core_pb2
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class WatchResourcesRequest(google.protobuf.message.Message):
    """WatchResourcesRequest starts a watch for specific permission updates
    for the given resource and subject types.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_OBJECT_TYPE_FIELD_NUMBER: builtins.int
    PERMISSION_FIELD_NUMBER: builtins.int
    SUBJECT_OBJECT_TYPE_FIELD_NUMBER: builtins.int
    OPTIONAL_SUBJECT_RELATION_FIELD_NUMBER: builtins.int
    OPTIONAL_START_CURSOR_FIELD_NUMBER: builtins.int
    resource_object_type: builtins.str
    """resource_object_type is the type of resource object for which we will
    watch for changes.
    """
    permission: builtins.str
    """permission is the name of the permission or relation for which we will
    watch for changes.
    """
    subject_object_type: builtins.str
    """subject_object_type is the type of the subject resource for which we will
    watch for changes.
    """
    optional_subject_relation: builtins.str
    """optional_subject_relation allows you to specify a group of subjects to watch
    for a given subject type.
    """
    @property
    def optional_start_cursor(self) -> authzed.api.v1.core_pb2.ZedToken: ...
    def __init__(
        self,
        *,
        resource_object_type: builtins.str = ...,
        permission: builtins.str = ...,
        subject_object_type: builtins.str = ...,
        optional_subject_relation: builtins.str = ...,
        optional_start_cursor: authzed.api.v1.core_pb2.ZedToken | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["optional_start_cursor", b"optional_start_cursor"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["optional_start_cursor", b"optional_start_cursor", "optional_subject_relation", b"optional_subject_relation", "permission", b"permission", "resource_object_type", b"resource_object_type", "subject_object_type", b"subject_object_type"]) -> None: ...

global___WatchResourcesRequest = WatchResourcesRequest

@typing_extensions.final
class PermissionUpdate(google.protobuf.message.Message):
    """PermissionUpdate represents a single permission update for a specific
    subject's permissions.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Permissionship:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _PermissionshipEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[PermissionUpdate._Permissionship.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        PERMISSIONSHIP_UNSPECIFIED: PermissionUpdate._Permissionship.ValueType  # 0
        PERMISSIONSHIP_NO_PERMISSION: PermissionUpdate._Permissionship.ValueType  # 1
        PERMISSIONSHIP_HAS_PERMISSION: PermissionUpdate._Permissionship.ValueType  # 2

    class Permissionship(_Permissionship, metaclass=_PermissionshipEnumTypeWrapper):
        """todo: work this into the v1 core API at some point since it's used
        across services.
        """

    PERMISSIONSHIP_UNSPECIFIED: PermissionUpdate.Permissionship.ValueType  # 0
    PERMISSIONSHIP_NO_PERMISSION: PermissionUpdate.Permissionship.ValueType  # 1
    PERMISSIONSHIP_HAS_PERMISSION: PermissionUpdate.Permissionship.ValueType  # 2

    SUBJECT_FIELD_NUMBER: builtins.int
    RESOURCE_FIELD_NUMBER: builtins.int
    RELATION_FIELD_NUMBER: builtins.int
    UPDATED_PERMISSION_FIELD_NUMBER: builtins.int
    @property
    def subject(self) -> authzed.api.v1.core_pb2.SubjectReference:
        """subject defines the subject resource whose permissions have changed."""
    @property
    def resource(self) -> authzed.api.v1.core_pb2.ObjectReference:
        """resource defines the specific object in the system."""
    relation: builtins.str
    updated_permission: global___PermissionUpdate.Permissionship.ValueType
    def __init__(
        self,
        *,
        subject: authzed.api.v1.core_pb2.SubjectReference | None = ...,
        resource: authzed.api.v1.core_pb2.ObjectReference | None = ...,
        relation: builtins.str = ...,
        updated_permission: global___PermissionUpdate.Permissionship.ValueType = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource", b"resource", "subject", b"subject"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["relation", b"relation", "resource", b"resource", "subject", b"subject", "updated_permission", b"updated_permission"]) -> None: ...

global___PermissionUpdate = PermissionUpdate

@typing_extensions.final
class WatchResourcesResponse(google.protobuf.message.Message):
    """WatchResourcesResponse enumerates the list of permission updates that have
    occurred as a result of one or more relationship updates.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    UPDATES_FIELD_NUMBER: builtins.int
    CHANGES_THROUGH_FIELD_NUMBER: builtins.int
    @property
    def updates(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___PermissionUpdate]: ...
    @property
    def changes_through(self) -> authzed.api.v1.core_pb2.ZedToken: ...
    def __init__(
        self,
        *,
        updates: collections.abc.Iterable[global___PermissionUpdate] | None = ...,
        changes_through: authzed.api.v1.core_pb2.ZedToken | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["changes_through", b"changes_through"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["changes_through", b"changes_through", "updates", b"updates"]) -> None: ...

global___WatchResourcesResponse = WatchResourcesResponse
