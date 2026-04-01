# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from everos import EverOS, AsyncEverOS
from tests.utils import assert_matches_type
from everos.types.v1 import GetTaskStatusResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTasks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: EverOS) -> None:
        task = client.v1.tasks.retrieve(
            "task_id",
        )
        assert_matches_type(GetTaskStatusResponse, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: EverOS) -> None:
        response = client.v1.tasks.with_raw_response.retrieve(
            "task_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(GetTaskStatusResponse, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: EverOS) -> None:
        with client.v1.tasks.with_streaming_response.retrieve(
            "task_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(GetTaskStatusResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: EverOS) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.v1.tasks.with_raw_response.retrieve(
                "",
            )


class TestAsyncTasks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncEverOS) -> None:
        task = await async_client.v1.tasks.retrieve(
            "task_id",
        )
        assert_matches_type(GetTaskStatusResponse, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncEverOS) -> None:
        response = await async_client.v1.tasks.with_raw_response.retrieve(
            "task_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(GetTaskStatusResponse, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncEverOS) -> None:
        async with async_client.v1.tasks.with_streaming_response.retrieve(
            "task_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(GetTaskStatusResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncEverOS) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.v1.tasks.with_raw_response.retrieve(
                "",
            )
