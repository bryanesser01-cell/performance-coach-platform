from api.services.ai_coach_api_controller_service import (
    run_api_coach_controller,
)
from api.services.ai_coach_response_formatter_service import (
    format_ai_coach_response,
)


def build_chat_context(
    athlete_id: int,
    question: str,
    athlete_profile: dict,
    training_history: list[dict],
    recovery_history: list[dict],
    decision_analysis: dict,
    current_state: dict,
) -> dict:
    """
    Build AI Coach chat context.
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


def execute_ai_coach_chat(
    context: dict,
    ai_response: dict,
) -> dict:
    """
    Execute AI Coach chat pipeline.
    """

    result = run_api_coach_controller(
        athlete_id=context[
            "athlete_id"
        ],
        question=context[
            "question"
        ],
        ai_response=ai_response,
        athlete_profile=context[
            "athlete_profile"
        ],
        training_history=context[
            "training_history"
        ],
        recovery_history=context[
            "recovery_history"
        ],
        decision_analysis=context[
            "decision_analysis"
        ],
        current_state=context[
            "current_state"
        ],
    )

    return format_ai_coach_response(
    athlete_id=context[
        "athlete_id"
    ],
    question=context[
        "question"
    ],
    coach_response={
        **result,
        **ai_response,
    },
    )


def format_chat_response(
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
    Build final chat response.
    """

    context = build_chat_context(
        athlete_id=athlete_id,
        question=question,
        athlete_profile=athlete_profile,
        training_history=training_history,
        recovery_history=recovery_history,
        decision_analysis=decision_analysis,
        current_state=current_state,
    )

    return execute_ai_coach_chat(
        context=context,
        ai_response=ai_response,
    )
