from typing import List, Optional
from datetime import datetime
from models.Order import Order

orders_db: List[Order] = []

def create_order(order: Order) -> Order:
    order.created_at = datetime.utcnow()
    orders_db.append(order)
    return order

def get_user_orders(user_id: int) -> List[Order]:
    return [order for order in orders_db if order.user_id == user_id]

def update_order_status(order_id: int, status: str) -> Optional[Order]:
    for order in orders_db:
        if order.id == order_id:
            order.status = status
            return order
    return None