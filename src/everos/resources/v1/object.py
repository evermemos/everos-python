# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v1 import object_get_presigned_url_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v1.object_get_presigned_url_response import ObjectGetPresignedURLResponse

__all__ = ["ObjectResource", "AsyncObjectResource"]


class ObjectResource(SyncAPIResource):
    """Multimodal content storage (pre-signed upload)"""

    @cached_property
    def with_raw_response(self) -> ObjectResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/everos-python#accessing-raw-response-data-eg-headers
        """
        return ObjectResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ObjectResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/everos-python#with_streaming_response
        """
        return ObjectResourceWithStreamingResponse(self)

    def get_presigned_url(
        self,
        *,
        object_list: Iterable[object_get_presigned_url_params.ObjectList],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectGetPresignedURLResponse:
        """Generate a pre-signed S3 upload URL for multimodal content.

        Gateway
        transparently forwards to MMS service with auto-injected mms-token header.
        Upload signature valid for 15 minutes, download signature valid for 7 days.

        **Note:** This endpoint is a transparent proxy to MMS. Request body must use
        `{objectList: [...]}` array wrapper. Response and error format follow MMS
        conventions (not the standard ErrorResponse schema used by other endpoints).

        Args:
          object_list: List of files to sign (supports batch signing)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/object/sign",
            body=maybe_transform(
                {"object_list": object_list}, object_get_presigned_url_params.ObjectGetPresignedURLParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectGetPresignedURLResponse,
        )


class AsyncObjectResource(AsyncAPIResource):
    """Multimodal content storage (pre-signed upload)"""

    @cached_property
    def with_raw_response(self) -> AsyncObjectResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/everos-python#accessing-raw-response-data-eg-headers
        """
        return AsyncObjectResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncObjectResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/everos-python#with_streaming_response
        """
        return AsyncObjectResourceWithStreamingResponse(self)

    async def get_presigned_url(
        self,
        *,
        object_list: Iterable[object_get_presigned_url_params.ObjectList],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectGetPresignedURLResponse:
        """Generate a pre-signed S3 upload URL for multimodal content.

        Gateway
        transparently forwards to MMS service with auto-injected mms-token header.
        Upload signature valid for 15 minutes, download signature valid for 7 days.

        **Note:** This endpoint is a transparent proxy to MMS. Request body must use
        `{objectList: [...]}` array wrapper. Response and error format follow MMS
        conventions (not the standard ErrorResponse schema used by other endpoints).

        Args:
          object_list: List of files to sign (supports batch signing)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/object/sign",
            body=await async_maybe_transform(
                {"object_list": object_list}, object_get_presigned_url_params.ObjectGetPresignedURLParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectGetPresignedURLResponse,
        )


class ObjectResourceWithRawResponse:
    def __init__(self, object: ObjectResource) -> None:
        self._object = object

        self.get_presigned_url = to_raw_response_wrapper(
            object.get_presigned_url,
        )


class AsyncObjectResourceWithRawResponse:
    def __init__(self, object: AsyncObjectResource) -> None:
        self._object = object

        self.get_presigned_url = async_to_raw_response_wrapper(
            object.get_presigned_url,
        )


class ObjectResourceWithStreamingResponse:
    def __init__(self, object: ObjectResource) -> None:
        self._object = object

        self.get_presigned_url = to_streamed_response_wrapper(
            object.get_presigned_url,
        )


class AsyncObjectResourceWithStreamingResponse:
    def __init__(self, object: AsyncObjectResource) -> None:
        self._object = object

        self.get_presigned_url = async_to_streamed_response_wrapper(
            object.get_presigned_url,
        )
