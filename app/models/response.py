from pydantic import BaseModel
from typing import List


class ResponseSuggestion(BaseModel):
    response_text: str
    confidence_score: float
    requires_approval: bool
    suggested_actions: List[str]
