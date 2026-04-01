"""Unit tests for everos.lib._detect — URI detection and message scanning."""
from __future__ import annotations

from typing import Any
from pathlib import Path

import pytest

from everos.lib._detect import (
    _is_http_uri,
    scan_messages,
    _is_local_file,
)

# ── _is_http_uri ─────────────────────────────────────────────────────────────


def test_is_http_uri_http() -> None:
    assert _is_http_uri("http://example.com/file.jpg") is True


def test_is_http_uri_https() -> None:
    assert _is_http_uri("https://example.com/image.png") is True


def test_is_http_uri_local_path() -> None:
    assert _is_http_uri("./photo.jpg") is False


def test_is_http_uri_object_key() -> None:
    assert _is_http_uri("uploads/2026/abc/photo.jpg") is False


def test_is_http_uri_ftp() -> None:
    assert _is_http_uri("ftp://example.com/file") is False


# ── _is_local_file ────────────────────────────────────────────────────────────


def test_is_local_file_existing(tmp_path: Path) -> None:
    f = tmp_path / "photo.jpg"
    f.write_bytes(b"data")
    assert _is_local_file(str(f)) is True


def test_is_local_file_nonexistent() -> None:
    assert _is_local_file("/nonexistent/path/file.jpg") is False


def test_is_local_file_directory(tmp_path: Path) -> None:
    assert _is_local_file(str(tmp_path)) is False


def test_is_local_file_protocol_prefix() -> None:
    # Anything with "://" in it should not be treated as a local file
    assert _is_local_file("s3://bucket/key") is False
    assert _is_local_file("minio://bucket/key.jpg") is False


def test_is_local_file_tilde_expansion(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    f = tmp_path / "notes.txt"
    f.write_bytes(b"hello")
    monkeypatch.setenv("HOME", str(tmp_path))
    assert _is_local_file("~/notes.txt") is True


def test_is_local_file_object_key_not_local() -> None:
    # A MinIO object_key like "uploads/uuid/file.jpg" won't exist on disk
    assert _is_local_file("uploads/abc123-uuid/photo.png") is False


# ── scan_messages ─────────────────────────────────────────────────────────────


def test_scan_messages_empty() -> None:
    assert scan_messages([]) == []


def test_scan_messages_text_only() -> None:
    msgs = [{"role": "user", "content": [{"type": "text", "text": "hello"}]}]
    assert scan_messages(msgs) == []


def test_scan_messages_str_content_skipped() -> None:
    # str shorthand for content → pure text, skip
    msgs = [{"role": "user", "content": "plain text message"}]
    assert scan_messages(msgs) == []


def test_scan_messages_none_content_skipped() -> None:
    msgs = [{"role": "user"}]
    assert scan_messages(msgs) == []


def test_scan_messages_empty_uri_skipped() -> None:
    msgs = [{"role": "user", "content": [{"type": "image", "uri": ""}]}]
    assert scan_messages(msgs) == []


def test_scan_messages_none_uri_skipped() -> None:
    msgs = [{"role": "user", "content": [{"type": "image"}]}]
    assert scan_messages(msgs) == []


def test_scan_messages_object_key_passthrough() -> None:
    # Already an object_key — not a local file, not http → passthrough
    msgs = [{"role": "user", "content": [{"type": "image", "uri": "uploads/uuid/photo.jpg"}]}]
    assert scan_messages(msgs) == []


def test_scan_messages_http_url(tmp_path: Path) -> None:  # noqa: ARG001
    msgs = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "see image"},
                {"type": "image", "uri": "https://example.com/photo.jpg", "name": "photo.jpg"},
            ],
        }
    ]
    tasks = scan_messages(msgs)
    assert len(tasks) == 1
    t = tasks[0]
    assert t.msg_idx == 0
    assert t.content_idx == 1
    assert t.uri == "https://example.com/photo.jpg"
    assert t.uri_type == "http"
    assert t.content_type == "image"
    assert t.file_type == "image"
    assert t.file_name == "photo.jpg"


def test_scan_messages_local_file(tmp_path: Path) -> None:
    f = tmp_path / "doc.pdf"
    f.write_bytes(b"pdf")
    msgs = [{"role": "user", "content": [{"type": "pdf", "uri": str(f), "ext": "pdf"}]}]
    tasks = scan_messages(msgs)
    assert len(tasks) == 1
    t = tasks[0]
    assert t.uri_type == "local"
    assert t.content_type == "pdf"
    assert t.file_type == "file"
    assert t.file_ext == "pdf"


def test_scan_messages_multiple_messages_and_items(tmp_path: Path) -> None:
    f = tmp_path / "audio.mp3"
    f.write_bytes(b"mp3")

    msgs = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "hello"},
                {"type": "audio", "uri": str(f)},
            ],
        },
        {
            "role": "assistant",
            "content": [
                {"type": "image", "uri": "https://example.com/img.png"},
                {"type": "doc", "uri": "uploads/existing-key/file.docx"},  # passthrough
            ],
        },
    ]
    tasks = scan_messages(msgs)
    assert len(tasks) == 2

    audio_task = tasks[0]
    assert audio_task.msg_idx == 0
    assert audio_task.content_idx == 1
    assert audio_task.uri_type == "local"
    assert audio_task.file_type == "file"

    img_task = tasks[1]
    assert img_task.msg_idx == 1
    assert img_task.content_idx == 0
    assert img_task.uri_type == "http"
    assert img_task.file_type == "image"


def test_scan_messages_content_type_mapping() -> None:
    """All non-image content types map to file_type='file'."""
    for ct in ("audio", "doc", "pdf", "html", "email"):
        msgs = [{"role": "user", "content": [{"type": ct, "uri": "https://example.com/x"}]}]
        tasks = scan_messages(msgs)
        assert len(tasks) == 1
        assert tasks[0].file_type == "file", f"Expected file_type='file' for type={ct}"


def test_scan_messages_does_not_mutate() -> None:
    """scan_messages must not mutate the input messages."""
    msgs: list[dict[str, Any]] = [{"role": "user", "content": [{"type": "image", "uri": "https://example.com/x.jpg"}]}]
    original_uri = msgs[0]["content"][0]["uri"]
    scan_messages(msgs)
    assert msgs[0]["content"][0]["uri"] == original_uri
