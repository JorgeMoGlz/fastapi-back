"""
Ruta creadora de usuario
"""
from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Body

from app.schema import user_schema
from app.service import user_service
from app.utils.db import get_db

router = APIRouter(prefix="/api")

@router.post("/user/",
             tags=["users"],
             status_code=status.HTTP_201_CREATED,
             response_model=user_schema.User,
             dependencies=[Depends(get_db)],
             summary="Create a new user")
def create_user(user: user_schema.UserRegister = Body(...)):
    """
    ## Create a new user in the app

    ### Args
    The app can receive next fields into a JSON
    - email: A valid email
    - username: Unique username
    - password: Strong password for authentication
    
    ### Returns
    - user: User info
    """
    return user_service.create_user(user)
