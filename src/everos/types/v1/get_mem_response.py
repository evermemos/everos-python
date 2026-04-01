# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .episode_item import EpisodeItem
from .profile_item import ProfileItem
from .memories.agent_case_item import AgentCaseItem
from .memories.agent_skill_item import AgentSkillItem

__all__ = ["GetMemResponse"]


class GetMemResponse(BaseModel):
    """Memory get result data"""

    agent_cases: Optional[List[AgentCaseItem]] = None
    """Agent case items"""

    agent_skills: Optional[List[AgentSkillItem]] = None
    """Agent skill items"""

    count: Optional[int] = None
    """Records in current page"""

    episodes: Optional[List[EpisodeItem]] = None
    """Episodic memory items"""

    profiles: Optional[List[ProfileItem]] = None
    """Profile items"""

    total_count: Optional[int] = None
    """Total records matching filters"""
