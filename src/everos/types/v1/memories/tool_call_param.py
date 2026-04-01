# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .tool_call_function_param import ToolCallFunctionParam

__all__ = ["ToolCallParam"]


class ToolCallParam(TypedDict, total=False):
    """OpenAI-format tool call made by the assistant"""

    id: Required[str]
    """Unique tool call ID"""

    function: Required[ToolCallFunctionParam]

    type: str
    """Tool call type"""
