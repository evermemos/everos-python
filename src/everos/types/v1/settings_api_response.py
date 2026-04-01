# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .settings_response import SettingsResponse

__all__ = ["SettingsAPIResponse"]


class SettingsAPIResponse(BaseModel):
    data: Optional[SettingsResponse] = None
