def detect_coach_intent(
    question: str,
) -> str:
    """
    Determine what the athlete is asking.

    Possible intents:
    - workout
    - race_strategy
    - adaptive_coaching
    - explanation
    - recovery
    - readiness
    - general
    """

    question_lower = question.lower()

    adaptive_keywords = [
        "why did you change",
        "why did you reduce",
        "why did you adjust",
        "why did you modify",
        "why is my training different",
        "why was my workout changed",
        "why was my training changed",
        "training changed",
        "workout changed",
        "adjust my training",
        "change my training",
        "am i ready for my race",
        "am i ready",
        "race ready",
        "ready for my race",
    ]

    workout_keywords = [
        "workout",
        "train",
        "training",
        "session",
        "tomorrow",
        "next run",
        "what should i do",
        "what do i do",
    ]

    race_keywords = [
        "race",
        "pace",
        "split",
        "1500",
        "800",
        "5k",
        "10k",
        "marathon",
    ]

    explanation_keywords = [
        "why",
        "what does",
        "what is",
        "explain",
        "mean",
        "how hard",
        "how fast",
    ]

    recovery_keywords = [
        "recover",
        "recovery",
        "rest",
        "tired",
        "fatigue",
        "sore",
    ]

    readiness_keywords = [
        "ready",
        "readiness",
        "should i train",
        "can i train",
        "am i okay",
    ]

    # Adaptive coaching must be checked first.
    if any(word in question_lower for word in adaptive_keywords):
        return "adaptive_coaching"

    if any(word in question_lower for word in recovery_keywords):
        return "recovery"

    if any(word in question_lower for word in readiness_keywords):
        return "readiness"

    if any(word in question_lower for word in explanation_keywords):
        return "explanation"

    if any(word in question_lower for word in race_keywords):
        return "race_strategy"

    if any(word in question_lower for word in workout_keywords):
        return "workout"

    return "general"


def get_coach_service_for_intent(
    intent: str,
) -> str:
    """
    Map intent to coaching engine.
    """

    services = {
        "workout": ("coach_workout_integration"),
        "race_strategy": ("race_strategy_integration"),
        "adaptive_coaching": ("coach_decision_integration"),
        "explanation": ("training_explanation"),
        "recovery": ("recovery_analysis"),
        "readiness": ("athlete_state"),
        "general": ("ai_coach"),
    }

    return services.get(
        intent,
        "ai_coach",
    )


def build_coach_routing_context(
    question: str,
) -> dict:
    """
    Build routing decision
    for AI Coach.
    """

    intent = detect_coach_intent(
        question,
    )

    return {
        "question": question,
        "intent": intent,
        "service": (
            get_coach_service_for_intent(
                intent,
            )
        ),
    }
