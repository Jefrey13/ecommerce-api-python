from fastapi import APIRouter
from typing import List
from models.Inventory import Inventory
from services.inventory import update_inventory, get_inventory

router = APIRouter()

@router.put("/inventory/{product_id}", response_model=Inventory, tags=["inventory"])
def update_stock(product_id: int, quantity: int):
    return update_inventory(product_id, quantity)

@router.get("/inventory", response_model=List[Inventory], tags=["inventory"])
def read_inventory():
    return get_inventory()