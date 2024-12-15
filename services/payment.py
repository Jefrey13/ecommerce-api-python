from typing import List
from datetime import datetime
from models.Payment import Payment

payments_db: List[Payment] = []

def create_payment(payment: Payment) -> Payment:
    payment.payment_date = datetime.utcnow()
    payments_db.append(payment)
    return payment

def get_payments_by_order(order_id: int) -> List[Payment]:
    return [payment for payment in payments_db if payment.order_id == order_id]