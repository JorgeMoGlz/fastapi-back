"""
Creación del modelo User
"""
import peewee

from app.utils.db import db

class User(peewee.Model):
    """
    La clase user extiende de peewee model para especificar los tipos
    de dato
    """
    email = peewee.CharField(unique=True, index=True)
    username = peewee.CharField(unique=True, index=True)
    password = peewee.CharField()

    class Meta:
        """
        Conexión con la base de datos
        """
        database = db
