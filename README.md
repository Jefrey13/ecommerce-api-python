# E-commerce Backend API with FastAPI

## Overview
This is a RESTful API for managing an E-commerce platform, built with **FastAPI**. The backend includes functionalities to handle products, categories, cart, orders, payments, reviews, and inventory. It also supports Excel export for products.

---

## Features
- **CRUD** operations for:
  - Products
  - Categories
  - Cart
  - Orders
  - Payments
  - Reviews
  - Inventory
- Export product data to **Excel**.
- Organized and modular architecture.

---

## Technologies
- **Python**
- **FastAPI**
- **Pydantic**
- **OpenPyXL** (for Excel export)

---
# API documentation - Swagger UI

![FastAPI](https://i.ibb.co/ryCxSdP/fastapi.png)

---
## Endpoints
### **Products**
- `GET /api/products` - Get all products
- `GET /api/products/{id}` - Get a product by ID
- `POST /api/products` - Create a new product
- `PUT /api/products/{id}` - Update a product
- `DELETE /api/products/{id}` - Delete a product
- `GET /api/products/export` - Export product data to Excel

### **Categories**
- `GET /api/categories` - Get all categories
- `GET /api/categories/{id}` - Get a category by ID
- `POST /api/categories` - Create a new category
- `PUT /api/categories/{id}` - Update a category
- `DELETE /api/categories/{id}` - Delete a category

### **Cart**
- `POST /api/cart` - Add a product to the cart
- `GET /api/cart/{user_id}` - Get the cart for a specific user
- `DELETE /api/cart/{user_id}/{product_id}` - Remove a product from the cart

### **Orders**
- `POST /api/orders` - Create a new order
- `GET /api/orders/{user_id}` - Get orders for a user
- `PUT /api/orders/{id}/{status}` - Update the status of an order

### **Payments**
- `POST /api/payments` - Register a payment
- `GET /api/payments/{order_id}` - Get payments for an order

### **Reviews**
- `POST /api/reviews` - Add a review for a product
- `GET /api/reviews/{product_id}` - Get reviews for a product

### **Inventory**
- `PUT /api/inventory/{product_id}` - Update inventory for a product
- `GET /api/inventory` - Get inventory data

---
