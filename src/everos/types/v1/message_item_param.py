# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .content_item_param import ContentItemParam

__all__ = ["MessageItemParam"]


class MessageItemParam(TypedDict, total=False):
    """Single message item for personal memories.

    Content accepts a plain string shorthand: "hello" is coerced to [{"type": "text", "text": "hello"}].
    """

    content: Required[Union[str, Iterable[ContentItemParam]]]
    """Content items array, or plain string shorthand"""

    role: Required[Literal["user", "assistant"]]
    """Message sender role"""

    timestamp: Required[int]
    """Message timestamp in unix milliseconds"""

    sender_id: Optional[str]
    """Sender identifier"""
