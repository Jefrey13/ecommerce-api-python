from fastapi import APIRouter, HTTPException
from typing import List
from fastapi.responses import FileResponse
from models.product import Product
from services.product import (
    get_all_products, get_product_by_id, create_product, 
    update_product, delete_product, export_products_to_excel
)

router = APIRouter()

@router.get("/products", response_model=List[Product], tags=["products"])
def read_products():
    return get_all_products()

@router.get("/products/{product_id}", response_model=Product, tags=["products"])
def read_product(product_id: int):
    product = get_product_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.post("/products", response_model=Product, tags=["products"])
def create_product_endpoint(product: Product):
    return create_product(product)

@router.put("/products/{product_id}", response_model=Product, tags=["products"])
def update_product_endpoint(product_id: int, product: Product):
    updated_product = update_product(product_id, product)
    if not updated_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product

@router.delete("/products/{product_id}", tags=["products"])
def delete_product_endpoint(product_id: int):
    if not delete_product(product_id):
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}

@router.get("/products/export", tags=["products"])
def export_products():
    file_path = export_products_to_excel()
    return FileResponse(
        path=file_path, 
        filename="productos.xlsx", 
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )