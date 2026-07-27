from sqlalchemy import Column, Float, ForeignKey, Integer, String

from database.base import Base


class Athlete(Base):
    """
    Athlete database model.
    """

    __tablename__ = "athletes"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    name = Column(
        String(100),
        nullable=False,
    )

    age = Column(
        Integer,
        nullable=False,
    )

    height_cm = Column(
        Float,
        nullable=False,
    )

    weight_kg = Column(
        Float,
        nullable=False,
    )

    resting_hr = Column(
        Integer,
        nullable=False,
    )

    max_hr = Column(
        Integer,
        nullable=False,
    )

    sport = Column(
        String(50),
        nullable=False,
    )

    primary_event = Column(
        String(50),
        nullable=False,
    )

    experience_level = Column(
        String(50),
        nullable=True,
    )

    weekly_distance = Column(
        Float,
        nullable=True,
    )

    training_days_per_week = Column(
        Integer,
        nullable=True,
    )

    current_5k_time = Column(
        Float,
        nullable=True,
    )

    injury_status = Column(
        String(100),
        nullable=True,
    )


class Goal(Base):
    """
    Athlete goal database model.
    """

    __tablename__ = "goals"

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

    goal_type = Column(
        String(50),
        nullable=False,
    )

    target_value = Column(
        Float,
        nullable=False,
    )

    target_unit = Column(
        String(20),
        nullable=False,
    )

    current_value = Column(
        Float,
        nullable=False,
    )

    status = Column(
        String(20),
        nullable=False,
        default="Active",
    )
