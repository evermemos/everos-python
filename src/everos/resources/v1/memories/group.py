# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v1.memories import group_flush_params, group_create_params
from ....types.v1.add_response import AddResponse
from ....types.v1.flush_response import FlushResponse

__all__ = ["GroupResource", "AsyncGroupResource"]


class GroupResource(SyncAPIResource):
    """Memory ingestion, retrieval, search, and deletion"""

    @cached_property
    def with_raw_response(self) -> GroupResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/evermemos/everos-python#accessing-raw-response-data-eg-headers
        """
        return GroupResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GroupResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/evermemos/everos-python#with_streaming_response
        """
        return GroupResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        group_id: str,
        messages: Iterable[group_create_params.Message],
        async_mode: bool | Omit = omit,
        group_meta: Optional[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddResponse:
        """Store batch messages into group memory space.

        Each message must include
        sender_id to identify participants.

        Args:
          group_id: Group identifier

          messages: Batch message array (1-500 items). sender_id is required per message.

          async_mode: Enable async processing. When true, returns 202 with task_id; when false,
              processes synchronously and returns 200.

          group_meta: Group metadata

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/memories/group",
            body=maybe_transform(
                {
                    "group_id": group_id,
                    "messages": messages,
                    "async_mode": async_mode,
                    "group_meta": group_meta,
                },
                group_create_params.GroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddResponse,
        )

    def flush(
        self,
        *,
        group_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FlushResponse:
        """
        Trigger boundary detection on accumulated group messages.

        Args:
          group_id: Target group

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/memories/group/flush",
            body=maybe_transform({"group_id": group_id}, group_flush_params.GroupFlushParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FlushResponse,
        )


class AsyncGroupResource(AsyncAPIResource):
    """Memory ingestion, retrieval, search, and deletion"""

    @cached_property
    def with_raw_response(self) -> AsyncGroupResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/evermemos/everos-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGroupResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGroupResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/evermemos/everos-python#with_streaming_response
        """
        return AsyncGroupResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        group_id: str,
        messages: Iterable[group_create_params.Message],
        async_mode: bool | Omit = omit,
        group_meta: Optional[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddResponse:
        """Store batch messages into group memory space.

        Each message must include
        sender_id to identify participants.

        Args:
          group_id: Group identifier

          messages: Batch message array (1-500 items). sender_id is required per message.

          async_mode: Enable async processing. When true, returns 202 with task_id; when false,
              processes synchronously and returns 200.

          group_meta: Group metadata

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/memories/group",
            body=await async_maybe_transform(
                {
                    "group_id": group_id,
                    "messages": messages,
                    "async_mode": async_mode,
                    "group_meta": group_meta,
                },
                group_create_params.GroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddResponse,
        )

    async def flush(
        self,
        *,
        group_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FlushResponse:
        """
        Trigger boundary detection on accumulated group messages.

        Args:
          group_id: Target group

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/memories/group/flush",
            body=await async_maybe_transform({"group_id": group_id}, group_flush_params.GroupFlushParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FlushResponse,
        )


class GroupResourceWithRawResponse:
    def __init__(self, group: GroupResource) -> None:
        self._group = group

        self.create = to_raw_response_wrapper(
            group.create,
        )
        self.flush = to_raw_response_wrapper(
            group.flush,
        )


class AsyncGroupResourceWithRawResponse:
    def __init__(self, group: AsyncGroupResource) -> None:
        self._group = group

        self.create = async_to_raw_response_wrapper(
            group.create,
        )
        self.flush = async_to_raw_response_wrapper(
            group.flush,
        )


class GroupResourceWithStreamingResponse:
    def __init__(self, group: GroupResource) -> None:
        self._group = group

        self.create = to_streamed_response_wrapper(
            group.create,
        )
        self.flush = to_streamed_response_wrapper(
            group.flush,
        )


class AsyncGroupResourceWithStreamingResponse:
    def __init__(self, group: AsyncGroupResource) -> None:
        self._group = group

        self.create = async_to_streamed_response_wrapper(
            group.create,
        )
        self.flush = async_to_streamed_response_wrapper(
            group.flush,
        )
