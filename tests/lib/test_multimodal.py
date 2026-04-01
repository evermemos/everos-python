"""Unit tests for everos.lib._multimodal — orchestration and resource override."""
from __future__ import annotations

from typing import Any
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from everos.lib._files import ResolvedFile
from everos.lib._detect import UploadTask
from everos.lib._errors import UploadError, MultimodalError
from everos.lib._upload import UploadResult
from everos.lib._multimodal import (
    MemoriesResourceWithMultimodal,
    AsyncMemoriesResourceWithMultimodal,
    _cleanup,
    _replace_uris,
)

# ── Helpers ───────────────────────────────────────────────────────────────────


def _make_upload_result(object_key: str = "uploads/uuid/photo.jpg", filename: str = "photo.jpg") -> UploadResult:
    return UploadResult(object_key=object_key, filename=filename, content_type="image/jpeg", size=10)


def _make_task(msg_idx: int = 0, content_idx: int = 1, uri: str = "photo.jpg") -> UploadTask:
    return UploadTask(
        msg_idx=msg_idx, content_idx=content_idx, uri=uri,
        uri_type="local", content_type="image", file_type="image",
        file_name="photo.jpg", file_ext="jpg",
    )


def _make_add_response() -> MagicMock:
    resp = MagicMock()
    resp.status = 0
    return resp


# ── _replace_uris ─────────────────────────────────────────────────────────────


def test_replace_uris_basic() -> None:
    msg_list: list[dict[str, Any]] = [{"role": "user", "content": [
        {"type": "text", "text": "hello"},
        {"type": "image", "uri": "./photo.jpg"},
    ]}]
    tasks = [_make_task(0, 1, "./photo.jpg")]
    results = [_make_upload_result("uploads/uuid/photo.jpg", "photo.jpg")]

    _replace_uris(msg_list, tasks, results)

    item = msg_list[0]["content"][1]
    assert item["uri"] == "uploads/uuid/photo.jpg"


def test_replace_uris_auto_fills_name() -> None:
    msg_list: list[dict[str, Any]] = [{"role": "user", "content": [{"type": "image", "uri": "./photo.jpg"}]}]
    tasks = [_make_task(0, 0)]
    results = [_make_upload_result(filename="photo.jpg")]

    _replace_uris(msg_list, tasks, results)
    assert msg_list[0]["content"][0]["name"] == "photo.jpg"


def test_replace_uris_auto_fills_ext() -> None:
    msg_list: list[dict[str, Any]] = [{"role": "user", "content": [{"type": "image", "uri": "./photo.jpg"}]}]
    tasks = [_make_task(0, 0)]
    results = [_make_upload_result(filename="photo.jpg")]

    _replace_uris(msg_list, tasks, results)
    assert msg_list[0]["content"][0]["ext"] == "jpg"


def test_replace_uris_does_not_overwrite_existing_name() -> None:
    msg_list: list[dict[str, Any]] = [{"role": "user", "content": [{"type": "image", "uri": "./x.jpg", "name": "custom_name.jpg"}]}]
    tasks = [_make_task(0, 0, "./x.jpg")]
    results = [_make_upload_result(filename="x.jpg")]

    _replace_uris(msg_list, tasks, results)
    assert msg_list[0]["content"][0]["name"] == "custom_name.jpg"


def test_replace_uris_multiple_items() -> None:
    msg_list: list[dict[str, Any]] = [{"role": "user", "content": [
        {"type": "image", "uri": "./a.jpg"},
        {"type": "doc", "uri": "./b.pdf"},
    ]}]
    tasks = [_make_task(0, 0, "./a.jpg"), _make_task(0, 1, "./b.pdf")]
    results = [
        _make_upload_result("uploads/uuid/a.jpg", "a.jpg"),
        _make_upload_result("uploads/uuid/b.pdf", "b.pdf"),
    ]

    _replace_uris(msg_list, tasks, results)
    assert msg_list[0]["content"][0]["uri"] == "uploads/uuid/a.jpg"
    assert msg_list[0]["content"][1]["uri"] == "uploads/uuid/b.pdf"


# ── _cleanup ──────────────────────────────────────────────────────────────────


def test_cleanup_removes_temp_files(tmp_path: Path) -> None:
    f = tmp_path / "tmp.bin"
    f.write_bytes(b"x")
    rf = ResolvedFile(file_path=f, content_type="application/octet-stream", filename="tmp.bin", size=1, is_temp=True)
    _cleanup([rf])
    assert not f.exists()


def test_cleanup_skips_non_temp(tmp_path: Path) -> None:
    f = tmp_path / "orig.bin"
    f.write_bytes(b"x")
    rf = ResolvedFile(file_path=f, content_type="application/octet-stream", filename="orig.bin", size=1, is_temp=False)
    _cleanup([rf])
    assert f.exists()


# ── MemoriesResourceWithMultimodal (sync) ─────────────────────────────────────


def _make_sync_resource(_tmp_path: Path) -> tuple[MemoriesResourceWithMultimodal, MagicMock]:
    """Return a resource instance and the mock super().add response."""
    mock_client = MagicMock()
    resource = MemoriesResourceWithMultimodal.__new__(MemoriesResourceWithMultimodal)
    resource._client = mock_client
    return resource, mock_client


def test_sync_add_passthrough_text_only(tmp_path: Path) -> None:
    resource, _ = _make_sync_resource(tmp_path)
    add_response = _make_add_response()

    msgs: list[dict[str, Any]] = [{"role": "user", "content": [{"type": "text", "text": "hello"}]}]

    with patch.object(
        MemoriesResourceWithMultimodal.__bases__[0], "add", return_value=add_response
    ) as mock_super:
        result = resource.add(messages=msgs, user_id="u1")  # type: ignore[arg-type]

    mock_super.assert_called_once()
    assert result is add_response


def test_sync_add_local_file_upload(tmp_path: Path) -> None:
    resource, mock_client = _make_sync_resource(tmp_path)

    f = tmp_path / "photo.jpg"
    f.write_bytes(b"fake-image" * 10)

    msgs: list[dict[str, Any]] = [{"role": "user", "content": [
        {"type": "text", "text": "see this"},
        {"type": "image", "uri": str(f), "name": "photo.jpg", "ext": "jpg"},
    ]}]

    sign_resp = MagicMock()
    sign_resp.status = 0
    sign_resp.error = "OK"
    signed_item = MagicMock()
    signed_item.object_key = "uploads/uuid/photo.jpg"
    signed_item.object_signed_info.url = "https://s3.example.com/"
    signed_item.object_signed_info.fields = {"policy": "x"}
    sign_resp.result.data.object_list = [signed_item]
    mock_client.v1.object.sign = MagicMock(return_value=sign_resp)

    add_response = _make_add_response()
    captured_msgs: list[Any] = []

    def _super_add(**kwargs: Any) -> MagicMock:
        captured_msgs.extend(kwargs["messages"])
        return add_response

    with patch("everos.lib._upload.httpx.post") as mock_s3:
        mock_s3.return_value = MagicMock(status_code=204)
        with patch.object(
            MemoriesResourceWithMultimodal.__bases__[0], "add", side_effect=_super_add
        ):
            result = resource.add(messages=msgs, user_id="u1")  # type: ignore[arg-type]

    assert result is add_response
    # URI should have been replaced in the message passed to super().add()
    assert captured_msgs[0]["content"][1]["uri"] == "uploads/uuid/photo.jpg"
    # Original msgs must NOT be mutated
    assert msgs[0]["content"][1]["uri"] == str(f)


def test_sync_add_deepcopy_original_not_mutated(tmp_path: Path) -> None:
    resource, mock_client = _make_sync_resource(tmp_path)
    f = tmp_path / "img.jpg"
    f.write_bytes(b"data")
    original_uri = str(f)

    msgs: list[dict[str, Any]] = [{"role": "user", "content": [{"type": "image", "uri": original_uri}]}]

    sign_resp = MagicMock()
    sign_resp.status = 0
    sign_resp.error = "OK"
    item = MagicMock()
    item.object_key = "uploads/uuid/img.jpg"
    item.object_signed_info.url = "https://s3.example.com/"
    item.object_signed_info.fields = {}
    sign_resp.result.data.object_list = [item]
    mock_client.v1.object.sign = MagicMock(return_value=sign_resp)

    with patch("everos.lib._upload.httpx.post", return_value=MagicMock(status_code=204)):
        with patch.object(MemoriesResourceWithMultimodal.__bases__[0], "add", return_value=_make_add_response()):
            resource.add(messages=msgs, user_id="u1")  # type: ignore[arg-type]

    assert msgs[0]["content"][0]["uri"] == original_uri


def test_sync_add_cleanup_on_success(tmp_path: Path) -> None:
    resource, mock_client = _make_sync_resource(tmp_path)
    f = tmp_path / "photo.jpg"
    f.write_bytes(b"data")

    msgs: list[dict[str, Any]] = [{"role": "user", "content": [{"type": "image", "uri": str(f)}]}]

    sign_resp = MagicMock()
    sign_resp.status = 0
    sign_resp.error = "OK"
    item = MagicMock()
    item.object_key = "uploads/uuid/photo.jpg"
    item.object_signed_info.url = "https://s3.example.com/"
    item.object_signed_info.fields = {}
    sign_resp.result.data.object_list = [item]
    mock_client.v1.object.sign = MagicMock(return_value=sign_resp)

    with patch("everos.lib._multimodal._cleanup") as mock_cleanup:
        with patch("everos.lib._upload.httpx.post", return_value=MagicMock(status_code=204)):
            with patch.object(MemoriesResourceWithMultimodal.__bases__[0], "add", return_value=_make_add_response()):
                resource.add(messages=msgs, user_id="u1")  # type: ignore[arg-type]

    mock_cleanup.assert_called_once()


def test_sync_add_cleanup_on_upload_failure(tmp_path: Path) -> None:
    resource, mock_client = _make_sync_resource(tmp_path)
    f = tmp_path / "photo.jpg"
    f.write_bytes(b"data")

    msgs: list[dict[str, Any]] = [{"role": "user", "content": [{"type": "image", "uri": str(f)}]}]

    sign_resp = MagicMock()
    sign_resp.status = 0
    sign_resp.error = "OK"
    item = MagicMock()
    item.object_key = "uploads/uuid/photo.jpg"
    item.object_signed_info.url = "https://s3.example.com/"
    item.object_signed_info.fields = {}
    sign_resp.result.data.object_list = [item]
    mock_client.v1.object.sign = MagicMock(return_value=sign_resp)

    with patch("everos.lib._multimodal._cleanup") as mock_cleanup:
        with patch("everos.lib._upload.httpx.post", return_value=MagicMock(status_code=500)):
            with patch("everos.lib._upload.time.sleep"):
                with pytest.raises(MultimodalError):
                    resource.add(messages=msgs, user_id="u1")  # type: ignore[arg-type]

    mock_cleanup.assert_called_once()


# ── AsyncMemoriesResourceWithMultimodal ───────────────────────────────────────


def _make_async_resource(_tmp_path: Path) -> AsyncMemoriesResourceWithMultimodal:
    mock_client = MagicMock()
    resource = AsyncMemoriesResourceWithMultimodal.__new__(AsyncMemoriesResourceWithMultimodal)
    resource._client = mock_client
    return resource


async def test_async_add_passthrough_text_only() -> None:
    resource = AsyncMemoriesResourceWithMultimodal.__new__(AsyncMemoriesResourceWithMultimodal)
    resource._client = MagicMock()
    add_response = _make_add_response()

    msgs: list[dict[str, Any]] = [{"role": "user", "content": [{"type": "text", "text": "hi"}]}]

    with patch.object(
        AsyncMemoriesResourceWithMultimodal.__bases__[0], "add",
        new_callable=AsyncMock, return_value=add_response,
    ) as mock_super:
        result = await resource.add(messages=msgs, user_id="u1")  # type: ignore[arg-type]

    mock_super.assert_called_once()
    assert result is add_response


async def test_async_add_local_file_upload(tmp_path: Path) -> None:
    resource = _make_async_resource(tmp_path)
    f = tmp_path / "audio.mp3"
    f.write_bytes(b"mp3" * 20)

    msgs: list[dict[str, Any]] = [{"role": "user", "content": [{"type": "audio", "uri": str(f)}]}]

    sign_resp = MagicMock()
    sign_resp.status = 0
    sign_resp.error = "OK"
    item = MagicMock()
    item.object_key = "uploads/uuid/audio.mp3"
    item.object_signed_info.url = "https://s3.example.com/"
    item.object_signed_info.fields = {"policy": "y"}
    sign_resp.result.data.object_list = [item]
    resource._client.v1.object.sign = AsyncMock(return_value=sign_resp)

    captured_msgs: list[Any] = []

    async def _super_add(**kwargs: Any) -> MagicMock:
        captured_msgs.extend(kwargs["messages"])
        return _make_add_response()

    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_http = AsyncMock()
    mock_http.post = AsyncMock(return_value=mock_resp)
    mock_http.__aenter__ = AsyncMock(return_value=mock_http)
    mock_http.__aexit__ = AsyncMock(return_value=False)

    with patch("everos.lib._upload.httpx.AsyncClient", return_value=mock_http):
        with patch.object(
            AsyncMemoriesResourceWithMultimodal.__bases__[0], "add",
            side_effect=_super_add,
        ):
            await resource.add(messages=msgs, user_id="u1")  # type: ignore[arg-type]

    assert captured_msgs[0]["content"][0]["uri"] == "uploads/uuid/audio.mp3"
    # Original untouched
    assert msgs[0]["content"][0]["uri"] == str(f)


async def test_async_add_cleanup_called_on_failure(tmp_path: Path) -> None:
    resource = _make_async_resource(tmp_path)
    f = tmp_path / "doc.pdf"
    f.write_bytes(b"pdf")

    msgs: list[dict[str, Any]] = [{"role": "user", "content": [{"type": "pdf", "uri": str(f)}]}]

    sign_resp = MagicMock()
    sign_resp.status = 1  # sign failure
    sign_resp.error = "InternalError"
    resource._client.v1.object.sign = AsyncMock(return_value=sign_resp)

    with patch("everos.lib._multimodal._cleanup") as mock_cleanup:
        with pytest.raises((UploadError, MultimodalError)):
            await resource.add(messages=msgs, user_id="u1")  # type: ignore[arg-type]

    mock_cleanup.assert_called_once()
