# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["MemoryGetParams"]


class MemoryGetParams(TypedDict, total=False):
    filters: Required[Dict[str, object]]
    """Filter conditions.

    Must contain user_id or group_id (see memory_type for scope constraints).
    Supports operators: eq (implicit), in, gt, gte, lt, lte. Combinators: AND, OR.
    """

    memory_type: Required[Literal["episodic_memory", "profile", "agent_case", "agent_skill"]]
    """Memory type to query. Scope constraint per type:

    - episodic_memory: supports both user_id and group_id
    - profile: user_id only (group_id will return 400)
    - agent_case: user_id only (group_id will return 400)
    - agent_skill: user_id only (group_id will return 400)
    """

    page: int
    """Page number (starts from 1)"""

    page_size: int
    """Items per page"""

    rank_by: str
    """Sort field"""

    rank_order: Literal["asc", "desc"]
    """Sort order"""
