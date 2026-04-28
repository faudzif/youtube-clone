from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID
from datetime import datetime

# what comes back from the API


class VideoOut(BaseModel):
    id: UUID
    title: str
    description: Optional[str]
    category: Optional[str]
    tags: Optional[List[str]]
    s3_key: str
    thumbnail_url: Optional[str]
    duration: Optional[int]
    views: int
    created_at: datetime

    # allows ORM → Pydantic conversion
    model_config = {"from_attributes": True}


# what the client sends when creating a video (after upload)
class VideoCreate(BaseModel):
    title:         str
    description:   Optional[str] = None
    category:      Optional[str] = None
    tags:          Optional[List[str]] = []
    s3_key:        str
    thumbnail_url: Optional[str] = None
    duration:      Optional[int] = None
