from api.services.ai_coach_decision_service import (
    generate_ai_coach_decision_response,
)


def test_ai_coach_recommends_recovery_when_fatigued():

    result = generate_ai_coach_decision_response(
        athlete_id=1,
        question="Should I do intervals today?",
        readiness_score=45,
        training_load_status="high_fatigue",
        performance_trend="declining",
    )

    assert result["decision"] == "REDUCE_TRAINING"

    assert "recovery" in result["recommendation"]


def test_ai_coach_progresses_when_ready():

    result = generate_ai_coach_decision_response(
        athlete_id=1,
        question="Can I increase training?",
        readiness_score=90,
        training_load_status="stable",
        performance_trend="improving",
    )

    assert result["decision"] == "PROGRESS_TRAINING"


def test_ai_coach_tapers_before_race():

    result = generate_ai_coach_decision_response(
        athlete_id=1,
        question="How should I prepare?",
        readiness_score=90,
        training_load_status="stable",
        performance_trend="improving",
        days_to_race=7,
    )

    assert result["decision"] == "RACE_TAPER"


def test_ai_coach_message_contains_question():

    result = generate_ai_coach_decision_response(
        athlete_id=1,
        question="Should I run today?",
        readiness_score=75,
        training_load_status="stable",
        performance_trend="stable",
    )

    assert "Should I run today?" in result["coach_message"]
