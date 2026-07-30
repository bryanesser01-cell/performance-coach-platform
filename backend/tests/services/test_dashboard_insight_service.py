from api.services.dashboard_insight_service import (
    create_coach_recommendation,
    generate_dashboard_insight,
    identify_dashboard_focus,
)


def test_identify_dashboard_focus():

    result = identify_dashboard_focus(
        {
            "overall_score": 90,
        },

        {
            "limiter": "speed",
        },
    )


    assert (
        result["focus"]
        == "performance_progression"
    )


    assert (
        result["limiter"]
        == "speed"
    )



def test_create_coach_recommendation():

    result = create_coach_recommendation(
        {
            "focus": "continued_development",

            "limiter": "aerobic",
        }
    )


    assert (
        result["limiter"]
        == "aerobic"
    )


    assert (
        "Continue"
        in result["recommendation"]
    )



def test_generate_dashboard_insight():

    result = generate_dashboard_insight(
        {
            "status": "excellent",

            "trend": "improving",
        },

        {
            "trend": "improving",
        },

        {
            "limiter": "speed",
        },
    )


    assert (
        result["current_status"]
        == "excellent"
    )


    assert (
        result["coaching_focus"]["limiter"]
        == "speed"
    )
