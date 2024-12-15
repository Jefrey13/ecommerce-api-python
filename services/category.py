from typing import List, Optional
from models.category import Category

categories_db: List[Category] = []

def get_all_categories() -> List[Category]:
    return categories_db

def get_category_by_id(category_id: int) -> Optional[Category]:
    return next((c for c in categories_db if c.id == category_id), None)

def create_category(category: Category) -> Category:
    categories_db.append(category)
    return category

def update_category(category_id: int, category: Category) -> Optional[Category]:
    for idx, existing_category in enumerate(categories_db):
        if existing_category.id == category_id:
            categories_db[idx] = category
            return category
    return None

def delete_category(category_id: int) -> bool:
    for idx, existing_category in enumerate(categories_db):
        if existing_category.id == category_id:
            del categories_db[idx]
            return True
    return False