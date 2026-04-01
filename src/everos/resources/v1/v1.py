# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

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
from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template
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
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from .memories.memories import (
    MemoriesResource,
    AsyncMemoriesResource,
    MemoriesResourceWithRawResponse,
    AsyncMemoriesResourceWithRawResponse,
    MemoriesResourceWithStreamingResponse,
    AsyncMemoriesResourceWithStreamingResponse,
)
from ...types.v1_query_task_status_response import V1QueryTaskStatusResponse

__all__ = ["V1Resource", "AsyncV1Resource"]


class V1Resource(SyncAPIResource):
    """Async task status tracking"""

    @cached_property
    def memories(self) -> MemoriesResource:
        """Memory ingestion, retrieval, search, and deletion"""
        return MemoriesResource(self._client)

    @cached_property
    def groups(self) -> GroupsResource:
        """Group resource CRUD operations"""
        return GroupsResource(self._client)

    @cached_property
    def senders(self) -> SendersResource:
        """Sender resource CRUD operations"""
        return SendersResource(self._client)

    @cached_property
    def object(self) -> ObjectResource:
        """Multimodal content storage (pre-signed upload)"""
        return ObjectResource(self._client)

    @cached_property
    def settings(self) -> SettingsResource:
        """Global settings management"""
        return SettingsResource(self._client)

    @cached_property
    def with_raw_response(self) -> V1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/everos-python#accessing-raw-response-data-eg-headers
        """
        return V1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/everos-python#with_streaming_response
        """
        return V1ResourceWithStreamingResponse(self)

    def query_task_status(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1QueryTaskStatusResponse:
        """Query the processing status of a specific async task by task_id.

        Task status is
        stored in Redis with a TTL of 1 hour. Internal status 'start' is mapped to
        'processing' in the response.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return self._get(
            path_template("/api/v1/tasks/{task_id}", task_id=task_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1QueryTaskStatusResponse,
        )


class AsyncV1Resource(AsyncAPIResource):
    """Async task status tracking"""

    @cached_property
    def memories(self) -> AsyncMemoriesResource:
        """Memory ingestion, retrieval, search, and deletion"""
        return AsyncMemoriesResource(self._client)

    @cached_property
    def groups(self) -> AsyncGroupsResource:
        """Group resource CRUD operations"""
        return AsyncGroupsResource(self._client)

    @cached_property
    def senders(self) -> AsyncSendersResource:
        """Sender resource CRUD operations"""
        return AsyncSendersResource(self._client)

    @cached_property
    def object(self) -> AsyncObjectResource:
        """Multimodal content storage (pre-signed upload)"""
        return AsyncObjectResource(self._client)

    @cached_property
    def settings(self) -> AsyncSettingsResource:
        """Global settings management"""
        return AsyncSettingsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/everos-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/everos-python#with_streaming_response
        """
        return AsyncV1ResourceWithStreamingResponse(self)

    async def query_task_status(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1QueryTaskStatusResponse:
        """Query the processing status of a specific async task by task_id.

        Task status is
        stored in Redis with a TTL of 1 hour. Internal status 'start' is mapped to
        'processing' in the response.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return await self._get(
            path_template("/api/v1/tasks/{task_id}", task_id=task_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1QueryTaskStatusResponse,
        )


class V1ResourceWithRawResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.query_task_status = to_raw_response_wrapper(
            v1.query_task_status,
        )

    @cached_property
    def memories(self) -> MemoriesResourceWithRawResponse:
        """Memory ingestion, retrieval, search, and deletion"""
        return MemoriesResourceWithRawResponse(self._v1.memories)

    @cached_property
    def groups(self) -> GroupsResourceWithRawResponse:
        """Group resource CRUD operations"""
        return GroupsResourceWithRawResponse(self._v1.groups)

    @cached_property
    def senders(self) -> SendersResourceWithRawResponse:
        """Sender resource CRUD operations"""
        return SendersResourceWithRawResponse(self._v1.senders)

    @cached_property
    def object(self) -> ObjectResourceWithRawResponse:
        """Multimodal content storage (pre-signed upload)"""
        return ObjectResourceWithRawResponse(self._v1.object)

    @cached_property
    def settings(self) -> SettingsResourceWithRawResponse:
        """Global settings management"""
        return SettingsResourceWithRawResponse(self._v1.settings)


class AsyncV1ResourceWithRawResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.query_task_status = async_to_raw_response_wrapper(
            v1.query_task_status,
        )

    @cached_property
    def memories(self) -> AsyncMemoriesResourceWithRawResponse:
        """Memory ingestion, retrieval, search, and deletion"""
        return AsyncMemoriesResourceWithRawResponse(self._v1.memories)

    @cached_property
    def groups(self) -> AsyncGroupsResourceWithRawResponse:
        """Group resource CRUD operations"""
        return AsyncGroupsResourceWithRawResponse(self._v1.groups)

    @cached_property
    def senders(self) -> AsyncSendersResourceWithRawResponse:
        """Sender resource CRUD operations"""
        return AsyncSendersResourceWithRawResponse(self._v1.senders)

    @cached_property
    def object(self) -> AsyncObjectResourceWithRawResponse:
        """Multimodal content storage (pre-signed upload)"""
        return AsyncObjectResourceWithRawResponse(self._v1.object)

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithRawResponse:
        """Global settings management"""
        return AsyncSettingsResourceWithRawResponse(self._v1.settings)


class V1ResourceWithStreamingResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.query_task_status = to_streamed_response_wrapper(
            v1.query_task_status,
        )

    @cached_property
    def memories(self) -> MemoriesResourceWithStreamingResponse:
        """Memory ingestion, retrieval, search, and deletion"""
        return MemoriesResourceWithStreamingResponse(self._v1.memories)

    @cached_property
    def groups(self) -> GroupsResourceWithStreamingResponse:
        """Group resource CRUD operations"""
        return GroupsResourceWithStreamingResponse(self._v1.groups)

    @cached_property
    def senders(self) -> SendersResourceWithStreamingResponse:
        """Sender resource CRUD operations"""
        return SendersResourceWithStreamingResponse(self._v1.senders)

    @cached_property
    def object(self) -> ObjectResourceWithStreamingResponse:
        """Multimodal content storage (pre-signed upload)"""
        return ObjectResourceWithStreamingResponse(self._v1.object)

    @cached_property
    def settings(self) -> SettingsResourceWithStreamingResponse:
        """Global settings management"""
        return SettingsResourceWithStreamingResponse(self._v1.settings)


class AsyncV1ResourceWithStreamingResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.query_task_status = async_to_streamed_response_wrapper(
            v1.query_task_status,
        )

    @cached_property
    def memories(self) -> AsyncMemoriesResourceWithStreamingResponse:
        """Memory ingestion, retrieval, search, and deletion"""
        return AsyncMemoriesResourceWithStreamingResponse(self._v1.memories)

    @cached_property
    def groups(self) -> AsyncGroupsResourceWithStreamingResponse:
        """Group resource CRUD operations"""
        return AsyncGroupsResourceWithStreamingResponse(self._v1.groups)

    @cached_property
    def senders(self) -> AsyncSendersResourceWithStreamingResponse:
        """Sender resource CRUD operations"""
        return AsyncSendersResourceWithStreamingResponse(self._v1.senders)

    @cached_property
    def object(self) -> AsyncObjectResourceWithStreamingResponse:
        """Multimodal content storage (pre-signed upload)"""
        return AsyncObjectResourceWithStreamingResponse(self._v1.object)

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithStreamingResponse:
        """Global settings management"""
        return AsyncSettingsResourceWithStreamingResponse(self._v1.settings)
