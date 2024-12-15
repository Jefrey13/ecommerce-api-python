from datetime import datetime
from pydantic import BaseModel

class Order(BaseModel):
    id: int
    user_id: int
    total_amount: float
    created_at: datetime
    status: str  # e.g., "Pending", "Paid", "Shipped", "Delivered", "Cancelled"