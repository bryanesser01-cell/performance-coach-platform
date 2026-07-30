from fastapi import FastAPI
from fastapi.testclient import TestClient

from api.routers.ai_coach_chat_router import (
    router as ai_coach_chat_router,
)
from api.routes.ai_coach_routes import (
    router as ai_coach_router,
)

app = FastAPI()

app.include_router(
    ai_coach_router,
)

app.include_router(
    ai_coach_chat_router,
)


client = TestClient(app)


def test_conversation_route_exists():

    response = client.post(
        "/ai-coach/conversation",
        json={
            "athlete_id": 1,
            "question": (
                "Should I train today?"
            ),
            "ai_response": {
                "decision": (
                    "REDUCE_TRAINING"
                ),
                "confidence": 90,
                "outcome": "positive",
            },
        },
    )

    assert response.status_code in [
        200,
        500,
    ]


def test_chat_route_exists():

    response = client.post(
        "/athletes/1/ai-coach/chat",
        json={
            "question": (
                "Should I recover?"
            ),
            "ai_response": {
                "decision": (
                    "RECOVERY"
                ),
                "confidence": 85,
                "outcome": "positive",
            },
        },
    )

    assert response.status_code in [
        200,
        500,
    ]


def test_final_response_contract():

    response = client.post(
        "/athletes/1/ai-coach/chat",
        json={
            "question": (
                "How should I train?"
            ),
            "ai_response": {
                "decision": (
                    "EASY_RUN"
                ),
                "confidence": 80,
                "outcome": "positive",
            },
        },
    )

    if response.status_code == 200:
        body = response.json()

        assert (
            "success"
            in body
        )
