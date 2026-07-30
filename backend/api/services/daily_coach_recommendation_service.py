def generate_running_workout(
    decision: str,
    goal: str = "5K performance",
) -> dict:
    """
    Generate running session recommendation.
    """

    if decision == "TRAIN_HARD":
        workout = {
            "type": "intervals",
            "duration": "45 minutes",
            "session": [
                "10 minute warm up",
                "6 x 400m hard efforts",
                "90 seconds recovery between efforts",
                "10 minute cool down",
            ],
        }

    elif decision == "TRAIN_MODERATE":
        workout = {
            "type": "tempo",
            "duration": "35 minutes",
            "session": [
                "10 minute warm up",
                "20 minute controlled tempo",
                "5 minute cool down",
            ],
        }

    elif decision == "EASY_SESSION":
        workout = {
            "type": "easy run",
            "duration": "30 minutes",
            "session": [
                "Easy conversational pace",
            ],
        }

    else:
        workout = {
            "type": "recovery",
            "duration": "20 minutes",
            "session": [
                "Walk or easy mobility",
            ],
        }

    return {
        "goal": goal,
        "running_workout": workout,
    }


def generate_strength_workout(
    athlete_level: str = "runner",
) -> dict:
    """
    Generate strength training session.

    Designed for runners.
    """

    exercises = [
        {
            "name": "Squats",
            "sets": 4,
            "reps": 10,
        },
        {
            "name": "Walking Lunges",
            "sets": 3,
            "reps": 12,
            "each_leg": True,
        },
        {
            "name": "Plank",
            "sets": 5,
            "duration": "45 seconds",
        },
        {
            "name": "Push Ups",
            "sets": 3,
            "reps": 15,
        },
        {
            "name": "Single Leg Calf Raises",
            "sets": 3,
            "reps": 15,
            "each_leg": True,
        },
    ]

    return {
        "session_type": "strength",
        "athlete_level": athlete_level,
        "duration": "35 minutes",
        "exercises": exercises,
    }


def generate_mobility_session() -> dict:
    """
    Generate mobility recovery session.
    """

    return {
        "session_type": "mobility",
        "duration": "15 minutes",
        "exercises": [
            "Hip mobility",
            "Calf stretching",
            "Hamstring mobility",
            "Thoracic rotation",
        ],
    }


def generate_recovery_session() -> dict:
    """
    Generate recovery recommendation.
    """

    return {
        "session_type": "recovery",
        "duration": "20 minutes",
        "activities": [
            "Easy walk",
            "Light stretching",
            "Breathing exercises",
        ],
    }


def build_daily_coach_message(
    decision: str,
    include_strength: bool = True,
) -> dict:
    """
    Build complete daily coach recommendation.
    """

    recommendation = {
        "decision": decision,
        "message": "",
        "sessions": [],
    }

    if decision == "RECOVER":
        recommendation["message"] = (
            "Recovery is the priority today. "
            "Allow your body to adapt."
        )

        recommendation["sessions"].append(
            generate_recovery_session()
        )

    else:
        recommendation["message"] = (
            "Complete today's planned training "
            "and focus on quality execution."
        )

        recommendation["sessions"].append(
            generate_running_workout(
                decision=decision,
            )
        )

        if include_strength:
            recommendation["sessions"].append(
                generate_strength_workout()
            )

    return recommendation
