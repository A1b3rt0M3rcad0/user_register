import os
from src.infra.db.config.database_connection.interface.i_string_connection import IStringConnection

class MysqlStringConnection(IStringConnection):

    @staticmethod
    def get_string_connection() -> str:
        return os.getenv('MYSQL_STRING_CONNECTION')