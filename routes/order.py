from fastapi import APIRouter, HTTPException
from typing import List
from models.Order import Order
from services.order import create_order, get_user_orders, update_order_status

router = APIRouter()

@router.post("/orders", response_model=Order, tags=["orders"])
def create_new_order(order: Order):
    return create_order(order)

@router.get("/orders/{user_id}", response_model=List[Order], tags=["orders"])
def read_user_orders(user_id: int):
    return get_user_orders(user_id)

@router.put("/orders/{order_id}/{status}", tags=["orders"])
def update_order_status_endpoint(order_id: int, status: str):
    updated_order = update_order_status(order_id, status)
    if not updated_order:
        raise HTTPException(status_code=404, detail="Order not found")
    return updated_order