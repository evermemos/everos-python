# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from everos import Everos, AsyncEveros
from tests.utils import assert_matches_type
from everos.types.v1 import ObjectGetPresignedURLResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestObject:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_presigned_url(self, client: Everos) -> None:
        object_ = client.v1.object.get_presigned_url(
            object_list=[
                {
                    "file_id": "file_abc123",
                    "file_name": "photo.png",
                    "file_type": "image",
                }
            ],
        )
        assert_matches_type(ObjectGetPresignedURLResponse, object_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_presigned_url(self, client: Everos) -> None:
        response = client.v1.object.with_raw_response.get_presigned_url(
            object_list=[
                {
                    "file_id": "file_abc123",
                    "file_name": "photo.png",
                    "file_type": "image",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = response.parse()
        assert_matches_type(ObjectGetPresignedURLResponse, object_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_presigned_url(self, client: Everos) -> None:
        with client.v1.object.with_streaming_response.get_presigned_url(
            object_list=[
                {
                    "file_id": "file_abc123",
                    "file_name": "photo.png",
                    "file_type": "image",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = response.parse()
            assert_matches_type(ObjectGetPresignedURLResponse, object_, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncObject:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_presigned_url(self, async_client: AsyncEveros) -> None:
        object_ = await async_client.v1.object.get_presigned_url(
            object_list=[
                {
                    "file_id": "file_abc123",
                    "file_name": "photo.png",
                    "file_type": "image",
                }
            ],
        )
        assert_matches_type(ObjectGetPresignedURLResponse, object_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_presigned_url(self, async_client: AsyncEveros) -> None:
        response = await async_client.v1.object.with_raw_response.get_presigned_url(
            object_list=[
                {
                    "file_id": "file_abc123",
                    "file_name": "photo.png",
                    "file_type": "image",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = await response.parse()
        assert_matches_type(ObjectGetPresignedURLResponse, object_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_presigned_url(self, async_client: AsyncEveros) -> None:
        async with async_client.v1.object.with_streaming_response.get_presigned_url(
            object_list=[
                {
                    "file_id": "file_abc123",
                    "file_name": "photo.png",
                    "file_type": "image",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = await response.parse()
            assert_matches_type(ObjectGetPresignedURLResponse, object_, path=["response"])

        assert cast(Any, response.is_closed) is True
