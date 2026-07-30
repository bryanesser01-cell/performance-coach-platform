"""
Performance Timeline Service

Creates an athlete performance journey.

Tracks:
- personal best milestones
- performance changes
- training phases
- progress over time
"""


def add_performance_milestone(
    timeline: list[dict],
    event: str,
    value: str,
    date: str,
) -> list[dict]:
    """
    Add performance milestone.
    """

    timeline.append(
        {
            "event": event,

            "value": value,

            "date": date,
        }
    )


    return timeline



def create_performance_timeline(
    milestones: list[dict],
) -> dict:
    """
    Create athlete performance timeline.
    """

    return {
        "total_milestones": len(
            milestones
        ),

        "milestones": milestones,
    }



def analyse_timeline_progress(
    milestones: list[dict],
) -> dict:
    """
    Analyse athlete progression.
    """

    if len(milestones) < 2:

        return {
            "trend": "insufficient_data",

            "improvements": 0,
        }


    improvements = 0


    for index in range(
        1,
        len(milestones),
    ):

        previous = milestones[
            index - 1
        ]

        current = milestones[
            index
        ]


        if (
            current.get("improved")
            is True
        ):

            improvements += 1


    if improvements > 0:

        trend = "improving"

    else:

        trend = "stable"


    return {
        "trend": trend,

        "improvements": improvements,

    }



def generate_timeline_summary(
    timeline_analysis: dict,
) -> dict:
    """
    Generate athlete-facing summary.
    """

    return {
        "headline": (
            "Performance timeline analysis"
        ),

        "message": (
            f"Athlete trend is "
            f"{timeline_analysis['trend']} "
            "based on recorded milestones."
        ),
    }
