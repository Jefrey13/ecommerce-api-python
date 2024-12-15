from fastapi import APIRouter, HTTPException
from typing import List
from models.category import Category
from services.category import (
    get_all_categories, get_category_by_id, create_category, 
    update_category, delete_category
)

router = APIRouter()

@router.get("/categories", response_model=List[Category], tags=["categories"])
def read_categories():
    return get_all_categories()

@router.get("/categories/{category_id}", response_model=Category, tags=["categories"])
def read_category(category_id: int):
    category = get_category_by_id(category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@router.post("/categories", response_model=Category, tags=["categories"])
def create_category_endpoint(category: Category):
    return create_category(category)

@router.put("/categories/{category_id}", response_model=Category, tags=["categories"])
def update_category_endpoint(category_id: int, category: Category):
    updated_category = update_category(category_id, category)
    if not updated_category:
        raise HTTPException(status_code=404, detail="Category not found")
    return updated_category

@router.delete("/categories/{category_id}", tags=["categories"])
def delete_category_endpoint(category_id: int):
    if not delete_category(category_id):
        raise HTTPException(status_code=404, detail="Category not found")
    return {"message": "Category deleted successfully"}