# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["EpisodeItem"]


class EpisodeItem(BaseModel):
    """Episodic memory item"""

    id: str
    """MongoDB ObjectId as string"""

    episode: Optional[str] = None
    """Full episodic memory text"""

    group_id: Optional[str] = None
    """Group ID"""

    parent_id: Optional[str] = None
    """Parent memory ID"""

    parent_type: Optional[str] = None
    """Parent memory type"""

    participants: Optional[List[str]] = None
    """Event participant names"""

    sender_ids: Optional[List[str]] = None
    """Sender IDs of event participants"""

    session_id: Optional[str] = None
    """Session identifier"""

    subject: Optional[str] = None
    """Memory subject"""

    summary: Optional[str] = None
    """Memory summary"""

    timestamp: Optional[datetime] = None
    """Event occurrence time"""

    type: Optional[str] = None
    """Episode type"""

    user_id: Optional[str] = None
    """Owner user ID"""
