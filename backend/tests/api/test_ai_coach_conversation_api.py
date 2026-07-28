from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_ai_coach_chat_endpoint_exists():

    response = client.post(
        "/athletes/1/ai-coach/chat",
        params={
            "question": "Should I train today?",
        },
    )

    assert response.status_code in [
        200,
        500,
    ]


def test_ai_coach_chat_endpoint_in_openapi():

    response = client.get(
        "/openapi.json",
    )

    paths = response.json()["paths"]

    assert (
        "/athletes/{athlete_id}/ai-coach/chat"
        in paths
    )
