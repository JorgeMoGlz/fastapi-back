"""
App
"""
from fastapi import FastAPI

from app.router.user_router import router as user_router

# Instancia de FastAPI
app = FastAPI()

app.include_router(user_router)

@app.get('/')
def home():
    """
    Hello world
    """
    return {"message": "Hello"}
