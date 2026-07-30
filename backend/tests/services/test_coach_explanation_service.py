from api.services.coach_explanation_service import (
    build_coach_explanation,
    explain_running_session,
    explain_strength_session,
)


def test_running_session_explanation():

    result = explain_running_session(
        age=11,
        event="1500m",
        session="6 x 200m",
        goal="improve performance",
    )

    assert (
        "why_this_session"
        in result
    )

    assert (
        "running economy"
        in result["what_to_focus_on"]
    )



def test_strength_explanation():

    result = explain_strength_session(
        age=11,
        event="1500m",
        exercises=[
            "Bodyweight Squat",
        ],
    )

    assert (
        result["session_type"]
        == "strength"
    )



def test_complete_coach_explanation():

    result = build_coach_explanation(
        session_type="running",
        age=25,
        event="marathon",
        session="60 minute easy run",
        goal="marathon preparation",
    )

    assert (
        result["session"]
        == "60 minute easy run"
    )
