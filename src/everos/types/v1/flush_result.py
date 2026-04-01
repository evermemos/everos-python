# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["FlushResult"]


class FlushResult(BaseModel):
    message: Optional[str] = None
    """Human-readable status description"""

    request_id: Optional[str] = None
    """Request tracking ID (reserved)"""

    status: Optional[Literal["extracted", "no_extraction"]] = None
    """Processing status"""
