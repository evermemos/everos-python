# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["V1QueryTaskStatusResponse", "Data"]


class Data(BaseModel):
    status: Literal["processing", "success", "failed"]
    """Task status"""

    task_id: str
    """Async task tracking ID"""


class V1QueryTaskStatusResponse(BaseModel):
    data: Data
