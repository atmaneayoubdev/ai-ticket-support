# tests/test_response_generation.py

import pytest
from app.agents.response_generation_agent import ResponseAgent
from app.models.analysis import TicketCategory, Priority, TicketAnalysis


@pytest.mark.asyncio
async def test_response_generation():
    # Sample ticket analysis
    ticket_analysis = TicketAnalysis(
        category=TicketCategory.ACCESS,
        priority=Priority.HIGH,
        key_points=["User cannot access the dashboard", "403 error"],
        required_expertise=["System Admin"],
        sentiment=0.2,
        urgency_indicators=["ASAP"],
        business_impact="High business impact due to access issue",
        suggested_response_type="Technical support"
    )

    context = {
        "name": "John Doe",
        "feature": "admin dashboard",
        "eta": "2 hours"
    }

    agent = ResponseAgent()

    # Call generate_response with a dummy response template dictionary
    response_suggestion = await agent.generate_response(ticket_analysis, response_templates={"access_issue": "Hello {name}, there is an issue with {feature}. Diagnosis: {diagnosis}. Next Steps: {next_steps}. ETA: {eta}"}, context=context)

    # Simple assertion to verify if we got a response
    assert "Hello John Doe" in response_suggestion.response_text
    assert "Permission issue detected" in response_suggestion.response_text
    assert "Check user permissions." in response_suggestion.response_text  # Should match now
