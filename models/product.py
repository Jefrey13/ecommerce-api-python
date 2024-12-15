from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    stock: int
    category_id: int  # Relación con categorías