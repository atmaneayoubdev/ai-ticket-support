from typing import Optional, List
from pydantic import BaseModel
# Import if necessary for API models
from app.models.analysis import TicketAnalysis


class ApiResponseSuggestion(BaseModel):
    response_text: str
    confidence_score: float
    requires_approval: bool
    suggested_actions: List[str]


class ApiTicketResolution(BaseModel):
    ticket_id: str
    analysis: Optional[TicketAnalysis] = None
    response: Optional[ApiResponseSuggestion] = None
    error: Optional[str] = None
