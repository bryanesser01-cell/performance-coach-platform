def classify_training_age_group(
    age: int | None,
) -> str:
    """
    Classify athlete development stage.
    """

    if age is None:
        return "UNKNOWN"

    if age < 12:
        return "YOUTH_U12"

    if age < 14:
        return "YOUTH_U14"

    if age < 18:
        return "YOUTH_U18"

    if age < 35:
        return "ADULT"

    if age < 50:
        return "MASTERS"

    return "MASTERS_PLUS"



def _get_event_phases(
    event: str,
) -> list[dict]:
    """
    Generate event specific training phases.
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

    marathon_events = [
        "half_marathon",
        "marathon",
    ]

    trail_events = [
        "trail",
        "ultra_marathon",
    ]


    if event in sprint_events:

        return [
            {
                "phase": "BASE",
                "focus": [
                    "sprint mechanics",
                    "strength foundation",
                    "mobility",
                ],
            },
            {
                "phase": "BUILD",
                "focus": [
                    "acceleration",
                    "maximum velocity",
                    "power development",
                ],
            },
            {
                "phase": "PEAK",
                "focus": [
                    "race speed",
                    "competition preparation",
                ],
            },
            {
                "phase": "TAPER",
                "focus": [
                    "freshness",
                    "speed maintenance",
                ],
            },
        ]


    if event in middle_distance_events:

        return [
            {
                "phase": "BASE",
                "focus": [
                    "aerobic development",
                    "running economy",
                    "strength foundation",
                ],
            },
            {
                "phase": "BUILD",
                "focus": [
                    "race pace",
                    "speed endurance",
                    "threshold",
                ],
            },
            {
                "phase": "PEAK",
                "focus": [
                    "race specific intensity",
                    "speed reserve",
                ],
            },
            {
                "phase": "TAPER",
                "focus": [
                    "recovery",
                    "maintain speed",
                ],
            },
        ]


    if event in endurance_events:

        return [
            {
                "phase": "BASE",
                "focus": [
                    "aerobic foundation",
                    "running durability",
                ],
            },
            {
                "phase": "BUILD",
                "focus": [
                    "threshold",
                    "longer endurance sessions",
                ],
            },
            {
                "phase": "PEAK",
                "focus": [
                    "race specific endurance",
                ],
            },
            {
                "phase": "TAPER",
                "focus": [
                    "recovery",
                    "freshness",
                ],
            },
        ]


    if event in marathon_events:

        return [
            {
                "phase": "BASE",
                "focus": [
                    "aerobic foundation",
                    "strength endurance",
                ],
            },
            {
                "phase": "BUILD",
                "focus": [
                    "long runs",
                    "threshold",
                    "fuel practice",
                ],
            },
            {
                "phase": "PEAK",
                "focus": [
                    "race endurance",
                    "marathon pace",
                ],
            },
            {
                "phase": "TAPER",
                "focus": [
                    "reduce volume",
                    "maintain fitness",
                ],
            },
        ]


    if event in trail_events:

        return [
            {
                "phase": "BASE",
                "focus": [
                    "aerobic base",
                    "strength durability",
                ],
            },
            {
                "phase": "BUILD",
                "focus": [
                    "hill strength",
                    "technical terrain",
                    "long duration effort",
                ],
            },
            {
                "phase": "PEAK",
                "focus": [
                    "race terrain preparation",
                    "fatigue resistance",
                ],
            },
            {
                "phase": "TAPER",
                "focus": [
                    "recovery",
                    "fresh legs",
                ],
            },
        ]


    return [
        {
            "phase": "BASE",
            "focus": [
                "general fitness",
            ],
        },
        {
            "phase": "BUILD",
            "focus": [
                "progressive training",
            ],
        },
        {
            "phase": "PEAK",
            "focus": [
                "performance preparation",
            ],
        },
        {
            "phase": "TAPER",
            "focus": [
                "recovery",
            ],
        },
    ]



def create_training_plan(
    goal: str,
    event: str,
    weeks: int,
    current_time: str,
    target_time: str,
    age: int | None = None,
    training_age: int | None = None,
    experience_level: str | None = None,
) -> dict:
    """
    Create adaptive training plan.

    Considers:
    - goal
    - event
    - age
    - training experience
    """

    return {
        "goal": goal,
        "event": event,
        "timeline_weeks": weeks,
        "current_time": current_time,
        "target_time": target_time,

        "age_group": (
            classify_training_age_group(age)
        ),

        "age": age,

        "training_age": training_age,

        "experience_level": (
            experience_level
        ),

        "phases": _get_event_phases(
            event,
        ),
    }



def adjust_weekly_load(
    previous_load: int,
    performance_response: str,
) -> dict:
    """
    Adjust weekly training load.
    """

    if performance_response == "improving":

        change = 10

    elif performance_response == "fatigued":

        change = -20

    else:

        change = 0


    new_load = int(
        previous_load
        * (1 + change / 100)
    )


    return {
        "previous_load": previous_load,
        "change_percent": change,
        "new_load": new_load,
    }



def adapt_plan_from_results(
    race_result: str,
    target_result: str,
    fatigue_score: int,
) -> dict:
    """
    Adapt training plan after results.
    """

    def convert_time(
        value: str,
    ) -> int:

        minutes, seconds = value.split(":")

        return (
            int(minutes) * 60
            + int(seconds)
        )


    race_seconds = convert_time(
        race_result,
    )

    target_seconds = convert_time(
        target_result,
    )


    if fatigue_score > 70:

        action = "REDUCE_LOAD"

    elif race_seconds <= target_seconds:

        action = "CONTINUE_PROGRESS"

    else:

        action = "MODIFY_PLAN"


    return {
        "race_result": race_result,
        "target_result": target_result,
        "fatigue_score": fatigue_score,
        "action": action,
    }



def generate_race_preparation_plan(
    event: str,
    race_date: str,
    goal: str,
    age: int | None = None,
) -> dict:
    """
    Generate race preparation strategy.
    """

    return {
        "event": event,
        "race_date": race_date,
        "goal": goal,
        "age_group": (
            classify_training_age_group(age)
        ),
        "strategy": [
            "build fitness",
            "race specific preparation",
            "taper before race",
        ],
    }
