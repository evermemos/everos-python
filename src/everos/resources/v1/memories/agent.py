# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

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
from ....types.v1.memories import agent_flush_params, agent_create_params
from ....types.v1.add_response import AddResponse
from ....types.v1.flush_response import FlushResponse

__all__ = ["AgentResource", "AsyncAgentResource"]


class AgentResource(SyncAPIResource):
    """Memory ingestion, retrieval, search, and deletion"""

    @cached_property
    def with_raw_response(self) -> AgentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/everos-python#accessing-raw-response-data-eg-headers
        """
        return AgentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/everos-python#with_streaming_response
        """
        return AgentResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        messages: Iterable[agent_create_params.Message],
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
        """Store agent trajectory messages (user/assistant/tool) into memory.

        Supports
        tool_calls and tool_call_id for OpenAI-format function calling.

        Args:
          messages: Agent trajectory messages (1-500 items)

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
            "/api/v1/memories/agent",
            body=maybe_transform(
                {
                    "messages": messages,
                    "user_id": user_id,
                    "async_mode": async_mode,
                    "session_id": session_id,
                },
                agent_create_params.AgentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddResponse,
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
        """
        Trigger agent-aware boundary detection on accumulated agent trajectory messages.
        Extracts agent cases and skills when boundary is detected.

        Args:
          user_id: Owner user ID

          session_id: Target session

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/memories/agent/flush",
            body=maybe_transform(
                {
                    "user_id": user_id,
                    "session_id": session_id,
                },
                agent_flush_params.AgentFlushParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FlushResponse,
        )


class AsyncAgentResource(AsyncAPIResource):
    """Memory ingestion, retrieval, search, and deletion"""

    @cached_property
    def with_raw_response(self) -> AsyncAgentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/everos-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAgentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/everos-python#with_streaming_response
        """
        return AsyncAgentResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        messages: Iterable[agent_create_params.Message],
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
        """Store agent trajectory messages (user/assistant/tool) into memory.

        Supports
        tool_calls and tool_call_id for OpenAI-format function calling.

        Args:
          messages: Agent trajectory messages (1-500 items)

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
            "/api/v1/memories/agent",
            body=await async_maybe_transform(
                {
                    "messages": messages,
                    "user_id": user_id,
                    "async_mode": async_mode,
                    "session_id": session_id,
                },
                agent_create_params.AgentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddResponse,
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
        """
        Trigger agent-aware boundary detection on accumulated agent trajectory messages.
        Extracts agent cases and skills when boundary is detected.

        Args:
          user_id: Owner user ID

          session_id: Target session

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/memories/agent/flush",
            body=await async_maybe_transform(
                {
                    "user_id": user_id,
                    "session_id": session_id,
                },
                agent_flush_params.AgentFlushParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FlushResponse,
        )


class AgentResourceWithRawResponse:
    def __init__(self, agent: AgentResource) -> None:
        self._agent = agent

        self.create = to_raw_response_wrapper(
            agent.create,
        )
        self.flush = to_raw_response_wrapper(
            agent.flush,
        )


class AsyncAgentResourceWithRawResponse:
    def __init__(self, agent: AsyncAgentResource) -> None:
        self._agent = agent

        self.create = async_to_raw_response_wrapper(
            agent.create,
        )
        self.flush = async_to_raw_response_wrapper(
            agent.flush,
        )


class AgentResourceWithStreamingResponse:
    def __init__(self, agent: AgentResource) -> None:
        self._agent = agent

        self.create = to_streamed_response_wrapper(
            agent.create,
        )
        self.flush = to_streamed_response_wrapper(
            agent.flush,
        )


class AsyncAgentResourceWithStreamingResponse:
    def __init__(self, agent: AsyncAgentResource) -> None:
        self._agent = agent

        self.create = async_to_streamed_response_wrapper(
            agent.create,
        )
        self.flush = async_to_streamed_response_wrapper(
            agent.flush,
        )
