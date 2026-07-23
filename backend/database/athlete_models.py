from sqlalchemy import (
    Column,
    Date,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database.database import Base


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

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
        index=True,
    )

    first_name = Column(
        String(100),
        nullable=False,
    )

    last_name = Column(
        String(100),
        nullable=False,
    )

    date_of_birth = Column(
        Date,
        nullable=True,
    )

    sex = Column(
        String(20),
        nullable=True,
    )

    height_cm = Column(
        Float,
        nullable=True,
    )

    weight_kg = Column(
        Float,
        nullable=True,
    )

    ftp = Column(
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

    resting_hr = Column(
        Integer,
        nullable=True,
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

    user = relationship(
        "User",
        back_populates="athletes",
    )