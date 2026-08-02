from api.services.athlete_state_builder_service import (
    build_athlete_state,
)


def test_build_athlete_state():

    state = build_athlete_state(
        readiness={
            "score": 85,
        },
        training={
            "load_status": "stable",
        },
        performance={
            "trend": "improving",
        },
        memory_context={
            "goal": [
                "sub 20 minute 5K",
            ],
        },
    )

    assert state["state_ready"] is True

    assert state["readiness"]["score"] == 85

    assert "goal" in state["memory"]
