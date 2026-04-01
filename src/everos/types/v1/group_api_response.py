# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .group_response import GroupResponse

__all__ = ["GroupAPIResponse"]


class GroupAPIResponse(BaseModel):
    data: Optional[GroupResponse] = None
