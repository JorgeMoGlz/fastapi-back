from app.model.user_model import User
from app.utils.db import db

def create_table():
    with db:
        db.create_tables([User])
