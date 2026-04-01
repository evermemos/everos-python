# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["MemoryFlushParams"]


class MemoryFlushParams(TypedDict, total=False):
    user_id: Required[str]
    """Owner user ID"""

    session_id: Optional[str]
    """Target session"""
