from fastapi import APIRouter, HTTPException
from typing import List
from models.Cart import CartItem
from services.cart import add_to_cart, get_user_cart, remove_from_cart

router = APIRouter()

@router.post("/cart", tags=["cart"])
def add_item_to_cart(item: CartItem):
    return add_to_cart(item)

@router.get("/cart/{user_id}", response_model=List[CartItem], tags=["cart"])
def read_user_cart(user_id: int):
    return get_user_cart(user_id)

@router.delete("/cart/{user_id}/{product_id}", tags=["cart"])
def delete_item_from_cart(user_id: int, product_id: int):
    if not remove_from_cart(user_id, product_id):
        raise HTTPException(status_code=404, detail="Item not found in cart")
    return {"message": "Item removed successfully"}