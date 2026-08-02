from api.services.performance_limitation_service import (
    analyse_performance_limitations,
    generate_limitation_summary,
    identify_primary_limiter,
)


def test_identifies_speed_limitation():

    result = analyse_performance_limitations(
        speed_score=60,
        aerobic_score=90,
        recovery_score=85,
    )

    assert result["primary_limiter"] == "speed"


def test_identifies_aerobic_limitation():

    result = analyse_performance_limitations(
        speed_score=90,
        aerobic_score=55,
        recovery_score=85,
    )

    assert result["primary_limiter"] == "aerobic"


def test_identifies_recovery_limitation():

    result = analyse_performance_limitations(
        speed_score=90,
        aerobic_score=85,
        recovery_score=50,
    )

    limiter = identify_primary_limiter(result)

    assert limiter["limiter"] == "recovery"


def test_generates_limitation_summary():

    result = generate_limitation_summary(
        {
            "limiter": "speed",
            "recommendation": ("Increase speed development."),
        }
    )

    assert result["primary_limitation"] == "speed"
