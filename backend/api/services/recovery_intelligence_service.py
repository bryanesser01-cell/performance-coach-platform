class RecoveryIntelligenceService:
    """
    Calculates athlete recovery status.

    This service combines training load and
    athlete readiness metrics into a single
    recovery score.
    """

    def calculate_recovery_score(
        self,
        sleep_score: int,
        soreness_score: int,
        energy_score: int,
        motivation_score: int,
    ) -> float:
        """
        Calculate a simple recovery score.

        Returns a score between 0 and 100.
        """

        return (
            sleep_score + (100 - soreness_score) + energy_score + motivation_score
        ) / 4

    def analyse(
        self,
        sleep_score: int,
        soreness_score: int,
        energy_score: int,
        motivation_score: int,
    ) -> dict:
        """
        Analyse athlete recovery.
        """

        score = self.calculate_recovery_score(
            sleep_score=sleep_score,
            soreness_score=soreness_score,
            energy_score=energy_score,
            motivation_score=motivation_score,
        )

        if score >= 80:
            status = "ready"
            message = "Athlete is ready for hard training."
            recommendation = "Proceed with the planned hard session."

        elif score >= 60:
            status = "moderate"
            message = "Athlete is moderately recovered."
            recommendation = "Train at a moderate intensity and monitor recovery."

        else:
            status = "recovery"
            message = "Recovery should be prioritised."
            recommendation = "Prioritise recovery before the next hard session."

        #
        # Keep returning a dictionary for now.
        #
        return {
            "recovery_score": score,
            "status": status,
            "message": message,
            "recommendation": recommendation,
        }


#
# ------------------------------------------------------------------
# Legacy compatibility functions
# ------------------------------------------------------------------
#


def analyse_recovery_status(
    readiness_score: int,
    soreness_score: int | None = None,
    energy_score: int | None = None,
    motivation_score: int | None = None,
) -> dict:
    """
    Backwards-compatible API.
    """

    #
    # Legacy API
    #
    if soreness_score is None and energy_score is None and motivation_score is None:

        if readiness_score >= 80:
            status = "excellent"
            message = "Recovery is excellent."

        elif readiness_score >= 60:
            status = "good"
            message = "Recovery is good."

        elif readiness_score >= 40:
            status = "moderate"
            message = "Recovery is moderate."

        else:
            status = "poor"
            message = "Recovery is poor."

        return {
            "recovery_score": readiness_score,
            "status": status,
            "message": message,
        }

    #
    # New API
    #
    return RecoveryIntelligenceService().analyse(
        sleep_score=readiness_score,
        soreness_score=soreness_score,
        energy_score=energy_score,
        motivation_score=motivation_score,
    )


def generate_recovery_recommendation(
    recovery: int | dict,
) -> dict:
    """
    Generate a recovery recommendation.
    """

    if isinstance(
        recovery,
        int,
    ):
        recovery = analyse_recovery_status(
            recovery,
        )

    status = recovery.get(
        "status",
        "moderate",
    )

    if status == "excellent":

        recommendation = "Proceed with the planned hard session."

    elif status == "good":

        recommendation = "Training can continue as planned."

    elif status == "moderate":

        recommendation = "Train at a moderate intensity and monitor recovery."

    else:

        recommendation = "Prioritise recovery before the next hard session."

    return {
        "status": status,
        "message": recovery.get(
            "message",
            "",
        ),
        "recommendation": recommendation,
    }
