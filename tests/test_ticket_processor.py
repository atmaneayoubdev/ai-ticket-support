from app.agents.ticket_processor import TicketProcessor
from app.models.analysis import TicketAnalysis
import pytest
from unittest.mock import AsyncMock
from app.models.ticket import SupportTicket
from app.models.response import ResponseSuggestion, TicketResolution
from app.agents.ticket_analysis_agent import TicketAnalysisAgent
from app.agents.response_generation_agent import ResponseAgent


@pytest.mark.asyncio
async def test_process_ticket_billing_issue():
    # Step 1: Create a mock SupportTicket with all required fields
    ticket = SupportTicket(
        id="1",  # Pass as string
        subject="Billing issue",
        user_id="123",  # Pass as string
        description="Payment issue with invoice #1234"
    )

    # Step 2: Create actual instances of the agents
    analysis_agent = TicketAnalysisAgent()
    response_agent = ResponseAgent()

    # Mock the behavior of the actual agents
    analysis_agent.analyze_ticket = AsyncMock(return_value=TicketAnalysis(
        category="BILLING",
        priority="MEDIUM",
        key_points=["Payment issue with invoice #1234"],
        required_expertise=["Billing Specialist"],
        sentiment=1.0,
        urgency_indicators=[],
        business_impact="Billing issue",
        suggested_response_type="standard"
    ))

    response_agent.generate_response = AsyncMock(return_value=ResponseSuggestion(
        response_text="Please contact billing support for assistance.",
        confidence_score=0.9,
        requires_approval=False,
        suggested_actions=["Follow up with customer"]
    ))

    # Step 3: Initialize the processor and process the ticket
    processor = TicketProcessor()
    resolution = await processor.process_ticket(ticket)

    # Step 4: Validate the returned resolution
    assert resolution.ticket_id == ticket.id  # Check ticket ID
    assert resolution.analysis.category == "BILLING"  # Ensure correct category
    # Check response text
    assert resolution.response.response_text == "Please contact billing support for assistance."
    assert resolution.response.confidence_score == 0.9  # Check confidence score
