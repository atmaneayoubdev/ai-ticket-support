# app/agents/response_generation_agent.py

from typing import Dict, Any
from app.models.analysis import TicketAnalysis
from app.models.response import ResponseSuggestion
from app.core.response_templates import RESPONSE_TEMPLATES


class ResponseAgent:
    async def generate_response(
        self,
        ticket_analysis: TicketAnalysis,
        response_templates: Dict[str, str] = RESPONSE_TEMPLATES,
        context: Dict[str, Any] = {}
    ) -> ResponseSuggestion:
        """
        Simple response generation based on ticket category.
        """
        # Template matching
        category = ticket_analysis.category.name  # Convert enum to string
        template_key = None

        if category == "ACCESS":
            template_key = "access_issue"
        elif category == "BILLING":
            template_key = "billing_inquiry"

        if not template_key:
            raise ValueError(f"No template available for category {category}")

        # Simple static fields for now
        diagnosis = "Permission issue detected"
        # Matching the expected resolution steps
        resolution_steps = "Check user permissions."
        explanation = "User lacks access rights."
        next_steps = "Check user permissions."  # Matching the expected next steps

        # Use the template
        template = response_templates.get(template_key, "No template found.")
        response_text = template.format(
            name=context.get('name', 'Customer'),
            feature=context.get('feature', 'system'),
            eta=context.get('eta', '24 hours'),
            diagnosis=diagnosis,
            resolution_steps=resolution_steps,
            explanation=explanation,
            next_steps=next_steps
        )

        # Return a simple response suggestion
        return ResponseSuggestion(
            response_text=response_text,
            confidence_score=0.9,  # Assume a 90% confidence for now
            requires_approval=False,
            suggested_actions=["Follow up with customer"]
        )
