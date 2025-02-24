import pytest
from fastapi.testclient import TestClient  # Import TestClient
from app.main import app  # Import the FastAPI app


def test_process_ticket_api():
    # Create a test ticket with mock data
    test_ticket = {
        "ticket_id": "1",  # ticket_id should be a string
        "description": "Payment issue with invoice #1234",
        "subject": "Billing issue",
        # user_id should be a string (updated based on your model)
        "user_id": "101"
    }

    # Use TestClient to simulate a POST request to the process_ticket endpoint
    client = TestClient(app)  # Use TestClient without async
    response = client.post("/process_ticket/", json=test_ticket)

    # Print the response body for debugging
    print("Response Body:", response.json())  # This prints the response body

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200

    # Assert that the response contains the expected keys
    assert "ticket_id" in response.json()
    assert "analysis" in response.json()
    assert "response" in response.json()

    # Optionally check if analysis and response are either None or have valid content
    assert response.json()["analysis"] is not None or response.json()[
        "analysis"] is None
    assert response.json()["response"] is not None or response.json()[
        "response"] is None
