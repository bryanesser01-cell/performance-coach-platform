"""
Performance Limitation Service

Responsible for:
- identifying athlete performance blockers
- analysing speed, aerobic and recovery limitations
- generating coaching recommendations
"""


def analyse_performance_limitations(
    speed_score: int,
    aerobic_score: int,
    recovery_score: int,
) -> dict:
    """
    Analyse athlete limitation areas.

    Higher score = stronger capability.
    Lowest score identifies likely limiter.
    """

    areas = {
        "speed": speed_score,
        "aerobic": aerobic_score,
        "recovery": recovery_score,
    }


    weakest_area = min(
        areas,
        key=areas.get,
    )


    return {
        "scores": areas,

        "primary_limiter": weakest_area,

        "limiter_score": areas[
            weakest_area
        ],
    }



def identify_primary_limiter(
    analysis: dict,
) -> dict:
    """
    Convert limitation into coaching advice.
    """

    limiter = analysis[
        "primary_limiter"
    ]


    recommendations = {
        "speed": (
            "Increase speed development "
            "and quality interval sessions."
        ),

        "aerobic": (
            "Improve aerobic capacity "
            "through consistent endurance work."
        ),

        "recovery": (
            "Adjust training load and "
            "prioritise recovery."
        ),
    }


    return {
        "limiter": limiter,

        "recommendation": recommendations[
            limiter
        ],
    }



def generate_limitation_summary(
    limitation_result: dict,
) -> dict:
    """
    Generate athlete-facing insight.
    """

    limiter = limitation_result[
        "limiter"
    ]


    return {
        "primary_limitation": limiter,

        "message": (
            f"Your current performance "
            f"limiter appears to be "
            f"{limiter}. "
            "Training can be adjusted "
            "to improve this area."
        ),

        "recommendation": limitation_result[
            "recommendation"
        ],
    }
