import json
from typing import List
from datetime import datetime
from models.Payment import Payment

# Ruta del archivo donde se almacenarán los pagos
PAYMENTS_FILE = "data/payments.json"


# Funciones auxiliares para manejar el archivo
def load_payments() -> List[Payment]:
    """Carga los pagos desde el archivo JSON."""
    try:
        with open(PAYMENTS_FILE, "r") as file:
            data = json.load(file)
            return [Payment(**item) for item in data]
    except FileNotFoundError:
        # Si el archivo no existe, lo crea vacío
        with open(PAYMENTS_FILE, "w") as file:
            json.dump([], file)
        return []
    except json.JSONDecodeError as e:
        print(f"Error al leer el archivo JSON: {e}")
        return []


def save_payments(payments: List[Payment]) -> None:
    """Guarda los pagos en el archivo JSON."""
    try:
        with open(PAYMENTS_FILE, "w") as file:
            json.dump([payment.dict() for payment in payments], file, indent=4)
    except Exception as e:
        print(f"Error al guardar los pagos: {e}")
        raise RuntimeError("No se pudo guardar los pagos.")


# CRUD Operaciones
def create_payment(payment: Payment) -> Payment:
    """Crea un nuevo pago."""
    payments = load_payments()
    payment.payment_date = datetime.utcnow()
    payments.append(payment)
    save_payments(payments)
    return payment


def get_payments_by_order(order_id: int) -> List[Payment]:
    """Obtiene todos los pagos relacionados con un pedido."""
    payments = load_payments()
    return [payment for payment in payments if payment.order_id == order_id]