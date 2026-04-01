# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from everos import EverOS, AsyncEverOS
from tests.utils import assert_matches_type
from everos.types.v1 import (
    AddResponse,
    FlushResponse,
    GetMemoriesResponse,
    SearchMemoriesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMemories:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: EverOS) -> None:
        memory = client.v1.memories.delete()
        assert memory is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: EverOS) -> None:
        memory = client.v1.memories.delete(
            group_id="group_id",
            memory_id="memory_id",
            sender_id="sender_id",
            session_id="session_id",
            user_id="user_id",
        )
        assert memory is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: EverOS) -> None:
        response = client.v1.memories.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert memory is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: EverOS) -> None:
        with client.v1.memories.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert memory is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add(self, client: EverOS) -> None:
        memory = client.v1.memories.add(
            messages=[
                {
                    "content": "x",
                    "role": "user",
                    "timestamp": 0,
                }
            ],
            user_id="user_id",
        )
        assert_matches_type(AddResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add_with_all_params(self, client: EverOS) -> None:
        memory = client.v1.memories.add(
            messages=[
                {
                    "content": "x",
                    "role": "user",
                    "timestamp": 0,
                    "sender_id": "sender_id",
                }
            ],
            user_id="user_id",
            async_mode=True,
            session_id="session_id",
        )
        assert_matches_type(AddResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_add(self, client: EverOS) -> None:
        response = client.v1.memories.with_raw_response.add(
            messages=[
                {
                    "content": "x",
                    "role": "user",
                    "timestamp": 0,
                }
            ],
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(AddResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_add(self, client: EverOS) -> None:
        with client.v1.memories.with_streaming_response.add(
            messages=[
                {
                    "content": "x",
                    "role": "user",
                    "timestamp": 0,
                }
            ],
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(AddResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_flush(self, client: EverOS) -> None:
        memory = client.v1.memories.flush(
            user_id="user_id",
        )
        assert_matches_type(FlushResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_flush_with_all_params(self, client: EverOS) -> None:
        memory = client.v1.memories.flush(
            user_id="user_id",
            session_id="session_id",
        )
        assert_matches_type(FlushResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_flush(self, client: EverOS) -> None:
        response = client.v1.memories.with_raw_response.flush(
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(FlushResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_flush(self, client: EverOS) -> None:
        with client.v1.memories.with_streaming_response.flush(
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(FlushResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: EverOS) -> None:
        memory = client.v1.memories.get(
            filters={"foo": "bar"},
            memory_type="episodic_memory",
        )
        assert_matches_type(GetMemoriesResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: EverOS) -> None:
        memory = client.v1.memories.get(
            filters={"foo": "bar"},
            memory_type="episodic_memory",
            page=1,
            page_size=1,
            rank_by="rank_by",
            rank_order="asc",
        )
        assert_matches_type(GetMemoriesResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: EverOS) -> None:
        response = client.v1.memories.with_raw_response.get(
            filters={"foo": "bar"},
            memory_type="episodic_memory",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(GetMemoriesResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: EverOS) -> None:
        with client.v1.memories.with_streaming_response.get(
            filters={"foo": "bar"},
            memory_type="episodic_memory",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(GetMemoriesResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search(self, client: EverOS) -> None:
        memory = client.v1.memories.search(
            filters={"foo": "bar"},
            query="What did Alice say about the project?",
        )
        assert_matches_type(SearchMemoriesResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: EverOS) -> None:
        memory = client.v1.memories.search(
            filters={"foo": "bar"},
            query="What did Alice say about the project?",
            include_original_data=True,
            memory_types=["episodic_memory"],
            method="keyword",
            radius=0,
            top_k=-1,
        )
        assert_matches_type(SearchMemoriesResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: EverOS) -> None:
        response = client.v1.memories.with_raw_response.search(
            filters={"foo": "bar"},
            query="What did Alice say about the project?",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(SearchMemoriesResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: EverOS) -> None:
        with client.v1.memories.with_streaming_response.search(
            filters={"foo": "bar"},
            query="What did Alice say about the project?",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(SearchMemoriesResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMemories:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncEverOS) -> None:
        memory = await async_client.v1.memories.delete()
        assert memory is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncEverOS) -> None:
        memory = await async_client.v1.memories.delete(
            group_id="group_id",
            memory_id="memory_id",
            sender_id="sender_id",
            session_id="session_id",
            user_id="user_id",
        )
        assert memory is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncEverOS) -> None:
        response = await async_client.v1.memories.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert memory is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncEverOS) -> None:
        async with async_client.v1.memories.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert memory is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add(self, async_client: AsyncEverOS) -> None:
        memory = await async_client.v1.memories.add(
            messages=[
                {
                    "content": "x",
                    "role": "user",
                    "timestamp": 0,
                }
            ],
            user_id="user_id",
        )
        assert_matches_type(AddResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add_with_all_params(self, async_client: AsyncEverOS) -> None:
        memory = await async_client.v1.memories.add(
            messages=[
                {
                    "content": "x",
                    "role": "user",
                    "timestamp": 0,
                    "sender_id": "sender_id",
                }
            ],
            user_id="user_id",
            async_mode=True,
            session_id="session_id",
        )
        assert_matches_type(AddResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncEverOS) -> None:
        response = await async_client.v1.memories.with_raw_response.add(
            messages=[
                {
                    "content": "x",
                    "role": "user",
                    "timestamp": 0,
                }
            ],
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(AddResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncEverOS) -> None:
        async with async_client.v1.memories.with_streaming_response.add(
            messages=[
                {
                    "content": "x",
                    "role": "user",
                    "timestamp": 0,
                }
            ],
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(AddResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_flush(self, async_client: AsyncEverOS) -> None:
        memory = await async_client.v1.memories.flush(
            user_id="user_id",
        )
        assert_matches_type(FlushResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_flush_with_all_params(self, async_client: AsyncEverOS) -> None:
        memory = await async_client.v1.memories.flush(
            user_id="user_id",
            session_id="session_id",
        )
        assert_matches_type(FlushResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_flush(self, async_client: AsyncEverOS) -> None:
        response = await async_client.v1.memories.with_raw_response.flush(
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(FlushResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_flush(self, async_client: AsyncEverOS) -> None:
        async with async_client.v1.memories.with_streaming_response.flush(
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(FlushResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncEverOS) -> None:
        memory = await async_client.v1.memories.get(
            filters={"foo": "bar"},
            memory_type="episodic_memory",
        )
        assert_matches_type(GetMemoriesResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncEverOS) -> None:
        memory = await async_client.v1.memories.get(
            filters={"foo": "bar"},
            memory_type="episodic_memory",
            page=1,
            page_size=1,
            rank_by="rank_by",
            rank_order="asc",
        )
        assert_matches_type(GetMemoriesResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncEverOS) -> None:
        response = await async_client.v1.memories.with_raw_response.get(
            filters={"foo": "bar"},
            memory_type="episodic_memory",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(GetMemoriesResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncEverOS) -> None:
        async with async_client.v1.memories.with_streaming_response.get(
            filters={"foo": "bar"},
            memory_type="episodic_memory",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(GetMemoriesResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncEverOS) -> None:
        memory = await async_client.v1.memories.search(
            filters={"foo": "bar"},
            query="What did Alice say about the project?",
        )
        assert_matches_type(SearchMemoriesResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncEverOS) -> None:
        memory = await async_client.v1.memories.search(
            filters={"foo": "bar"},
            query="What did Alice say about the project?",
            include_original_data=True,
            memory_types=["episodic_memory"],
            method="keyword",
            radius=0,
            top_k=-1,
        )
        assert_matches_type(SearchMemoriesResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncEverOS) -> None:
        response = await async_client.v1.memories.with_raw_response.search(
            filters={"foo": "bar"},
            query="What did Alice say about the project?",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(SearchMemoriesResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncEverOS) -> None:
        async with async_client.v1.memories.with_streaming_response.search(
            filters={"foo": "bar"},
            query="What did Alice say about the project?",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(SearchMemoriesResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True
