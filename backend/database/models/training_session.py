from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.sql import func

from database.base import Base


class TrainingSession(Base):
    """
    Stores planned and completed training sessions.

    Examples:
    - Interval session
    - Tempo run
    - Long run
    - Recovery run
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

    session_date = Column(
        DateTime,
        nullable=False,
    )

    session_type = Column(
        String(50),
        nullable=False,
    )

    focus = Column(
        String(100),
        nullable=False,
    )

    status = Column(
        String(30),
        nullable=False,
        default="planned",
    )

    notes = Column(
        String(1000),
        nullable=True,
    )

    created_at = Column(
        DateTime,
        nullable=False,
        server_default=func.now(),
    )
