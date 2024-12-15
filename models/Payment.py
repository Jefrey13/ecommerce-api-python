from datetime import datetime
from pydantic import BaseModel


class Payment(BaseModel):
    id: int
    order_id: int
    payment_method: str  # e.g., "Credit Card", "PayPal"
    payment_date: datetime
    amount: float