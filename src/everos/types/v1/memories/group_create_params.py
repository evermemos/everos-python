# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ..content_item_param import ContentItemParam

__all__ = ["GroupCreateParams", "Message"]


class GroupCreateParams(TypedDict, total=False):
    group_id: Required[str]
    """Group identifier"""

    messages: Required[Iterable[Message]]
    """Batch message array (1-500 items). sender_id is required per message."""

    async_mode: bool
    """Enable async processing.

    When true, returns 202 with task_id; when false, processes synchronously and
    returns 200.
    """

    group_meta: Optional[Dict[str, object]]
    """Group metadata"""


class Message(TypedDict, total=False):
    """Single message item for group memories.

    Each message must include sender_id to identify participants.
    """

    content: Required[Union[str, Iterable[ContentItemParam]]]
    """Content items array, or plain string shorthand"""

    role: Required[Literal["user", "assistant"]]
    """Message sender role"""

    sender_id: Required[str]
    """Sender identifier (required for group)"""

    timestamp: Required[int]
    """Message timestamp in unix milliseconds"""

    message_id: Optional[str]
    """Message unique ID"""

    sender_name: Optional[str]
    """Sender display name"""
