from datetime import UTC, datetime

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from database.base import Base


class CoachLearningEvent(Base):
    """
    Stores AI Coach learning outcomes.

    Represents:
    - Coaching decision
    - Athlete response
    - Confidence adjustment
    """

    __tablename__ = "coach_learning_events"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    athlete_id: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        index=True,
    )

    decision: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    outcome: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    confidence_change: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    timestamp: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(UTC),
        nullable=False,
    )
