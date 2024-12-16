import json
from typing import List, Optional
from models.product import Product
from openpyxl import Workbook
from openpyxl.utils.exceptions import InvalidFileException

# Ruta del archivo donde se almacenarán los productos
PRODUCTS_FILE = "data/products.json"

# Funciones auxiliares para manejar el archivo


def load_products() -> List[Product]:
    """Carga los productos desde el archivo JSON."""
    try:
        with open(PRODUCTS_FILE, "r") as file:
            data = json.load(file)
            return [Product(**item) for item in data]
    except FileNotFoundError:
        # Si el archivo no existe, lo crea vacío
        with open(PRODUCTS_FILE, "w") as file:
            json.dump([], file)
        return []
    except json.JSONDecodeError as e:
        print(f"Error al leer el archivo JSON: {e}")
        return []


def save_products(products: List[Product]) -> None:
    """Guarda los productos en el archivo JSON."""
    try:
        with open(PRODUCTS_FILE, "w") as file:
            json.dump([product.dict() for product in products], file, indent=4)
    except Exception as e:
        print(f"Error al guardar los productos: {e}")
        raise RuntimeError("No se pudo guardar los productos.")


# CRUD Operaciones


def get_all_products() -> List[Product]:
    """Obtiene todos los productos."""
    return load_products()


def get_product_by_id(product_id: int) -> Optional[Product]:
    """Obtiene un producto por su ID."""
    products = load_products()
    product = next((p for p in products if p.id == product_id), None)
    if not product:
        raise ValueError(f"No se encontró el producto con ID {product_id}.")
    return product


def create_product(product: Product) -> Product:
    """Crea un nuevo producto."""
    products = load_products()
    if any(p.id == product.id for p in products):
        raise ValueError(f"El producto con ID {product.id} ya existe.")
    products.append(product)
    save_products(products)
    return product


def update_product(product_id: int, product: Product) -> Optional[Product]:
    """Actualiza un producto existente."""
    products = load_products()
    for idx, existing_product in enumerate(products):
        if existing_product.id == product_id:
            products[idx] = product
            save_products(products)
            return product
    raise ValueError(f"No se encontró el producto con ID {product_id} para actualizar.")


def delete_product(product_id: int) -> bool:
    """Elimina un producto por su ID."""
    products = load_products()
    updated_products = [p for p in products if p.id != product_id]
    if len(updated_products) == len(products):
        raise ValueError(f"No se encontró el producto con ID {product_id} para eliminar.")
    save_products(updated_products)
    return True


def export_products_to_excel() -> str:
    """Exporta los productos a un archivo Excel."""
    products = load_products()
    if not products:
        raise ValueError("No hay productos para exportar.")

    try:
        wb = Workbook()
        ws = wb.active
        ws.title = "Productos"

        headers = ["ID", "Nombre", "Descripción", "Precio", "Stock", "Category_ID"]
        ws.append(headers)

        for product in products:
            ws.append([
                product.id, product.name, product.description,
                product.price, product.stock, product.category_id
            ])

        file_path = "productos.xlsx"
        wb.save(file_path)
        return file_path
    except InvalidFileException as e:
        print(f"Error al generar el archivo Excel: {e}")
        raise RuntimeError("No se pudo generar el archivo Excel.")
    except Exception as e:
        print(f"Error al exportar los productos: {e}")
        raise RuntimeError("No se pudo exportar los productos a Excel.")