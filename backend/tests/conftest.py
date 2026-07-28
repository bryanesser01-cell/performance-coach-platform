import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database import (
    activity_models,  # noqa: F401
    models,  # noqa: F401
    training_models,  # noqa: F401
)
from database.base import Base


@pytest.fixture
def db_session():
    """
    Create an in-memory SQLite database session for tests.
    """

    engine = create_engine(
        "sqlite:///:memory:",
    )

    Base.metadata.create_all(
        bind=engine,
    )

    session_factory = sessionmaker(
        bind=engine,
    )

    session = session_factory()

    try:
        yield session
    finally:
        session.close()
