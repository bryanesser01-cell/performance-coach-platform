"""
Dashboard Insight Service

Creates athlete-facing coaching insights.

Combines:
- performance scorecard
- performance timeline
- readiness
- limitations
"""


def identify_dashboard_focus(
    scorecard: dict,
    limitation: dict,
) -> dict:
    """
    Identify the main coaching focus.
    """

    overall_score = scorecard.get(
        "overall_score",
        0,
    )

    limiter = limitation.get(
        "limiter",
        "unknown",
    )


    if overall_score >= 85:

        focus = "performance_progression"

    elif overall_score >= 70:

        focus = "continued_development"

    else:

        focus = "foundation_building"


    return {
        "focus": focus,

        "limiter": limiter,
    }



def create_coach_recommendation(
    focus_data: dict,
) -> dict:
    """
    Create coaching recommendation.
    """

    recommendations = {
        "performance_progression": (
            "Maintain training consistency "
            "and introduce targeted performance work."
        ),

        "continued_development": (
            "Continue building fitness while "
            "improving identified limitations."
        ),

        "foundation_building": (
            "Prioritise consistency, recovery, "
            "and gradual progression."
        ),
    }


    return {
        "focus": focus_data["focus"],

        "recommendation": recommendations[
            focus_data["focus"]
        ],

        "limiter": focus_data["limiter"],
    }



def generate_dashboard_insight(
    scorecard: dict,
    timeline: dict,
    limitation: dict,
) -> dict:
    """
    Generate complete AI dashboard insight.
    """

    focus = identify_dashboard_focus(
        scorecard,
        limitation,
    )


    recommendation = create_coach_recommendation(
        focus,
    )


    return {
        "current_status": scorecard.get(
            "status",
            "unknown",
        ),

        "trend": scorecard.get(
            "trend",
            "unknown",
        ),

        "timeline_progress": timeline.get(
            "trend",
            "unknown",
        ),

        "coaching_focus": recommendation,
    }
