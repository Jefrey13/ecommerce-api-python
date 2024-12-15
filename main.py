from fastapi import FastAPI
from routes.product import router as product_router
from routes.category import router as category_router
from routes.cart import router as cart_router
from routes.order import router as order_router
from routes.payment import router as payment_router
from routes.review import router as review_router
from routes.inventory import router as inventory_router

app = FastAPI()
app.title = "E-commerce Backend API"
app.version = "3.0.0"

app.include_router(product_router, prefix="/api")
app.include_router(category_router, prefix="/api")
app.include_router(cart_router, prefix="/api")
app.include_router(order_router, prefix="/api")
app.include_router(payment_router, prefix="/api")
app.include_router(review_router, prefix="/api")
app.include_router(inventory_router, prefix="/api")

@app.get("/", tags=["home"])
def read_root():
    return {"message": "Welcome to the E-commerce Backend API v3.0"}