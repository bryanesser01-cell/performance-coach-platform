from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.sql import func

from database.database import Base


class BaseModel(Base):
    """
    Abstract base model inherited by all database models.
    Provides common fields shared across every table.
    """

    __abstract__ = True

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )
