def calculate_strategy_confidence(
    success_rate: int,
    learning_confidence: int = 50,
) -> int:
    """
    Calculate final confidence for a coaching strategy.

    Combines:
    - Historical success rate
    - Existing AI learning confidence
    """

    confidence = (
        success_rate
        + learning_confidence
    ) // 2

    return max(
        0,
        min(
            confidence,
            100,
        ),
    )


def select_best_coaching_strategy(
    decision_analysis: dict,
) -> dict:
    """
    Select the best historical coaching strategy.

    Uses highest success rate.
    """

    if not decision_analysis:

        return {
            "decision": None,
            "success_rate": 0,
        }

    best_decision = None
    best_rate = -1

    for decision, data in decision_analysis.items():

        success_rate = data.get(
            "success_rate",
            0,
        )

        if success_rate > best_rate:

            best_rate = success_rate
            best_decision = decision

    return {
        "decision": best_decision,
        "success_rate": best_rate,
    }


def optimise_future_decision(
    proposed_decision: str,
    decision_analysis: dict,
    learning_confidence: int = 50,
) -> dict:
    """
    Optimise future AI Coach decision.

    Compares proposed decision against
    historical successful strategies.
    """

    best_strategy = select_best_coaching_strategy(
        decision_analysis,
    )

    selected_decision = proposed_decision

    if (
        best_strategy["decision"]
        and best_strategy["success_rate"]
        >
        decision_analysis.get(
            proposed_decision,
            {},
        ).get(
            "success_rate",
            0,
        )
    ):

        selected_decision = (
            best_strategy["decision"]
        )

    confidence = calculate_strategy_confidence(
        success_rate=decision_analysis.get(
            selected_decision,
            {},
        ).get(
            "success_rate",
            0,
        ),
        learning_confidence=learning_confidence,
    )

    return {
        "recommended_decision": selected_decision,
        "confidence": confidence,
        "reason": (
            "Decision selected using "
            "historical coaching success."
        ),
    }


def generate_strategy_optimisation_report(
    decision_analysis: dict,
) -> dict:
    """
    Generate coaching strategy insights.
    """

    best_strategy = select_best_coaching_strategy(
        decision_analysis,
    )

    return {
        "best_strategy": best_strategy[
            "decision"
        ],
        "success_rate": best_strategy[
            "success_rate"
        ],
        "available_strategies": len(
            decision_analysis,
        ),
    }
