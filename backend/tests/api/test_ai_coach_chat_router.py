from fastapi import FastAPI
from fastapi.testclient import TestClient

from api.routers.ai_coach_chat_router import (
    router,
)

app = FastAPI()

app.include_router(router)

client = TestClient(app)


def test_ai_coach_chat_endpoint():

    response = client.post(
        "/athletes/1/ai-coach/chat",
        json={
            "question": (
                "Should I train today?"
            ),
            "ai_response": {
                "coach_message": (
                    "Recover today."
                ),
                "confidence": 90,
                "memory_used": True,
            },
            "athlete_profile": {
                "sport": "running",
            },
            "training_history": [],
            "recovery_history": [],
            "decision_analysis": {},
            "current_state": {},
        },
    )

    assert (
        response.status_code
        == 200
    )

    body = response.json()

    assert (
        body["success"]
        is True
    )

    assert (
        body["athlete_id"]
        == 1
    )


def test_ai_coach_chat_contract():

    response = client.post(
        "/athletes/5/ai-coach/chat",
        json={
            "question": (
                "How should I train?"
            ),
            "ai_response": {
                "coach_message": (
                    "Complete an easy session."
                ),
                "confidence": 80,
            },
        },
    )

    assert (
        response.status_code
        == 200
    )

    body = response.json()

    required_fields = [
        "success",
        "coach_message",
        "confidence",
        "memory_used",
        "learning_updated",
    ]

    for field in required_fields:
        assert field in body
