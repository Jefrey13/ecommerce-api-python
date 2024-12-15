from pydantic import BaseModel

class CartItem(BaseModel):
    user_id: int
    product_id: int
    quantity: int