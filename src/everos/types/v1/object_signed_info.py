# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ObjectSignedInfo"]


class ObjectSignedInfo(BaseModel):
    fields: Optional[Dict[str, str]] = None
    """
    Form fields required for S3 POST upload (key, policy, x-amz-\\** headers,
    Content-Type)
    """

    max_size: Optional[int] = FieldInfo(alias="maxSize", default=None)
    """Maximum file size in bytes. image: 10MB, file: 100MB, video: 500MB"""

    url: Optional[str] = None
    """Pre-signed S3 upload URL"""
