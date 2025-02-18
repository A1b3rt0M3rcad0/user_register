from src.infra.db.config.dabase_connection.interface.i_string_connection import IStringConnection
from src.infra.db.connection.connection_handler.db_connection_handler import DBConnectionHandler

class DBConnectionHandlerFactory:

    @staticmethod
    def create_connection(string_connection: IStringConnection) -> DBConnectionHandler:
        return DBConnectionHandler(string_connection)