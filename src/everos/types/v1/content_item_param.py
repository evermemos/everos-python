# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ContentItemParam"]


class ContentItemParam(TypedDict, total=False):
    """Single content item in a message. This phase only supports type='text'."""

    type: Required[Literal["text", "audio", "image", "doc", "pdf", "html", "email"]]
    """Content type"""

    base64: Optional[str]
    """Base64-encoded content"""

    ext: Optional[str]
    """File extension (e.g., png, mp3, pdf)"""

    extras: Optional[Dict[str, object]]
    """Type-specific extra fields"""

    name: Optional[str]
    """File name"""

    source: Optional[str]
    """Content source (e.g., google_doc, notion, confluence, zoom)"""

    source_info: Optional[Dict[str, object]]
    """Source-related traceability info"""

    text: Optional[str]
    """Content body. For type='text', this is the actual text."""

    uri: Optional[str]
    """File URI (MinIO, HTTP, etc.)"""
