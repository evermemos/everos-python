# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ToolCallFunctionParam"]


class ToolCallFunctionParam(TypedDict, total=False):
    arguments: Required[str]
    """JSON-encoded arguments string"""

    name: Required[str]
    """Function/tool name"""
