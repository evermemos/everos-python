# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable, Optional
from typing_extensions import Literal

import httpx

from .agent import (
    AgentResource,
    AsyncAgentResource,
    AgentResourceWithRawResponse,
    AsyncAgentResourceWithRawResponse,
    AgentResourceWithStreamingResponse,
    AsyncAgentResourceWithStreamingResponse,
)
from .group import (
    GroupResource,
    AsyncGroupResource,
    GroupResourceWithRawResponse,
    AsyncGroupResourceWithRawResponse,
    GroupResourceWithStreamingResponse,
    AsyncGroupResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ....types.v1 import (
    memory_get_params,
    memory_flush_params,
    memory_create_params,
    memory_delete_params,
    memory_search_params,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v1.add_response import AddResponse
from ....types.v1.flush_response import FlushResponse
from ....types.v1.memory_get_response import MemoryGetResponse
from ....types.v1.memory_search_response import MemorySearchResponse

__all__ = ["MemoriesResource", "AsyncMemoriesResource"]


class MemoriesResource(SyncAPIResource):
    """Memory ingestion, retrieval, search, and deletion"""

    @cached_property
    def group(self) -> GroupResource:
        """Memory ingestion, retrieval, search, and deletion"""
        return GroupResource(self._client)

    @cached_property
    def agent(self) -> AgentResource:
        """Memory ingestion, retrieval, search, and deletion"""
        return AgentResource(self._client)

    @cached_property
    def with_raw_response(self) -> MemoriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/everos-python#accessing-raw-response-data-eg-headers
        """
        return MemoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MemoriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/everos-python#with_streaming_response
        """
        return MemoriesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        messages: Iterable[memory_create_params.Message],
        user_id: str,
        async_mode: bool | Omit = omit,
        session_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddResponse:
        """Store batch messages into personal memory space.

        Messages are accumulated and
        boundary detection triggers memory extraction automatically.

        Args:
          messages: Batch message array (1-500 items)

          user_id: Owner user ID

          async_mode: Enable async processing. When true, returns 202 with task_id; when false,
              processes synchronously and returns 200.

          session_id: Session identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/memories",
            body=maybe_transform(
                {
                    "messages": messages,
                    "user_id": user_id,
                    "async_mode": async_mode,
                    "session_id": session_id,
                },
                memory_create_params.MemoryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddResponse,
        )

    def delete(
        self,
        *,
        group_id: Optional[str] | Omit = omit,
        memory_id: Optional[str] | Omit = omit,
        sender_id: Optional[str] | Omit = omit,
        session_id: Optional[str] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Soft delete memories by ID or by filter conditions.

        Two mutually exclusive modes:

        - **By ID**: provide `memory_id` only (no other fields allowed)
        - **By filters**: provide `user_id` and/or `group_id` (session_id, sender_id
          optional)

        Filter semantics: omitted fields skip filtering; `null` or `""` matches
        null/empty records; string value = exact match.

        Args:
          group_id: Group ID scope for batch delete

          memory_id: MemCell ID for single delete

          sender_id: Sender filter, matches participants array (batch delete only)

          session_id: Session filter (batch delete only)

          user_id: User ID scope for batch delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/api/v1/memories/delete",
            body=maybe_transform(
                {
                    "group_id": group_id,
                    "memory_id": memory_id,
                    "sender_id": sender_id,
                    "session_id": session_id,
                    "user_id": user_id,
                },
                memory_delete_params.MemoryDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def flush(
        self,
        *,
        user_id: str,
        session_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FlushResponse:
        """Trigger boundary detection on accumulated personal messages.

        If a boundary is
        detected, memory extraction is triggered immediately.

        Args:
          user_id: Owner user ID

          session_id: Target session

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/memories/flush",
            body=maybe_transform(
                {
                    "user_id": user_id,
                    "session_id": session_id,
                },
                memory_flush_params.MemoryFlushParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FlushResponse,
        )

    def get(
        self,
        *,
        filters: Dict[str, object],
        memory_type: Literal["episodic_memory", "profile", "agent_case", "agent_skill"],
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        rank_by: str | Omit = omit,
        rank_order: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryGetResponse:
        """Retrieve structured memories using filters DSL with pagination.

        Supports
        episodic_memory, profile, agent_case, and agent_skill types.

        ## Filters DSL

        Allowlist-based: only the following fields are processed, unknown fields are
        silently ignored.

        | Field        | Type                           | Operators                | Description                            |
        | ------------ | ------------------------------ | ------------------------ | -------------------------------------- |
        | `user_id`    | string                         | eq, in                   | User ID filter (conditional required)  |
        | `group_id`   | string                         | eq, in                   | Group ID filter (conditional required) |
        | `session_id` | string                         | eq, in, gt, gte, lt, lte | Session ID filter                      |
        | `timestamp`  | int (epoch ms/s) or ISO string | eq, gt, gte, lt, lte     | Time range filter                      |
        | `AND`        | array                          | -                        | All conditions must match              |
        | `OR`         | array                          | -                        | Any condition must match               |

        **Operator syntax**: plain value = eq, `{"in": [...]}`, `{"gte": v, "lt": v}`

        Args:
          filters: Filter conditions. Must contain user_id or group_id (see memory_type for scope
              constraints). Supports operators: eq (implicit), in, gt, gte, lt, lte.
              Combinators: AND, OR.

          memory_type:
              Memory type to query. Scope constraint per type:

              - episodic_memory: supports both user_id and group_id
              - profile: user_id only (group_id will return 400)
              - agent_case: user_id only (group_id will return 400)
              - agent_skill: user_id only (group_id will return 400)

          page: Page number (starts from 1)

          page_size: Items per page

          rank_by: Sort field

          rank_order: Sort order

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/memories/get",
            body=maybe_transform(
                {
                    "filters": filters,
                    "memory_type": memory_type,
                    "page": page,
                    "page_size": page_size,
                    "rank_by": rank_by,
                    "rank_order": rank_order,
                },
                memory_get_params.MemoryGetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryGetResponse,
        )

    def search(
        self,
        *,
        filters: Dict[str, object],
        query: str,
        include_original_data: bool | Omit = omit,
        memory_types: List[Literal["episodic_memory", "profile", "raw_message", "agent_memory"]] | Omit = omit,
        method: Literal["keyword", "vector", "hybrid", "agentic"] | Omit = omit,
        radius: Optional[float] | Omit = omit,
        top_k: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemorySearchResponse:
        """
        Unified memory search endpoint supporting multiple memory types and retrieval
        methods.

        ## Retrieval Methods

        - **keyword**: BM25 keyword retrieval (Elasticsearch only)
        - **vector**: Vector semantic retrieval (Milvus only)
        - **hybrid** (default): Hybrid retrieval with rerank (ES + Milvus + Rerank)
        - **agentic**: LLM-guided multi-round intelligent retrieval

        ## Memory Types

        - **episodic_memory**: Episodic memory (ES + Milvus)
        - **profile**: User profile (Milvus only)
        - **raw_message**: Raw unprocessed messages (ES only)
        - **agent_memory**: Agent memory - cases and skills (ES + Milvus)

        ## Filters DSL

        Same syntax as the GET endpoint. Must contain at least one of `user_id` or
        `group_id`.

        Args:
          filters: Filter conditions. Must contain user_id or group_id (agent_memory and profile
              require user_id only, same scope constraints as GET endpoint). Same DSL as GET
              endpoint.

          query: Search query text

          include_original_data: Whether to return original data

          memory_types: Memory types to search

          method: Retrieval method

          radius: COSINE similarity threshold (0.0-1.0) for vector methods

          top_k: Max results. -1 = return all meeting threshold (up to 100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/memories/search",
            body=maybe_transform(
                {
                    "filters": filters,
                    "query": query,
                    "include_original_data": include_original_data,
                    "memory_types": memory_types,
                    "method": method,
                    "radius": radius,
                    "top_k": top_k,
                },
                memory_search_params.MemorySearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemorySearchResponse,
        )


class AsyncMemoriesResource(AsyncAPIResource):
    """Memory ingestion, retrieval, search, and deletion"""

    @cached_property
    def group(self) -> AsyncGroupResource:
        """Memory ingestion, retrieval, search, and deletion"""
        return AsyncGroupResource(self._client)

    @cached_property
    def agent(self) -> AsyncAgentResource:
        """Memory ingestion, retrieval, search, and deletion"""
        return AsyncAgentResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMemoriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/everos-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMemoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMemoriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/everos-python#with_streaming_response
        """
        return AsyncMemoriesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        messages: Iterable[memory_create_params.Message],
        user_id: str,
        async_mode: bool | Omit = omit,
        session_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddResponse:
        """Store batch messages into personal memory space.

        Messages are accumulated and
        boundary detection triggers memory extraction automatically.

        Args:
          messages: Batch message array (1-500 items)

          user_id: Owner user ID

          async_mode: Enable async processing. When true, returns 202 with task_id; when false,
              processes synchronously and returns 200.

          session_id: Session identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/memories",
            body=await async_maybe_transform(
                {
                    "messages": messages,
                    "user_id": user_id,
                    "async_mode": async_mode,
                    "session_id": session_id,
                },
                memory_create_params.MemoryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddResponse,
        )

    async def delete(
        self,
        *,
        group_id: Optional[str] | Omit = omit,
        memory_id: Optional[str] | Omit = omit,
        sender_id: Optional[str] | Omit = omit,
        session_id: Optional[str] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Soft delete memories by ID or by filter conditions.

        Two mutually exclusive modes:

        - **By ID**: provide `memory_id` only (no other fields allowed)
        - **By filters**: provide `user_id` and/or `group_id` (session_id, sender_id
          optional)

        Filter semantics: omitted fields skip filtering; `null` or `""` matches
        null/empty records; string value = exact match.

        Args:
          group_id: Group ID scope for batch delete

          memory_id: MemCell ID for single delete

          sender_id: Sender filter, matches participants array (batch delete only)

          session_id: Session filter (batch delete only)

          user_id: User ID scope for batch delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/api/v1/memories/delete",
            body=await async_maybe_transform(
                {
                    "group_id": group_id,
                    "memory_id": memory_id,
                    "sender_id": sender_id,
                    "session_id": session_id,
                    "user_id": user_id,
                },
                memory_delete_params.MemoryDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def flush(
        self,
        *,
        user_id: str,
        session_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FlushResponse:
        """Trigger boundary detection on accumulated personal messages.

        If a boundary is
        detected, memory extraction is triggered immediately.

        Args:
          user_id: Owner user ID

          session_id: Target session

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/memories/flush",
            body=await async_maybe_transform(
                {
                    "user_id": user_id,
                    "session_id": session_id,
                },
                memory_flush_params.MemoryFlushParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FlushResponse,
        )

    async def get(
        self,
        *,
        filters: Dict[str, object],
        memory_type: Literal["episodic_memory", "profile", "agent_case", "agent_skill"],
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        rank_by: str | Omit = omit,
        rank_order: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryGetResponse:
        """Retrieve structured memories using filters DSL with pagination.

        Supports
        episodic_memory, profile, agent_case, and agent_skill types.

        ## Filters DSL

        Allowlist-based: only the following fields are processed, unknown fields are
        silently ignored.

        | Field        | Type                           | Operators                | Description                            |
        | ------------ | ------------------------------ | ------------------------ | -------------------------------------- |
        | `user_id`    | string                         | eq, in                   | User ID filter (conditional required)  |
        | `group_id`   | string                         | eq, in                   | Group ID filter (conditional required) |
        | `session_id` | string                         | eq, in, gt, gte, lt, lte | Session ID filter                      |
        | `timestamp`  | int (epoch ms/s) or ISO string | eq, gt, gte, lt, lte     | Time range filter                      |
        | `AND`        | array                          | -                        | All conditions must match              |
        | `OR`         | array                          | -                        | Any condition must match               |

        **Operator syntax**: plain value = eq, `{"in": [...]}`, `{"gte": v, "lt": v}`

        Args:
          filters: Filter conditions. Must contain user_id or group_id (see memory_type for scope
              constraints). Supports operators: eq (implicit), in, gt, gte, lt, lte.
              Combinators: AND, OR.

          memory_type:
              Memory type to query. Scope constraint per type:

              - episodic_memory: supports both user_id and group_id
              - profile: user_id only (group_id will return 400)
              - agent_case: user_id only (group_id will return 400)
              - agent_skill: user_id only (group_id will return 400)

          page: Page number (starts from 1)

          page_size: Items per page

          rank_by: Sort field

          rank_order: Sort order

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/memories/get",
            body=await async_maybe_transform(
                {
                    "filters": filters,
                    "memory_type": memory_type,
                    "page": page,
                    "page_size": page_size,
                    "rank_by": rank_by,
                    "rank_order": rank_order,
                },
                memory_get_params.MemoryGetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryGetResponse,
        )

    async def search(
        self,
        *,
        filters: Dict[str, object],
        query: str,
        include_original_data: bool | Omit = omit,
        memory_types: List[Literal["episodic_memory", "profile", "raw_message", "agent_memory"]] | Omit = omit,
        method: Literal["keyword", "vector", "hybrid", "agentic"] | Omit = omit,
        radius: Optional[float] | Omit = omit,
        top_k: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemorySearchResponse:
        """
        Unified memory search endpoint supporting multiple memory types and retrieval
        methods.

        ## Retrieval Methods

        - **keyword**: BM25 keyword retrieval (Elasticsearch only)
        - **vector**: Vector semantic retrieval (Milvus only)
        - **hybrid** (default): Hybrid retrieval with rerank (ES + Milvus + Rerank)
        - **agentic**: LLM-guided multi-round intelligent retrieval

        ## Memory Types

        - **episodic_memory**: Episodic memory (ES + Milvus)
        - **profile**: User profile (Milvus only)
        - **raw_message**: Raw unprocessed messages (ES only)
        - **agent_memory**: Agent memory - cases and skills (ES + Milvus)

        ## Filters DSL

        Same syntax as the GET endpoint. Must contain at least one of `user_id` or
        `group_id`.

        Args:
          filters: Filter conditions. Must contain user_id or group_id (agent_memory and profile
              require user_id only, same scope constraints as GET endpoint). Same DSL as GET
              endpoint.

          query: Search query text

          include_original_data: Whether to return original data

          memory_types: Memory types to search

          method: Retrieval method

          radius: COSINE similarity threshold (0.0-1.0) for vector methods

          top_k: Max results. -1 = return all meeting threshold (up to 100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/memories/search",
            body=await async_maybe_transform(
                {
                    "filters": filters,
                    "query": query,
                    "include_original_data": include_original_data,
                    "memory_types": memory_types,
                    "method": method,
                    "radius": radius,
                    "top_k": top_k,
                },
                memory_search_params.MemorySearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemorySearchResponse,
        )


class MemoriesResourceWithRawResponse:
    def __init__(self, memories: MemoriesResource) -> None:
        self._memories = memories

        self.create = to_raw_response_wrapper(
            memories.create,
        )
        self.delete = to_raw_response_wrapper(
            memories.delete,
        )
        self.flush = to_raw_response_wrapper(
            memories.flush,
        )
        self.get = to_raw_response_wrapper(
            memories.get,
        )
        self.search = to_raw_response_wrapper(
            memories.search,
        )

    @cached_property
    def group(self) -> GroupResourceWithRawResponse:
        """Memory ingestion, retrieval, search, and deletion"""
        return GroupResourceWithRawResponse(self._memories.group)

    @cached_property
    def agent(self) -> AgentResourceWithRawResponse:
        """Memory ingestion, retrieval, search, and deletion"""
        return AgentResourceWithRawResponse(self._memories.agent)


class AsyncMemoriesResourceWithRawResponse:
    def __init__(self, memories: AsyncMemoriesResource) -> None:
        self._memories = memories

        self.create = async_to_raw_response_wrapper(
            memories.create,
        )
        self.delete = async_to_raw_response_wrapper(
            memories.delete,
        )
        self.flush = async_to_raw_response_wrapper(
            memories.flush,
        )
        self.get = async_to_raw_response_wrapper(
            memories.get,
        )
        self.search = async_to_raw_response_wrapper(
            memories.search,
        )

    @cached_property
    def group(self) -> AsyncGroupResourceWithRawResponse:
        """Memory ingestion, retrieval, search, and deletion"""
        return AsyncGroupResourceWithRawResponse(self._memories.group)

    @cached_property
    def agent(self) -> AsyncAgentResourceWithRawResponse:
        """Memory ingestion, retrieval, search, and deletion"""
        return AsyncAgentResourceWithRawResponse(self._memories.agent)


class MemoriesResourceWithStreamingResponse:
    def __init__(self, memories: MemoriesResource) -> None:
        self._memories = memories

        self.create = to_streamed_response_wrapper(
            memories.create,
        )
        self.delete = to_streamed_response_wrapper(
            memories.delete,
        )
        self.flush = to_streamed_response_wrapper(
            memories.flush,
        )
        self.get = to_streamed_response_wrapper(
            memories.get,
        )
        self.search = to_streamed_response_wrapper(
            memories.search,
        )

    @cached_property
    def group(self) -> GroupResourceWithStreamingResponse:
        """Memory ingestion, retrieval, search, and deletion"""
        return GroupResourceWithStreamingResponse(self._memories.group)

    @cached_property
    def agent(self) -> AgentResourceWithStreamingResponse:
        """Memory ingestion, retrieval, search, and deletion"""
        return AgentResourceWithStreamingResponse(self._memories.agent)


class AsyncMemoriesResourceWithStreamingResponse:
    def __init__(self, memories: AsyncMemoriesResource) -> None:
        self._memories = memories

        self.create = async_to_streamed_response_wrapper(
            memories.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            memories.delete,
        )
        self.flush = async_to_streamed_response_wrapper(
            memories.flush,
        )
        self.get = async_to_streamed_response_wrapper(
            memories.get,
        )
        self.search = async_to_streamed_response_wrapper(
            memories.search,
        )

    @cached_property
    def group(self) -> AsyncGroupResourceWithStreamingResponse:
        """Memory ingestion, retrieval, search, and deletion"""
        return AsyncGroupResourceWithStreamingResponse(self._memories.group)

    @cached_property
    def agent(self) -> AsyncAgentResourceWithStreamingResponse:
        """Memory ingestion, retrieval, search, and deletion"""
        return AsyncAgentResourceWithStreamingResponse(self._memories.agent)
