from fastapi import FastAPI
from fastapi.testclient import TestClient

from api.routes.ai_coach_routes import router

app = FastAPI()

app.include_router(router)

client = TestClient(app)


def test_ai_coach_conversation_standard_contract():

    response = client.post(
        "/ai-coach/conversation",
        json={
            "athlete_id": 1,
            "question": (
                "Should I train today?"
            ),
            "ai_response": {
                "coach_message": (
                    "Recover today."
                ),
                "decision": (
                    "REDUCE_TRAINING"
                ),
                "recommendation": (
                    "Easy recovery run."
                ),
                "confidence": 90,
                "memory_used": True,
                "learning_updated": True,
                "strategy": (
                    "RECOVERY_FIRST"
                ),
            },
            "decision_analysis": {
                "REDUCE_TRAINING": {
                    "success_rate": 90,
                },
            },
            "current_state": {
                "readiness_score": 60,
            },
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
    "coach_message"
    in body
    )


def test_ai_coach_response_contains_required_fields():

    response = client.post(
        "/ai-coach/conversation",
        json={
            "athlete_id": 1,
            "question": (
                "Should I run?"
            ),
            "ai_response": {
                "coach_message": (
                    "Run easy today."
                ),
            },
        },
    )

    assert (
        response.status_code
        == 200
    )

    data = response.json()

    required_fields = [
        "success",
        "coach_message",
        "confidence",
        "memory_used",
        "learning_updated",
    ]

    for field in required_fields:
        assert field in data


def test_ai_coach_health_contract():

    response = client.get(
        "/ai-coach/health"
    )

    assert (
        response.status_code
        == 200
    )

    body = response.json()

    assert (
        body["status"]
        == "healthy"
    )
