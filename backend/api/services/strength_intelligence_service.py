def classify_athlete_strength_profile(
    age: int,
    race_distance: str,
    training_level: str,
) -> dict:
    """
    Classify athlete strength requirements.

    Event determines athletic demands.
    Age modifies training prescription.
    """

    sprint_events = [
        "100m",
        "200m",
        "400m",
    ]

    middle_distance_events = [
        "800m",
        "1500m",
        "mile",
    ]

    endurance_events = [
        "3000m",
        "5000m",
        "10000m",
        "5K",
        "10K",
    ]

    road_events = [
        "half_marathon",
        "marathon",
    ]

    trail_events = [
        "trail",
        "ultra_marathon",
    ]

    # -------------------------
    # EVENT CLASSIFICATION
    # -------------------------

    if race_distance in sprint_events:

        event_type = "sprint"

        event_focus = [
            "explosive_power",
            "maximum_strength",
            "speed_development",
        ]

    elif race_distance in middle_distance_events:

        event_type = "middle_distance"

        event_focus = [
            "power",
            "elasticity",
            "running_economy",
        ]

    elif race_distance in endurance_events:

        event_type = "endurance"

        event_focus = [
            "strength_endurance",
            "running_economy",
            "injury_prevention",
        ]

    elif race_distance in road_events:

        event_type = "road_endurance"

        event_focus = [
            "durability",
            "fatigue_resistance",
            "core_strength",
        ]

    elif race_distance in trail_events:

        event_type = "trail"

        event_focus = [
            "single_leg_strength",
            "stability",
            "elevation_strength",
        ]

    else:

        event_type = "general"

        event_focus = [
            "foundational_strength",
        ]

    # -------------------------
    # AGE CLASSIFICATION
    # -------------------------

    if age < 12:

        age_group = "U12"

        age_adjustment = [
            "coordination",
            "movement_quality",
            "body_control",
            "safe_strength_foundation",
        ]

    elif age < 14:

        age_group = "U14"

        age_adjustment = [
            "technique",
            "strength_foundation",
            "athletic_development",
        ]

    elif age < 18:

        age_group = "U18"

        age_adjustment = [
            "progressive_strength",
            "power_development",
            "injury_prevention",
        ]

    elif age < 35:

        age_group = "ADULT"

        age_adjustment = [
            "performance_strength",
            "progressive_overload",
        ]

    elif age < 50:

        age_group = "MASTERS"

        age_adjustment = [
            "strength_maintenance",
            "recovery_management",
            "injury_prevention",
        ]

    else:

        age_group = "MASTERS_PLUS"

        age_adjustment = [
            "strength_retention",
            "mobility",
            "recovery_priority",
        ]

    # -------------------------
    # BACKWARD COMPATIBILITY
    # -------------------------

    if age < 14:

        athlete_type = "junior_runner"

    elif event_type == "sprint":

        athlete_type = "sprinter"

    elif event_type == "middle_distance":

        athlete_type = "middle_distance_runner"

    elif event_type == "road_endurance":

        athlete_type = "marathon_runner"

    elif event_type == "trail":

        athlete_type = "trail_runner"

    else:

        athlete_type = "distance_runner"

    return {
        "athlete_type": athlete_type,
        "age": age,
        "age_group": age_group,
        "race_distance": race_distance,
        "event_type": event_type,
        "training_level": training_level,
        "event_focus": event_focus,
        "age_adjustment": age_adjustment,
        "strength_focus": (event_focus + age_adjustment),
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

    if "explosive_power" in focus or "power" in focus:

        objective = "POWER_DEVELOPMENT"

    elif "strength_endurance" in focus:

        objective = "RUNNING_DURABILITY"

    elif "durability" in focus:

        objective = "ENDURANCE_RESILIENCE"

    else:

        objective = "FOUNDATIONAL_STRENGTH"

    return {
        "objective": objective,
        "focus": focus,
    }


def recommend_strength_exercises(
    event_type: str = None,
    age_group: str = None,
    athlete_type: str = None,
) -> list[dict]:
    """
    Recommend strength exercises.

    Supports:
    - New event based system
    - Legacy athlete_type calls
    """

    # Legacy support

    if athlete_type == "junior_runner":

        return [
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
        ]

    if athlete_type == "middle_distance_runner":

        return [
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
                "exercise": "Calf Raise",
                "sets": 3,
                "reps": 15,
            },
        ]

    # New system

    if age_group in [
        "U12",
        "U14",
    ]:

        return [
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
        ]

    if event_type == "sprint":

        return [
            {
                "exercise": "Squat",
                "sets": 4,
                "reps": 5,
            },
            {
                "exercise": "Box Jump",
                "sets": 4,
                "reps": 5,
            },
            {
                "exercise": "Romanian Deadlift",
                "sets": 3,
                "reps": 6,
            },
        ]

    if event_type == "middle_distance":

        return [
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
                "exercise": "Calf Raise",
                "sets": 3,
                "reps": 15,
            },
        ]

    if event_type == "road_endurance":

        return [
            {
                "exercise": "Split Squat",
                "sets": 3,
                "reps": 10,
            },
            {
                "exercise": "Calf Raise",
                "sets": 4,
                "reps": 15,
            },
            {
                "exercise": "Plank",
                "sets": 4,
                "duration": "45 seconds",
            },
        ]

    if event_type == "trail":

        return [
            {
                "exercise": "Step Ups",
                "sets": 4,
                "reps": 10,
            },
            {
                "exercise": "Single Leg Squat",
                "sets": 3,
                "reps": 8,
            },
            {
                "exercise": "Calf Raise",
                "sets": 4,
                "reps": 15,
            },
        ]

    return [
        {
            "exercise": "Split Squat",
            "sets": 3,
            "reps": 10,
        }
    ]


def apply_strength_progression_rules(
    age: int,
    current_week: int,
) -> dict:
    """
    Apply safe progression rules.
    """

    if age < 14:

        increase = 5

    else:

        increase = 10

    return {
        "weekly_progression_percent": increase,
        "week": current_week,
        "progression_type": ("gradual_load_increase"),
    }


def generate_strength_program(
    age: int,
    race_distance: str,
    training_level: str,
) -> dict:
    """
    Generate personalised strength program.
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
        event_type=profile["event_type"],
        age_group=profile["age_group"],
        athlete_type=profile["athlete_type"],
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
