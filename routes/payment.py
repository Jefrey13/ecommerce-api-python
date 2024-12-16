from fastapi import APIRouter, HTTPException
from typing import List
from models.Payment import Payment
from services.payment import (
    create_payment,
    get_payments_by_order
)

router = APIRouter(prefix="/payments", tags=["payments"])

@router.post("/", response_model=Payment)
def add_payment(payment: Payment):
    try:
        return create_payment(payment)
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/order/{order_id}", response_model=List[Payment])
def read_payments_by_order(order_id: int):
    try:
        payments = get_payments_by_order(order_id)
        if not payments:
            raise HTTPException(status_code=404, detail=f"No se encontraron pagos para la orden con ID {order_id}.")
        return payments
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))