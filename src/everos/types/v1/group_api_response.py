# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["GroupAPIResponse", "Data"]


class Data(BaseModel):
    created_at: str
    """Creation time (ISO 8601)"""

    group_id: str
    """Group identifier"""

    updated_at: str
    """Last update time (ISO 8601)"""

    description: Optional[str] = None
    """Group description"""

    name: Optional[str] = None
    """Group display name"""


class GroupAPIResponse(BaseModel):
    data: Optional[Data] = None
