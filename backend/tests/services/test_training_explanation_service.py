TRAINING_EXPLANATIONS = {

    "threshold": {
        "name": "Threshold",
        "explanation": (
            "A strong but controlled running pace. "
            "You are working hard but not racing."
        ),
        "effort": "7/10",
        "feeling": (
            "Breathing is strong. "
            "You can say a few words but not hold a conversation."
        ),
        "purpose": (
            "Improve your ability to maintain a fast pace "
            "for longer."
        ),
    },

    "interval": {
        "name": "Interval",
        "explanation": (
            "Short faster efforts with recovery between repeats."
        ),
        "effort": "8-9/10",
        "feeling": (
            "Fast and controlled. "
            "The goal is consistency, not sprinting."
        ),
        "purpose": (
            "Improve speed, race pace ability, "
            "and running efficiency."
        ),
    },

    "tempo": {
        "name": "Tempo",
        "explanation": (
            "A comfortably hard sustained effort."
        ),
        "effort": "7-8/10",
        "feeling": (
            "Controlled discomfort. "
            "You are working but staying relaxed."
        ),
        "purpose": (
            "Improve endurance at faster speeds."
        ),
    },

    "recovery": {
        "name": "Recovery",
        "explanation": (
            "An easy run designed to help your body recover."
        ),
        "effort": "3-4/10",
        "feeling": (
            "You should finish feeling better "
            "than when you started."
        ),
        "purpose": (
            "Allow adaptation and prepare for harder sessions."
        ),
    },

    "easy": {
        "name": "Easy Run",
        "explanation": (
            "A relaxed aerobic run at comfortable pace."
        ),
        "effort": "4-5/10",
        "feeling": (
            "You can comfortably talk while running."
        ),
        "purpose": (
            "Build aerobic fitness and consistency."
        ),
    },
}


def get_training_explanation(
    term: str,
) -> dict:
    """
    Return athlete-friendly explanation
    for training terms.
    """

    key = term.lower()

    return TRAINING_EXPLANATIONS.get(
        key,
        {
            "name": term,
            "explanation": (
                "Training session designed "
                "to improve performance."
            ),
            "effort": "Unknown",
            "feeling": (
                "Run according to your coach's guidance."
            ),
            "purpose": (
                "Improve your fitness."
            ),
        },
    )


def explain_workout(
    workout: dict,
) -> dict:
    """
    Add athlete-friendly explanations
    to a workout recommendation.
    """

    session_type = workout.get(
        "session_type",
        "training",
    )

    explanation = get_training_explanation(
        session_type,
    )

    return {
        **workout,
        "athlete_explanation": explanation,
    }


def get_effort_description(
    effort_level: str,
) -> str:
    """
    Convert effort rating into words.
    """

    descriptions = {
        "3-4/10": (
            "Easy. You could hold a conversation."
        ),
        "5-6/10": (
            "Moderate. Comfortable but focused."
        ),
        "7/10": (
            "Strong. Controlled hard effort."
        ),
        "8-9/10": (
            "Hard. Fast but repeatable."
        ),
        "10/10": (
            "Maximum effort."
        ),
    }

    return descriptions.get(
        effort_level,
        "Run by feel.",
    )
