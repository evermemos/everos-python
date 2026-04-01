# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .agent_message_item_param import AgentMessageItemParam

__all__ = ["AgentAddParams"]


class AgentAddParams(TypedDict, total=False):
    messages: Required[Iterable[AgentMessageItemParam]]
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
