"""Unit tests for everos.lib._files — FileInput, ResolvedFile, resolve_file."""
from __future__ import annotations

import os
import tempfile
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from everos.lib._files import (
    FileInput,
    ResolvedFile,
    resolve_file,
    async_resolve_file,
)
from everos.lib._errors import FileResolveError

# ── FileInput validation ──────────────────────────────────────────────────────


def test_file_input_path_only(tmp_path: Path) -> None:
    fi = FileInput(path=str(tmp_path / "file.txt"))
    assert fi.path is not None
    assert fi.url is None


def test_file_input_url_only() -> None:
    fi = FileInput(url="https://example.com/file.jpg")
    assert fi.url is not None
    assert fi.path is None


def test_file_input_both_raises() -> None:
    with pytest.raises(ValueError, match="only one"):
        FileInput(path="./file.jpg", url="https://example.com/file.jpg")


def test_file_input_neither_raises() -> None:
    with pytest.raises(ValueError, match="requires exactly one"):
        FileInput()


# ── ResolvedFile ──────────────────────────────────────────────────────────────


def test_resolved_file_cleanup_temp(tmp_path: Path) -> None:
    f = tmp_path / "temp.bin"
    f.write_bytes(b"data")
    rf = ResolvedFile(file_path=f, content_type="application/octet-stream", filename="temp.bin", size=4, is_temp=True)
    assert f.exists()
    rf.cleanup()
    assert not f.exists()


def test_resolved_file_cleanup_non_temp(tmp_path: Path) -> None:
    f = tmp_path / "orig.bin"
    f.write_bytes(b"data")
    rf = ResolvedFile(file_path=f, content_type="application/octet-stream", filename="orig.bin", size=4, is_temp=False)
    rf.cleanup()
    assert f.exists()  # should NOT be deleted


def test_resolved_file_cleanup_idempotent(tmp_path: Path) -> None:
    f = tmp_path / "temp2.bin"
    f.write_bytes(b"x")
    rf = ResolvedFile(file_path=f, content_type="application/octet-stream", filename="temp2.bin", size=1, is_temp=True)
    rf.cleanup()
    rf.cleanup()  # second call must not raise


def test_resolved_file_open(tmp_path: Path) -> None:
    f = tmp_path / "data.bin"
    f.write_bytes(b"hello world")
    rf = ResolvedFile(file_path=f, content_type="application/octet-stream", filename="data.bin", size=11, is_temp=False)
    with rf.open() as fh:
        assert fh.read() == b"hello world"


# ── resolve_file (local path) ─────────────────────────────────────────────────


def test_resolve_file_local_existing(tmp_path: Path) -> None:
    f = tmp_path / "photo.jpg"
    f.write_bytes(b"\xff\xd8\xff" * 10)
    fi = FileInput(path=str(f))
    rf = resolve_file(fi)
    assert rf.filename == "photo.jpg"
    assert rf.size == 30
    assert rf.is_temp is False
    assert rf.file_path == f


def test_resolve_file_local_missing() -> None:
    fi = FileInput(path="/nonexistent/totally/missing.jpg")
    with pytest.raises(FileResolveError, match="not found"):
        resolve_file(fi)


def test_resolve_file_local_directory(tmp_path: Path) -> None:
    fi = FileInput(path=str(tmp_path))
    with pytest.raises(FileResolveError, match="Not a file"):
        resolve_file(fi)


def test_resolve_file_local_mime_inference(tmp_path: Path) -> None:
    for fname, expected_mime in [("photo.jpg", "image/jpeg"), ("doc.pdf", "application/pdf")]:
        f = tmp_path / fname
        f.write_bytes(b"data")
        rf = resolve_file(FileInput(path=str(f)))
        assert rf.content_type == expected_mime, f"Expected {expected_mime} for {fname}"


def test_resolve_file_local_explicit_content_type(tmp_path: Path) -> None:
    f = tmp_path / "data.bin"
    f.write_bytes(b"data")
    rf = resolve_file(FileInput(path=str(f), content_type="image/webp"))
    assert rf.content_type == "image/webp"


def test_resolve_file_local_explicit_filename(tmp_path: Path) -> None:
    f = tmp_path / "data.bin"
    f.write_bytes(b"data")
    rf = resolve_file(FileInput(path=str(f), filename="custom_name.bin"))
    assert rf.filename == "custom_name.bin"


def test_resolve_file_local_tilde(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    f = tmp_path / "me.txt"
    f.write_bytes(b"hi")
    monkeypatch.setenv("HOME", str(tmp_path))
    rf = resolve_file(FileInput(path="~/me.txt"))
    assert rf.size == 2


# ── resolve_file (URL download) ───────────────────────────────────────────────


def _make_mock_response(content: bytes, content_type: str = "image/jpeg", status: int = 200) -> MagicMock:
    """Build a mock httpx streaming response."""
    mock_resp = MagicMock()
    mock_resp.status_code = status
    mock_resp.headers = {"content-type": content_type}

    def raise_for_status() -> None:
        if status >= 400:
            raise Exception(f"HTTP {status}")

    mock_resp.raise_for_status = raise_for_status
    mock_resp.iter_bytes = lambda chunk_size=None: iter([content])  # noqa: ARG005  # pyright: ignore[reportUnknownLambdaType]
    mock_resp.__enter__ = lambda s: s  # pyright: ignore[reportUnknownLambdaType]
    mock_resp.__exit__ = MagicMock(return_value=False)
    return mock_resp


def test_resolve_file_url_downloads_to_temp() -> None:
    content = b"fake-image-data"
    fi = FileInput(url="https://example.com/photo.jpg")

    mock_client = MagicMock()
    mock_client.__enter__ = lambda s: s  # pyright: ignore[reportUnknownLambdaType]
    mock_client.__exit__ = MagicMock(return_value=False)
    mock_client.stream = MagicMock(return_value=_make_mock_response(content, "image/jpeg"))

    with patch("everos.lib._files.httpx.Client", return_value=mock_client):
        rf = resolve_file(fi)

    assert rf.is_temp is True
    assert rf.size == len(content)
    assert rf.content_type == "image/jpeg"
    assert rf.filename == "photo.jpg"
    rf.cleanup()


def test_resolve_file_url_filename_fallback() -> None:
    """URLs with no path segment fall back to 'download'."""
    content = b"data"
    fi = FileInput(url="https://example.com/")

    mock_client = MagicMock()
    mock_client.__enter__ = lambda s: s  # pyright: ignore[reportUnknownLambdaType]
    mock_client.__exit__ = MagicMock(return_value=False)
    mock_client.stream = MagicMock(return_value=_make_mock_response(content))

    with patch("everos.lib._files.httpx.Client", return_value=mock_client):
        rf = resolve_file(fi)

    assert rf.filename == "download"
    rf.cleanup()


def test_resolve_file_url_size_limit_exceeded() -> None:
    big_chunk = b"x" * 1024  # 1 KB
    fi = FileInput(url="https://example.com/big.bin")

    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.headers = {"content-type": "application/octet-stream"}
    mock_resp.raise_for_status = MagicMock()
    mock_resp.iter_bytes = lambda chunk_size=None: iter([big_chunk, big_chunk])  # noqa: ARG005  # pyright: ignore[reportUnknownLambdaType]  # 2 KB total
    mock_resp.__enter__ = lambda s: s  # pyright: ignore[reportUnknownLambdaType]
    mock_resp.__exit__ = MagicMock(return_value=False)

    mock_client = MagicMock()
    mock_client.__enter__ = lambda s: s  # pyright: ignore[reportUnknownLambdaType]
    mock_client.__exit__ = MagicMock(return_value=False)
    mock_client.stream = MagicMock(return_value=mock_resp)

    with patch("everos.lib._files.httpx.Client", return_value=mock_client):
        with pytest.raises(FileResolveError, match="exceeded"):
            resolve_file(fi, max_download_size=1500)  # limit < 2 KB


def test_resolve_file_url_cleans_up_temp_on_error() -> None:
    fi = FileInput(url="https://example.com/fail.jpg")

    mock_client = MagicMock()
    mock_client.__enter__ = lambda s: s  # pyright: ignore[reportUnknownLambdaType]
    mock_client.__exit__ = MagicMock(return_value=False)
    mock_client.stream = MagicMock(side_effect=Exception("connection refused"))

    created_temps: list[str] = []
    original_mkstemp = tempfile.mkstemp

    def spy_mkstemp(**_kwargs: object) -> tuple[int, str]:
        fd, path = original_mkstemp(prefix="everos_")
        created_temps.append(path)
        return fd, path

    with patch("everos.lib._files.httpx.Client", return_value=mock_client):
        with patch("everos.lib._files.tempfile.mkstemp", side_effect=spy_mkstemp):
            with pytest.raises(FileResolveError):
                resolve_file(fi)

    for p in created_temps:
        assert not os.path.exists(p), f"Temp file {p} was not cleaned up"


# ── async_resolve_file ────────────────────────────────────────────────────────


async def test_async_resolve_file_local(tmp_path: Path) -> None:
    f = tmp_path / "audio.mp3"
    f.write_bytes(b"\x00" * 100)
    rf = await async_resolve_file(FileInput(path=str(f)))
    assert rf.filename == "audio.mp3"
    assert rf.size == 100
    assert rf.is_temp is False


async def test_async_resolve_file_url() -> None:
    content = b"async-image-data"
    fi = FileInput(url="https://example.com/async.jpg")

    # Use MagicMock (not AsyncMock) for the response so headers remains a plain dict
    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.headers = {"content-type": "image/jpeg"}
    mock_resp.raise_for_status = MagicMock()

    async def aiter_bytes(chunk_size: int = 65536) -> None:  # noqa: ARG001  # type: ignore[override]
        yield content  # pyright: ignore[reportReturnType]

    mock_resp.aiter_bytes = aiter_bytes
    mock_resp.__aenter__ = AsyncMock(return_value=mock_resp)
    mock_resp.__aexit__ = AsyncMock(return_value=False)

    mock_client = MagicMock()
    mock_client.__aenter__ = AsyncMock(return_value=mock_client)
    mock_client.__aexit__ = AsyncMock(return_value=False)
    mock_client.stream = MagicMock(return_value=mock_resp)

    with patch("everos.lib._files.httpx.AsyncClient", return_value=mock_client):
        rf = await async_resolve_file(fi)

    assert rf.is_temp is True
    assert rf.size == len(content)
    rf.cleanup()
