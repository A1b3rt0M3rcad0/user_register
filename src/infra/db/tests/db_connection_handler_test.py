import pytest
from sqlalchemy import text
from src.infra.db.connection.factory.db_connection_handler_factory import DBConnectionHandlerFactory
from src.infra.db.config.dabase_connection.connection.mysql_string_connection import MysqlStringConnection

@pytest.mark.skip('Sensitive Test')
def test_mysql_connection():
    db_connection_handler_factory = DBConnectionHandlerFactory()
    mysql_string_connection = MysqlStringConnection()
    mysql_connection = db_connection_handler_factory.create_connection(mysql_string_connection)
    engine = mysql_connection.get_engine()

    assert engine
    assert hasattr(engine, 'connect')
    
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        assert result.scalar() == 1
