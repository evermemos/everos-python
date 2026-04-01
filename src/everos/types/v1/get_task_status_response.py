# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .task_status_result import TaskStatusResult

__all__ = ["GetTaskStatusResponse"]


class GetTaskStatusResponse(BaseModel):
    data: TaskStatusResult
