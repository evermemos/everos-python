# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .object_sign_item_request_param import ObjectSignItemRequestParam

__all__ = ["ObjectSignParams"]


class ObjectSignParams(TypedDict, total=False):
    object_list: Required[Annotated[Iterable[ObjectSignItemRequestParam], PropertyInfo(alias="objectList")]]
    """List of files to sign (supports batch signing)"""
