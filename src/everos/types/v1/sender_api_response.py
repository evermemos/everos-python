# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .sender_response import SenderResponse

__all__ = ["SenderAPIResponse"]


class SenderAPIResponse(BaseModel):
    data: Optional[SenderResponse] = None
