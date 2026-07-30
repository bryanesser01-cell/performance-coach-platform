from fastapi import APIRouter

from api.services.ai_coach_chat_service import (
    format_chat_response,
)

router = APIRouter(
    prefix="/athletes",
    tags=[
        "AI Coach Conversation",
    ],
)


@router.post("/{athlete_id}/ai-coach/chat")
def post_ai_coach_chat(
    athlete_id: int,
    payload: dict | None = None,
    question: str = "",
):
    """
    AI Coach athlete chat endpoint.

    Supports:

    JSON body:
    {
        "question": "Should I train today?"
    }

    OR query parameter:

    /athletes/1/ai-coach/chat?question=Should%20I%20train%20today

    Flow:

    Athlete
       ↓
    Chat Router
       ↓
    AI Coach Chat Service
       ↓
    AI Coach Controller
       ↓
    AI Coach Brain
       ↓
    Response Formatter
       ↓
    Standard Response
    """

    if payload is None:
        payload = {
            "question": question,
            "ai_response": {
                "coach_message": "",
            },
        }

    response = format_chat_response(
        athlete_id=athlete_id,
        question=payload.get(
            "question",
            question,
        ),
        ai_response=payload.get(
            "ai_response",
            {
                "coach_message": "",
            },
        ),
        athlete_profile=payload.get(
            "athlete_profile",
            {},
        ),
        training_history=payload.get(
            "training_history",
            [],
        ),
        recovery_history=payload.get(
            "recovery_history",
            [],
        ),
        decision_analysis=payload.get(
            "decision_analysis",
            {},
        ),
        current_state=payload.get(
            "current_state",
            {},
        ),
    )

    return response
