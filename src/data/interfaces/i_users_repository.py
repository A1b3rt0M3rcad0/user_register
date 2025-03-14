from abc import ABC, abstractmethod
from src.domain.models.users import Users
from typing import Dict, List
from src.infra.db.connection.connection_handler.db_connection_handler import DBConnectionHandler

class IUsersRepository(ABC):

    @abstractmethod
    def get_db_connection_handler(self) -> DBConnectionHandler:pass

    @abstractmethod
    def insert(self, username:str, password:str) -> None:pass

    @abstractmethod
    def select(self, username:str) -> List[Users]:pass

    @abstractmethod
    def delete(self, username:str) -> None:pass

    @abstractmethod
    def update(self, username:str, update_params:Dict) -> None:pass