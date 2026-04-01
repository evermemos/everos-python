# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AddResponse", "Data"]


class Data(BaseModel):
    message: Optional[str] = None
    """Human-readable status description"""

    message_count: Optional[int] = None
    """Number of messages accepted"""

    status: Optional[Literal["accumulated", "extracted"]] = None
    """Processing status"""

    task_id: Optional[str] = None
    """Task tracking ID"""


class AddResponse(BaseModel):
    data: Optional[Data] = None
