from api.services.performance_intelligence_service import (
    analyse_performance_trend,
    calculate_training_consistency,
    generate_performance_insight,
)


def test_analyse_improving_trend():

    result = analyse_performance_trend(
        [
            {
                "pace_seconds": 320,
            },
            {
                "pace_seconds": 300,
            },
        ]
    )


    assert (
        result["trend"]
        == "improving"
    )



def test_training_consistency():

    result = calculate_training_consistency(
        [
            {},
            {},
            {},
            {},
        ]
    )


    assert (
        result["consistency_score"]
        == 100
    )



def test_generate_performance_insight():

    result = generate_performance_insight(
        [
            {
                "pace_seconds": 320,
            },
            {
                "pace_seconds": 300,
            },
        ]
    )


    assert (
        "performance_trend"
        in result
    )
