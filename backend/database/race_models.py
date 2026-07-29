from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.sql import func

from database.base import Base


class RaceGoal(Base):
    """
    Athlete race goal.

    Example:
    1500m target 4:45
    """

    __tablename__ = "race_goals"

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

    target_time = Column(
        String(20),
        nullable=False,
    )

    race_date = Column(
        DateTime,
        nullable=True,
    )

    priority = Column(
        String(50),
        nullable=False,
        default="primary",
    )

    created_at = Column(
        DateTime,
        nullable=False,
        server_default=func.now(),
    )


class RaceCheckpoint(Base):
    """
    Stores race split checkpoints.

    Examples:

    1500m:
    300m
    700m
    1100m
    1500m
    """

    __tablename__ = "race_checkpoints"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    race_goal_id = Column(
        Integer,
        ForeignKey("race_goals.id"),
        nullable=False,
        index=True,
    )

    distance_marker = Column(
        Integer,
        nullable=False,
    )

    target_split = Column(
        String(20),
        nullable=False,
    )

    cumulative_time = Column(
        String(20),
        nullable=False,
    )

    instruction = Column(
        String(500),
        nullable=True,
    )
