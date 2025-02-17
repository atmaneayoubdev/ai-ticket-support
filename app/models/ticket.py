from pydantic import BaseModel
from typing import Optional


class CustomerInfo(BaseModel):
    role: str
    plan: str
    company_size: str


class Ticket(BaseModel):
    id: str
    subject: str
    content: str
    customer_info: CustomerInfo
