from sqlalchemy import Column, Date, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship

from database.base_model import BaseModel


class Goal(BaseModel):
    __tablename__ = "goals"

    athlete_id = Column(
        Integer,
        ForeignKey("athletes.id"),
        nullable=False,
        index=True,
    )

    target_distance = Column(
        Float,
        nullable=False,
    )

    target_time_minutes = Column(
        Float,
        nullable=False,
    )

    target_date = Column(
        Date,
        nullable=False,
    )

    athlete = relationship(
        "Athlete",
        back_populates="goals",
    )
