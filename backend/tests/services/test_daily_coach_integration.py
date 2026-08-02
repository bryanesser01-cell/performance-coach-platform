from api.services.daily_coach_recommendation_service import (
    build_daily_coach_message,
)


def test_complete_daily_coach_response():

    result = build_daily_coach_message(
        decision="TRAIN_HARD",
        event="1500m",
        age_group="YOUTH_U12",
        age=11,
        goal="improve performance",
    )

    assert len(result["sessions"]) > 0

    assert "coach_explanation" in result

    assert "why_this_session" in result["coach_explanation"]
