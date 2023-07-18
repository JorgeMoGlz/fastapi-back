"""
Obtención de los campos del usuario
"""
from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr

class UserBase(BaseModel):
    """
    Clase para obtener los datos básicos del usuario
    """
    email: EmailStr = Field(...,
                            example="user@raisacv.com")
    username: str = Field(...,
                          min_length=3,
                          max_length=50,
                          example="username")

class User(UserBase):
    """
    Clase extendida para obtener el id del usuario
    """
    id: int = Field(...,
                    example="1")

class UserRegister(UserBase):
    """
    Clase extendida para obtener la contraseña
    """
    password: str = Field(...,
                          min_length=8,
                          max_length=64,
                          example="strongpass123")
