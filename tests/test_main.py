# tests/test_main.py

import httpx
import pytest


@pytest.mark.asyncio
async def test_root():
    """Test if the root endpoint returns the correct message"""
    async with httpx.AsyncClient(base_url="http://127.0.0.1:8000") as client:
        response = await client.get("/")
        assert response.status_code == 200
        assert response.json() == {
            "message": "AI Ticket Support API is running 🚀"}


@pytest.mark.asyncio
async def test_api_health():
    """Test if the /api/tickets endpoint is reachable"""
    async with httpx.AsyncClient(base_url="http://127.0.0.1:8000") as client:
        response = await client.get("/api/tickets/")
    assert response.status_code == 200  # Endpoint should return 200 OK
