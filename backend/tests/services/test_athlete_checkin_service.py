from api.services.athlete_checkin_service import (
    calculate_readiness_score,
    create_checkin,
    generate_checkin_recommendation,
)


def test_high_readiness_score():

    score = calculate_readiness_score(
        energy=9,
        sleep_quality=9,
        soreness=1,
        motivation=9,
    )

    assert score >= 80


def test_low_readiness_score():

    score = calculate_readiness_score(
        energy=3,
        sleep_quality=3,
        soreness=8,
        motivation=3,
    )

    assert score < 60


def test_create_checkin():

    result = create_checkin(
        athlete_id=1,
        energy=8,
        sleep_quality=8,
        soreness=2,
        motivation=9,
        notes="Feeling good",
    )

    assert result["athlete_id"] == 1

    assert result["notes"] == "Feeling good"


def test_generate_recommendation():

    recommendation = generate_checkin_recommendation(
        90,
    )

    assert "quality training" in recommendation
