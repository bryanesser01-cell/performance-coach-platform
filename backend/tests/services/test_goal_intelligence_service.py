from api.services.goal_intelligence_service import (
    GoalIntelligenceService,
)


def test_no_goals():

    service = GoalIntelligenceService()

    result = service.analyse({})

    assert result["has_goal"] is False
    assert result["confidence"] == 0
    assert result["on_track"] is False


def test_goal_on_track():

    service = GoalIntelligenceService()

    athlete_state = {
        "goals": [
            {
                "title": "Sub 20 5K",
            }
        ],
        "performance": {
            "trend": "improving",
        },
        "readiness": {
            "score": 80,
        },
    }

    result = service.analyse(
        athlete_state,
    )

    assert result["has_goal"] is True
    assert result["on_track"] is True
    assert result["confidence"] == 90


def test_goal_needs_attention():

    service = GoalIntelligenceService()

    athlete_state = {
        "goals": [
            {
                "title": "Marathon",
            }
        ],
        "performance": {
            "trend": "declining",
        },
        "readiness": {
            "score": 50,
        },
    }

    result = service.analyse(
        athlete_state,
    )

    assert result["goal_status"] == "Needs Attention"
    assert result["confidence"] == 40
