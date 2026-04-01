# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .search_memories_response_data import SearchMemoriesResponseData

__all__ = ["SearchMemoriesResponse"]


class SearchMemoriesResponse(BaseModel):
    data: Optional[SearchMemoriesResponseData] = None
    """Memory search result data"""
