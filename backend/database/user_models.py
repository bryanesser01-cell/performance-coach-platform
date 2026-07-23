from sqlalchemy import Column, Integer, String

from database.database import Base


class User(Base):
    """
    User database model.
    """

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

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