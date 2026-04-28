# backend/app/api/v1/endpoints/videos.py
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import or_
from typing import Optional, List
from uuid import UUID

from app.core.database import get_db
from app.models.video import Video
from app.schemas.video import VideoOut, VideoCreate

router = APIRouter()


@router.get("/", response_model=List[VideoOut])
def get_videos(
    search:   Optional[str] = Query(None),
    category: Optional[str] = Query(None),
    tags:     Optional[List[str]] = Query(None),
    db:       Session = Depends(get_db)
):
    query = db.query(Video)

    if search:
        query = query.filter(
            or_(
                Video.title.ilike(f"%{search}%"),
                Video.description.ilike(f"%{search}%")
            )
        )

    if category:
        query = query.filter(Video.category == category)

    if tags:
        # returns videos that contain ANY of the provided tags
        query = query.filter(Video.tags.overlap(tags))

    return query.order_by(Video.created_at.desc()).all()


@router.get("/{video_id}", response_model=VideoOut)
def get_video(video_id: UUID, db: Session = Depends(get_db)):
    video = db.query(Video).filter(Video.id == video_id).first()
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")

    # increment view count
    video.views += 1
    db.commit()
    db.refresh(video)

    return video


@router.post("/", response_model=VideoOut)
def create_video(payload: VideoCreate, db: Session = Depends(get_db)):
    video = Video(**payload.model_dump())
    db.add(video)
    db.commit()
    db.refresh(video)
    return video
