# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Required, TypedDict

from .group_message_item_param import GroupMessageItemParam

__all__ = ["GroupAddParams"]


class GroupAddParams(TypedDict, total=False):
    group_id: Required[str]
    """Group identifier"""

    messages: Required[Iterable[GroupMessageItemParam]]
    """Batch message array (1-500 items). sender_id is required per message."""

    async_mode: bool
    """Enable async processing.

    When true, returns 202 with task_id; when false, processes synchronously and
    returns 200.
    """

    group_meta: Optional[Dict[str, object]]
    """Group metadata"""
