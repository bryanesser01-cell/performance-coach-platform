from api.services.coach_decision_explanation_service import (
    build_short_coach_explanation,
    explain_coach_decision,
)


def test_reduce_training_explanation():

    result = explain_coach_decision(
        decision="REDUCE_TRAINING",
        reason="High fatigue detected",
        execution_score=65,
        fatigue_signal="high",
    )

    assert (
        result["decision"]
        == "REDUCE_TRAINING"
    )

    assert (
        "recovery"
        in result["athlete_message"]
    )


def test_progress_training_explanation():

    result = explain_coach_decision(
        decision="PROGRESS_TRAINING",
        reason="Fitness improving",
        execution_score=95,
        fatigue_signal="low",
    )

    assert (
        result["decision"]
        == "PROGRESS_TRAINING"
    )

    assert (
        "progressing"
        in result["athlete_message"]
    )


def test_race_taper_explanation():

    result = explain_coach_decision(
        decision="RACE_TAPER",
        reason="Race approaching",
    )

    assert (
        "race"
        in result["athlete_message"]
    )


def test_short_explanation():

    result = build_short_coach_explanation(
        {
            "athlete_message": (
                "Recovery is the priority."
            )
        }
    )

    assert result == (
        "Recovery is the priority."
    )
