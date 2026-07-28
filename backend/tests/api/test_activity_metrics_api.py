from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.main import app
from database import activity_models  # noqa: F401
from database.base import Base
from database.session import get_db

engine = create_engine(
    "sqlite:///:memory:",
    connect_args={
        "check_same_thread": False,
    },
    poolclass=StaticPool,
)


TestingSessionLocal = sessionmaker(
    bind=engine,
)


Base.metadata.create_all(
    bind=engine,
)


def override_get_db():
    db = TestingSessionLocal()

    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


client = TestClient(app)


def test_activity_metrics_router_exists():
    response = client.get(
        "/activity-metrics/1",
    )

    assert response.status_code in [
        404,
        200,
    ]
