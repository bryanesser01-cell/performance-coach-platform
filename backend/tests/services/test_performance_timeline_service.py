from api.services.performance_timeline_service import (
    add_performance_milestone,
    analyse_timeline_progress,
    create_performance_timeline,
    generate_timeline_summary,
)


def test_add_performance_milestone():

    timeline = []

    result = add_performance_milestone(
        timeline,
        event="5K",
        value="23:05",
        date="2026-01-01",
    )

    assert result[0]["event"] == "5K"


def test_create_performance_timeline():

    result = create_performance_timeline(
        [
            {
                "event": "5K",
                "value": "23:05",
            }
        ]
    )

    assert result["total_milestones"] == 1


def test_analyse_timeline_progress():

    result = analyse_timeline_progress(
        [
            {
                "event": "5K",
                "value": "23:05",
                "improved": False,
            },
            {
                "event": "5K",
                "value": "22:30",
                "improved": True,
            },
        ]
    )

    assert result["trend"] == "improving"


def test_generate_timeline_summary():

    result = generate_timeline_summary(
        {
            "trend": "improving",
        }
    )

    assert "improving" in result["message"]
