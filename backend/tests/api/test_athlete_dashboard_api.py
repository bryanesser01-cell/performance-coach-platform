from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_dashboard_endpoint_path():

    response = client.get(
        "/openapi.json",
    )

    paths = response.json()["paths"]

    assert "/athletes/{athlete_id}/dashboard" in paths


def test_dashboard_intelligence_endpoint_path():

    response = client.get(
        "/openapi.json",
    )

    paths = response.json()["paths"]

    assert "/athletes/{athlete_id}/intelligence" in paths
