from fastapi import APIRouter
from typing import List
from models.Review import Review
from services.review import create_review, get_product_reviews

router = APIRouter()

@router.post("/reviews", response_model=Review, tags=["reviews"])
def create_review_endpoint(review: Review):
    return create_review(review)

@router.get("/reviews/{product_id}", response_model=List[Review], tags=["reviews"])
def get_reviews(product_id: int):
    return get_product_reviews(product_id)