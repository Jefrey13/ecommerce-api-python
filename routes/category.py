from fastapi import APIRouter, HTTPException
from typing import List
from models.category import Category
from services.category import (
    get_all_categories,
    get_category_by_id,
    create_category,
    update_category,
    delete_category
)

router = APIRouter(prefix="/categories", tags=["categories"])

@router.get("/", response_model=List[Category])
def read_categories():
    try:
        categories = get_all_categories()
        if not categories:
            raise HTTPException(status_code=404, detail="No se encontraron categorías.")
        return categories
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{category_id}", response_model=Category)
def read_category(category_id: int):
    try:
        return get_category_by_id(category_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/", response_model=Category)
def add_category(category: Category):
    try:
        return create_category(category)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/{category_id}", response_model=Category)
def update_existing_category(category_id: int, category: Category):
    try:
        return update_category(category_id, category)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{category_id}", status_code=204)
def remove_category(category_id: int):
    try:
        if delete_category(category_id):
            return {"detail": f"Categoría con ID {category_id} eliminada exitosamente."}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))