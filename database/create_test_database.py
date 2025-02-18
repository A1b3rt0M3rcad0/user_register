from src.infra.db.config.database_creator.database_creator import create_tables
from src.infra.db.config.database_connection.connection.test_string_connection import TestStringConnection
from src.infra.db.connection.factory.db_connection_handler_factory import DBConnectionHandlerFactory

def create_test_database() -> None:
    conn = DBConnectionHandlerFactory.create_connection(TestStringConnection)
    create_tables(conn.get_engine())