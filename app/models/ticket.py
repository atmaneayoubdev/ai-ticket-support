from pydantic import BaseModel
from typing import Optional


class SupportTicket(BaseModel):
    id: str
    subject: str
    description: str
    user_id: str
    # You can adjust this based on actual data
    created_at: Optional[str] = None
