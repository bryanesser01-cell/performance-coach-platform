from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_progress_timeline_endpoint_exists():

    response = client.get(
        "/athletes/1/progress-timeline",
    )

    assert response.status_code == 200

    assert response.json()["athlete_id"] == 1
