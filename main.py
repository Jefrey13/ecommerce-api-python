from fastapi import FastAPI
from routes.product import router as product_router
from routes.category import router as category_router
from routes.cart import router as cart_router
from routes.order import router as order_router
from routes.payment import router as payment_router
from routes.inventory import router as inventory_router
from routes.user import router as user_router

app = FastAPI(
    title="E-commerce Backend API",
    description="API para gestionar productos, categorías, carritos, órdenes, pagos, inventarios y usuarios.",
    version="3.0.0",
    contact={
        "name": "Soporte API",
        "email": "jefreyzuniga@gmail.com",
        "url": "https://jefreyzuniga.com"
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
)

# Rutas incluidas
app.include_router(product_router, prefix="/api")
app.include_router(category_router, prefix="/api")
app.include_router(cart_router, prefix="/api")
app.include_router(order_router, prefix="/api")
app.include_router(payment_router, prefix="/api")
app.include_router(inventory_router, prefix="/api")
app.include_router(user_router, prefix="/api")

@app.get("/", tags=["home"])
def read_root():
    return {
        "message": "Hi, I'm Jefrey Zuniga. Welcome to the E-commerce Backend API v3.0",
        "documentation_url": "/docs",
        "redoc_url": "/redoc",
    }