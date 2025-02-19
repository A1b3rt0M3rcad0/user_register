from abc import ABC, abstractmethod
from src.domain.dtos.create_user_dto import CreateUserDTO

class ICreateUser(ABC):

    @abstractmethod
    def create(self, username:str, password:str) -> CreateUserDTO:pass