from pydantic import BaseModel, Field


class FitnessSummarySchema(BaseModel):
    """
    Athlete fitness summary.
    """

    fitness_score: int = Field(
        default=0,
        ge=0,
        le=100,
    )

    trend: str = "unknown"

    improvement_score: int = Field(
        default=0,
        ge=0,
        le=100,
    )


class TrainingStatusSchema(BaseModel):
    """
    Current athlete training status.
    """

    status: str = "unknown"

    consistency_score: int = Field(
        default=0,
        ge=0,
        le=100,
    )


class RaceReadinessSchema(BaseModel):
    """
    Athlete race readiness assessment.
    """

    readiness_score: int = Field(
        default=0,
        ge=0,
        le=100,
    )

    confidence: int = Field(
        default=0,
        ge=0,
        le=100,
    )


class PredictionSchema(BaseModel):
    """
    Performance prediction output.
    """

    event: str | None = None

    predicted_time: str | None = None


class DashboardInsightSchema(BaseModel):
    """
    AI coaching insight.
    """

    current_status: str = "unknown"

    trend: str = "unknown"

    coaching_focus: dict = {}


class AthleteDashboardIntelligenceSchema(BaseModel):
    """
    Complete athlete dashboard intelligence response.
    """

    athlete_id: int

    fitness_summary: FitnessSummarySchema

    training_status: TrainingStatusSchema

    race_readiness: RaceReadinessSchema

    prediction: PredictionSchema

    scorecard: dict = {}

    timeline: dict = {}

    insight: DashboardInsightSchema
