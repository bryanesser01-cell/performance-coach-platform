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