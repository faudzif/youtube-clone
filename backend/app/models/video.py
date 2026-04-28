from sqlalchemy import Column, String, Integer, Text, ARRAY, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid
from app.core.database import Base


class Video(Base):
    __tablename__ = "videos"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(Text, nullable=False)
    description = Column(Text)
    category = Column(String)
    tags = Column(ARRAY(String))
    s3_key = Column(Text, nullable=False)
    thumbnail_url = Column(Text)
    duration = Column(Integer)
    views = Column(Integer, default=0)
    created_at = Column(TIMESTAMP, server_default=func.now())



