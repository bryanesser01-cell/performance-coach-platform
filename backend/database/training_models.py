from sqlalchemy import (
    Column,
    Date,
    Float,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import relationship

from database.base_model import BaseModel


class TrainingSession(BaseModel):
    """
    Individual training session completed by an athlete.
    """

    __tablename__ = "training_sessions"

    athlete_id = Column(
        Integer,
        ForeignKey("athletes.id"),
        nullable=False,
        index=True,
    )

    # -------------------------
    # Session Information
    # -------------------------

    date = Column(
        Date,
        nullable=False,
    )

    session_type = Column(
        String(100),
        nullable=False,
    )

    # -------------------------
    # Performance Metrics
    # -------------------------

    distance = Column(
        Float,
        nullable=False,
    )

    duration = Column(
        Float,
        nullable=False,
    )

    average_pace = Column(
        Float,
        nullable=False,
    )

    average_hr = Column(
        Integer,
        nullable=True,
    )

    max_hr = Column(
        Integer,
        nullable=True,
    )

    cadence = Column(
        Integer,
        nullable=True,
    )

    elevation_gain = Column(
        Float,
        nullable=True,
    )

    training_load = Column(
        Float,
        nullable=True,
    )

    rpe = Column(
        Integer,
        nullable=True,
    )

    notes = Column(
        Text,
        nullable=True,
    )

    # -------------------------
    # Relationships
    # -------------------------

    athlete = relationship(
        "Athlete",
        back_populates="training_sessions",
    )
