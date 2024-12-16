from fastapi import APIRouter, HTTPException
from typing import List
from models.Cart import CartItem
from services.cart import (
    add_to_cart,
    get_user_cart,
    remove_from_cart
)

router = APIRouter(prefix="/cart", tags=["cart"])

@router.post("/", response_model=CartItem)
def add_item_to_cart(item: CartItem):
    try:
        return add_to_cart(item)
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{user_id}", response_model=List[CartItem])
def read_user_cart(user_id: int):
    try:
        user_cart = get_user_cart(user_id)
        if not user_cart:
            raise HTTPException(status_code=404, detail=f"El carrito del usuario con ID {user_id} está vacío.")
        return user_cart
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{user_id}/{product_id}", status_code=204)
def remove_item_from_cart(user_id: int, product_id: int):
    try:
        if remove_from_cart(user_id, product_id):
            return {"detail": f"Producto con ID {product_id} eliminado del carrito del usuario con ID {user_id}."}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))