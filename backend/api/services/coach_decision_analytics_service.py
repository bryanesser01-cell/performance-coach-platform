from collections import defaultdict


def calculate_decision_success_rate(
    outcomes: list[str],
) -> int:
    """
    Calculate percentage of positive outcomes.

    Example:
    8 positive out of 10 decisions = 80%
    """

    if not outcomes:
        return 0

    positive_count = sum(1 for outcome in outcomes if outcome == "positive")

    return int((positive_count / len(outcomes)) * 100)


def analyse_decision_history(
    history: list[dict],
) -> dict:
    """
    Analyse AI Coach decision history.

    Groups decisions and measures:
    - usage count
    - positive outcomes
    - success rate
    """

    analysis = defaultdict(
        lambda: {
            "times_used": 0,
            "positive_outcomes": 0,
            "outcomes": [],
        }
    )

    for item in history:

        decision = item.get(
            "decision",
            "UNKNOWN",
        )

        outcome = item.get(
            "outcome",
            "neutral",
        )

        analysis[decision]["times_used"] += 1

        analysis[decision]["outcomes"].append(outcome)

        if outcome == "positive":

            analysis[decision]["positive_outcomes"] += 1

    result = {}

    for decision, data in analysis.items():

        result[decision] = {
            "times_used": data["times_used"],
            "positive_outcomes": data["positive_outcomes"],
            "success_rate": (
                calculate_decision_success_rate(
                    data["outcomes"],
                )
            ),
        }

    return result


def generate_coach_performance_report(
    history: list[dict],
) -> dict:
    """
    Generate overall AI Coach performance report.
    """

    analysis = analyse_decision_history(
        history,
    )

    total_decisions = len(
        history,
    )

    positive_results = sum(
        1
        for item in history
        if item.get(
            "outcome",
        )
        == "positive"
    )

    overall_success_rate = 0

    if total_decisions:

        overall_success_rate = int((positive_results / total_decisions) * 100)

    return {
        "total_decisions": total_decisions,
        "positive_outcomes": positive_results,
        "overall_success_rate": (overall_success_rate),
        "decision_analysis": analysis,
    }
