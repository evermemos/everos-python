# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["MemoryGetResponse", "Data", "DataAgentCase", "DataAgentSkill", "DataEpisode", "DataProfile"]


class DataAgentCase(BaseModel):
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


class DataAgentSkill(BaseModel):
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


class DataEpisode(BaseModel):
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


class DataProfile(BaseModel):
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


class Data(BaseModel):
    """Memory get result data"""

    agent_cases: Optional[List[DataAgentCase]] = None
    """Agent case items"""

    agent_skills: Optional[List[DataAgentSkill]] = None
    """Agent skill items"""

    count: Optional[int] = None
    """Records in current page"""

    episodes: Optional[List[DataEpisode]] = None
    """Episodic memory items"""

    profiles: Optional[List[DataProfile]] = None
    """Profile items"""

    total_count: Optional[int] = None
    """Total records matching filters"""


class MemoryGetResponse(BaseModel):
    data: Optional[Data] = None
    """Memory get result data"""
