# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["MemoryDeleteParams"]


class MemoryDeleteParams(TypedDict, total=False):
    group_id: Optional[str]
    """Group ID scope for batch delete"""

    memory_id: Optional[str]
    """MemCell ID for single delete"""

    sender_id: Optional[str]
    """Sender filter, matches participants array (batch delete only)"""

    session_id: Optional[str]
    """Session filter (batch delete only)"""

    user_id: Optional[str]
    """User ID scope for batch delete"""
