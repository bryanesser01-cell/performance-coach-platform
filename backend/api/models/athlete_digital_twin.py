from __future__ import annotations

from dataclasses import (
    dataclass,
    field,
)


@dataclass
class AthleteDigitalTwin:
    """
    Complete AI representation of an athlete.

    This object becomes the single source of truth
    used by the AI Coach.

    Every intelligence service contributes data to
    this model.

    Future versions will also include:

    - physiology
    - biomechanics
    - nutrition
    - sleep
    - psychology
    - wearable metrics
    """

    #
    # Athlete
    #
    athlete: dict = field(
        default_factory=dict,
    )

    #
    # Intelligence
    #
    goal_intelligence: dict = field(
        default_factory=dict,
    )

    performance_intelligence: dict = field(
        default_factory=dict,
    )

    recovery_intelligence: dict = field(
        default_factory=dict,
    )

    training_load_intelligence: dict = field(
        default_factory=dict,
    )

    race_intelligence: dict = field(
        default_factory=dict,
    )

    #
    # Memory
    #
    memory_context: dict = field(
        default_factory=dict,
    )

    memory_reasoning: dict = field(
        default_factory=dict,
    )

    #
    # Coach
    #
    decision_history: list = field(
        default_factory=list,
    )

    metadata: dict = field(
        default_factory=dict,
    )

    # ---------------------------------------------------------
    # Rich Domain Behaviours
    # ---------------------------------------------------------

    def readiness_score(
        self,
    ) -> int:
        """
        Returns the athlete readiness score.
        """

        return self.athlete.get(
            "readiness",
            {},
        ).get(
            "score",
            0,
        )

    def recovery_status(
        self,
    ) -> str:
        """
        Returns the recovery status.
        """

        return self.recovery_intelligence.get(
            "status",
            "",
        ).lower()

    def training_risk(
        self,
    ) -> str:
        """
        Returns training load risk.
        """

        return self.training_load_intelligence.get(
            "risk",
            "",
        ).lower()

    def race_phase(
        self,
    ) -> str:
        """
        Returns current race phase.
        """

        return self.race_intelligence.get(
            "phase",
            "",
        ).lower()

    def is_ready(
        self,
    ) -> bool:
        """
        Athlete is ready for a quality session.
        """

        return self.recovery_status() == "ready" or self.readiness_score() >= 80

    def needs_recovery(
        self,
    ) -> bool:
        """
        Returns True if recovery should
        be prioritised.
        """

        return (
            self.recovery_status() == "recovery"
            or self.training_risk() == "high"
            or self.readiness_score() < 40
        )

    def has_high_training_risk(
        self,
    ) -> bool:
        """
        Returns True if training load risk
        is high.
        """

        return self.training_risk() == "high"

    def is_goal_on_track(
        self,
    ) -> bool:
        """
        Returns whether the athlete is
        progressing towards their goal.
        """

        return self.goal_intelligence.get(
            "on_track",
            True,
        )

    def is_tapering(
        self,
    ) -> bool:
        """
        Returns True if athlete is currently
        in taper phase.
        """

        return self.race_phase() == "taper"

    def fatigue_trend(
        self,
    ) -> str:
        """
        Returns fatigue trend.
        """

        return self.memory_reasoning.get(
            "fatigue_trend",
            "stable",
        ).lower()

    def injury_risk(
        self,
    ) -> str:
        """
        Returns injury risk.
        """

        return self.memory_reasoning.get(
            "injury_risk",
            "low",
        ).lower()

    def is_improving(
        self,
    ) -> bool:
        """
        Returns True if performance is improving.
        """

        return self.performance_trend() == "improving"

    def goal(
        self,
    ) -> str:
        """
        Returns the athlete's primary goal.
        """

        return self.goal_intelligence.get(
            "goal",
            self.athlete.get(
                "primary_event",
                "",
            ),
        )

    def performance_trend(
        self,
    ) -> str:
        """
        Returns the current performance trend.
        """

        return (
            self.performance_intelligence.get(
                "trend",
            )
            or self.performance_intelligence.get(
                "performance_trend",
                {},
            ).get(
                "trend",
                "stable",
            )
        ).lower()

    def should_progress_training(
        self,
    ) -> bool:
        """
        Determines if training should
        progress.
        """

        return (
            self.is_ready()
            and self.is_goal_on_track()
            and self.is_improving()
            and not self.has_high_training_risk()
            and self.injury_risk() == "low"
        )
