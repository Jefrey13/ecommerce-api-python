from typing import List, Optional
from models.user import User

users_db: List[User] = []

def create_user(user: User) -> User:
    users_db.append(user)
    return user

def get_all_users() -> List[User]:
    return users_db

def authenticate_user(username: str, password: str) -> bool:
    return any(u for u in users_db if u.username == username and u.password == password)