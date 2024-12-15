from typing import List
from datetime import datetime
from models.Review import Review

reviews_db: List[Review] = []

def create_review(review: Review) -> Review:
    review.created_at = datetime.utcnow()
    reviews_db.append(review)
    return review

def get_product_reviews(product_id: int) -> List[Review]:
    return [review for review in reviews_db if review.product_id == product_id]