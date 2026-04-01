# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .object_sign_item import ObjectSignItem

__all__ = ["ObjectSignResponse", "Result", "ResultData"]


class ResultData(BaseModel):
    """On success: contains objectList. On validation error: string error message."""

    object_list: Optional[List[ObjectSignItem]] = FieldInfo(alias="objectList", default=None)


class Result(BaseModel):
    data: Optional[ResultData] = None
    """On success: contains objectList. On validation error: string error message."""


class ObjectSignResponse(BaseModel):
    """
    MMS service response format (Gateway transparent proxy, not standard ErrorResponse format)
    """

    error: Optional[str] = None
    """Error message. 'OK' on success, error description on failure"""

    request_id: Optional[str] = None
    """MMS request tracking ID"""

    result: Optional[Result] = None

    status: Optional[int] = None
    """MMS status code. 0 = success, 2018 = validation error"""
