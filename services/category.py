import json
from typing import List, Optional
from models.category import Category

# Ruta del archivo donde se almacenarán las categorías
CATEGORIES_FILE = "data/categories.json"


# Funciones auxiliares para manejar el archivo
def load_categories() -> List[Category]:
    """Carga las categorías desde el archivo JSON."""
    try:
        with open(CATEGORIES_FILE, "r") as file:
            data = json.load(file)
            return [Category(**item) for item in data]
    except FileNotFoundError:
        # Si el archivo no existe, lo crea vacío
        with open(CATEGORIES_FILE, "w") as file:
            json.dump([], file)
        return []
    except json.JSONDecodeError as e:
        print(f"Error al leer el archivo JSON: {e}")
        return []


def save_categories(categories: List[Category]) -> None:
    """Guarda las categorías en el archivo JSON."""
    try:
        with open(CATEGORIES_FILE, "w") as file:
            json.dump([category.dict() for category in categories], file, indent=4)
    except Exception as e:
        print(f"Error al guardar las categorías: {e}")
        raise RuntimeError("No se pudo guardar las categorías.")


# CRUD Operaciones
def get_all_categories() -> List[Category]:
    """Obtiene todas las categorías."""
    return load_categories()


def get_category_by_id(category_id: int) -> Optional[Category]:
    """Obtiene una categoría por su ID."""
    categories = load_categories()
    category = next((c for c in categories if c.id == category_id), None)
    if not category:
        raise ValueError(f"No se encontró la categoría con ID {category_id}.")
    return category


def create_category(category: Category) -> Category:
    """Crea una nueva categoría."""
    categories = load_categories()
    if any(c.id == category.id for c in categories):
        raise ValueError(f"La categoría con ID {category.id} ya existe.")
    categories.append(category)
    save_categories(categories)
    return category


def update_category(category_id: int, category: Category) -> Optional[Category]:
    """Actualiza una categoría existente."""
    categories = load_categories()
    for idx, existing_category in enumerate(categories):
        if existing_category.id == category_id:
            categories[idx] = category
            save_categories(categories)
            return category
    raise ValueError(f"No se encontró la categoría con ID {category_id} para actualizar.")


def delete_category(category_id: int) -> bool:
    """Elimina una categoría por su ID."""
    categories = load_categories()
    updated_categories = [c for c in categories if c.id != category_id]
    if len(updated_categories) == len(categories):
        raise ValueError(f"No se encontró la categoría con ID {category_id} para eliminar.")
    save_categories(updated_categories)
    return True