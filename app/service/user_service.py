"""
Servicio de creación de usuarios
"""
from fastapi import HTTPException, status

from passlib.context import CryptContext

from app.model.user_model import User as UserModel
from app.schema import user_schema

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    """
    Convierte el texto plano de la contraseña a uno encriptado por medio del hash
    """
    return pwd_context.hash(password)

def create_user(user: user_schema.UserRegister):
    """
    Revisa y crea el nuevo usuario
    """
    get_user = UserModel.filter(
        (UserModel.email == user.email) | (UserModel.username == user.username)).first()

    if get_user:
        msg= "Email already registered"

        if get_user.username == user.username:
            msg = "Username already registered"
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=msg
        )

    db_user = UserModel(
        username = user.username,
        email = user.email,
        password = get_password_hash(user.password)
    )

    db_user.save()

    return user_schema.User(
        id=db_user.id,
        username=db_user.username,
        email=db_user.email
    )
