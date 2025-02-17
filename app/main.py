from fastapi import FastAPI
# Import ticket-related routes
from app.routes.tickets import router as tickets_router
from app.core.config import settings  # Import settings to use configurations

# Initialize FastAPI app
app = FastAPI(title="AI Ticket Support")

# Include ticket-related routes
app.include_router(tickets_router, prefix="/api/tickets", tags=["tickets"])

# Root endpoint for testing the API server


@app.get("/")
def root():
    return {"message": "AI Ticket Support API is running 🚀"}

# You can add other initialization or configurations here
