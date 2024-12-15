from fastapi import APIRouter
from typing import List
from models.Payment import Payment
from services.payment import create_payment, get_payments_by_order

router = APIRouter()

@router.post("/payments", response_model=Payment, tags=["payments"])
def create_payment_endpoint(payment: Payment):
    return create_payment(payment)

@router.get("/payments/{order_id}", response_model=List[Payment], tags=["payments"])
def get_payments(order_id: int):
    return get_payments_by_order(order_id)