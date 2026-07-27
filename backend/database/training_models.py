from sqlalchemy import (
    Column,
    Float,
    ForeignKey,
    Integer,
    String,
)

from database.base import Base


class TrainingSession(Base):
    """
    Athlete training session database model.
    """

    __tablename__ = "training_sessions"

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

    date = Column(
        String,
        nullable=False,
    )

    session_type = Column(
        String,
        nullable=False,
    )

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
        String,
        nullable=True,
    )
