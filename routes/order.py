from fastapi import APIRouter, HTTPException
from typing import List
from models.Order import Order
from services.order import (
    create_order,
    get_user_orders,
    update_order_status
)

router = APIRouter(prefix="/orders", tags=["orders"])

@router.post("/", response_model=Order)
def add_order(order: Order):
    try:
        return create_order(order)
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/user/{user_id}", response_model=List[Order])
def read_user_orders(user_id: int):
    try:
        orders = get_user_orders(user_id)
        if not orders:
            raise HTTPException(status_code=404, detail=f"No se encontraron órdenes para el usuario con ID {user_id}.")
        return orders
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/{order_id}/status", response_model=Order)
def modify_order_status(order_id: int, status: str):
    try:
        return update_order_status(order_id, status)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))