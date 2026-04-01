# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ObjectGetPresignedURLParams", "ObjectList"]


class ObjectGetPresignedURLParams(TypedDict, total=False):
    object_list: Required[Annotated[Iterable[ObjectList], PropertyInfo(alias="objectList")]]
    """List of files to sign (supports batch signing)"""


class ObjectList(TypedDict, total=False):
    """Single file sign request item"""

    file_id: Required[Annotated[str, PropertyInfo(alias="fileId")]]
    """Business-defined unique file identifier"""

    file_name: Required[Annotated[str, PropertyInfo(alias="fileName")]]
    """File name (may include extension)"""

    file_type: Required[Annotated[Literal["image", "file", "video"], PropertyInfo(alias="fileType")]]
    """File type category. Max size: image=10MB, file=100MB, video=500MB"""
