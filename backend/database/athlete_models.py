from sqlalchemy import (
    Column,
    Date,
    Enum,
    Float,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import relationship

from database.base_model import BaseModel
from database.enums import (
    ExperienceLevel,
    InjuryStatus,
    Sex,
    Sport,
)


class Athlete(BaseModel):
    """
    Athlete profile.

    Stores the athlete's current profile.
    Historical metrics (body weight, performance,
    recovery, etc.) are stored in dedicated tables.
    """

    __tablename__ = "athletes"

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
        index=True,
    )

    # -------------------------
    # Personal Information
    # -------------------------

    first_name = Column(
        String(100),
        nullable=False,
    )

    last_name = Column(
        String(100),
        nullable=False,
    )

    preferred_name = Column(
        String(100),
        nullable=True,
    )

    date_of_birth = Column(
        Date,
        nullable=True,
    )

    sex = Column(
        Enum(Sex),
        nullable=True,
    )

    # -------------------------
    # Physical Profile
    # -------------------------

    height_cm = Column(
        Float,
        nullable=True,
    )

    weight_kg = Column(
        Float,
        nullable=True,
    )

    # -------------------------
    # Sport Profile
    # -------------------------

    sport = Column(
        Enum(Sport),
        nullable=True,
    )

    primary_event = Column(
        String(100),
        nullable=True,
    )

    experience_level = Column(
        Enum(ExperienceLevel),
        nullable=True,
    )

    years_training = Column(
        Integer,
        nullable=True,
    )

    # -------------------------
    # Training Profile
    # -------------------------

    weekly_training_days = Column(
        Integer,
        nullable=True,
    )

    weekly_training_hours = Column(
        Float,
        nullable=True,
    )

    weekly_distance = Column(
        Float,
        nullable=True,
    )

    # -------------------------
    # Physiology
    # -------------------------

    resting_hr = Column(
        Integer,
        nullable=True,
    )

    threshold_hr = Column(
        Integer,
        nullable=True,
    )

    max_hr = Column(
        Integer,
        nullable=True,
    )

    ftp = Column(
        Integer,
        nullable=True,
    )

    vo2_max = Column(
        Float,
        nullable=True,
    )

    # -------------------------
    # Health
    # -------------------------

    injury_status = Column(
        Enum(InjuryStatus),
        nullable=True,
    )

    # -------------------------
    # Coaching
    # -------------------------

    coach_notes = Column(
        Text,
        nullable=True,
    )

    # -------------------------
    # Relationships
    # -------------------------

    user = relationship(
        "User",
        back_populates="athletes",
    )

    goals = relationship(
        "Goal",
        back_populates="athlete",
        cascade="all, delete-orphan",
    )

    training_sessions = relationship(
        "TrainingSession",
        back_populates="athlete",
        cascade="all, delete-orphan",
    )

    performance_cycles = relationship(
        "PerformanceCycle",
        back_populates="athlete",
        cascade="all, delete-orphan",
    )

    workout_plans = relationship(
        "WorkoutPlan",
        back_populates="athlete",
        cascade="all, delete-orphan",
    )
