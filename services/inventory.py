import json
from typing import List, Optional
from datetime import datetime
from models.Inventory import Inventory

# Ruta del archivo que almacenará los datos
INVENTORY_FILE = "data/inventory.json"

def load_inventory() -> List[Inventory]:
    """Carga el inventario desde el archivo JSON con manejo de errores."""
    try:
        with open(INVENTORY_FILE, "r") as file:
            data = json.load(file)
            return [Inventory(**item) for item in data]
    except FileNotFoundError:
        # Si el archivo no existe, retorna una lista vacía y lo crea
        with open(INVENTORY_FILE, "w") as file:
            json.dump([], file)
        return []
    except json.JSONDecodeError as e:
        # Si el archivo tiene un formato incorrecto, lo reescribe vacío
        print(f"Error al decodificar JSON: {e}")
        with open(INVENTORY_FILE, "w") as file:
            json.dump([], file)
        return []

def save_inventory(inventory: List[Inventory]) -> None:
    """Guarda el inventario en el archivo JSON con manejo de errores."""
    try:
        with open(INVENTORY_FILE, "w") as file:
            json.dump([inv.dict() for inv in inventory], file, indent=4)
    except Exception as e:
        # Manejo de errores genéricos al guardar
        print(f"Error al guardar el inventario: {e}")
        raise RuntimeError("No se pudo guardar el inventario.")

def get_inventory() -> List[Inventory]:
    """Obtiene todos los registros del inventario."""
    try:
        return load_inventory()
    except Exception as e:
        print(f"Error al obtener el inventario: {e}")
        raise RuntimeError("No se pudo cargar el inventario.")

def create_inventory(product_id: int, quantity_available: int) -> Inventory:
    """Crea un nuevo registro en el inventario con validaciones."""
    try:
        inventory = load_inventory()

        # Validar si el producto ya existe
        if any(inv.product_id == product_id for inv in inventory):
            raise ValueError(f"El producto con ID {product_id} ya existe en el inventario.")

        new_item = Inventory(
            product_id=product_id,
            quantity_available=quantity_available,
            last_updated=datetime.utcnow()
        )
        inventory.append(new_item)
        save_inventory(inventory)
        return new_item
    except ValueError as e:
        print(e)
        raise
    except Exception as e:
        print(f"Error al crear un nuevo inventario: {e}")
        raise RuntimeError("No se pudo crear el registro en el inventario.")

def update_inventory(product_id: int, quantity: int) -> Optional[Inventory]:
    """Actualiza un registro existente en el inventario."""
    try:
        inventory = load_inventory()
        for inv in inventory:
            if inv.product_id == product_id:
                inv.quantity_available = quantity
                inv.last_updated = datetime.utcnow()
                save_inventory(inventory)
                return inv
        raise ValueError(f"No se encontró el producto con ID {product_id}.")
    except ValueError as e:
        print(e)
        raise
    except Exception as e:
        print(f"Error al actualizar el inventario: {e}")
        raise RuntimeError("No se pudo actualizar el inventario.")

def delete_inventory(product_id: int) -> bool:
    """Elimina un registro del inventario."""
    try:
        inventory = load_inventory()
        updated_inventory = [inv for inv in inventory if inv.product_id != product_id]

        if len(updated_inventory) == len(inventory):
            raise ValueError(f"No se encontró el producto con ID {product_id} para eliminar.")

        save_inventory(updated_inventory)
        return True
    except ValueError as e:
        print(e)
        raise
    except Exception as e:
        print(f"Error al eliminar del inventario: {e}")
        raise RuntimeError("No se pudo eliminar el registro del inventario.")