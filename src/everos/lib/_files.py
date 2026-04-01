"""File input abstraction and streaming file resolution.

ResolvedFile holds a local file path (never raw bytes), so uploads are always
streamed rather than loaded into memory.
"""

from __future__ import annotations

import os
import tempfile
import mimetypes
from typing import BinaryIO
from pathlib import Path
from dataclasses import field, dataclass
from urllib.parse import unquote, urlparse

import httpx

from ._errors import FileResolveError

_DEFAULT_MAX_DOWNLOAD_SIZE = 100 * 1024 * 1024  # 100 MB
_DEFAULT_DOWNLOAD_TIMEOUT = 60.0  # seconds
_STREAM_CHUNK_SIZE = 64 * 1024   # 64 KB


@dataclass
class FileInput:
    """Unified file input. Exactly one of path / url must be set.

    Examples::

        FileInput(path="./photo.jpg")
        FileInput(url="https://example.com/image.png")
    """

    path: str | Path | None = None
    url: str | None = None
    content_type: str | None = None
    filename: str | None = None

    def __post_init__(self) -> None:
        sources = sum(x is not None for x in [self.path, self.url])
        if sources == 0:
            raise ValueError("FileInput requires exactly one of: path, url")
        if sources > 1:
            raise ValueError("FileInput accepts only one of: path, url")


@dataclass
class ResolvedFile:
    """Resolved file — holds a local path, never raw bytes.

    Attributes:
        file_path: Absolute path to the local file (original or downloaded temp file).
        content_type: MIME type.
        filename: Original filename.
        size: File size in bytes.
        is_temp: True if this is a downloaded temp file that must be cleaned up.
    """

    file_path: Path
    content_type: str
    filename: str
    size: int
    is_temp: bool = field(default=False)

    def cleanup(self) -> None:
        """Delete temp file if applicable. Safe to call multiple times."""
        if self.is_temp and self.file_path.exists():
            self.file_path.unlink()

    def open(self) -> BinaryIO:
        """Open for streaming read."""
        return open(self.file_path, "rb")  # type: ignore[return-value]


# ── Public resolution functions ───────────────────────────────────────────────


def resolve_file(
    file_input: FileInput,
    *,
    max_download_size: int = _DEFAULT_MAX_DOWNLOAD_SIZE,
    download_timeout: float = _DEFAULT_DOWNLOAD_TIMEOUT,
) -> ResolvedFile:
    """Resolve a FileInput to a ResolvedFile (synchronous)."""
    if file_input.path is not None:
        return _resolve_from_path(file_input)
    else:
        return _resolve_from_url(file_input, max_download_size, download_timeout)


async def async_resolve_file(
    file_input: FileInput,
    *,
    max_download_size: int = _DEFAULT_MAX_DOWNLOAD_SIZE,
    download_timeout: float = _DEFAULT_DOWNLOAD_TIMEOUT,
) -> ResolvedFile:
    """Resolve a FileInput to a ResolvedFile (asynchronous)."""
    if file_input.path is not None:
        import anyio
        return await anyio.to_thread.run_sync(lambda: _resolve_from_path(file_input))  # type: ignore[attr-defined]
    else:
        return await _async_resolve_from_url(file_input, max_download_size, download_timeout)


# ── Internal helpers ──────────────────────────────────────────────────────────


def _resolve_from_path(fi: FileInput) -> ResolvedFile:
    p = Path(os.path.expanduser(str(fi.path))).resolve()
    if not p.exists():
        raise FileResolveError(f"File not found: {p}")
    if not p.is_file():
        raise FileResolveError(f"Not a file: {p}")

    size = p.stat().st_size
    ct = fi.content_type or mimetypes.guess_type(str(p))[0] or "application/octet-stream"
    fn = fi.filename or p.name
    return ResolvedFile(file_path=p, content_type=ct, filename=fn, size=size, is_temp=False)


def _resolve_from_url(fi: FileInput, max_size: int, timeout: float) -> ResolvedFile:
    """Stream-download URL to a temp file; abort if size exceeds max_size."""
    tmp_fd, tmp_path = tempfile.mkstemp(prefix="everos_")
    tmp_file = Path(tmp_path)
    downloaded = 0
    ct_header = "application/octet-stream"

    try:
        with httpx.Client(timeout=timeout, follow_redirects=True) as client:
            with client.stream("GET", fi.url) as resp:  # type: ignore[arg-type]
                resp.raise_for_status()
                ct_header = resp.headers.get("content-type", ct_header).split(";")[0].strip()

                with os.fdopen(tmp_fd, "wb") as f:
                    for chunk in resp.iter_bytes(chunk_size=_STREAM_CHUNK_SIZE):
                        downloaded += len(chunk)
                        if downloaded > max_size:
                            raise FileResolveError(
                                f"Download from {fi.url} exceeded {max_size} bytes limit "
                                f"({downloaded} bytes so far). "
                                "Use the low-level object.sign() API for large files."
                            )
                        f.write(chunk)
                    tmp_fd = -1  # fdopen closed it

    except FileResolveError:
        tmp_file.unlink(missing_ok=True)
        raise
    except Exception as exc:
        tmp_file.unlink(missing_ok=True)
        if tmp_fd >= 0:
            os.close(tmp_fd)
        raise FileResolveError(f"Failed to download {fi.url}: {exc}") from exc

    ct = fi.content_type or ct_header
    fn = fi.filename or _filename_from_url(fi.url)  # type: ignore[arg-type]
    return ResolvedFile(
        file_path=tmp_file, content_type=ct, filename=fn,
        size=downloaded, is_temp=True,
    )


async def _async_resolve_from_url(fi: FileInput, max_size: int, timeout: float) -> ResolvedFile:
    """Async streaming download to temp file."""
    tmp_fd, tmp_path = tempfile.mkstemp(prefix="everos_")
    tmp_file = Path(tmp_path)
    downloaded = 0
    ct_header = "application/octet-stream"

    try:
        async with httpx.AsyncClient(timeout=timeout, follow_redirects=True) as client:
            async with client.stream("GET", fi.url) as resp:  # type: ignore[arg-type]
                resp.raise_for_status()
                ct_header = resp.headers.get("content-type", ct_header).split(";")[0].strip()

                with os.fdopen(tmp_fd, "wb") as f:
                    async for chunk in resp.aiter_bytes(chunk_size=_STREAM_CHUNK_SIZE):
                        downloaded += len(chunk)
                        if downloaded > max_size:
                            raise FileResolveError(
                                f"Download from {fi.url} exceeded {max_size} bytes limit."
                            )
                        f.write(chunk)
                    tmp_fd = -1

    except FileResolveError:
        tmp_file.unlink(missing_ok=True)
        raise
    except Exception as exc:
        tmp_file.unlink(missing_ok=True)
        if tmp_fd >= 0:
            os.close(tmp_fd)
        raise FileResolveError(f"Failed to download {fi.url}: {exc}") from exc

    ct = fi.content_type or ct_header
    fn = fi.filename or _filename_from_url(fi.url)  # type: ignore[arg-type]
    return ResolvedFile(
        file_path=tmp_file, content_type=ct, filename=fn,
        size=downloaded, is_temp=True,
    )


def _filename_from_url(url: str) -> str:
    parsed = urlparse(url)
    name = Path(unquote(parsed.path)).name
    return name if name else "download"
