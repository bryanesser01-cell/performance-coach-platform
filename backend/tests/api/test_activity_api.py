from unittest.mock import patch

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_ai_coach_existing_endpoint():

    with patch(
        "api.routers.ai_coach.generate_ai_coach_response",
    ) as mock_response:

        mock_response.return_value = {
            "athlete_id": 1,
            "coach_message": ("Continue current training."),
        }

        response = client.get(
            "/athletes/1/ai-coach",
        )

    assert response.status_code == 200

    data = response.json()

    assert data["athlete_id"] == 1


def test_ai_coach_orchestrator_endpoint():

    with patch(
        "api.routers.ai_coach.run_ai_coach_orchestrator",
    ) as mock_orchestrator:

        mock_orchestrator.return_value = {
            "athlete_id": 1,
            "decision": {
                "decision": "PROGRESS_TRAINING",
            },
            "ai_coach": True,
        }

        response = client.get(
            "/athletes/1/coach",
        )

    assert response.status_code == 200

    data = response.json()

    assert data["athlete_id"] == 1

    assert data["decision"]["decision"] == "PROGRESS_TRAINING"

    assert data["ai_coach"] is True


def test_ai_coach_endpoints_in_openapi():

    response = client.get(
        "/openapi.json",
    )

    paths = response.json()["paths"]

    assert "/athletes/{athlete_id}/ai-coach" in paths

    assert "/athletes/{athlete_id}/coach" in paths
