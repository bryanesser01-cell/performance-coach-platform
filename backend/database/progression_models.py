from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.sql import func

from database.base import Base


class TrainingProgression(Base):
    """
    Stores recommended next training sessions.

    Example:
    Athlete needs:
    5 x 400m @ race pace
    """

    __tablename__ = "training_progressions"

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

    event = Column(
        String(50),
        nullable=False,
    )

    goal_time = Column(
        String(20),
        nullable=True,
    )

    session_type = Column(
        String(100),
        nullable=False,
    )

    workout_description = Column(
        String(500),
        nullable=False,
    )

    target_pace = Column(
        String(50),
        nullable=True,
    )

    recovery = Column(
        String(100),
        nullable=True,
    )

    purpose = Column(
        String(300),
        nullable=True,
    )

    created_at = Column(
        DateTime,
        nullable=False,
        server_default=func.now(),
    )
