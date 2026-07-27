from pydantic import BaseModel, Field


class PerformanceAnalysis(BaseModel):
    total_sessions: int
    total_distance: float
    total_duration: float
    average_pace: float
    average_heart_rate: float
    average_rpe: float
    total_training_load: float
    longest_run: float

    coach_comment: str

    strengths: list[str] = Field(default_factory=list)
    risks: list[str] = Field(default_factory=list)
    recommendations: list[str] = Field(default_factory=list)
