# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["GroupCreateParams"]


class GroupCreateParams(TypedDict, total=False):
    group_id: Required[str]
    """Group identifier (unique)"""

    description: Optional[str]
    """Group description"""

    name: Optional[str]
    """Group display name"""
