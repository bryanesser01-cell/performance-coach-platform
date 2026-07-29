from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.sql import func

from database.base import Base


class WorkoutBlock(Base):
    """
    Stores structured workout blocks.

    Examples:
    Warm up
    Main set
    Cool down
    """

    __tablename__ = "workout_blocks"

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

    block_type = Column(
        String(50),
        nullable=False,
    )

    description = Column(
        String(500),
        nullable=True,
    )

    order_number = Column(
        Integer,
        nullable=False,
        default=1,
    )

    created_at = Column(
        DateTime,
        nullable=False,
        server_default=func.now(),
    )


class WorkoutDetail(Base):
    """
    Stores detailed workout instructions.

    Examples:

    4 x 200m
    5 x 400m
    3 x 1km
    30 minute tempo
    """

    __tablename__ = "workout_details"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    workout_block_id = Column(
        Integer,
        ForeignKey(
            "workout_blocks.id",
        ),
        nullable=False,
        index=True,
    )

    detail_type = Column(
        String(50),
        nullable=False,
    )

    distance_meters = Column(
        Integer,
        nullable=True,
    )

    duration_minutes = Column(
        Integer,
        nullable=True,
    )

    repetitions = Column(
        Integer,
        nullable=True,
    )

    target = Column(
        String(100),
        nullable=True,
    )

    recovery = Column(
        String(100),
        nullable=True,
    )

    notes = Column(
        String(500),
        nullable=True,
    )
