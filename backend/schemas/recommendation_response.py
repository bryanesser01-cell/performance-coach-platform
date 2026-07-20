from pydantic import BaseModel

from schemas.recommendation import Recommendation


class RecommendationResponse(BaseModel):
    recommendations: list[Recommendation]