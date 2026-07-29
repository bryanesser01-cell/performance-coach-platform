from database.repositories.performance_trend_repository import (
    PerformanceTrendRepository,
)


def test_performance_trend_repository_exists():

    assert hasattr(
        PerformanceTrendRepository,
        "calculate_performance_trend",
    )


def test_recent_activity_method_exists():

    assert hasattr(
        PerformanceTrendRepository,
        "get_recent_activities",
    )


def test_current_metric_method_exists():

    assert hasattr(
        PerformanceTrendRepository,
        "get_current_performance_metric",
    )
