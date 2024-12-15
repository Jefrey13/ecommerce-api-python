from typing import List
from models.product import Product
from models.Cart import CartItem

cart_db: List[CartItem] = []

def add_to_cart(item: CartItem) -> CartItem:
    cart_db.append(item)
    return item

def get_user_cart(user_id: int) -> List[CartItem]:
    return [item for item in cart_db if item.user_id == user_id]

def remove_from_cart(user_id: int, product_id: int) -> bool:
    for idx, item in enumerate(cart_db):
        if item.user_id == user_id and item.product_id == product_id:
            del cart_db[idx]
            return True
    return False