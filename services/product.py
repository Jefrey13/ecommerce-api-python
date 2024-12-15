from typing import List, Optional
from models.product import Product
from openpyxl import Workbook

# Base de datos simulada
products_db: List[Product] = []

def get_all_products() -> List[Product]:
    return products_db

def get_product_by_id(product_id: int) -> Optional[Product]:
    return next((p for p in products_db if p.id == product_id), None)

def create_product(product: Product) -> Product:
    products_db.append(product)
    return product

def update_product(product_id: int, product: Product) -> Optional[Product]:
    for idx, existing_product in enumerate(products_db):
        if existing_product.id == product_id:
            products_db[idx] = product
            return product
    return None

def delete_product(product_id: int) -> bool:
    for idx, existing_product in enumerate(products_db):
        if existing_product.id == product_id:
            del products_db[idx]
            return True
    return False

def export_products_to_excel() -> str:
    wb = Workbook()
    ws = wb.active
    ws.title = "Productos"

    headers = ["ID", "Nombre", "Descripción", "Precio", "Stock", "Category_ID"]
    ws.append(headers)

    for product in products_db:
        ws.append([
            product.id, product.name, product.description, 
            product.price, product.stock, product.category_id
        ])

    file_path = "productos.xlsx"
    wb.save(file_path)
    return file_path