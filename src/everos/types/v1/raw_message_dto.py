# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel

__all__ = ["RawMessageDto"]


class RawMessageDto(BaseModel):
    """Raw unprocessed message waiting for memory extraction"""

    id: str
    """MongoDB ObjectId as string"""

    request_id: str
    """Request ID"""

    content_items: Optional[List[Dict[str, object]]] = None

    created_at: Optional[str] = None
    """ISO 8601 format"""

    group_id: Optional[str] = None
    """Group ID"""

    message_id: Optional[str] = None
    """Message ID"""

    sender_id: Optional[str] = None
    """Sender ID"""

    sender_name: Optional[str] = None
    """Sender name"""

    session_id: Optional[str] = None
    """Session identifier"""

    timestamp: Optional[str] = None
    """ISO 8601 format"""

    updated_at: Optional[str] = None
    """ISO 8601 format"""
