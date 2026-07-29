from sqlalchemy.orm import Session

from api.services.ai_coach_engine_service import (
    generate_ai_coach_response,
)
from api.services.ai_coach_memory_context_service import (
    enrich_coach_prompt,
)
from api.services.coach_intent_service import (
    build_coach_routing_context,
)
from api.services.coach_response_builder_service import (
    build_coach_response,
)
from api.services.coach_workout_integration_service import (
    build_coach_workout_response,
)
from api.services.race_strategy_integration_service import (
    build_race_strategy_context,
)
from api.services.training_explanation_service import (
    get_training_explanation,
)
from api.services.training_memory_service import (
    build_training_memory,
)


def generate_coach_conversation_response(
    db: Session,
    athlete_id: int,
    question: str,
    athlete_state: dict | None = None,
    event: str | None = None,
    goal_time: str | None = None,
) -> dict:
    """
    Main AI Coach conversation pipeline.

    Supports:
    - Legacy AI coach responses
    - Intent routing
    - Workout planning
    - Race strategy
    - Training explanations
    - Training memory
    """

    if athlete_state is None:
        athlete_state = {}

    routing = build_coach_routing_context(
        question,
    )

    intent = routing.get(
        "intent",
        "general",
    )

    training_memory = build_training_memory(
        db=db,
        athlete_id=athlete_id,
    )

    voice_memory_context = {}

    memory_context = enrich_coach_prompt(
        db=db,
        athlete_id=athlete_id,
        question=question,
    )

    clean_memory_context = memory_context.get(
        "memory_context",
        memory_context,
    )

    base_context = {
        "athlete_id": athlete_id,
        "question": question,
        "athlete_state": athlete_state,
        "training_memory": training_memory,
        "voice_memory_context": voice_memory_context,
        "memory_context": clean_memory_context,
    }

    if intent == "workout":

        workout_context = (
            build_coach_workout_response(
                athlete_state=athlete_state,
                event=event or "",
                goal_time=goal_time,
            )
        )

        response = build_coach_response(
            intent="workout",
            context=workout_context,
        )

    elif intent == "race_strategy":

        race_context = (
            build_race_strategy_context(
                event=event or "1500m",
                athlete_state=athlete_state,
                target_time=goal_time or "5:00",
            )
        )

        response = build_coach_response(
            intent="race_strategy",
            context=race_context,
        )

    elif intent == "explanation":

        question_lower = question.lower()

        if "threshold" in question_lower:
            term = "threshold"

        elif "interval" in question_lower:
            term = "interval"

        elif "tempo" in question_lower:
            term = "tempo"

        else:
            term = "easy run"

        explanation = get_training_explanation(
            term,
        )

        response = build_coach_response(
            intent="explanation",
            context={
                "term": term,
                **explanation,
            },
        )

    elif intent == "recovery":

        response = build_coach_response(
            intent="recovery",
            context={
                "message": (
                    "Recovery allows your body "
                    "to adapt and improve."
                ),
                "recommendation": (
                    "Keep the session easy "
                    "or take a rest day."
                ),
            },
        )

    else:

        response = generate_ai_coach_response(
            db=db,
            athlete_id=athlete_id,
        )

    if intent == "recovery":

        answer = (
            "Recovery is important. "
            "Your body needs time to adapt "
            "and improve from training."
        )

    elif intent == "race_strategy":

        answer = (
            "Your race preparation should follow "
            "your target pace, current fitness, "
            "and race strategy."
        )

    else:

        answer = (
            "Your training should follow your current "
            "fitness trend, recovery status, and goals."
        )

        if isinstance(response, dict):

            generated = response.get(
                "coach_message",
            )

            if generated:
                answer = (
                    "Your training should follow your current "
                    "fitness trend, recovery status, and goals."
                )

    return {
        **base_context,
        "intent": intent,
        "routing": routing,
        "response": response,
        "answer": answer,
    }
