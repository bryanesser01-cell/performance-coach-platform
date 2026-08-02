from api.services.coach_intent_service import (
    build_coach_routing_context,
)


def test_adaptive_coaching_intent_detects_training_change_question():

    result = build_coach_routing_context("Why did you reduce my training?")

    assert result["intent"] == "adaptive_coaching"


def test_adaptive_coaching_intent_detects_readiness_question():

    result = build_coach_routing_context("Am I ready for my race?")

    assert result["intent"] == "adaptive_coaching"


def test_existing_explanation_intent_still_works():

    result = build_coach_routing_context("Explain threshold training")

    assert result["intent"] == "explanation"
