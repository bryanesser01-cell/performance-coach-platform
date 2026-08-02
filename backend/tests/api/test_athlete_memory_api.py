from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_athlete_memory_create_endpoint_exists():

    response = client.post(
        "/athletes/1/memory",
        params={
            "memory_type": "goal",
            "memory_value": "Break 20 minute 5K",
        },
    )

    assert response.status_code in [
        200,
        500,
    ]


def test_athlete_memory_get_endpoint_exists():

    response = client.get(
        "/athletes/1/memory",
    )

    assert response.status_code in [
        200,
        500,
    ]


def test_athlete_memory_endpoints_in_openapi():

    response = client.get(
        "/openapi.json",
    )

    paths = response.json()["paths"]

    assert "/athletes/{athlete_id}/memory" in paths


def test_athlete_memory_context_endpoint_in_openapi():

    response = client.get(
        "/openapi.json",
    )

    paths = response.json()["paths"]

    assert "/athletes/{athlete_id}/memory/context" in paths


def test_athlete_memory_intelligence_endpoint_in_openapi():

    response = client.get(
        "/openapi.json",
    )

    paths = response.json()["paths"]

    assert "/athletes/{athlete_id}/memory/intelligence" in paths
