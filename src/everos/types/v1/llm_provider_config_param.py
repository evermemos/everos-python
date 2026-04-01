# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["LlmProviderConfigParam"]


class LlmProviderConfigParam(TypedDict, total=False):
    model: Required[str]
    """Model name"""

    provider: Required[str]
    """LLM provider name"""

    extra: Optional[Dict[str, object]]
    """Additional provider-specific configuration"""
