"""
Configuraciones para obtener las variables de entorno
"""
import os

from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Cargamos las variables de entorno
load_dotenv()

class Settings(BaseSettings):
    """
    Clase Settings extiende de BaseSettings para
    forzar los tipos de datos, en este caso str
    """
    db_name: str = os.getenv('DB_NAME')
    db_user: str = os.getenv('DB_USER')
    db_pass: str = os.getenv('DB_PASS')
    db_host: str = os.getenv('DB_HOST')
    db_port: str = os.getenv('DB_PORT')
