# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ..content_item_param import ContentItemParam

__all__ = ["AgentCreateParams", "Message", "MessageToolCall", "MessageToolCallFunction"]


class AgentCreateParams(TypedDict, total=False):
    messages: Required[Iterable[Message]]
    """Agent trajectory messages (1-500 items)"""

    user_id: Required[str]
    """Owner user ID"""

    async_mode: bool
    """Enable async processing.

    When true, returns 202 with task_id; when false, processes synchronously and
    returns 200.
    """

    session_id: Optional[str]
    """Session identifier"""


class MessageToolCallFunction(TypedDict, total=False):
    arguments: Required[str]
    """JSON-encoded arguments string"""

    name: Required[str]
    """Function/tool name"""


class MessageToolCall(TypedDict, total=False):
    """OpenAI-format tool call made by the assistant"""

    id: Required[str]
    """Unique tool call ID"""

    function: Required[MessageToolCallFunction]

    type: str
    """Tool call type"""


class Message(TypedDict, total=False):
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

    tool_calls: Optional[Iterable[MessageToolCall]]
    """Tool calls made by assistant (OpenAI format). Only when role='assistant'."""
