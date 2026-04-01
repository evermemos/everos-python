# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ..._models import BaseModel

__all__ = ["SettingsResponse"]


class SettingsResponse(BaseModel):
    boundary_detection_timeout: int
    """MemCell auto-flush idle timeout in seconds"""

    created_at: str
    """Creation time (ISO 8601)"""

    extraction_mode: str
    """Extraction mode"""

    offline_profile_extraction_interval: int
    """Offline profile extraction interval in seconds"""

    timezone: str
    """IANA timezone identifier"""

    updated_at: str
    """Last update time (ISO 8601)"""

    llm_custom_setting: Optional[Dict[str, object]] = None
    """LLM custom settings (serialized)"""
