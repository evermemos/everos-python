# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v1 import sender_update_params, sender_create_or_update_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v1.sender_api_response import SenderAPIResponse

__all__ = ["SendersResource", "AsyncSendersResource"]


class SendersResource(SyncAPIResource):
    """Sender resource CRUD operations"""

    @cached_property
    def with_raw_response(self) -> SendersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/evermemos/everos-python#accessing-raw-response-data-eg-headers
        """
        return SendersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SendersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/evermemos/everos-python#with_streaming_response
        """
        return SendersResourceWithStreamingResponse(self)

    def retrieve(
        self,
        sender_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SenderAPIResponse:
        """
        Retrieve a sender's details by its sender_id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        return self._get(
            path_template("/api/v1/senders/{sender_id}", sender_id=sender_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SenderAPIResponse,
        )

    def update(
        self,
        sender_id: str,
        *,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SenderAPIResponse:
        """
        Update a sender's display name.

        Args:
          name: New sender display name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        return self._patch(
            path_template("/api/v1/senders/{sender_id}", sender_id=sender_id),
            body=maybe_transform({"name": name}, sender_update_params.SenderUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SenderAPIResponse,
        )

    def create_or_update(
        self,
        *,
        sender_id: str,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SenderAPIResponse:
        """
        Create a new sender or update an existing one (upsert by sender_id).

        Args:
          sender_id: Sender identifier (unique)

          name: Sender display name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/senders",
            body=maybe_transform(
                {
                    "sender_id": sender_id,
                    "name": name,
                },
                sender_create_or_update_params.SenderCreateOrUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SenderAPIResponse,
        )


class AsyncSendersResource(AsyncAPIResource):
    """Sender resource CRUD operations"""

    @cached_property
    def with_raw_response(self) -> AsyncSendersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/evermemos/everos-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSendersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSendersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/evermemos/everos-python#with_streaming_response
        """
        return AsyncSendersResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        sender_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SenderAPIResponse:
        """
        Retrieve a sender's details by its sender_id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        return await self._get(
            path_template("/api/v1/senders/{sender_id}", sender_id=sender_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SenderAPIResponse,
        )

    async def update(
        self,
        sender_id: str,
        *,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SenderAPIResponse:
        """
        Update a sender's display name.

        Args:
          name: New sender display name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sender_id:
            raise ValueError(f"Expected a non-empty value for `sender_id` but received {sender_id!r}")
        return await self._patch(
            path_template("/api/v1/senders/{sender_id}", sender_id=sender_id),
            body=await async_maybe_transform({"name": name}, sender_update_params.SenderUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SenderAPIResponse,
        )

    async def create_or_update(
        self,
        *,
        sender_id: str,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SenderAPIResponse:
        """
        Create a new sender or update an existing one (upsert by sender_id).

        Args:
          sender_id: Sender identifier (unique)

          name: Sender display name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/senders",
            body=await async_maybe_transform(
                {
                    "sender_id": sender_id,
                    "name": name,
                },
                sender_create_or_update_params.SenderCreateOrUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SenderAPIResponse,
        )


class SendersResourceWithRawResponse:
    def __init__(self, senders: SendersResource) -> None:
        self._senders = senders

        self.retrieve = to_raw_response_wrapper(
            senders.retrieve,
        )
        self.update = to_raw_response_wrapper(
            senders.update,
        )
        self.create_or_update = to_raw_response_wrapper(
            senders.create_or_update,
        )


class AsyncSendersResourceWithRawResponse:
    def __init__(self, senders: AsyncSendersResource) -> None:
        self._senders = senders

        self.retrieve = async_to_raw_response_wrapper(
            senders.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            senders.update,
        )
        self.create_or_update = async_to_raw_response_wrapper(
            senders.create_or_update,
        )


class SendersResourceWithStreamingResponse:
    def __init__(self, senders: SendersResource) -> None:
        self._senders = senders

        self.retrieve = to_streamed_response_wrapper(
            senders.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            senders.update,
        )
        self.create_or_update = to_streamed_response_wrapper(
            senders.create_or_update,
        )


class AsyncSendersResourceWithStreamingResponse:
    def __init__(self, senders: AsyncSendersResource) -> None:
        self._senders = senders

        self.retrieve = async_to_streamed_response_wrapper(
            senders.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            senders.update,
        )
        self.create_or_update = async_to_streamed_response_wrapper(
            senders.create_or_update,
        )
