"""Unit tests for everos.lib._upload — batch_sign and s3_post_upload."""
from __future__ import annotations

from typing import Any
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, call, patch

import httpx
import pytest

from everos.lib._files import ResolvedFile
from everos.lib._detect import UploadTask
from everos.lib._errors import UploadError
from everos.lib._upload import (
    _RETRY_BACKOFF_S,
    _MAX_UPLOAD_RETRIES,
    SignedFile,
    batch_sign,
    s3_post_upload,
    async_batch_sign,
    async_s3_post_upload,
)

# ── Helpers ───────────────────────────────────────────────────────────────────


def _make_resolved(tmp_path: Path, name: str = "photo.jpg", size: int = 10) -> ResolvedFile:
    f = tmp_path / name
    f.write_bytes(b"x" * size)
    return ResolvedFile(file_path=f, content_type="image/jpeg", filename=name, size=size, is_temp=False)


def _make_task(msg_idx: int = 0, content_idx: int = 0, uri: str = "photo.jpg") -> UploadTask:
    return UploadTask(
        msg_idx=msg_idx,
        content_idx=content_idx,
        uri=uri,
        uri_type="local",
        content_type="image",
        file_type="image",
        file_name="photo.jpg",
        file_ext="jpg",
    )


def _make_sign_response(items: list[dict[str, Any]]) -> MagicMock:
    sign_resp = MagicMock()
    sign_resp.status = 0
    sign_resp.error = "OK"

    data = MagicMock()
    object_items: list[MagicMock] = []
    for it in items:
        item = MagicMock()
        item.object_key = it["object_key"]
        item.object_signed_info.url = it["url"]
        item.object_signed_info.fields = it.get("fields", {})
        object_items.append(item)

    data.object_list = object_items
    result = MagicMock()
    result.data = data
    sign_resp.result = result
    return sign_resp


def _make_signed_file(tmp_path: Path, name: str = "photo.jpg") -> SignedFile:
    return SignedFile(
        resolved=_make_resolved(tmp_path, name),
        task=_make_task(),
        object_key=f"uploads/uuid/{name}",
        upload_url="https://s3.example.com/bucket",
        upload_fields={"key": f"uploads/uuid/{name}", "policy": "abc"},
    )


# ── batch_sign ────────────────────────────────────────────────────────────────


def test_batch_sign_success(tmp_path: Path) -> None:
    resolved = [_make_resolved(tmp_path)]
    tasks = [_make_task()]

    sign_resp = _make_sign_response([
        {"object_key": "uploads/uuid/photo.jpg", "url": "https://s3.example.com/", "fields": {"policy": "x"}},
    ])

    mock_client = MagicMock()
    mock_client.v1.object.sign = MagicMock(return_value=sign_resp)

    signed = batch_sign(mock_client, tasks, resolved)

    assert len(signed) == 1
    assert signed[0].object_key == "uploads/uuid/photo.jpg"
    assert signed[0].upload_url == "https://s3.example.com/"
    assert signed[0].upload_fields == {"policy": "x"}


def test_batch_sign_passes_file_id_uuid() -> None:
    """file_id should be a full UUID hex string (no truncation)."""
    resolved = [MagicMock(filename="f.jpg")]
    tasks = [_make_task()]

    captured: list[dict[str, Any]] = []

    def _sign(object_list: list[dict[str, Any]]) -> MagicMock:
        captured.extend(object_list)
        return _make_sign_response([{"object_key": "k", "url": "u"}])

    mock_client = MagicMock()
    mock_client.v1.object.sign = _sign

    batch_sign(mock_client, tasks, resolved)  # type: ignore[arg-type]

    assert len(captured) == 1
    file_id = captured[0]["file_id"]
    assert file_id.startswith("sdk-")
    hex_part = file_id[len("sdk-"):]
    assert len(hex_part) == 32, f"Expected 32-char hex, got {len(hex_part)}: {hex_part}"


def test_batch_sign_api_failure() -> None:
    sign_resp = MagicMock()
    sign_resp.status = 1
    sign_resp.error = "Unauthorized"

    mock_client = MagicMock()
    mock_client.v1.object.sign = MagicMock(return_value=sign_resp)

    with pytest.raises(UploadError, match="Sign failed"):
        batch_sign(mock_client, [_make_task()], [MagicMock(filename="f.jpg")])  # type: ignore[arg-type]


def test_batch_sign_count_mismatch(tmp_path: Path) -> None:
    resolved = [_make_resolved(tmp_path, "a.jpg"), _make_resolved(tmp_path, "b.jpg")]
    tasks = [_make_task(0, 0, "a.jpg"), _make_task(0, 1, "b.jpg")]

    # Returns only 1 item for 2 tasks
    sign_resp = _make_sign_response([{"object_key": "k1", "url": "u1"}])
    mock_client = MagicMock()
    mock_client.v1.object.sign = MagicMock(return_value=sign_resp)

    with pytest.raises(UploadError, match="expected 2"):
        batch_sign(mock_client, tasks, resolved)


# ── s3_post_upload (sync) ─────────────────────────────────────────────────────


def _mock_httpx_response(status_code: int) -> MagicMock:
    resp = MagicMock(spec=httpx.Response)
    resp.status_code = status_code
    resp.text = "error text"
    return resp


def test_s3_post_upload_success_204(tmp_path: Path) -> None:
    signed = _make_signed_file(tmp_path)
    with patch("everos.lib._upload.httpx.post", return_value=_mock_httpx_response(204)) as mock_post:
        result = s3_post_upload(signed)

    assert result.object_key == signed.object_key
    assert result.filename == "photo.jpg"
    assert mock_post.call_count == 1


def test_s3_post_upload_success_200(tmp_path: Path) -> None:
    signed = _make_signed_file(tmp_path)
    with patch("everos.lib._upload.httpx.post", return_value=_mock_httpx_response(200)):
        result = s3_post_upload(signed)
    assert result.object_key == signed.object_key


def test_s3_post_upload_4xx_no_retry(tmp_path: Path) -> None:
    signed = _make_signed_file(tmp_path)
    with patch("everos.lib._upload.httpx.post", return_value=_mock_httpx_response(403)) as mock_post:
        with pytest.raises(UploadError, match="HTTP 403"):
            s3_post_upload(signed)
    assert mock_post.call_count == 1  # no retry on 4xx


def test_s3_post_upload_5xx_retries_and_fails(tmp_path: Path) -> None:
    signed = _make_signed_file(tmp_path)
    with patch("everos.lib._upload.httpx.post", return_value=_mock_httpx_response(503)) as mock_post:
        with patch("everos.lib._upload.time.sleep"):
            with pytest.raises(UploadError, match="after 3 attempts"):
                s3_post_upload(signed)
    assert mock_post.call_count == _MAX_UPLOAD_RETRIES


def test_s3_post_upload_5xx_then_success(tmp_path: Path) -> None:
    signed = _make_signed_file(tmp_path)
    responses = [_mock_httpx_response(503), _mock_httpx_response(204)]
    with patch("everos.lib._upload.httpx.post", side_effect=responses) as mock_post:
        with patch("everos.lib._upload.time.sleep"):
            result = s3_post_upload(signed)
    assert mock_post.call_count == 2
    assert result.object_key == signed.object_key


def test_s3_post_upload_timeout_retries(tmp_path: Path) -> None:
    signed = _make_signed_file(tmp_path)
    with patch(
        "everos.lib._upload.httpx.post",
        side_effect=httpx.TimeoutException("timeout"),
    ) as mock_post:
        with patch("everos.lib._upload.time.sleep"):
            with pytest.raises(UploadError, match="after 3 attempts"):
                s3_post_upload(signed)
    assert mock_post.call_count == _MAX_UPLOAD_RETRIES


def test_s3_post_upload_sync_backoff_called(tmp_path: Path) -> None:
    """Backoff sleep is called between retries (not after last attempt)."""
    signed = _make_signed_file(tmp_path)
    with patch("everos.lib._upload.httpx.post", return_value=_mock_httpx_response(503)):
        with patch("everos.lib._upload.time.sleep") as mock_sleep:
            with pytest.raises(UploadError):
                s3_post_upload(signed)
    # 3 attempts → 2 backoffs
    assert mock_sleep.call_count == _MAX_UPLOAD_RETRIES - 1
    mock_sleep.assert_called_with(_RETRY_BACKOFF_S)


# ── async_batch_sign ──────────────────────────────────────────────────────────


async def test_async_batch_sign_success(tmp_path: Path) -> None:
    resolved = [_make_resolved(tmp_path)]
    tasks = [_make_task()]

    sign_resp = _make_sign_response([
        {"object_key": "uploads/uuid/photo.jpg", "url": "https://s3.example.com/", "fields": {"p": "q"}},
    ])

    mock_client = MagicMock()
    mock_client.v1.object.sign = AsyncMock(return_value=sign_resp)

    signed = await async_batch_sign(mock_client, tasks, resolved)
    assert len(signed) == 1
    assert signed[0].object_key == "uploads/uuid/photo.jpg"


async def test_async_batch_sign_failure() -> None:
    sign_resp = MagicMock()
    sign_resp.status = 1
    sign_resp.error = "Forbidden"
    mock_client = MagicMock()
    mock_client.v1.object.sign = AsyncMock(return_value=sign_resp)

    with pytest.raises(UploadError, match="Sign failed"):
        await async_batch_sign(mock_client, [_make_task()], [MagicMock(filename="x.jpg")])  # type: ignore[arg-type]


# ── async_s3_post_upload ──────────────────────────────────────────────────────


async def test_async_s3_post_upload_success(tmp_path: Path) -> None:
    signed = _make_signed_file(tmp_path)

    mock_resp = MagicMock(spec=httpx.Response)
    mock_resp.status_code = 204

    mock_http = AsyncMock()
    mock_http.post = AsyncMock(return_value=mock_resp)
    mock_http.__aenter__ = AsyncMock(return_value=mock_http)
    mock_http.__aexit__ = AsyncMock(return_value=False)

    with patch("everos.lib._upload.httpx.AsyncClient", return_value=mock_http):
        result = await async_s3_post_upload(signed)

    assert result.object_key == signed.object_key


async def test_async_s3_post_upload_4xx_no_retry(tmp_path: Path) -> None:
    signed = _make_signed_file(tmp_path)

    mock_resp = MagicMock(spec=httpx.Response)
    mock_resp.status_code = 403
    mock_resp.text = "forbidden"

    mock_http = AsyncMock()
    mock_http.post = AsyncMock(return_value=mock_resp)
    mock_http.__aenter__ = AsyncMock(return_value=mock_http)
    mock_http.__aexit__ = AsyncMock(return_value=False)

    with patch("everos.lib._upload.httpx.AsyncClient", return_value=mock_http):
        with pytest.raises(UploadError, match="HTTP 403"):
            await async_s3_post_upload(signed)

    assert mock_http.post.call_count == 1


async def test_async_s3_post_upload_5xx_retries_all_fail(tmp_path: Path) -> None:
    # asyncio is imported locally inside the function, so patch via the asyncio module directly
    signed = _make_signed_file(tmp_path)

    mock_resp = MagicMock(spec=httpx.Response)
    mock_resp.status_code = 503

    mock_http = AsyncMock()
    mock_http.post = AsyncMock(return_value=mock_resp)
    mock_http.__aenter__ = AsyncMock(return_value=mock_http)
    mock_http.__aexit__ = AsyncMock(return_value=False)

    with patch("everos.lib._upload.httpx.AsyncClient", return_value=mock_http):
        with patch("everos.lib._upload.asyncio.sleep", new_callable=AsyncMock):
            with pytest.raises(UploadError, match="after 3 attempts"):
                await async_s3_post_upload(signed)

    assert mock_http.post.call_count == _MAX_UPLOAD_RETRIES


async def test_async_s3_post_upload_backoff_called(tmp_path: Path) -> None:
    signed = _make_signed_file(tmp_path)

    mock_resp = MagicMock(spec=httpx.Response)
    mock_resp.status_code = 503

    mock_http = AsyncMock()
    mock_http.post = AsyncMock(return_value=mock_resp)
    mock_http.__aenter__ = AsyncMock(return_value=mock_http)
    mock_http.__aexit__ = AsyncMock(return_value=False)

    with patch("everos.lib._upload.httpx.AsyncClient", return_value=mock_http):
        with patch("everos.lib._upload.asyncio.sleep", new_callable=AsyncMock) as mock_sleep:
            with pytest.raises(UploadError):
                await async_s3_post_upload(signed)

    # Count only calls with our specific backoff value (session-scoped event loop may
    # call asyncio.sleep internally with other arguments, e.g. 0)
    backoff_calls = [c for c in mock_sleep.call_args_list if c == call(_RETRY_BACKOFF_S)]
    assert len(backoff_calls) == _MAX_UPLOAD_RETRIES - 1
