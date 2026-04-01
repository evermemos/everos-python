# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .flush_result import FlushResult

__all__ = ["FlushResponse"]


class FlushResponse(BaseModel):
    data: Optional[FlushResult] = None
