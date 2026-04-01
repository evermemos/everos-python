# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, TypedDict

from .llm_provider_config_param import LlmProviderConfigParam

__all__ = ["SettingUpdateParams", "LlmCustomSetting"]


class SettingUpdateParams(TypedDict, total=False):
    boundary_detection_timeout: Optional[int]
    """MemCell auto-flush idle timeout in seconds"""

    extraction_mode: Optional[Literal["default", "pro"]]
    """Extraction mode"""

    llm_custom_setting: Optional[LlmCustomSetting]
    """LLM custom settings for algorithm control"""

    offline_profile_extraction_interval: Optional[int]
    """Offline profile extraction interval in seconds"""

    timezone: Optional[str]
    """IANA timezone identifier"""


class LlmCustomSetting(TypedDict, total=False):
    """LLM custom settings for algorithm control"""

    boundary: Optional[LlmProviderConfigParam]
    """LLM config for boundary detection (fast, cheap model recommended)"""

    extra: Optional[Dict[str, object]]
    """Additional task-specific LLM configurations"""

    extraction: Optional[LlmProviderConfigParam]
    """LLM config for memory extraction (high quality model recommended)"""
