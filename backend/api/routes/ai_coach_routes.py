from fastapi import APIRouter

from api.services.ai_coach_api_controller_service import (
    run_api_coach_controller,
)
from api.services.ai_coach_response_formatter_service import (
    format_ai_coach_response,
)

router = APIRouter(
    prefix="/ai-coach",
    tags=[
        "AI Coach",
    ],
)


@router.get("/health")
def get_ai_coach_health():
    """
    AI Coach service health check.
    """

    return {
        "status": "healthy",
        "service": "ai-coach",
    }


@router.post("/conversation")
def post_ai_coach_conversation(
    payload: dict,
):
    """
    Main AI Coach conversation endpoint.

    Flow:

    Client
      ↓
    FastAPI Route
      ↓
    AI Coach Controller
      ↓
    AI Coach Brain
      ↓
    Response
    """

    result = run_api_coach_controller(
        athlete_id=payload.get(
            "athlete_id",
            1,
        ),
        question=payload.get(
            "question",
            "",
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

    formatted_response = format_ai_coach_response(
        athlete_id=payload.get(
            "athlete_id",
            1,
        ),
        question=payload.get(
            "question",
            "",
        ),
        coach_response=result,
    )

    return formatted_response
