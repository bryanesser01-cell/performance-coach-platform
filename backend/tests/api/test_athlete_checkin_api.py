from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_checkin_endpoint_exists():

    response = client.post(
        "/athletes/1/checkin",
        params={
            "energy": 8,
            "sleep_quality": 8,
            "soreness": 2,
            "motivation": 9,
        },
    )

    assert response.status_code == 200


def test_checkin_contains_readiness_score():

    response = client.post(
        "/athletes/1/checkin",
        params={
            "energy": 8,
            "sleep_quality": 8,
            "soreness": 2,
            "motivation": 9,
        },
    )

    data = response.json()

    assert "readiness_score" in data


def test_checkin_endpoint_in_openapi():

    response = client.get(
        "/openapi.json",
    )

    paths = response.json()["paths"]

    assert "/athletes/{athlete_id}/checkin" in paths
