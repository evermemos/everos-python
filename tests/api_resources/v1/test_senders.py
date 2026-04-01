# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from everos import EverOS, AsyncEverOS
from tests.utils import assert_matches_type
from everos.types.v1 import SenderAPIResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSenders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: EverOS) -> None:
        sender = client.v1.senders.create(
            sender_id="user_123",
        )
        assert_matches_type(SenderAPIResponse, sender, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: EverOS) -> None:
        sender = client.v1.senders.create(
            sender_id="user_123",
            name="Alice",
        )
        assert_matches_type(SenderAPIResponse, sender, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: EverOS) -> None:
        response = client.v1.senders.with_raw_response.create(
            sender_id="user_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sender = response.parse()
        assert_matches_type(SenderAPIResponse, sender, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: EverOS) -> None:
        with client.v1.senders.with_streaming_response.create(
            sender_id="user_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sender = response.parse()
            assert_matches_type(SenderAPIResponse, sender, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: EverOS) -> None:
        sender = client.v1.senders.retrieve(
            "user_123",
        )
        assert_matches_type(SenderAPIResponse, sender, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: EverOS) -> None:
        response = client.v1.senders.with_raw_response.retrieve(
            "user_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sender = response.parse()
        assert_matches_type(SenderAPIResponse, sender, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: EverOS) -> None:
        with client.v1.senders.with_streaming_response.retrieve(
            "user_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sender = response.parse()
            assert_matches_type(SenderAPIResponse, sender, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: EverOS) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            client.v1.senders.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_patch(self, client: EverOS) -> None:
        sender = client.v1.senders.patch(
            sender_id="user_123",
        )
        assert_matches_type(SenderAPIResponse, sender, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_patch_with_all_params(self, client: EverOS) -> None:
        sender = client.v1.senders.patch(
            sender_id="user_123",
            name="name",
        )
        assert_matches_type(SenderAPIResponse, sender, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_patch(self, client: EverOS) -> None:
        response = client.v1.senders.with_raw_response.patch(
            sender_id="user_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sender = response.parse()
        assert_matches_type(SenderAPIResponse, sender, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_patch(self, client: EverOS) -> None:
        with client.v1.senders.with_streaming_response.patch(
            sender_id="user_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sender = response.parse()
            assert_matches_type(SenderAPIResponse, sender, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_patch(self, client: EverOS) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            client.v1.senders.with_raw_response.patch(
                sender_id="",
            )


class TestAsyncSenders:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncEverOS) -> None:
        sender = await async_client.v1.senders.create(
            sender_id="user_123",
        )
        assert_matches_type(SenderAPIResponse, sender, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncEverOS) -> None:
        sender = await async_client.v1.senders.create(
            sender_id="user_123",
            name="Alice",
        )
        assert_matches_type(SenderAPIResponse, sender, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncEverOS) -> None:
        response = await async_client.v1.senders.with_raw_response.create(
            sender_id="user_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sender = await response.parse()
        assert_matches_type(SenderAPIResponse, sender, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncEverOS) -> None:
        async with async_client.v1.senders.with_streaming_response.create(
            sender_id="user_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sender = await response.parse()
            assert_matches_type(SenderAPIResponse, sender, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncEverOS) -> None:
        sender = await async_client.v1.senders.retrieve(
            "user_123",
        )
        assert_matches_type(SenderAPIResponse, sender, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncEverOS) -> None:
        response = await async_client.v1.senders.with_raw_response.retrieve(
            "user_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sender = await response.parse()
        assert_matches_type(SenderAPIResponse, sender, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncEverOS) -> None:
        async with async_client.v1.senders.with_streaming_response.retrieve(
            "user_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sender = await response.parse()
            assert_matches_type(SenderAPIResponse, sender, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncEverOS) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            await async_client.v1.senders.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_patch(self, async_client: AsyncEverOS) -> None:
        sender = await async_client.v1.senders.patch(
            sender_id="user_123",
        )
        assert_matches_type(SenderAPIResponse, sender, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_patch_with_all_params(self, async_client: AsyncEverOS) -> None:
        sender = await async_client.v1.senders.patch(
            sender_id="user_123",
            name="name",
        )
        assert_matches_type(SenderAPIResponse, sender, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_patch(self, async_client: AsyncEverOS) -> None:
        response = await async_client.v1.senders.with_raw_response.patch(
            sender_id="user_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sender = await response.parse()
        assert_matches_type(SenderAPIResponse, sender, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_patch(self, async_client: AsyncEverOS) -> None:
        async with async_client.v1.senders.with_streaming_response.patch(
            sender_id="user_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sender = await response.parse()
            assert_matches_type(SenderAPIResponse, sender, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_patch(self, async_client: AsyncEverOS) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sender_id` but received ''"):
            await async_client.v1.senders.with_raw_response.patch(
                sender_id="",
            )
