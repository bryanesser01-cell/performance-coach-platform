def classify_athlete_strength_profile(
    age: int,
    race_distance: str,
    training_level: str,
) -> dict:
    """
    Classify athlete strength requirements.

    Considers:
    - age
    - race event
    - athlete development level
    """

    if age < 14:
        athlete_type = "junior_runner"
        focus = [
            "coordination",
            "movement_quality",
            "stability",
            "body_control",
        ]

    elif race_distance in [
        "800m",
        "1500m",
    ]:
        athlete_type = "middle_distance_runner"
        focus = [
            "power",
            "elasticity",
            "running_economy",
        ]

    elif race_distance in [
        "3000m",
        "5000m",
    ]:
        athlete_type = "distance_runner"
        focus = [
            "strength_endurance",
            "injury_prevention",
            "running_economy",
        ]

    else:
        athlete_type = "endurance_runner"
        focus = [
            "durability",
            "core_strength",
            "fatigue_resistance",
        ]

    return {
        "athlete_type": athlete_type,
        "age": age,
        "race_distance": race_distance,
        "training_level": training_level,
        "strength_focus": focus,
    }


def select_strength_focus(
    athlete_profile: dict,
) -> dict:
    """
    Select primary strength objective.
    """

    focus = athlete_profile.get(
        "strength_focus",
        [],
    )

    if "power" in focus:
        objective = "POWER_DEVELOPMENT"

    elif "strength_endurance" in focus:
        objective = "RUNNING_DURABILITY"

    else:
        objective = "FOUNDATIONAL_STRENGTH"

    return {
        "objective": objective,
        "focus": focus,
    }


def recommend_strength_exercises(
    athlete_type: str,
) -> list[dict]:
    """
    Recommend exercises based on athlete type.
    """

    exercises = {
        "junior_runner": [
            {
                "exercise": "Bodyweight Squat",
                "sets": 3,
                "reps": 10,
            },
            {
                "exercise": "Single Leg Balance",
                "sets": 3,
                "duration": "30 seconds",
            },
            {
                "exercise": "Plank",
                "sets": 3,
                "duration": "30 seconds",
            },
        ],
        "middle_distance_runner": [
            {
                "exercise": "Squat",
                "sets": 4,
                "reps": 8,
            },
            {
                "exercise": "Jump Squat",
                "sets": 3,
                "reps": 6,
            },
            {
                "exercise": "Single Leg Calf Raise",
                "sets": 3,
                "reps": 15,
            },
        ],
        "distance_runner": [
            {
                "exercise": "Split Squat",
                "sets": 3,
                "reps": 10,
            },
            {
                "exercise": "Romanian Deadlift",
                "sets": 3,
                "reps": 8,
            },
            {
                "exercise": "Plank",
                "sets": 4,
                "duration": "45 seconds",
            },
        ],
    }

    return exercises.get(
        athlete_type,
        exercises["junior_runner"],
    )


def apply_strength_progression_rules(
    age: int,
    current_week: int,
) -> dict:
    """
    Apply safe progression rules.

    Junior athletes progress slower.
    """

    if age < 14:
        increase = 5

    else:
        increase = 10

    return {
        "weekly_progression_percent": increase,
        "week": current_week,
        "progression_type": (
            "gradual_load_increase"
        ),
    }


def generate_strength_program(
    age: int,
    race_distance: str,
    training_level: str,
) -> dict:
    """
    Generate personalised strength program.

    Flow:

    Athlete Profile
          ↓
    Classification
          ↓
    Exercise Selection
          ↓
    Progression Rules
          ↓
    Strength Program
    """

    profile = classify_athlete_strength_profile(
        age=age,
        race_distance=race_distance,
        training_level=training_level,
    )

    focus = select_strength_focus(
        athlete_profile=profile,
    )

    exercises = recommend_strength_exercises(
        athlete_type=profile[
            "athlete_type"
        ],
    )

    progression = apply_strength_progression_rules(
        age=age,
        current_week=1,
    )

    return {
        "athlete_profile": profile,
        "strength_focus": focus,
        "exercises": exercises,
        "progression": progression,
    }
