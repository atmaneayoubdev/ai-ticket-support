from app.agents.ticket_analysis_agent import TicketAnalysisAgent
from app.agents.response_generation_agent import ResponseAgent
from app.models.analysis import Priority, TicketAnalysis, TicketCategory
from app.models.ticket import SupportTicket
from app.models.response import ResponseSuggestion, TicketResolution
from app.core.logging import get_logger


class TicketProcessor:
    def __init__(self):
        # Initialize agents
        # self.analysis_agent = TicketAnalysisAgent()
        # self.response_agent = ResponseAgent()
        # self.context = {}

        # Get the logger
        self.logger = get_logger()
        self.logger.info('TicketProcessor initialized')

    async def process_ticket(self, ticket: SupportTicket) -> TicketResolution:
        self.logger.info(f'Start processing ticket {ticket.id}')

        # Perform analysis to create TicketAnalysis
        analysis = TicketAnalysis(
            category=TicketCategory.BILLING,  # mock category
            priority=Priority.MEDIUM,   # mock priority
            key_points=["Payment issue with invoice #1234"],  # mock key points
            required_expertise=["Billing Specialist"],  # mock expertise
            sentiment=1.0,  # mock sentiment score
            urgency_indicators=[],  # no urgency
            business_impact="Billing issue",  # mock business impact
            suggested_response_type="standard"  # mock response type
        )
        self.logger.debug(f'Ticket analysis completed: {analysis}')

        # Now pass the TicketAnalysis object to the response agent
        response = ResponseSuggestion(
            response_text="Please contact billing support for assistance.",
            confidence_score=0.9,
            requires_approval=False,
            suggested_actions=["Follow up with customer"]
        )
        self.logger.debug(f'Response generated: {response}')

        # Return the TicketResolution with analysis and response
        resolution = TicketResolution(
            ticket_id=ticket.id,
            analysis=analysis,
            response=response
        )

        self.logger.info(f'Ticket processing completed for ticket {ticket.id}')
        return resolution
