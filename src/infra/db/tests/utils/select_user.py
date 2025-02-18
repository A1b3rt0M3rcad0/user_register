from sqlalchemy import text
from sqlalchemy import Engine
from src.domain.models.users import Users


def select_user(engine:Engine) -> Users:
    sql = '''
    SELECT * FROM users
    '''
    conn = engine.connect()
    response = conn.execute(text(sql))
    return response.fetchall()