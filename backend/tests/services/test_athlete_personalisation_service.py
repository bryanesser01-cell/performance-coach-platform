from api.services.athlete_personalisation_service import (
    apply_athlete_history,
    build_athlete_profile,
    build_personalised_coach_memory,
    personalise_daily_recommendation,
    remember_training_preferences,
)


def test_build_athlete_profile():

    result = build_athlete_profile(
        athlete_id=1,
        name="Athlete",
        age=11,
        race_distance="1500m",
        goal="Improve race time",
    )

    assert (
        result["age"]
        == 11
    )

    assert (
        result["race_distance"]
        == "1500m"
    )


def test_remember_training_preferences():

    result = remember_training_preferences(
        preferred_sessions=[
            "intervals",
            "strength",
        ],
        disliked_sessions=[
            "long_runs",
        ],
        preferred_training_days=[
            "Monday",
            "Wednesday",
        ],
    )

    assert (
        "strength"
        in result["preferred_sessions"]
    )


def test_apply_athlete_history():

    result = apply_athlete_history(
        previous_results=[
            {
                "race": "1500m",
                "time": "5:00",
            },
        ],
        injury_history=[
            "calf tightness",
        ],
        training_response=[
            "responds well to intervals",
        ],
    )

    assert (
        result["history_available"]
        is True
    )


def test_personalise_daily_recommendation():

    result = personalise_daily_recommendation(
        recommendation={
            "message": "Complete training today.",
        },
        athlete_profile={
            "athlete_id": 1,
            "race_distance": "1500m",
        },
        preferences={},
        history={
            "injury_history": [],
        },
    )

    assert (
        "running economy"
        in result["personalised_message"]
    )


def test_build_personalised_coach_memory():

    result = build_personalised_coach_memory(
        athlete_profile={
            "athlete_id": 1,
        },
        preferences={},
        history={},
    )

    assert (
        result["memory_ready"]
        is True
    )
