from api.services.strength_intelligence_service import (
    classify_athlete_strength_profile,
    generate_strength_program,
    recommend_strength_exercises,
)


def test_classify_junior_1500m_runner():

    result = classify_athlete_strength_profile(
        age=11,
        race_distance="1500m",
        training_level="developing",
    )

    assert result["athlete_type"] == "junior_runner"

    assert "coordination" in result["strength_focus"]


def test_classify_middle_distance_runner():

    result = classify_athlete_strength_profile(
        age=20,
        race_distance="1500m",
        training_level="advanced",
    )

    assert result["athlete_type"] == "middle_distance_runner"


def test_recommend_strength_exercises():

    result = recommend_strength_exercises(
        athlete_type="junior_runner",
    )

    assert result[0]["exercise"] == "Bodyweight Squat"


def test_generate_strength_program():

    result = generate_strength_program(
        age=11,
        race_distance="1500m",
        training_level="developing",
    )

    assert result["athlete_profile"]["athlete_type"] == "junior_runner"

    assert len(result["exercises"]) > 0

    assert result["progression"]["weekly_progression_percent"] == 5
