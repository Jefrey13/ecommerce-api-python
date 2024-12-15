from typing import List, Optional
from datetime import datetime
from models.Inventory import Inventory

inventory_db: List[Inventory] = []

def update_inventory(product_id: int, quantity: int) -> Optional[Inventory]:
    for inv in inventory_db:
        if inv.product_id == product_id:
            inv.quantity_available = quantity
            inv.last_updated = datetime.utcnow()
            return inv
    return None

def get_inventory() -> List[Inventory]:
    return inventory_db