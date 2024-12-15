from datetime import datetime
from pydantic import BaseModel


class Review(BaseModel):
    id: int
    user_id: int
    product_id: int
    rating: int  # 1 a 5
    comment: str
    created_at: datetime