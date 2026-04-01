# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["AgentCaseItem"]


class AgentCaseItem(BaseModel):
    """Agent case item (task experience)"""

    id: str
    """MongoDB ObjectId as string"""

    approach: Optional[str] = None
    """Step-by-step approach with decisions and lessons"""

    group_id: Optional[str] = None
    """Group ID"""

    parent_id: Optional[str] = None
    """Parent memory ID"""

    parent_type: Optional[str] = None
    """Parent memory type"""

    quality_score: Optional[float] = None
    """Task completion quality score (0.0-1.0)"""

    session_id: Optional[str] = None
    """Session identifier"""

    task_intent: Optional[str] = None
    """Rewritten task intent as retrieval key"""

    timestamp: Optional[datetime] = None
    """Task occurrence time"""

    user_id: Optional[str] = None
    """User ID"""
