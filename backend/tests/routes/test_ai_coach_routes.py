from fastapi import FastAPI
from fastapi.testclient import TestClient

from api.routes.ai_coach_routes import router

app = FastAPI()

app.include_router(
    router,
)


client = TestClient(
    app,
)


def test_ai_coach_health():

    response = client.get(
        "/ai-coach/health",
    )

    assert (
        response.status_code
        == 200
    )

    assert (
        response.json()["status"]
        == "healthy"
    )


def test_ai_coach_conversation():

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
            },
            "athlete_profile": {
                "sport": "running",
            },
            "training_history": [],
            "recovery_history": [],
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


def test_ai_coach_conversation_contains_strategy():

    response = client.post(
        "/ai-coach/conversation",
        json={
            "athlete_id": 1,
            "question": (
                "Should I reduce training?"
            ),
            "ai_response": {
                "coach_message": (
                    "Reduce load."
                ),
            },
            "decision_analysis": {
                "REDUCE_TRAINING": {
                    "success_rate": 85,
                },
            },
            "current_state": {
                "readiness_score": 50,
            },
        },
    )

    result = response.json()

    assert (
    result["strategy"]
    == "RECOVERY_FIRST"
    )


def test_health_response_structure():

    response = client.get(
        "/ai-coach/health",
    )

    result = response.json()

    assert (
        "service"
        in result
    )

    assert (
        result["service"]
        == "ai-coach"
    )
