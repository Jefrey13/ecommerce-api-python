from datetime import datetime
from pydantic import BaseModel


class Inventory(BaseModel):
    product_id: int
    quantity_available: int
    last_updated: datetime