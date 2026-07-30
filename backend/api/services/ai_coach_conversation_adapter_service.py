from api.services.ai_coach_conversation_gateway_service import (
    run_conversation_gateway,
)


def adapt_conversation_request(
    athlete_id: int,
    question: str,
    athlete_profile: dict,
    training_history: list[dict],
    recovery_history: list[dict],
    decision_analysis: dict,
    current_state: dict,
) -> dict:
    """
    Adapt incoming conversation request.

    Converts conversation input into
    AI Coach gateway format.
    """

    return {
        "athlete_id": athlete_id,
        "question": question,
        "athlete_profile": athlete_profile,
        "training_history": training_history,
        "recovery_history": recovery_history,
        "decision_analysis": decision_analysis,
        "current_state": current_state,
    }


def convert_ai_response_to_gateway(
    ai_response: dict,
) -> dict:
    """
    Convert AI engine response into
    gateway compatible format.
    """

    return {
        "coach_message": ai_response.get(
            "coach_message",
            "",
        ),
    }


def run_adapted_conversation(
    athlete_id: int,
    question: str,
    ai_response: dict,
    athlete_profile: dict,
    training_history: list[dict],
    recovery_history: list[dict],
    decision_analysis: dict,
    current_state: dict,
) -> dict:
    """
    Run adapted production conversation.

    Flow:

    Conversation Service
            ↓
    Adapter
            ↓
    Gateway
            ↓
    Full AI Coach Brain
    """

    request = adapt_conversation_request(
        athlete_id=athlete_id,
        question=question,
        athlete_profile=athlete_profile,
        training_history=training_history,
        recovery_history=recovery_history,
        decision_analysis=decision_analysis,
        current_state=current_state,
    )

    gateway_response = (
        convert_ai_response_to_gateway(
            ai_response,
        )
    )

    return run_conversation_gateway(
        athlete_id=request["athlete_id"],
        question=request["question"],
        ai_response=gateway_response,
        athlete_profile=request[
            "athlete_profile"
        ],
        training_history=request[
            "training_history"
        ],
        recovery_history=request[
            "recovery_history"
        ],
        decision_analysis=request[
            "decision_analysis"
        ],
        current_state=request[
            "current_state"
        ],
    )
