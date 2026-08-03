from collections.abc import Generator

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from database.base import Base

TEST_DATABASE_URL = "sqlite:///:memory:"


engine = create_engine(
    TEST_DATABASE_URL,
)


TestingSessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)


@pytest.fixture
def db_session() -> Generator[Session, None, None]:
    """
    Creates an isolated in-memory database for each test.

    Every repository test receives a fresh SQLAlchemy
    session with all tables created before the test and
    dropped afterwards.
    """

    Base.metadata.create_all(
        bind=engine,
    )

    session = TestingSessionLocal()

    try:
        yield session

    finally:
        session.close()

        Base.metadata.drop_all(
            bind=engine,
        )
