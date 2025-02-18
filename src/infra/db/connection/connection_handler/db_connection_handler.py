from src.infra.db.connection.interface.i_db_connection_handler import IDBConnectionHandler
from src.infra.db.config.dabase_connection.interface.i_string_connection import IStringConnection
from typing import Self
from sqlalchemy import Engine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler(IDBConnectionHandler):

    def __init__(self, string_connection:IStringConnection) -> None:
        self.__string_connection = string_connection.get_string_connection()
        self.__engine = self._create_database_engine()
        self.session = None

    def _create_database_engine(self) -> Engine:
        return create_engine(self.__string_connection)

    def get_engine(self) -> Engine:
        return self.__engine

    def __enter__(self) -> Self:
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.session.close()