from typing import Optional
from app.core.openai_utils import generate_response_with_gpt
from app.models.analysis import TicketAnalysis, TicketCategory, Priority


class TicketAnalysisAgent:
    async def analyze_ticket(
        self,
        ticket_content: str,
        customer_info: Optional[dict] = None
    ) -> TicketAnalysis:
        """
        Analyze a ticket to classify its category, assess its priority, and extract key points.

        Requirements:
        1. Identify ticket category based on content and subject.
        2. Determine priority using urgency words, customer role, and business impact.
        3. Extract key points from the ticket content.
        """

        # Use GPT to analyze the ticket content for more sophisticated insights
        gpt_analysis_prompt = f"Analyze the following ticket and categorize it into one of the following categories: Technical Issue, Billing Question, Feature Request, Account Access. Also, assess the priority based on urgency, role, and business impact. Extract key points and suggest required expertise.\n\nTicket content: {ticket_content}"

        gpt_analysis = generate_response_with_gpt(gpt_analysis_prompt)

        # Parse GPT's response for further analysis (this could be extended as needed)
        if "Technical Issue" in gpt_analysis:
            category = TicketCategory.TECHNICAL
        elif "Billing Question" in gpt_analysis:
            category = TicketCategory.BILLING
        elif "Feature Request" in gpt_analysis:
            category = TicketCategory.FEATURE
        else:
            category = TicketCategory.ACCESS

        # Dummy priority based on GPT response (you can refine this logic)
        priority = Priority.URGENT if "ASAP" in ticket_content else Priority.MEDIUM

        # You can refine further based on GPT response
        key_points = ["Key point identified by GPT"]
        required_expertise = [
            "Technical Support"] if category == TicketCategory.TECHNICAL else ["Billing Support"]

        sentiment = 0.85  # Dummy sentiment score
        urgency_indicators = ["ASAP"] if "ASAP" in ticket_content else []
        business_impact = "High"  # Example impact, could be extended based on content
        suggested_response_type = "access_issue" if category == TicketCategory.ACCESS else "billing_inquiry"

        return TicketAnalysis(
            category=category,
            priority=priority,
            key_points=key_points,
            required_expertise=required_expertise,
            sentiment=sentiment,
            urgency_indicators=urgency_indicators,
            business_impact=business_impact,
            suggested_response_type=suggested_response_type
        )
