from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_ai_coach_endpoint_exists():

    response = client.get(
        "/athletes/1/ai-coach",
    )

    assert response.status_code in [
        200,
        500,
    ]


def test_ai_coach_endpoint_path():

    response = client.get(
        "/openapi.json",
    )

    paths = response.json()["paths"]

    assert "/athletes/{athlete_id}/ai-coach" in paths
