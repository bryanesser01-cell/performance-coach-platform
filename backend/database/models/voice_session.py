from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.sql import func

from database.base import Base


class VoiceSession(Base):
    """
    Stores athlete voice coach conversations.

    Stores:
    - Athlete
    - Session identifier
    - Athlete messages
    - Coach responses
    """

    __tablename__ = "voice_sessions"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    athlete_id = Column(
        Integer,
        ForeignKey("athletes.id"),
        nullable=False,
        index=True,
    )

    session_id = Column(
        String(100),
        nullable=False,
        index=True,
    )

    user_message = Column(
        String(1000),
        nullable=False,
    )

    coach_response = Column(
        String(2000),
        nullable=False,
    )

    created_at = Column(
        DateTime,
        nullable=False,
        server_default=func.now(),
    )
