from sqlalchemy import Column, Float, Integer, String

from database.database import Base


class Goal(Base):
    __tablename__ = "goals"

    id = Column(Integer, primary_key=True, index=True)

    athlete_id = Column(Integer, nullable=False, index=True)

    goal_type = Column(String(50), nullable=False)

    target_value = Column(Float, nullable=False)

    target_unit = Column(String(20), nullable=False)

    current_value = Column(Float, nullable=False)

    status = Column(
        String(20),
        nullable=False,
        default="Active",
    )