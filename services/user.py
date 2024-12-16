import json
from typing import List, Optional
from models.user import User
from hashlib import sha256

# Ruta del archivo donde se almacenarán los usuarios
USERS_FILE = "data/users.json"


# Funciones auxiliares para manejar el archivo
def load_users() -> List[User]:
    """Carga los usuarios desde el archivo JSON."""
    try:
        with open(USERS_FILE, "r") as file:
            data = json.load(file)
            return [User(**item) for item in data]
    except FileNotFoundError:
        # Si el archivo no existe, lo crea vacío
        with open(USERS_FILE, "w") as file:
            json.dump([], file)
        return []
    except json.JSONDecodeError as e:
        print(f"Error al leer el archivo JSON: {e}")
        return []


def save_users(users: List[User]) -> None:
    """Guarda los usuarios en el archivo JSON."""
    try:
        with open(USERS_FILE, "w") as file:
            json.dump([user.dict() for user in users], file, indent=4)
    except Exception as e:
        print(f"Error al guardar los usuarios: {e}")
        raise RuntimeError("No se pudo guardar los usuarios.")


# Funciones auxiliares de seguridad
def hash_password(password: str) -> str:
    """Genera un hash SHA-256 para la contraseña."""
    return sha256(password.encode()).hexdigest()


# CRUD Operaciones
def create_user(user: User) -> User:
    """Crea un nuevo usuario."""
    users = load_users()

    # Validar si el nombre de usuario ya existe
    if any(u.username == user.username for u in users):
        raise ValueError(f"El usuario con username '{user.username}' ya existe.")

    # Hashear la contraseña antes de guardarla
    user.password = hash_password(user.password)

    users.append(user)
    save_users(users)
    return user


def get_all_users() -> List[User]:
    """Obtiene todos los usuarios."""
    return load_users()


def authenticate_user(username: str, password: str) -> bool:
    """Autentica a un usuario."""
    users = load_users()
    hashed_password = hash_password(password)
    return any(u for u in users if u.username == username and u.password == hashed_password)