from sqlalchemy import (
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.sql import func

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


class Activity(Base):
    """
    Athlete activity database model.
    """

    __tablename__ = "activities"

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

    source = Column(
        String(50),
        nullable=False,
        index=True,
    )

    external_id = Column(
        String(100),
        nullable=True,
        index=True,
    )

    category = Column(
        String(50),
        nullable=False,
    )

    name = Column(
        String(100),
        nullable=False,
    )

    started_at = Column(
        DateTime,
        nullable=False,
    )

    ended_at = Column(
        DateTime,
        nullable=True,
    )

    created_at = Column(
        DateTime,
        nullable=False,
    )


class AthleteMemory(Base):
    """
    Long-term AI athlete memory.
    """

    __tablename__ = "athlete_memories"

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

    memory_type = Column(
        String(50),
        nullable=False,
    )

    memory_value = Column(
        String(500),
        nullable=False,
    )

    created_at = Column(
        DateTime,
        nullable=False,
        server_default=func.now(),
    )


class AthleteCheckin(Base):
    """
    Daily athlete readiness check-in.
    """

    __tablename__ = "athlete_checkins"

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

    sleep_score = Column(
        Integer,
        nullable=False,
    )

    soreness_score = Column(
        Integer,
        nullable=False,
    )

    energy_score = Column(
        Integer,
        nullable=False,
    )

    motivation_score = Column(
        Integer,
        nullable=False,
    )

    created_at = Column(
        DateTime,
        nullable=False,
        server_default=func.now(),
    )


class VoiceSession(Base):
    """
    Stores athlete voice coach conversations.
    """

    __tablename__ = "voice_sessions"

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

    session_id = Column(
        String(100),
        nullable=False,
        index=True,
    )

    user_message = Column(
        String(1000),
        nullable=False,
    )

    coach_response = Column(
        String(2000),
        nullable=False,
    )

    created_at = Column(
        DateTime,
        nullable=False,
        server_default=func.now(),
    )


class CoachLearningEvent(Base):
    """
    Stores AI Coach learning outcomes.

    Records:
    - Coaching decision
    - Athlete response
    - Confidence adjustment
    """

    __tablename__ = "coach_learning_events"

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

    decision = Column(
        String(50),
        nullable=False,
    )

    outcome = Column(
        String(50),
        nullable=False,
    )

    confidence_change = Column(
        Integer,
        nullable=False,
    )

    timestamp = Column(
        DateTime,
        nullable=False,
        server_default=func.now(),
    )


class CoachDecision(Base):
    """
    Stores AI Coach decisions.

    Keeps an audit trail of:
    - Decision made
    - Reason
    - Confidence
    - Athlete
    """

    __tablename__ = "coach_decisions"

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

    decision = Column(
        String(50),
        nullable=False,
    )

    reason = Column(
        String(500),
        nullable=False,
    )

    confidence = Column(
        Integer,
        nullable=False,
    )

    created_at = Column(
        DateTime,
        nullable=False,
        server_default=func.now(),
    )
