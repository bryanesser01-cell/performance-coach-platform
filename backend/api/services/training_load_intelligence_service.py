class TrainingLoadIntelligenceService:
    """
    Calculates training load metrics.
    """

    def calculate_acute_load(
        self,
        activities: list[dict],
    ) -> int:
        """
        Acute Training Load (ATL).
        """

        return sum(
            activity.get(
                "training_stress",
                0,
            )
            for activity in activities
        )

    def calculate_chronic_load(
        self,
        activities: list[dict],
    ) -> int:
        """
        Chronic Training Load (CTL).
        """

        return sum(
            activity.get(
                "training_stress",
                0,
            )
            for activity in activities
        )

    def calculate_acwr(
        self,
        acute_load: float,
        chronic_load: float,
    ) -> float:
        """
        Acute : Chronic Workload Ratio.
        """

        if chronic_load == 0:
            return 0.0

        return acute_load / chronic_load

    def analyse(
        self,
        activities: list[dict],
    ) -> dict:

        acute_load = self.calculate_acute_load(
            activities,
        )

        chronic_load = self.calculate_chronic_load(
            activities,
        )

        acwr = self.calculate_acwr(
            acute_load=acute_load,
            chronic_load=chronic_load,
        )

        weekly_load = self.calculate_weekly_load(
            activities,
        )

        monthly_load = self.calculate_monthly_load(
            activities,
        )

        fatigue_score = self.calculate_fatigue_score(
            acute_load=acute_load,
            chronic_load=chronic_load,
        )

        return {
            "acute_load": acute_load,
            "chronic_load": chronic_load,
            "weekly_load": weekly_load,
            "monthly_load": monthly_load,
            "acwr": acwr,
            "fatigue_score": fatigue_score,
        }

    def calculate_weekly_load(
        self,
        activities: list[dict],
    ) -> int:
        """
        Calculate total weekly training load.

        For now this sums the supplied
        activities. Later it will use
        activity dates to filter the last
        seven days.
        """

        return sum(
            activity.get(
                "training_stress",
                0,
            )
            for activity in activities
        )

    def calculate_monthly_load(
        self,
        activities: list[dict],
    ) -> int:
        """
        Calculate total monthly training load.

        Currently sums the supplied activities.
        Later this will use activity dates to
        calculate a rolling 28-day load.
        """

        return sum(
            activity.get(
                "training_stress",
                0,
            )
            for activity in activities
        )

    def calculate_fatigue_score(
        self,
        acute_load: float,
        chronic_load: float,
    ) -> float:
        """
        Estimate fatigue using the ratio of
        acute to chronic training load.

        Returns a score between 0 and 100.
        """

        if chronic_load == 0:
            return 0.0

        fatigue = (acute_load / chronic_load) * 100

        return min(
            fatigue,
            100.0,
        )
