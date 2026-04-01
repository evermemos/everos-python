# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["SenderCreateParams"]


class SenderCreateParams(TypedDict, total=False):
    sender_id: Required[str]
    """Sender identifier (unique)"""

    name: Optional[str]
    """Sender display name"""
