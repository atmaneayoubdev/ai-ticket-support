import re
from typing import Optional, Dict, Any
from app.models.analysis import TicketCategory, Priority, TicketAnalysis


class TicketAnalysisAgent:
    def __init__(self):
        self.urgency_keywords = ["ASAP", "urgent",
                                 "immediately", "critical", "high priority", "as soon as possible"]
        self.high_priority_roles = ["Director", "C-level", "Manager", "Admin"]

    async def analyze_ticket(
        self,
        ticket_content: str,
        customer_info: Optional[Dict[str, Any]] = None
    ) -> TicketAnalysis:
        category = self.classify_ticket(ticket_content)
        priority, urgency_indicators, business_impact = self.assess_priority(
            ticket_content, customer_info)
        key_points = self.extract_key_points(ticket_content)
        sentiment = self.analyze_sentiment(ticket_content)
        required_expertise = self.determine_expertise(category)
        suggested_response_type = "detailed" if priority.value >= Priority.HIGH.value else "standard"

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

    def classify_ticket(self, ticket_content: str) -> TicketCategory:
        content = ticket_content.lower()

        if "billing" in content or "invoice" in content:
            return TicketCategory.BILLING
        if "feature request" in content or "new feature" in content:
            return TicketCategory.FEATURE
        if any(keyword in content for keyword in ["log in", "account access", "dashboard", "403 error"]):
            return TicketCategory.ACCESS
        return TicketCategory.TECHNICAL

    # type: ignore
    def assess_priority(self, content: str, customer_info: Optional[Dict[str, Any]]) -> (Priority, list, str):
        """Determines priority based on urgency and customer role."""
        urgency_indicators = [
            word for word in self.urgency_keywords if word.lower() in content.lower()]
        business_impact = "Normal"

        priority = Priority.LOW  # Default priority
        # Ensure billing-related tickets get MEDIUM priority, but only if no other overriding conditions
        if any(keyword in content.lower() for keyword in ["billing", "invoice"]):
            priority = Priority.MEDIUM
            business_impact = "Billing issue"
        elif "payroll" in content.lower():
            priority = Priority.URGENT
            business_impact = "Payroll issue"

        # Check for urgency based on keywords
        if urgency_indicators:
            priority = Priority.URGENT

        # Check for high-priority roles that should escalate the priority
        if customer_info and customer_info.get("role") in self.high_priority_roles:
            if "ASAP" in urgency_indicators:
                # Ensure that urgent role-based tickets are handled with highest priority
                priority = Priority.URGENT
            else:
                priority = Priority.HIGH  # Other high-priority roles, even without urgency indicators

        return priority, urgency_indicators, business_impact

    def extract_key_points(self, content: str) -> list:
        """Extracts key points from the ticket."""
        sentences = [s.strip() for s in content.split("\n") if s.strip()]
        return sentences[:3]  # First 3 lines as key points

    def analyze_sentiment(self, content: str) -> float:
        """Simple sentiment analysis (placeholder)."""
        negative_words = ["frustrated", "angry", "unacceptable"]
        return -1.0 if any(word in content.lower() for word in negative_words) else 1.0

    def determine_expertise(self, category: TicketCategory) -> list:
        """Determines required expertise for the ticket."""
        expertise_map = {
            TicketCategory.TECHNICAL: ["Support Engineer"],
            TicketCategory.BILLING: ["Billing Specialist"],
            TicketCategory.FEATURE: ["Product Manager"],
            TicketCategory.ACCESS: ["IT Support"]
        }
        return expertise_map.get(category, ["General Support"])
