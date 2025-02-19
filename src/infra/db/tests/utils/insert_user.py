from sqlalchemy import text
from sqlalchemy import Engine
from datetime import datetime



def insert_user(username: str, password: str, created_at: datetime, engine: Engine) -> None:
    sql = text('''
        INSERT INTO users (username, password, created_at) 
        VALUES (:username, :password, :created_at)
    ''')

    with engine.connect() as conn:
        conn.execute(sql, {"username": username, "password": password, "created_at": created_at})
        conn.commit()