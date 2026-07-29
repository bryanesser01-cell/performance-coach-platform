from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
)

from database.base import Base


class WorkoutInterval(Base):
    """
    Stores interval details inside
    a training session.

    Example:

    4 x 200m
    Target: 40 seconds
    Recovery: 60 seconds
    """

    __tablename__ = "workout_intervals"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    training_session_id = Column(
        Integer,
        ForeignKey(
            "training_sessions.id",
        ),
        nullable=False,
        index=True,
    )

    distance_meters = Column(
        Integer,
        nullable=False,
    )

    repetitions = Column(
        Integer,
        nullable=False,
    )

    target_time = Column(
        String(50),
        nullable=True,
    )

    recovery = Column(
        String(50),
        nullable=True,
    )
