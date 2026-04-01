# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ..._models import BaseModel

__all__ = ["ProfileItem"]


class ProfileItem(BaseModel):
    """User profile item"""

    id: str
    """MongoDB ObjectId as string"""

    group_id: Optional[str] = None
    """Group ID"""

    memcell_count: Optional[int] = None
    """Number of MemCells"""

    profile_data: Optional[Dict[str, object]] = None
    """Profile data (explicit_info, implicit_traits)"""

    scenario: Optional[str] = None
    """Scenario type: solo or team"""

    user_id: Optional[str] = None
    """User ID"""
