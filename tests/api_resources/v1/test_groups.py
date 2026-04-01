# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from everos import Everos, AsyncEveros
from tests.utils import assert_matches_type
from everos.types.v1 import GroupAPIResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGroups:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Everos) -> None:
        group = client.v1.groups.retrieve(
            "group_abc",
        )
        assert_matches_type(GroupAPIResponse, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Everos) -> None:
        response = client.v1.groups.with_raw_response.retrieve(
            "group_abc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = response.parse()
        assert_matches_type(GroupAPIResponse, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Everos) -> None:
        with client.v1.groups.with_streaming_response.retrieve(
            "group_abc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = response.parse()
            assert_matches_type(GroupAPIResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Everos) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            client.v1.groups.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Everos) -> None:
        group = client.v1.groups.update(
            group_id="group_abc",
        )
        assert_matches_type(GroupAPIResponse, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Everos) -> None:
        group = client.v1.groups.update(
            group_id="group_abc",
            description="description",
            name="name",
        )
        assert_matches_type(GroupAPIResponse, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Everos) -> None:
        response = client.v1.groups.with_raw_response.update(
            group_id="group_abc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = response.parse()
        assert_matches_type(GroupAPIResponse, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Everos) -> None:
        with client.v1.groups.with_streaming_response.update(
            group_id="group_abc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = response.parse()
            assert_matches_type(GroupAPIResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Everos) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            client.v1.groups.with_raw_response.update(
                group_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_or_update(self, client: Everos) -> None:
        group = client.v1.groups.create_or_update(
            group_id="group_abc",
        )
        assert_matches_type(GroupAPIResponse, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_or_update_with_all_params(self, client: Everos) -> None:
        group = client.v1.groups.create_or_update(
            group_id="group_abc",
            description="Weekly sync on Project X",
            name="Project Discussion",
        )
        assert_matches_type(GroupAPIResponse, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_or_update(self, client: Everos) -> None:
        response = client.v1.groups.with_raw_response.create_or_update(
            group_id="group_abc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = response.parse()
        assert_matches_type(GroupAPIResponse, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_or_update(self, client: Everos) -> None:
        with client.v1.groups.with_streaming_response.create_or_update(
            group_id="group_abc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = response.parse()
            assert_matches_type(GroupAPIResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncGroups:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncEveros) -> None:
        group = await async_client.v1.groups.retrieve(
            "group_abc",
        )
        assert_matches_type(GroupAPIResponse, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncEveros) -> None:
        response = await async_client.v1.groups.with_raw_response.retrieve(
            "group_abc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = await response.parse()
        assert_matches_type(GroupAPIResponse, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncEveros) -> None:
        async with async_client.v1.groups.with_streaming_response.retrieve(
            "group_abc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = await response.parse()
            assert_matches_type(GroupAPIResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncEveros) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            await async_client.v1.groups.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncEveros) -> None:
        group = await async_client.v1.groups.update(
            group_id="group_abc",
        )
        assert_matches_type(GroupAPIResponse, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncEveros) -> None:
        group = await async_client.v1.groups.update(
            group_id="group_abc",
            description="description",
            name="name",
        )
        assert_matches_type(GroupAPIResponse, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncEveros) -> None:
        response = await async_client.v1.groups.with_raw_response.update(
            group_id="group_abc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = await response.parse()
        assert_matches_type(GroupAPIResponse, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncEveros) -> None:
        async with async_client.v1.groups.with_streaming_response.update(
            group_id="group_abc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = await response.parse()
            assert_matches_type(GroupAPIResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncEveros) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            await async_client.v1.groups.with_raw_response.update(
                group_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_or_update(self, async_client: AsyncEveros) -> None:
        group = await async_client.v1.groups.create_or_update(
            group_id="group_abc",
        )
        assert_matches_type(GroupAPIResponse, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_or_update_with_all_params(self, async_client: AsyncEveros) -> None:
        group = await async_client.v1.groups.create_or_update(
            group_id="group_abc",
            description="Weekly sync on Project X",
            name="Project Discussion",
        )
        assert_matches_type(GroupAPIResponse, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_or_update(self, async_client: AsyncEveros) -> None:
        response = await async_client.v1.groups.with_raw_response.create_or_update(
            group_id="group_abc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = await response.parse()
        assert_matches_type(GroupAPIResponse, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_or_update(self, async_client: AsyncEveros) -> None:
        async with async_client.v1.groups.with_streaming_response.create_or_update(
            group_id="group_abc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = await response.parse()
            assert_matches_type(GroupAPIResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True
