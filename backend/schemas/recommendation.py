from pydantic import BaseModel


class Recommendation(BaseModel):
    priority: int
    category: str
    title: str
    description: str
