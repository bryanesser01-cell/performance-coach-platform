from sqlalchemy import (
    Column,
    Date,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
    func,
)
from sqlalchemy.orm import relationship

from database.database import Base


class WorkoutPlan(Base):
    """
    SQLAlchemy model representing a workout plan assigned to an athlete.
    """

    __tablename__ = "workout_plans"

    id = Column(Integer, primary_key=True, index=True)

    athlete_id = Column(
        Integer,
        ForeignKey("athletes.id"),
        nullable=False,
    )

    title = Column(
        String(150),
        nullable=False,
    )

    description = Column(Text)

    start_date = Column(
        Date,
        nullable=False,
    )

    end_date = Column(Date)

    goal = Column(String(100))

    status = Column(
        String(50),
        nullable=False,
        default="Draft",
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    athlete = relationship(
        "Athlete",
        back_populates="workout_plans",
    )
