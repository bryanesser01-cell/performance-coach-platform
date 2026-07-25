from sqlalchemy import Column, Date, Enum, ForeignKey, String
from sqlalchemy.orm import relationship

from database.base_model import BaseModel
from database.enums import PerformanceCycleStatus


class PerformanceCycle(BaseModel):
    """
    Represents a performance training cycle for an athlete.
    """

    __tablename__ = "performance_cycles"

    athlete_id = Column(
        ForeignKey("athletes.id"),
        nullable=False,
        index=True,
    )

    title = Column(
        String(100),
        nullable=False,
    )

    start_date = Column(
        Date,
        nullable=False,
    )

    end_date = Column(
        Date,
        nullable=False,
    )

    status = Column(
        Enum(
            PerformanceCycleStatus,
            name="performance_cycle_status",
        ),
        nullable=False,
        default=PerformanceCycleStatus.PLANNED,
    )

    athlete = relationship(
        "Athlete",
        back_populates="performance_cycles",
    )
