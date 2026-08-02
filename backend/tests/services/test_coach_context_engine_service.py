from api.services.coach_context_engine_service import (
    build_coach_context,
    generate_coach_summary,
)


def test_build_coach_context_contains_athlete_state():

    context = build_coach_context(
        athlete_id=1,
        goal="Run sub 20 minute 5K",
        readiness_score=85,
        training_load_status="stable",
        performance_trend="improving",
        memories=[
            "Prefers morning sessions",
        ],
    )

    assert context["athlete_id"] == 1

    assert context["goal"] == "Run sub 20 minute 5K"

    assert context["memories"][0] == "Prefers morning sessions"


def test_context_generates_progression_decision():

    context = build_coach_context(
        athlete_id=1,
        goal="Improve 5K time",
        readiness_score=90,
        training_load_status="stable",
        performance_trend="improving",
    )

    assert context["decision"]["decision"] == "PROGRESS_TRAINING"


def test_context_detects_recovery_need():

    context = build_coach_context(
        athlete_id=1,
        goal="Prepare for race",
        readiness_score=45,
        training_load_status="high_fatigue",
        performance_trend="declining",
    )

    assert context["decision"]["decision"] == "REDUCE_TRAINING"


def test_generate_coach_summary():

    context = build_coach_context(
        athlete_id=1,
        goal="Run sub 20 minute 5K",
        readiness_score=80,
        training_load_status="stable",
        performance_trend="stable",
    )

    summary = generate_coach_summary(
        context,
    )

    assert "Run sub 20 minute 5K" in summary
