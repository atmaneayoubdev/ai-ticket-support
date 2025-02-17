from typing import Any, Dict
from app.core.openai_utils import generate_response_with_gpt
from app.models.response import ResponseSuggestion


class ResponseAgent:
    async def generate_response(
        self,
        ticket_analysis: dict,
        response_templates: Dict[str, str],
        context: Dict[str, Any]
    ) -> ResponseSuggestion:
        """
        Generate a response based on ticket analysis and customer context.
        """

        # Use GPT to generate a response dynamically
        gpt_prompt = f"Generate a customer support response for a ticket that falls under {ticket_analysis['suggested_response_type']} category. The ticket content is: {ticket_analysis['key_points']} and the customer's role is {context.get('customer_role', 'User')}."

        response_text = generate_response_with_gpt(gpt_prompt)

        # You can enhance further by adjusting response logic based on response_text
        confidence_score = 0.9  # Dummy value, you can calculate confidence based on some criteria
        requires_approval = False
        suggested_actions = [
            "Escalate to Admin"] if ticket_analysis["priority"] == "URGENT" else []

        return ResponseSuggestion(response_text, confidence_score, requires_approval, suggested_actions)
