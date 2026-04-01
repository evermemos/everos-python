# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .tasks import (
    TasksResource,
    AsyncTasksResource,
    TasksResourceWithRawResponse,
    AsyncTasksResourceWithRawResponse,
    TasksResourceWithStreamingResponse,
    AsyncTasksResourceWithStreamingResponse,
)
from .groups import (
    GroupsResource,
    AsyncGroupsResource,
    GroupsResourceWithRawResponse,
    AsyncGroupsResourceWithRawResponse,
    GroupsResourceWithStreamingResponse,
    AsyncGroupsResourceWithStreamingResponse,
)
from .object import (
    ObjectResource,
    AsyncObjectResource,
    ObjectResourceWithRawResponse,
    AsyncObjectResourceWithRawResponse,
    ObjectResourceWithStreamingResponse,
    AsyncObjectResourceWithStreamingResponse,
)
from .senders import (
    SendersResource,
    AsyncSendersResource,
    SendersResourceWithRawResponse,
    AsyncSendersResourceWithRawResponse,
    SendersResourceWithStreamingResponse,
    AsyncSendersResourceWithStreamingResponse,
)
from .settings import (
    SettingsResource,
    AsyncSettingsResource,
    SettingsResourceWithRawResponse,
    AsyncSettingsResourceWithRawResponse,
    SettingsResourceWithStreamingResponse,
    AsyncSettingsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .memories.memories import (
    MemoriesResource,
    AsyncMemoriesResource,
    MemoriesResourceWithRawResponse,
    AsyncMemoriesResourceWithRawResponse,
    MemoriesResourceWithStreamingResponse,
    AsyncMemoriesResourceWithStreamingResponse,
)

__all__ = ["V1Resource", "AsyncV1Resource"]


class V1Resource(SyncAPIResource):
    @cached_property
    def groups(self) -> GroupsResource:
        """Group resource CRUD operations"""
        return GroupsResource(self._client)

    @cached_property
    def settings(self) -> SettingsResource:
        """Global settings management"""
        return SettingsResource(self._client)

    @cached_property
    def senders(self) -> SendersResource:
        """Sender resource CRUD operations"""
        return SendersResource(self._client)

    @cached_property
    def memories(self) -> MemoriesResource:
        """Memory ingestion, retrieval, search, and deletion"""
        return MemoriesResource(self._client)

    @cached_property
    def object(self) -> ObjectResource:
        """Multimodal content storage (pre-signed upload)"""
        return ObjectResource(self._client)

    @cached_property
    def tasks(self) -> TasksResource:
        """Async task status tracking"""
        return TasksResource(self._client)

    @cached_property
    def with_raw_response(self) -> V1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/everos/everos-python#accessing-raw-response-data-eg-headers
        """
        return V1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/everos/everos-python#with_streaming_response
        """
        return V1ResourceWithStreamingResponse(self)


class AsyncV1Resource(AsyncAPIResource):
    @cached_property
    def groups(self) -> AsyncGroupsResource:
        """Group resource CRUD operations"""
        return AsyncGroupsResource(self._client)

    @cached_property
    def settings(self) -> AsyncSettingsResource:
        """Global settings management"""
        return AsyncSettingsResource(self._client)

    @cached_property
    def senders(self) -> AsyncSendersResource:
        """Sender resource CRUD operations"""
        return AsyncSendersResource(self._client)

    @cached_property
    def memories(self) -> AsyncMemoriesResource:
        """Memory ingestion, retrieval, search, and deletion"""
        return AsyncMemoriesResource(self._client)

    @cached_property
    def object(self) -> AsyncObjectResource:
        """Multimodal content storage (pre-signed upload)"""
        return AsyncObjectResource(self._client)

    @cached_property
    def tasks(self) -> AsyncTasksResource:
        """Async task status tracking"""
        return AsyncTasksResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/everos/everos-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/everos/everos-python#with_streaming_response
        """
        return AsyncV1ResourceWithStreamingResponse(self)


class V1ResourceWithRawResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

    @cached_property
    def groups(self) -> GroupsResourceWithRawResponse:
        """Group resource CRUD operations"""
        return GroupsResourceWithRawResponse(self._v1.groups)

    @cached_property
    def settings(self) -> SettingsResourceWithRawResponse:
        """Global settings management"""
        return SettingsResourceWithRawResponse(self._v1.settings)

    @cached_property
    def senders(self) -> SendersResourceWithRawResponse:
        """Sender resource CRUD operations"""
        return SendersResourceWithRawResponse(self._v1.senders)

    @cached_property
    def memories(self) -> MemoriesResourceWithRawResponse:
        """Memory ingestion, retrieval, search, and deletion"""
        return MemoriesResourceWithRawResponse(self._v1.memories)

    @cached_property
    def object(self) -> ObjectResourceWithRawResponse:
        """Multimodal content storage (pre-signed upload)"""
        return ObjectResourceWithRawResponse(self._v1.object)

    @cached_property
    def tasks(self) -> TasksResourceWithRawResponse:
        """Async task status tracking"""
        return TasksResourceWithRawResponse(self._v1.tasks)


class AsyncV1ResourceWithRawResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

    @cached_property
    def groups(self) -> AsyncGroupsResourceWithRawResponse:
        """Group resource CRUD operations"""
        return AsyncGroupsResourceWithRawResponse(self._v1.groups)

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithRawResponse:
        """Global settings management"""
        return AsyncSettingsResourceWithRawResponse(self._v1.settings)

    @cached_property
    def senders(self) -> AsyncSendersResourceWithRawResponse:
        """Sender resource CRUD operations"""
        return AsyncSendersResourceWithRawResponse(self._v1.senders)

    @cached_property
    def memories(self) -> AsyncMemoriesResourceWithRawResponse:
        """Memory ingestion, retrieval, search, and deletion"""
        return AsyncMemoriesResourceWithRawResponse(self._v1.memories)

    @cached_property
    def object(self) -> AsyncObjectResourceWithRawResponse:
        """Multimodal content storage (pre-signed upload)"""
        return AsyncObjectResourceWithRawResponse(self._v1.object)

    @cached_property
    def tasks(self) -> AsyncTasksResourceWithRawResponse:
        """Async task status tracking"""
        return AsyncTasksResourceWithRawResponse(self._v1.tasks)


class V1ResourceWithStreamingResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

    @cached_property
    def groups(self) -> GroupsResourceWithStreamingResponse:
        """Group resource CRUD operations"""
        return GroupsResourceWithStreamingResponse(self._v1.groups)

    @cached_property
    def settings(self) -> SettingsResourceWithStreamingResponse:
        """Global settings management"""
        return SettingsResourceWithStreamingResponse(self._v1.settings)

    @cached_property
    def senders(self) -> SendersResourceWithStreamingResponse:
        """Sender resource CRUD operations"""
        return SendersResourceWithStreamingResponse(self._v1.senders)

    @cached_property
    def memories(self) -> MemoriesResourceWithStreamingResponse:
        """Memory ingestion, retrieval, search, and deletion"""
        return MemoriesResourceWithStreamingResponse(self._v1.memories)

    @cached_property
    def object(self) -> ObjectResourceWithStreamingResponse:
        """Multimodal content storage (pre-signed upload)"""
        return ObjectResourceWithStreamingResponse(self._v1.object)

    @cached_property
    def tasks(self) -> TasksResourceWithStreamingResponse:
        """Async task status tracking"""
        return TasksResourceWithStreamingResponse(self._v1.tasks)


class AsyncV1ResourceWithStreamingResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

    @cached_property
    def groups(self) -> AsyncGroupsResourceWithStreamingResponse:
        """Group resource CRUD operations"""
        return AsyncGroupsResourceWithStreamingResponse(self._v1.groups)

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithStreamingResponse:
        """Global settings management"""
        return AsyncSettingsResourceWithStreamingResponse(self._v1.settings)

    @cached_property
    def senders(self) -> AsyncSendersResourceWithStreamingResponse:
        """Sender resource CRUD operations"""
        return AsyncSendersResourceWithStreamingResponse(self._v1.senders)

    @cached_property
    def memories(self) -> AsyncMemoriesResourceWithStreamingResponse:
        """Memory ingestion, retrieval, search, and deletion"""
        return AsyncMemoriesResourceWithStreamingResponse(self._v1.memories)

    @cached_property
    def object(self) -> AsyncObjectResourceWithStreamingResponse:
        """Multimodal content storage (pre-signed upload)"""
        return AsyncObjectResourceWithStreamingResponse(self._v1.object)

    @cached_property
    def tasks(self) -> AsyncTasksResourceWithStreamingResponse:
        """Async task status tracking"""
        return AsyncTasksResourceWithStreamingResponse(self._v1.tasks)
