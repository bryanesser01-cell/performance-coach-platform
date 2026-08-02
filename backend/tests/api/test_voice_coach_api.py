from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_voice_coach_endpoint_exists():

    response = client.post(
        "/voice-coach/chat",
        params={
            "athlete_id": 1,
            "voice_text": ("Should I train today?"),
        },
    )

    assert response.status_code != 404
