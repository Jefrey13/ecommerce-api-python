import json
from typing import List, Optional
from datetime import datetime
from models.Order import Order

# Ruta del archivo donde se almacenarán las órdenes
ORDERS_FILE = "data/orders.json"


# Funciones auxiliares para manejar el archivo
def load_orders() -> List[Order]:
    """Carga las órdenes desde el archivo JSON."""
    try:
        with open(ORDERS_FILE, "r") as file:
            data = json.load(file)
            return [Order(**item) for item in data]
    except FileNotFoundError:
        # Si el archivo no existe, lo crea vacío
        with open(ORDERS_FILE, "w") as file:
            json.dump([], file)
        return []
    except json.JSONDecodeError as e:
        print(f"Error al leer el archivo JSON: {e}")
        return []


def save_orders(orders: List[Order]) -> None:
    """Guarda las órdenes en el archivo JSON."""
    try:
        with open(ORDERS_FILE, "w") as file:
            json.dump([order.dict() for order in orders], file, indent=4)
    except Exception as e:
        print(f"Error al guardar las órdenes: {e}")
        raise RuntimeError("No se pudo guardar las órdenes.")


# CRUD Operaciones
def create_order(order: Order) -> Order:
    """Crea una nueva orden."""
    orders = load_orders()
    order.created_at = datetime.utcnow()
    orders.append(order)
    save_orders(orders)
    return order


def get_user_orders(user_id: int) -> List[Order]:
    """Obtiene todas las órdenes de un usuario."""
    orders = load_orders()
    return [order for order in orders if order.user_id == user_id]


def update_order_status(order_id: int, status: str) -> Optional[Order]:
    """Actualiza el estado de una orden."""
    orders = load_orders()
    for order in orders:
        if order.id == order_id:
            order.status = status
            save_orders(orders)
            return order
    raise ValueError(f"No se encontró la orden con ID {order_id} para actualizar.")