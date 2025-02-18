from src.infra.db.config.database_connection.interface.i_string_connection import IStringConnection

class TestStringConnection(IStringConnection):

    @staticmethod
    def get_string_connection() -> str:
        return 'sqlite:///src/infra/db/tests/test.db'