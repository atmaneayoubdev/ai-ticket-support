from typing import List, Optional
from pydantic import BaseModel
from app.models.analysis import TicketAnalysis


class ResponseSuggestion(BaseModel):
    response_text: str
    confidence_score: float
    requires_approval: bool
    suggested_actions: List[str]


class TicketResolution(BaseModel):
    ticket_id: str
    analysis: Optional[TicketAnalysis]
    response: Optional[ResponseSuggestion]
    error: Optional[str] = None
