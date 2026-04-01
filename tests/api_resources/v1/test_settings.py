# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from everos import EverOS, AsyncEverOS
from tests.utils import assert_matches_type
from everos.types.v1 import SettingsAPIResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSettings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: EverOS) -> None:
        setting = client.v1.settings.retrieve()
        assert_matches_type(SettingsAPIResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: EverOS) -> None:
        response = client.v1.settings.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(SettingsAPIResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: EverOS) -> None:
        with client.v1.settings.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(SettingsAPIResponse, setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: EverOS) -> None:
        setting = client.v1.settings.update()
        assert_matches_type(SettingsAPIResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: EverOS) -> None:
        setting = client.v1.settings.update(
            boundary_detection_timeout=3600,
            extraction_mode="default",
            llm_custom_setting={
                "boundary": {
                    "model": "gpt-4.1-mini",
                    "provider": "openai",
                    "extra": {"foo": "bar"},
                },
                "extra": {"foo": "bar"},
                "extraction": {
                    "model": "gpt-4.1-mini",
                    "provider": "openai",
                    "extra": {"foo": "bar"},
                },
            },
            offline_profile_extraction_interval=86400,
            timezone="UTC",
        )
        assert_matches_type(SettingsAPIResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: EverOS) -> None:
        response = client.v1.settings.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(SettingsAPIResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: EverOS) -> None:
        with client.v1.settings.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(SettingsAPIResponse, setting, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSettings:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncEverOS) -> None:
        setting = await async_client.v1.settings.retrieve()
        assert_matches_type(SettingsAPIResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncEverOS) -> None:
        response = await async_client.v1.settings.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(SettingsAPIResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncEverOS) -> None:
        async with async_client.v1.settings.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(SettingsAPIResponse, setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncEverOS) -> None:
        setting = await async_client.v1.settings.update()
        assert_matches_type(SettingsAPIResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncEverOS) -> None:
        setting = await async_client.v1.settings.update(
            boundary_detection_timeout=3600,
            extraction_mode="default",
            llm_custom_setting={
                "boundary": {
                    "model": "gpt-4.1-mini",
                    "provider": "openai",
                    "extra": {"foo": "bar"},
                },
                "extra": {"foo": "bar"},
                "extraction": {
                    "model": "gpt-4.1-mini",
                    "provider": "openai",
                    "extra": {"foo": "bar"},
                },
            },
            offline_profile_extraction_interval=86400,
            timezone="UTC",
        )
        assert_matches_type(SettingsAPIResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncEverOS) -> None:
        response = await async_client.v1.settings.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(SettingsAPIResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncEverOS) -> None:
        async with async_client.v1.settings.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(SettingsAPIResponse, setting, path=["response"])

        assert cast(Any, response.is_closed) is True
