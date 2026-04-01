"""Scan messages for content items that reference uploadable files.

Detection rules (applied to each content item where type != 'text'):
  - uri starts with http:// or https://  → HTTP file, download then upload
  - uri is an existing local file path    → local file, upload directly
  - anything else                         → treat as existing object_key, pass through
"""

from __future__ import annotations

import os
from typing import Any, List, Literal
from dataclasses import dataclass

# ContentItem type  →  object.sign file_type
_CONTENT_TYPE_TO_FILE_TYPE: dict[str, Literal["image", "file", "video"]] = {
    "image": "image",
    "audio": "file",
    "doc":   "file",
    "pdf":   "file",
    "html":  "file",
    "email": "file",
    # "video": "video",  # reserved, not in current ContentItemParam
}


@dataclass
class UploadTask:
    """Describes a single content item that needs to be uploaded."""

    msg_idx: int
    """Index of the message in the messages list."""

    content_idx: int
    """Index of the content item within message.content."""

    uri: str
    """Original uri value from the content item."""

    uri_type: Literal["local", "http"]
    """Whether the uri is a local file path or an HTTP(S) URL."""

    content_type: str
    """ContentItem type (e.g. 'image', 'doc')."""

    file_type: Literal["image", "file", "video"]
    """file_type for the object.sign API."""

    file_name: str | None
    """ContentItem name field (may be None)."""

    file_ext: str | None
    """ContentItem ext field (may be None)."""


def _is_http_uri(uri: str) -> bool:
    return uri.startswith("http://") or uri.startswith("https://")


def _is_local_file(uri: str) -> bool:
    """Return True only if uri refers to an existing local file.

    MinIO object keys contain server-generated UUID segments and will never
    match a local path, so os.path.isfile() is a reliable discriminator.
    """
    if "://" in uri:
        return False
    return os.path.isfile(os.path.expanduser(uri))


def scan_messages(messages: list[dict[str, Any]]) -> List[UploadTask]:
    """Scan messages and return a list of UploadTask for content items that need uploading.

    Returns an empty list when no uploads are needed (caller can skip multimodal path).
    Does NOT modify messages.
    """
    tasks: list[UploadTask] = []

    for msg_idx, msg in enumerate(messages):
        content = msg.get("content")

        # str shorthand → plain text, skip
        if content is None or isinstance(content, str):
            continue

        for ci_idx, item in enumerate(content):
            item_type = item.get("type", "text")

            if item_type == "text":
                continue

            uri = item.get("uri")
            if not uri or not isinstance(uri, str):
                continue

            if _is_http_uri(uri):
                uri_type: Literal["local", "http"] = "http"
            elif _is_local_file(uri):
                uri_type = "local"
            else:
                continue  # already an object_key or unsupported scheme

            file_type = _CONTENT_TYPE_TO_FILE_TYPE.get(item_type, "file")

            tasks.append(UploadTask(
                msg_idx=msg_idx,
                content_idx=ci_idx,
                uri=uri,
                uri_type=uri_type,
                content_type=item_type,
                file_type=file_type,
                file_name=item.get("name"),
                file_ext=item.get("ext"),
            ))

    return tasks
