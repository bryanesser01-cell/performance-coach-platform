def generate_training_plan(
    goal: str,
    fitness_status: str,
    training_load: str,
) -> dict:
    """
    Generate a personalised weekly training plan.
    """

    sessions = []

    if fitness_status == "needs_attention":
        sessions = [
            {
                "day": "Monday",
                "workout": "Recovery Run",
                "duration_minutes": 30,
            },
            {
                "day": "Wednesday",
                "workout": "Easy Aerobic Run",
                "duration_minutes": 40,
            },
            {
                "day": "Saturday",
                "workout": "Long Easy Run",
                "duration_minutes": 50,
            },
        ]

    elif training_load == "increasing":
        sessions = [
            {
                "day": "Monday",
                "workout": "Easy Run",
                "duration_minutes": 35,
            },
            {
                "day": "Wednesday",
                "workout": "Threshold Session",
                "duration_minutes": 45,
            },
            {
                "day": "Saturday",
                "workout": "Long Run",
                "duration_minutes": 60,
            },
        ]

    else:
        sessions = [
            {
                "day": "Monday",
                "workout": "Easy Run",
                "duration_minutes": 30,
            },
            {
                "day": "Wednesday",
                "workout": "Intervals",
                "duration_minutes": 40,
            },
            {
                "day": "Saturday",
                "workout": "Long Run",
                "duration_minutes": 60,
            },
        ]

    return {
        "goal": goal,
        "plan_type": f"{goal} improvement",
        "weekly_sessions": sessions,
    }
