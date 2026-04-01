# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["MemorySearchParams"]


class MemorySearchParams(TypedDict, total=False):
    filters: Required[Dict[str, object]]
    """Filter conditions.

    Must contain user_id or group_id (agent_memory and profile require user_id only,
    same scope constraints as GET endpoint). Same DSL as GET endpoint.
    """

    query: Required[str]
    """Search query text"""

    include_original_data: bool
    """Whether to return original data"""

    memory_types: List[Literal["episodic_memory", "profile", "raw_message", "agent_memory"]]
    """Memory types to search"""

    method: Literal["keyword", "vector", "hybrid", "agentic"]
    """Retrieval method"""

    radius: Optional[float]
    """COSINE similarity threshold (0.0-1.0) for vector methods"""

    top_k: int
    """Max results. -1 = return all meeting threshold (up to 100)"""
