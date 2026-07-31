from api.services.athlete_dashboard_intelligence_service import (
    generate_dashboard_intelligence,
)


def test_generate_dashboard_intelligence():


    result = generate_dashboard_intelligence(

        fitness_summary={
            "fitness_score": 90,
            "improvement_score": 85,
            "trend": "improving",
        },


        training_status={
            "consistency_score": 88,
        },


        race_readiness={
            "readiness_score": 90,
        },


        prediction={
            "5k": "20:00",
        },


        timeline={
            "trend": "improving",
        },


        limitation={
            "limiter": "speed",
        },

    )


    assert (
        "scorecard"
        in result
    )


    assert (
        "insight"
        in result
    )


def test_dashboard_intelligence_contains_prediction():

    result = generate_dashboard_intelligence(

        {},
        {},
        {},
        {
            "time": "20:00",
        },
        {},
        {},

    )


    assert (
        "prediction"
        in result
    )
