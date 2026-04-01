# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SenderResponse"]


class SenderResponse(BaseModel):
    created_at: str
    """Creation time (ISO 8601)"""

    sender_id: str
    """Sender identifier"""

    updated_at: str
    """Last update time (ISO 8601)"""

    name: Optional[str] = None
    """Sender display name"""
