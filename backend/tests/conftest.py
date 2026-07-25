from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from app.main import app
from database.database import Base, get_db
from tests.testing_database import (
    TestingSessionLocal,
    get_test_db,
    test_engine,
)


@pytest.fixture(scope="session", autouse=True)
def setup_database():
    """
    Create a fresh test database before the test session
    and remove it after all tests complete.
    """
    test_db = Path("test_performance_coach.db")

    if test_db.exists():
        test_db.unlink()

    Base.metadata.create_all(bind=test_engine)

    yield

    Base.metadata.drop_all(bind=test_engine)


@pytest.fixture(scope="session")
def test_app():
    """
    Configure the FastAPI application for testing.
    """
    app.dependency_overrides[get_db] = get_test_db

    yield app

    app.dependency_overrides.clear()


@pytest.fixture
def client(test_app):
    """
    Return a FastAPI TestClient.
    """
    with TestClient(test_app) as client:
        yield client


@pytest.fixture(autouse=True)
def clean_database():
    """
    Remove all data before each test.
    """
    db = TestingSessionLocal()

    try:
        for table in reversed(Base.metadata.sorted_tables):
            db.execute(table.delete())

        db.commit()

        yield

    finally:
        db.close()


@pytest.fixture
def db_session():
    """
    Provide a database session for repository tests.
    """
    db = TestingSessionLocal()

    try:
        yield db
    finally:
        db.close()
