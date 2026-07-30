from sqlalchemy.orm import Session

from api.services.ai_coach_engine_service import (
    generate_ai_coach_response,
)
from api.services.ai_coach_memory_context_service import (
    enrich_coach_prompt,
)
from api.services.coach_context_aggregator_service import (
    build_coach_context,
    generate_coach_context_summary,
)
from api.services.coach_decision_integration_service import (
    generate_coach_decision_context,
)
from api.services.coach_decision_record_service import (
    record_coach_decision,
)
from api.services.coach_intent_service import (
    build_coach_routing_context,
)
from api.services.coach_learning_memory_service import (
    get_learning_context,
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
    activities: list[dict] | None = None,
    recovery_data: dict | None = None,
) -> dict:

    if athlete_state is None:
        athlete_state = {}

    if activities is None:
        activities = []

    if recovery_data is None:
        recovery_data = {
            "readiness_score": 0,
        }

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

    learning_memory = get_learning_context(
        db=db,
        athlete_id=athlete_id,
    )

    memory_context = enrich_coach_prompt(
        db=db,
        athlete_id=athlete_id,
        question=question,
    )

    clean_memory_context = memory_context.get(
        "memory_context",
        memory_context,
    )

    adaptive_context = (
        generate_coach_decision_context(
            athlete_state,
        )
    )

    decision = adaptive_context.get(
        "coach_decision",
        {},
    )

    if decision.get("decision"):

        record_coach_decision(
            db=db,
            athlete_id=athlete_id,
            decision=decision.get(
                "decision",
                "",
            ),
            reason=decision.get(
                "reason",
                "",
            ),
            confidence=adaptive_context.get(
                "learning_confidence",
                50,
            ),
        )

    coach_context = build_coach_context(
        athlete_id=athlete_id,
        athlete_state=athlete_state,
        training_memory=training_memory,
        learning_memory=learning_memory,
        activities=activities,
        recovery_data=recovery_data,
    )

    coach_context_summary = (
        generate_coach_context_summary(
            coach_context,
        )
    )

    base_context = {
        "athlete_id": athlete_id,
        "question": question,
        "athlete_state": athlete_state,
        "training_memory": training_memory,
        "learning_memory": learning_memory,
        "memory_context": clean_memory_context,
        "coach_decision_context": adaptive_context,
        "coach_context": coach_context,
        "coach_context_summary": coach_context_summary,
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

    elif intent == "adaptive_coaching":

        from api.services.coach_learning_explanation_service import (
            build_athlete_friendly_message,
            build_learning_explanation,
        )

        confidence = adaptive_context.get(
            "learning_confidence",
            learning_memory.get(
                "confidence_adjustment",
                50,
            ),
        )

        explanation = build_learning_explanation(
            decision=decision.get(
                "decision",
                "",
            ),
            confidence=confidence,
            reason=decision.get(
                "reason",
                "",
            ),
            learning_history=learning_memory.get(
                "learning_events",
                [],
            ),
        )

        coach_message = (
            build_athlete_friendly_message(
                explanation,
            )
        )

        response = {
            "coach_message": coach_message,
            "decision": decision.get(
                "decision",
                "",
            ),
            "reason": decision.get(
                "reason",
                "",
            ),
            "confidence": confidence,
            "explanation": explanation,
            "coach_context_summary": coach_context_summary,
        }

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
                "coach_context_summary": (
                    coach_context_summary
                ),
            },
        )

    else:

        response = generate_ai_coach_response(
            db=db,
            athlete_id=athlete_id,
        )

    if intent == "adaptive_coaching":

        answer = response.get(
            "coach_message",
            "Your training has been adjusted.",
        )

    elif intent == "recovery":

        answer = (
            "Recovery is important. "
            "Your readiness and training load "
            "guide today's recommendation."
        )

    elif intent == "race_strategy":

        answer = (
            "Your race preparation should follow "
            "your target pace, fitness and strategy."
        )

    else:

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
