from api.services.coach_explanation_service import (
    build_coach_explanation,
)


def generate_running_workout(
    decision: str,
    event: str = "5K",
    age_group: str = "ADULT",
    training_phase: str = "BUILD",
    goal: str = "performance",
) -> dict:
    """
    Generate event-specific running session.
    """

    if decision == "TRAIN_HARD":

        if event in [
            "100m",
            "200m",
            "400m",
        ]:
            session = [
                "Dynamic warm up",
                "Sprint drills",
                "Acceleration efforts",
                "Full recovery",
                "Cool down",
            ]

            workout_type = "speed_power"

        elif event in [
            "800m",
            "1500m",
            "mile",
        ]:
            session = [
                "15 minute warm up",
                "Running drills",
                "6 x 400m race pace efforts",
                "90 seconds recovery",
                "Cool down",
            ]

            workout_type = "middle_distance_intervals"

        elif event in [
            "marathon",
            "half_marathon",
        ]:
            session = [
                "Warm up",
                "Threshold endurance block",
                "Fuel practice",
                "Cool down",
            ]

            workout_type = "endurance_quality"

        elif event in [
            "trail",
            "ultra_marathon",
        ]:
            session = [
                "Trail warm up",
                "Hill efforts",
                "Technical terrain work",
                "Recovery",
            ]

            workout_type = "trail_endurance"

        else:

            session = [
                "Warm up",
                "6 x 400m intervals",
                "Recovery",
                "Cool down",
            ]

            workout_type = "intervals"

    elif decision == "TRAIN_MODERATE":

        session = [
            "Warm up",
            "Controlled tempo effort",
            "Cool down",
        ]

        workout_type = "tempo"

    elif decision == "EASY_SESSION":

        session = [
            "Easy conversational running",
        ]

        workout_type = "easy_run"

    else:

        session = [
            "Walk",
            "Mobility",
        ]

        workout_type = "recovery"

    return {
        "goal": goal,
        "event": event,
        "age_group": age_group,
        "training_phase": training_phase,
        "running_workout": {
            "type": workout_type,
            "session": session,
        },
    }


def generate_strength_workout(
    event: str = "5K",
    age_group: str = "ADULT",
) -> dict:
    """
    Generate event and age appropriate strength.
    """

    if age_group in [
        "YOUTH_U12",
        "YOUTH_U14",
    ]:

        exercises = [
            {
                "name": "Bodyweight Squats",
                "sets": 3,
                "reps": 10,
            },
            {
                "name": "Single Leg Balance",
                "sets": 3,
                "duration": "30 seconds",
            },
            {
                "name": "Plank",
                "sets": 3,
                "duration": "30 seconds",
            },
        ]

    elif event in [
        "100m",
        "200m",
        "400m",
    ]:

        exercises = [
            {
                "name": "Squats",
                "sets": 4,
                "reps": 5,
            },
            {
                "name": "Box Jumps",
                "sets": 4,
                "reps": 5,
            },
            {
                "name": "Romanian Deadlift",
                "sets": 3,
                "reps": 6,
            },
        ]

    else:

        exercises = [
            {
                "name": "Squats",
                "sets": 4,
                "reps": 8,
            },
            {
                "name": "Walking Lunges",
                "sets": 3,
                "reps": 12,
            },
            {
                "name": "Plank",
                "sets": 4,
                "duration": "45 seconds",
            },
        ]

    return {
        "session_type": "strength",
        "event": event,
        "age_group": age_group,
        "duration": "35 minutes",
        "exercises": exercises,
    }


def generate_recovery_session() -> dict:
    """
    Recovery session.
    """

    return {
        "session_type": "recovery",
        "duration": "20 minutes",
        "activities": [
            "Easy walk",
            "Mobility",
            "Stretching",
        ],
    }


def build_daily_coach_message(
    decision: str,
    event: str = "5K",
    age_group: str = "ADULT",
    training_phase: str = "BUILD",
    goal: str = "performance",
    age: int = 25,
    include_strength: bool = True,
) -> dict:
    """
    Build athlete-facing daily recommendation.
    """

    response = {
        "decision": decision,
        "event": event,
        "age_group": age_group,
        "sessions": [],
        "message": "",
    }

    if decision == "RECOVER":

        response["message"] = "Recovery is the priority today."

        response["sessions"].append(generate_recovery_session())

        return response

    running = generate_running_workout(
        decision=decision,
        event=event,
        age_group=age_group,
        training_phase=training_phase,
        goal=goal,
    )

    response["sessions"].append(running)

    if include_strength:

        response["sessions"].append(
            generate_strength_workout(
                event=event,
                age_group=age_group,
            )
        )

    explanation = build_coach_explanation(
        session_type="running",
        age=age,
        event=event,
        session=str(running["running_workout"]["session"]),
        goal=goal,
        training_phase=training_phase,
    )

    response["coach_explanation"] = explanation

    response["message"] = (
        "Today's training has been personalised "
        "using your event, age and training goal."
    )

    return response
