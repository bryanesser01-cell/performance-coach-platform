from api.services.personal_best_service import (
    calculate_improvement,
    compare_personal_best,
    generate_personal_best_summary,
    record_personal_best,
)


def test_record_personal_best():

    result = record_personal_best(
        event="5K",
        time_seconds=1380,
        date="2026-08-01",
    )

    assert result["event"] == "5K"


def test_calculate_improvement():

    result = calculate_improvement(
        previous_time_seconds=1500,
        current_time_seconds=1400,
    )

    assert result["trend"] == "improving"

    assert result["improvement_seconds"] == 100


def test_compare_personal_best():

    result = compare_personal_best(
        previous_pb={
            "event": "1500m",
            "time_seconds": 300,
        },
        current_pb={
            "event": "1500m",
            "time_seconds": 292,
        },
    )

    assert result["improvement"]["improvement_seconds"] == 8


def test_generate_personal_best_summary():

    result = generate_personal_best_summary(
        {
            "event": "5K",
            "improvement": {
                "trend": "improving",
                "improvement_seconds": 30,
                "improvement_percentage": 2.5,
            },
        }
    )

    assert "improving" in result["message"]
