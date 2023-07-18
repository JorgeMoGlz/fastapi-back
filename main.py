"""
App
"""
from fastapi import FastAPI

# Instancia de FastAPI
app = FastAPI()

@app.get('/')
def home():
    """
    Hello world
    """
    return {"message": "Hello"}
