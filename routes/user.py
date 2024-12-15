from fastapi import APIRouter, HTTPException
from typing import List
from models.user import User
from services.user import create_user, get_all_users, authenticate_user

router = APIRouter()

@router.post("/users", response_model=User, tags=["users"])
def create_user_endpoint(user: User):
    return create_user(user)

@router.get("/users", response_model=List[User], tags=["users"])
def read_users():
    return get_all_users()

@router.post("/users/auth", tags=["users"])
def login(username: str, password: str):
    if authenticate_user(username, password):
        return {"message": "Login successful"}
    raise HTTPException(status_code=401, detail="Invalid credentials")