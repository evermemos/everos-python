# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from everos import Everos, AsyncEveros
from tests.utils import assert_matches_type
from everos.types.v1 import AddResponse, FlushResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGroup:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Everos) -> None:
        group = client.v1.memories.group.create(
            group_id="group_id",
            messages=[
                {
                    "content": "x",
                    "role": "user",
                    "sender_id": "sender_id",
                    "timestamp": 0,
                }
            ],
        )
        assert_matches_type(AddResponse, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Everos) -> None:
        group = client.v1.memories.group.create(
            group_id="group_id",
            messages=[
                {
                    "content": "x",
                    "role": "user",
                    "sender_id": "sender_id",
                    "timestamp": 0,
                    "message_id": "message_id",
                    "sender_name": "sender_name",
                }
            ],
            async_mode=True,
            group_meta={"foo": "bar"},
        )
        assert_matches_type(AddResponse, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Everos) -> None:
        response = client.v1.memories.group.with_raw_response.create(
            group_id="group_id",
            messages=[
                {
                    "content": "x",
                    "role": "user",
                    "sender_id": "sender_id",
                    "timestamp": 0,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = response.parse()
        assert_matches_type(AddResponse, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Everos) -> None:
        with client.v1.memories.group.with_streaming_response.create(
            group_id="group_id",
            messages=[
                {
                    "content": "x",
                    "role": "user",
                    "sender_id": "sender_id",
                    "timestamp": 0,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = response.parse()
            assert_matches_type(AddResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_flush(self, client: Everos) -> None:
        group = client.v1.memories.group.flush(
            group_id="group_id",
        )
        assert_matches_type(FlushResponse, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_flush(self, client: Everos) -> None:
        response = client.v1.memories.group.with_raw_response.flush(
            group_id="group_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = response.parse()
        assert_matches_type(FlushResponse, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_flush(self, client: Everos) -> None:
        with client.v1.memories.group.with_streaming_response.flush(
            group_id="group_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = response.parse()
            assert_matches_type(FlushResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncGroup:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncEveros) -> None:
        group = await async_client.v1.memories.group.create(
            group_id="group_id",
            messages=[
                {
                    "content": "x",
                    "role": "user",
                    "sender_id": "sender_id",
                    "timestamp": 0,
                }
            ],
        )
        assert_matches_type(AddResponse, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncEveros) -> None:
        group = await async_client.v1.memories.group.create(
            group_id="group_id",
            messages=[
                {
                    "content": "x",
                    "role": "user",
                    "sender_id": "sender_id",
                    "timestamp": 0,
                    "message_id": "message_id",
                    "sender_name": "sender_name",
                }
            ],
            async_mode=True,
            group_meta={"foo": "bar"},
        )
        assert_matches_type(AddResponse, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncEveros) -> None:
        response = await async_client.v1.memories.group.with_raw_response.create(
            group_id="group_id",
            messages=[
                {
                    "content": "x",
                    "role": "user",
                    "sender_id": "sender_id",
                    "timestamp": 0,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = await response.parse()
        assert_matches_type(AddResponse, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncEveros) -> None:
        async with async_client.v1.memories.group.with_streaming_response.create(
            group_id="group_id",
            messages=[
                {
                    "content": "x",
                    "role": "user",
                    "sender_id": "sender_id",
                    "timestamp": 0,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = await response.parse()
            assert_matches_type(AddResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_flush(self, async_client: AsyncEveros) -> None:
        group = await async_client.v1.memories.group.flush(
            group_id="group_id",
        )
        assert_matches_type(FlushResponse, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_flush(self, async_client: AsyncEveros) -> None:
        response = await async_client.v1.memories.group.with_raw_response.flush(
            group_id="group_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = await response.parse()
        assert_matches_type(FlushResponse, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_flush(self, async_client: AsyncEveros) -> None:
        async with async_client.v1.memories.group.with_streaming_response.flush(
            group_id="group_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = await response.parse()
            assert_matches_type(FlushResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True
