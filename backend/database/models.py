from sqlalchemy import Column, Integer, String, Float

from database.database import Base


class Athlete(Base):
    __tablename__ = "athletes"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)

    height_cm = Column(Float, nullable=False)
    weight_kg = Column(Float, nullable=False)

    resting_hr = Column(Integer, nullable=False)
    max_hr = Column(Integer, nullable=False)

    sport = Column(String, nullable=False)
    primary_event = Column(String, nullable=False)

    experience_level = Column(String)
    weekly_distance = Column(Float)
    training_days_per_week = Column(Integer)
    current_5k_time = Column(Float)
    injury_status = Column(String)


class Goal(Base):
    __tablename__ = "goals"

    id = Column(Integer, primary_key=True, index=True)

    athlete_id = Column(Integer, nullable=False)

    goal_type = Column(String, nullable=False)

    target_value = Column(Float, nullable=False)

    target_unit = Column(String, nullable=False)

    current_value = Column(Float, nullable=False)

    status = Column(String, default="Active")