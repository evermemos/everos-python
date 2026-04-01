# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = [
    "MemorySearchResponse",
    "Data",
    "DataQuery",
    "DataAgentMemory",
    "DataAgentMemoryCase",
    "DataAgentMemorySkill",
    "DataEpisode",
    "DataEpisodeAtomicFact",
    "DataProfile",
    "DataRawMessage",
]


class DataQuery(BaseModel):
    method: str
    """Retrieval method used"""

    text: str
    """Search query text"""

    filters_applied: Optional[Dict[str, object]] = None
    """Filters applied"""


class DataAgentMemoryCase(BaseModel):
    """Agent case search result with relevance score"""

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

    score: Optional[float] = None
    """Relevance score"""

    session_id: Optional[str] = None
    """Session identifier"""

    task_intent: Optional[str] = None
    """Rewritten task intent as retrieval key"""

    timestamp: Optional[datetime] = None
    """Task occurrence time"""

    user_id: Optional[str] = None
    """User ID"""


class DataAgentMemorySkill(BaseModel):
    """Agent skill search result with relevance score"""

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

    score: Optional[float] = None
    """Relevance score"""

    source_case_ids: Optional[List[str]] = None
    """Source AgentCase IDs"""

    user_id: Optional[str] = None
    """User ID"""


class DataAgentMemory(BaseModel):
    """Agent memory search results (cases + skills)"""

    cases: Optional[List[DataAgentMemoryCase]] = None
    """Agent case search results"""

    skills: Optional[List[DataAgentMemorySkill]] = None
    """Agent skill search results"""


class DataEpisodeAtomicFact(BaseModel):
    """Atomic fact expanded from an episode"""

    id: str
    """MongoDB ObjectId as string"""

    atomic_fact: Optional[str] = None
    """Atomic fact content"""

    group_id: Optional[str] = None
    """Group ID"""

    original_text: Optional[str] = None
    """Original text from parent episode"""

    parent_episode_id: Optional[str] = None
    """Source episode ID (MRAG expansion)"""

    parent_id: Optional[str] = None
    """Parent memory ID"""

    parent_type: Optional[str] = None
    """Parent memory type"""

    participants: Optional[List[str]] = None
    """Related participant IDs"""

    score: Optional[float] = None
    """Relevance score"""

    session_id: Optional[str] = None
    """Session identifier"""

    timestamp: Optional[datetime] = None
    """Event occurrence time"""

    user_id: Optional[str] = None
    """User ID"""


class DataEpisode(BaseModel):
    """Episode search result with relevance score"""

    id: str
    """MongoDB ObjectId as string"""

    atomic_facts: Optional[List[DataEpisodeAtomicFact]] = None
    """Atomic facts expanded from this episode"""

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

    score: Optional[float] = None
    """Relevance score"""

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
    """Profile search result with relevance score"""

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

    score: Optional[float] = None
    """Relevance score"""

    user_id: Optional[str] = None
    """User ID"""


class DataRawMessage(BaseModel):
    """Raw unprocessed message waiting for memory extraction"""

    id: str
    """MongoDB ObjectId as string"""

    request_id: str
    """Request ID"""

    content_items: Optional[List[Dict[str, object]]] = None

    created_at: Optional[str] = None
    """ISO 8601 format"""

    group_id: Optional[str] = None
    """Group ID"""

    message_id: Optional[str] = None
    """Message ID"""

    sender_id: Optional[str] = None
    """Sender ID"""

    sender_name: Optional[str] = None
    """Sender name"""

    session_id: Optional[str] = None
    """Session identifier"""

    timestamp: Optional[str] = None
    """ISO 8601 format"""

    updated_at: Optional[str] = None
    """ISO 8601 format"""


class Data(BaseModel):
    """Memory search result data"""

    query: DataQuery

    agent_memory: Optional[DataAgentMemory] = None
    """Agent memory search results (cases + skills)"""

    episodes: Optional[List[DataEpisode]] = None
    """Episodic memory search results"""

    original_data: Optional[Dict[str, object]] = None
    """Original data (if include_original_data=true)"""

    profiles: Optional[List[DataProfile]] = None
    """Profile search results"""

    raw_messages: Optional[List[DataRawMessage]] = None
    """Raw unprocessed messages (pending)"""


class MemorySearchResponse(BaseModel):
    data: Optional[Data] = None
    """Memory search result data"""
