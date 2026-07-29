from api.services.athlete_context_service import (
    build_athlete_context,
    generate_context_summary,
)


def test_build_athlete_context():

    context = build_athlete_context(
        athlete_id=1,
        athlete_profile={
            "name": "Bryan",
            "sport": "running",
            "primary_event": "5K",
            "goal": "Sub 20 minute 5K",
        },
        training_state={
            "readiness_score": 85,
            "training_load_status": "stable",
            "performance_trend": "improving",
        },
        memories=[
            "Prefers morning sessions",
        ],
    )

    assert (
        context["athlete"]["id"]
        == 1
    )

    assert (
        context["goal"]
        == "Sub 20 minute 5K"
    )

    assert (
        context["memories"][0]
        == "Prefers morning sessions"
    )


def test_context_generates_training_decision():

    context = build_athlete_context(
        athlete_id=1,
        athlete_profile={
            "name": "Bryan",
            "goal": "Improve 5K",
        },
        training_state={
            "readiness_score": 90,
            "training_load_status": "stable",
            "performance_trend": "improving",
        },
    )

    assert (
        context["decision"]["decision"]
        == "PROGRESS_TRAINING"
    )


def test_context_detects_fatigue():

    context = build_athlete_context(
        athlete_id=1,
        athlete_profile={
            "name": "Bryan",
            "goal": "Race preparation",
        },
        training_state={
            "readiness_score": 45,
            "training_load_status": "high_fatigue",
            "performance_trend": "declining",
        },
    )

    assert (
        context["decision"]["decision"]
        == "REDUCE_TRAINING"
    )


def test_generate_context_summary():

    context = build_athlete_context(
        athlete_id=1,
        athlete_profile={
            "name": "Bryan",
            "goal": "Sub 20 minute 5K",
        },
        training_state={
            "readiness_score": 80,
            "training_load_status": "stable",
            "performance_trend": "stable",
        },
    )

    summary = generate_context_summary(
        context,
    )

    assert (
        "Bryan"
        in summary
    )

    assert (
        "Sub 20 minute 5K"
        in summary
    )
