from sqlalchemy import (
    Column,
    Float,
    ForeignKey,
    Integer,
    String,
)

from database.base import Base


class TrainingSession(Base):
    __tablename__ = "training_sessions"

    id = Column(Integer, primary_key=True, index=True)

    athlete_id = Column(
        Integer,
        ForeignKey("athletes.id"),
        nullable=False,
    )

    date = Column(String, nullable=False)

    session_type = Column(String, nullable=False)

    distance = Column(Float, nullable=False)

    duration = Column(Float, nullable=False)

    average_pace = Column(Float, nullable=False)

    average_hr = Column(Integer)

    max_hr = Column(Integer)

    cadence = Column(Integer)

    elevation_gain = Column(Float)

    training_load = Column(Float)

    rpe = Column(Integer)

    notes = Column(String)
