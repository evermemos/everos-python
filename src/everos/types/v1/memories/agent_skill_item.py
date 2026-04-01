# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["AgentSkillItem"]


class AgentSkillItem(BaseModel):
    """Agent skill item (reusable skill from clustered cases)"""

    id: str
    """MongoDB ObjectId as string"""

    cluster_id: Optional[str] = None
    """MemScene cluster ID"""

    confidence: Optional[float] = None
    """Confidence score (0.0-1.0)"""

    content: Optional[str] = None
    """Full skill content"""

    description: Optional[str] = None
    """What this skill does and when to use it"""

    group_id: Optional[str] = None
    """Group ID"""

    maturity_score: Optional[float] = None
    """Maturity score (0.0-1.0)"""

    name: Optional[str] = None
    """Skill name"""

    source_case_ids: Optional[List[str]] = None
    """Source AgentCase IDs"""

    user_id: Optional[str] = None
    """User ID"""
