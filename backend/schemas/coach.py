from typing import Any

from pydantic import BaseModel

from schemas.analysis import PerformanceAnalysis
from schemas.recommendation import Recommendation
from schemas.workout import WorkoutRecommendation


class CoachResponse(BaseModel):
    analysis: PerformanceAnalysis
    workout: WorkoutRecommendation
    recommendations: list[Recommendation]
    insights: dict[str, Any]
