from api.services.activity_metrics_service import (
    calculate_pace,
    calculate_speed,
    calculate_training_load,
    generate_metric_summary,
)


def test_calculate_pace():
    pace = calculate_pace(
        5,
        1500,
    )

    assert pace == 300


def test_calculate_speed():
    speed = calculate_speed(
        5,
        1500,
    )

    assert round(speed, 2) == 12.0


def test_calculate_training_load():
    load = calculate_training_load(
        3600,
        150,
    )

    assert load == 90


def test_generate_metric_summary():
    summary = generate_metric_summary(
        10,
        3000,
        160,
    )

    assert summary["distance_km"] == 10
    assert summary["pace_seconds_per_km"] == 300
