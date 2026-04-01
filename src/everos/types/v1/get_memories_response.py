# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .get_mem_response import GetMemResponse

__all__ = ["GetMemoriesResponse"]


class GetMemoriesResponse(BaseModel):
    data: Optional[GetMemResponse] = None
    """Memory get result data"""
