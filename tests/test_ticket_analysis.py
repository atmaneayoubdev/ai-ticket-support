import httpx
import pytest

SAMPLE_TICKETS = [
    {
        "ticket_content": """
        Hi Support,
        Since this morning I can't access the admin dashboard. I keep getting a 403 error.
        I need this fixed ASAP as I need to process payroll today.
        
        Thanks,
        John Smith
        Finance Director
        """,
        "customer_info": {
            "role": "Admin",
            "plan": "Enterprise",
            "company_size": "250+"
        }
    },
    {
        "ticket_content": """
        Hello,
        Our invoice shows billing from the 15th but we signed up on the 20th.
        Can you explain how the pro-rating works?
        
        Best regards,
        Sarah Jones
        """,
        "customer_info": {
            "role": "Billing Admin",
            "plan": "Professional",
            "company_size": "50-249"
        }
    }
]


@pytest.mark.asyncio
async def test_analyze_ticket_1():
    """Test ticket analysis for a technical issue (Access Issue)"""
    async with httpx.AsyncClient(base_url="http://127.0.0.1:8000") as client:
        payload = SAMPLE_TICKETS[0]  # TKT-001
        response = await client.post("/api/tickets/analyze", json=payload)

    assert response.status_code == 200
    analysis = response.json()

    # Check for expected analysis values
    assert analysis["category"] == "access"
    assert analysis["priority"] == "urgent"
    assert "key_points" in analysis
    assert analysis["key_points"] == [
        "Cannot access admin dashboard",
        "403 error",
        "Need fix ASAP"
    ]
    assert analysis["required_expertise"] == ["Technical Support"]
    assert analysis["business_impact"] == "High"
    assert analysis["sentiment"] > 0  # Sentiment should be positive
    assert analysis["urgency_indicators"] == ["ASAP"]


@pytest.mark.asyncio
async def test_analyze_ticket_2():
    """Test ticket analysis for a billing issue (Billing Question)"""
    async with httpx.AsyncClient(base_url="http://127.0.0.1:8000") as client:
        payload = SAMPLE_TICKETS[1]  # TKT-002
        response = await client.post("/api/tickets/analyze", json=payload)

    assert response.status_code == 200
    analysis = response.json()

    # Check for expected analysis values
    assert analysis["category"] == "billing"
    assert analysis["priority"] == "medium"
    assert "key_points" in analysis
    assert analysis["key_points"] == [
        "Billing cycle discrepancy",
        "Pro-rating question"
    ]
    assert analysis["required_expertise"] == ["Billing Support"]
    assert analysis["business_impact"] == "Medium"
    assert analysis["sentiment"] > 0  # Sentiment should be positive
    assert analysis["urgency_indicators"] == []  # No urgent markers
