from pydantic import BaseModel, Field


class AICoachResponseSchema(BaseModel):
    """
    Standard AI Coach API response contract.
    """

    success: bool = True

    athlete_id: int | None = None

    question: str | None = None

    coach_message: str

    decision: str | None = None

    recommendation: str | None = None

    confidence: int = Field(
        default=0,
        ge=0,
        le=100,
    )

    memory_used: bool = False

    learning_updated: bool = False

    strategy: str | None = None

    metadata: dict = {}
