from fastapi import APIRouter, HTTPException
from typing import List
from models.product import Product
from services.product import (
    get_all_products,
    get_product_by_id,
    create_product,
    update_product,
    delete_product,
    export_products_to_excel
)

router = APIRouter(prefix="/products", tags=["products"])

@router.get("/", response_model=List[Product])
def read_products():
    try:
        products = get_all_products()
        if not products:
            raise HTTPException(status_code=404, detail="No se encontraron productos.")
        return products
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{product_id}", response_model=Product)
def read_product(product_id: int):
    try:
        return get_product_by_id(product_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/", response_model=Product)
def add_product(product: Product):
    try:
        return create_product(product)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/{product_id}", response_model=Product)
def update_existing_product(product_id: int, product: Product):
    try:
        return update_product(product_id, product)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{product_id}", status_code=204)
def remove_product(product_id: int):
    try:
        if delete_product(product_id):
            return {"detail": f"Producto con ID {product_id} eliminado exitosamente."}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/export", response_model=dict)
def export_products():
    try:
        file_path = export_products_to_excel()
        return {"detail": f"Productos exportados exitosamente a {file_path}"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))