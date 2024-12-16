from fastapi import APIRouter, HTTPException
from typing import List
from models.Inventory import Inventory
from services.inventory import (
    create_inventory,
    update_inventory,
    delete_inventory,
    get_inventory,
)

router = APIRouter(prefix="/inventory", tags=["inventory"])


@router.get("/", response_model=List[Inventory])
def read_inventory():
    try:
        inventory = get_inventory()
        if not inventory:
            raise HTTPException(status_code=404, detail="No se encontraron productos en el inventario.")
        return inventory
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/", response_model=Inventory)
def create_stock(product_id: int, quantity_available: int):
    try:
        return create_inventory(product_id, quantity_available)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/{product_id}", response_model=Inventory)
def update_stock(product_id: int, quantity: int):
    try:
        updated_inventory = update_inventory(product_id, quantity)
        if updated_inventory is None:
            raise HTTPException(status_code=404, detail=f"Producto con ID {product_id} no encontrado.")
        return updated_inventory
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{product_id}", status_code=204)
def delete_stock(product_id: int):
    try:
        if delete_inventory(product_id):
            return {"detail": f"Producto con ID {product_id} eliminado exitosamente."}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))