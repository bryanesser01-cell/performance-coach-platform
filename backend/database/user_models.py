from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from database.base_model import BaseModel


class User(BaseModel):
    """
    Application user.

    A user can own one or more athlete profiles.
    Authentication credentials are stored here.
    """

    __tablename__ = "users"

    email = Column(
        String(255),
        unique=True,
        nullable=False,
        index=True,
    )

    full_name = Column(
        String(100),
        nullable=False,
    )

    password_hash = Column(
        String(255),
        nullable=False,
    )

    # -------------------------
    # Relationships
    # -------------------------

    athletes = relationship(
        "Athlete",
        back_populates="user",
        cascade="all, delete-orphan",
    )
