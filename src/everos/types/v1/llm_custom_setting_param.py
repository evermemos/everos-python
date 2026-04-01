# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

from .llm_provider_config_param import LlmProviderConfigParam

__all__ = ["LlmCustomSettingParam"]


class LlmCustomSettingParam(TypedDict, total=False):
    boundary: Optional[LlmProviderConfigParam]
    """LLM config for boundary detection (fast, cheap model recommended)"""

    extra: Optional[Dict[str, object]]
    """Additional task-specific LLM configurations"""

    extraction: Optional[LlmProviderConfigParam]
    """LLM config for memory extraction (high quality model recommended)"""
