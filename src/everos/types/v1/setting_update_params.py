# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .llm_custom_setting_param import LlmCustomSettingParam

__all__ = ["SettingUpdateParams"]


class SettingUpdateParams(TypedDict, total=False):
    boundary_detection_timeout: Optional[int]
    """MemCell auto-flush idle timeout in seconds"""

    extraction_mode: Optional[Literal["default", "pro"]]
    """Extraction mode"""

    llm_custom_setting: Optional[LlmCustomSettingParam]
    """LLM custom settings for algorithm control"""

    offline_profile_extraction_interval: Optional[int]
    """Offline profile extraction interval in seconds"""

    timezone: Optional[str]
    """IANA timezone identifier"""
