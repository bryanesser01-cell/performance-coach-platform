from unittest.mock import patch
from uuid import uuid4

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_import_activity_from_garmin():
    with patch(
        "api.routers.activity.ingest_activity",
        return_value={
            "id": 1,
            "name": "Morning Run",
            "source": "garmin",
        },
    ):
        response = client.post(
            "/activities/import",
            json={
                "source": "garmin",
                "activity_id": "garmin-123",
                "athlete_id": str(uuid4()),
                "activity_name": "Morning Run",
                "start_time": "2026-07-28T06:00:00+00:00",
                "distance": 5000,
                "duration": 1800,
            },
        )

    assert response.status_code == 200

    data = response.json()

    assert data["source"] == "garmin"


def test_import_activity_from_strava():
    with patch(
        "api.routers.activity.ingest_activity",
        return_value={
            "id": 2,
            "name": "Tempo Run",
            "source": "strava",
        },
    ):
        response = client.post(
            "/activities/import",
            json={
                "source": "strava",
                "activity_id": "strava-123",
                "athlete_id": str(uuid4()),
                "activity_name": "Tempo Run",
                "start_time": "2026-07-28T06:00:00+00:00",
                "distance": 8000,
                "duration": 2400,
            },
        )

    assert response.status_code == 200

    data = response.json()

    assert data["source"] == "strava"
