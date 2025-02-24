from fastapi import HTTPException
from fastapi import FastAPI, HTTPException

from app.agents.ticket_processor import TicketProcessor
from app.models.api import ApiTicketResolution
from app.models.ticket import SupportTicket

from app.core.logging import get_logger
logger = get_logger()

app = FastAPI(title="AI Ticket Support")


# Initialize the ticket processor
ticket_processor = TicketProcessor()


@app.get("/")
def root():
    return {"message": "AI Ticket Support API is running 🚀"}


@app.post("/process_ticket/", response_model=ApiTicketResolution)
async def process_ticket(ticket: SupportTicket):
    # Step 1: Initialize the ticket processor
    # write log using fast api logger
    logger.info(f"initilizing ticket processor")
    processor = TicketProcessor()

    try:
        logger.info(f"Processing ticket: {ticket.id}")
        # Step 2: Process the ticket using the processor (this will call the analyze and response generation agents)
        resolution = await processor.process_ticket(ticket)

        logger.info(f"Ticket processed successfully final ")

        # Step 3: Return the processed ticket resolution (which includes analysis and response)
        return ApiTicketResolution(
            ticket_id=resolution.ticket_id,
            analysis=resolution.analysis,  # Directly return Pydantic model instance
            response=resolution.response,  # and this one as well
        )

    except Exception as e:
        logger.info(f"Error processing ticket: {str(e)})")

        # Handle any errors that might occur during processing
        raise HTTPException(

            status_code=500, detail=f"Error processing ticket: {str(e)}")
