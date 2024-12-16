from fastapi import APIRouter, HTTPException
from typing import List
from models.user import User
from services.user import (
    create_user,
    get_all_users,
    authenticate_user
)

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=User)
def add_user(user: User):
    try:
        return create_user(user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/", response_model=List[User])
def read_all_users():
    try:
        users = get_all_users()
        if not users:
            raise HTTPException(status_code=404, detail="No se encontraron usuarios.")
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/authenticate", response_model=dict)
def login(username: str, password: str):
    try:
        if authenticate_user(username, password):
            return {"detail": "Autenticación exitosa."}
        raise HTTPException(status_code=401, detail="Credenciales inválidas.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))