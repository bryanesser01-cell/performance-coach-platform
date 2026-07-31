from api.models.coach_context import CoachContext


def test_create_empty_context():

    context = CoachContext(
        athlete_id=1,
    )

    assert context.athlete_id == 1

    assert context.athlete_state == {}

    assert context.memory_context == {}

    assert context.decision == {}


def test_context_stores_values():

    context = CoachContext(
        athlete_id=7,
        athlete_state={
            "readiness": {
                "score": 82,
            }
        },
        decision={
            "decision": "PROGRESS_TRAINING",
        },
    )

    assert (
        context.athlete_state["readiness"]["score"]
        == 82
    )

    assert (
        context.decision["decision"]
        == "PROGRESS_TRAINING"
    )
