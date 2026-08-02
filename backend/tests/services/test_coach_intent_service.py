from api.services.coach_intent_service import (
    build_coach_routing_context,
    detect_coach_intent,
    get_coach_service_for_intent,
)


def test_detect_workout_intent():

    intent = detect_coach_intent("What should I do tomorrow?")

    assert intent == "workout"


def test_detect_race_strategy_intent():

    intent = detect_coach_intent("How should I run my 1500m race?")

    assert intent == "race_strategy"


def test_detect_training_explanation_intent():

    intent = detect_coach_intent("What does threshold mean?")

    assert intent == "explanation"


def test_detect_recovery_intent():

    intent = detect_coach_intent("Should I recover today?")

    assert intent == "recovery"


def test_service_mapping():

    service = get_coach_service_for_intent(
        "workout",
    )

    assert service == "coach_workout_integration"


def test_build_routing_context():

    context = build_coach_routing_context("What workout should I do next?")

    assert context["intent"] == "workout"

    assert context["service"] == "coach_workout_integration"
