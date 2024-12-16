import json
from typing import List
from models.Cart import CartItem

# Ruta del archivo donde se almacenarán los datos del carrito
CART_FILE = "data/cart.json"


# Funciones auxiliares para manejar el archivo
def load_cart() -> List[CartItem]:
    """Carga los elementos del carrito desde el archivo JSON."""
    try:
        with open(CART_FILE, "r") as file:
            data = json.load(file)
            return [CartItem(**item) for item in data]
    except FileNotFoundError:
        # Si el archivo no existe, lo crea vacío
        with open(CART_FILE, "w") as file:
            json.dump([], file)
        return []
    except json.JSONDecodeError as e:
        print(f"Error al leer el archivo JSON: {e}")
        return []


def save_cart(cart: List[CartItem]) -> None:
    """Guarda los elementos del carrito en el archivo JSON."""
    try:
        with open(CART_FILE, "w") as file:
            json.dump([item.dict() for item in cart], file, indent=4)
    except Exception as e:
        print(f"Error al guardar el carrito: {e}")
        raise RuntimeError("No se pudo guardar el carrito.")


# CRUD Operaciones
def add_to_cart(item: CartItem) -> CartItem:
    """Agrega un elemento al carrito."""
    cart = load_cart()

    # Verificar si el producto ya está en el carrito del usuario
    for cart_item in cart:
        if cart_item.user_id == item.user_id and cart_item.product_id == item.product_id:
            cart_item.quantity += item.quantity  # Sumar la cantidad al existente
            save_cart(cart)
            return cart_item

    cart.append(item)  # Si no existe, lo agrega
    save_cart(cart)
    return item


def get_user_cart(user_id: int) -> List[CartItem]:
    """Obtiene el carrito de un usuario."""
    cart = load_cart()
    return [item for item in cart if item.user_id == user_id]


def remove_from_cart(user_id: int, product_id: int) -> bool:
    """Elimina un producto del carrito de un usuario."""
    cart = load_cart()
    updated_cart = [item for item in cart if not (item.user_id == user_id and item.product_id == product_id)]

    if len(updated_cart) == len(cart):  # No se encontró el producto
        raise ValueError(f"No se encontró el producto con ID {product_id} en el carrito del usuario con ID {user_id}.")

    save_cart(updated_cart)
    return True