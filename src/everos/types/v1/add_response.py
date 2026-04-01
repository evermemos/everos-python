# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .add_result import AddResult

__all__ = ["AddResponse"]


class AddResponse(BaseModel):
    data: Optional[AddResult] = None
