# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .tool_call_param import ToolCallParam
from ..content_item_param import ContentItemParam

__all__ = ["AgentMessageItemParam"]


class AgentMessageItemParam(TypedDict, total=False):
    """Agent trajectory message.

    Supports role='tool' in addition to 'user'/'assistant'. Does not support message_id or sender_name (stripped by Gateway).
    """

    role: Required[Literal["user", "assistant", "tool"]]
    """Message sender role"""

    timestamp: Required[int]
    """Message timestamp in unix milliseconds"""

    content: Union[str, Iterable[ContentItemParam], None]
    """Message content. Conditional requirement by role:

    - role='user': required, must not be empty
    - role='assistant' with tool_calls: optional, can be null/empty/omitted (OpenAI
      compatible)
    - role='assistant' without tool_calls: required, must not be empty
    - role='tool': required (tool execution result)
    """

    sender_id: Optional[str]
    """Sender identifier"""

    tool_call_id: Optional[str]
    """ID of the tool call this message responds to. Required when role='tool'."""

    tool_calls: Optional[Iterable[ToolCallParam]]
    """Tool calls made by assistant (OpenAI format). Only when role='assistant'."""
