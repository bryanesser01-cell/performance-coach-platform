from api.services.athlete_state_service import (
    build_athlete_state,
    generate_athlete_state_summary,
)


def test_build_athlete_state():

    state = build_athlete_state(
        athlete={
            "id": 1,
            "name": "Bryan",
            "sport": "running",
            "primary_event": "5K",
        },
        goal={
            "target": "Sub 20 minute 5K",
            "status": "active",
        },
        readiness={
            "score": 85,
            "status": "ready",
        },
        training={
            "load_status": "optimal",
            "weekly_distance": 35,
        },
        performance={
            "trend": "improving",
            "current_metric": "21:30 5K",
        },
    )

    assert state["athlete"]["name"] == "Bryan"

    assert state["goal"]["target"] == "Sub 20 minute 5K"

    assert state["readiness"]["score"] == 85


def test_athlete_state_contains_training_data():

    state = build_athlete_state(
        athlete={
            "id": 1,
            "name": "Runner",
        },
        training={
            "load_status": "high",
            "weekly_distance": 50,
        },
    )

    assert state["training"]["load_status"] == "high"

    assert state["training"]["weekly_distance"] == 50


def test_generate_athlete_state_summary():

    state = build_athlete_state(
        athlete={
            "id": 1,
            "name": "Bryan",
            "primary_event": "5K",
        },
        readiness={
            "score": 90,
        },
        performance={
            "trend": "improving",
        },
    )

    summary = generate_athlete_state_summary(
        state,
    )

    assert "Bryan" in summary

    assert "improving" in summary
