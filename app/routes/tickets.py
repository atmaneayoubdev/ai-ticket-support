# app/routes/tickets.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.agents.ticket_analysis_agent import TicketAnalysisAgent
from app.agents.response_generation_agent import ResponseAgent
from app.models.analysis import TicketAnalysis
from app.models.response import ResponseSuggestion
from app.models.ticket import Ticket, CustomerInfo
from typing import Dict, Any

router = APIRouter()

# Request model for analyzing a ticket


class TicketContent(BaseModel):
    ticket_content: str
    customer_info: CustomerInfo  # Use the CustomerInfo model for validation

# Request model for generating a response


class TicketAnalysisInput(BaseModel):
    ticket_analysis: Dict[str, Any]
    response_templates: Dict[str, str]
    context: Dict[str, Any]

# Ticket Analysis Endpoint


@router.post("/analyze", response_model=TicketAnalysis)
async def analyze_ticket(ticket_data: TicketContent):
    agent = TicketAnalysisAgent()

    try:
        # Perform ticket analysis
        ticket_analysis: TicketAnalysis = await agent.analyze_ticket(ticket_data.ticket_content, ticket_data.customer_info)
        return ticket_analysis
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Response Generation Endpoint


@router.post("/generate-response", response_model=ResponseSuggestion)
async def generate_response(ticket_data: TicketAnalysisInput):
    agent = ResponseAgent()

    try:
        # Generate response based on the ticket analysis
        response_suggestion: ResponseSuggestion = await agent.generate_response(
            ticket_data.ticket_analysis,
            ticket_data.response_templates,
            ticket_data.context
        )
        return response_suggestion
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Sample health check endpoint


@router.get("/")
async def get_tickets():
    return {"message": "Tickets API is running!"}
