# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from everos import Everos, AsyncEveros
from tests.utils import assert_matches_type
from everos.types.v1 import AddResponse, FlushResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAgent:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Everos) -> None:
        agent = client.v1.memories.agent.create(
            messages=[
                {
                    "role": "user",
                    "timestamp": 0,
                }
            ],
            user_id="user_id",
        )
        assert_matches_type(AddResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Everos) -> None:
        agent = client.v1.memories.agent.create(
            messages=[
                {
                    "role": "user",
                    "timestamp": 0,
                    "content": "string",
                    "sender_id": "sender_id",
                    "tool_call_id": "tool_call_id",
                    "tool_calls": [
                        {
                            "id": "id",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                            "type": "type",
                        }
                    ],
                }
            ],
            user_id="user_id",
            async_mode=True,
            session_id="session_id",
        )
        assert_matches_type(AddResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Everos) -> None:
        response = client.v1.memories.agent.with_raw_response.create(
            messages=[
                {
                    "role": "user",
                    "timestamp": 0,
                }
            ],
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AddResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Everos) -> None:
        with client.v1.memories.agent.with_streaming_response.create(
            messages=[
                {
                    "role": "user",
                    "timestamp": 0,
                }
            ],
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AddResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_flush(self, client: Everos) -> None:
        agent = client.v1.memories.agent.flush(
            user_id="user_id",
        )
        assert_matches_type(FlushResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_flush_with_all_params(self, client: Everos) -> None:
        agent = client.v1.memories.agent.flush(
            user_id="user_id",
            session_id="session_id",
        )
        assert_matches_type(FlushResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_flush(self, client: Everos) -> None:
        response = client.v1.memories.agent.with_raw_response.flush(
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(FlushResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_flush(self, client: Everos) -> None:
        with client.v1.memories.agent.with_streaming_response.flush(
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(FlushResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAgent:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncEveros) -> None:
        agent = await async_client.v1.memories.agent.create(
            messages=[
                {
                    "role": "user",
                    "timestamp": 0,
                }
            ],
            user_id="user_id",
        )
        assert_matches_type(AddResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncEveros) -> None:
        agent = await async_client.v1.memories.agent.create(
            messages=[
                {
                    "role": "user",
                    "timestamp": 0,
                    "content": "string",
                    "sender_id": "sender_id",
                    "tool_call_id": "tool_call_id",
                    "tool_calls": [
                        {
                            "id": "id",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                            "type": "type",
                        }
                    ],
                }
            ],
            user_id="user_id",
            async_mode=True,
            session_id="session_id",
        )
        assert_matches_type(AddResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncEveros) -> None:
        response = await async_client.v1.memories.agent.with_raw_response.create(
            messages=[
                {
                    "role": "user",
                    "timestamp": 0,
                }
            ],
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AddResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncEveros) -> None:
        async with async_client.v1.memories.agent.with_streaming_response.create(
            messages=[
                {
                    "role": "user",
                    "timestamp": 0,
                }
            ],
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AddResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_flush(self, async_client: AsyncEveros) -> None:
        agent = await async_client.v1.memories.agent.flush(
            user_id="user_id",
        )
        assert_matches_type(FlushResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_flush_with_all_params(self, async_client: AsyncEveros) -> None:
        agent = await async_client.v1.memories.agent.flush(
            user_id="user_id",
            session_id="session_id",
        )
        assert_matches_type(FlushResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_flush(self, async_client: AsyncEveros) -> None:
        response = await async_client.v1.memories.agent.with_raw_response.flush(
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(FlushResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_flush(self, async_client: AsyncEveros) -> None:
        async with async_client.v1.memories.agent.with_streaming_response.flush(
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(FlushResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True
