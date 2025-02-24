from abc import ABC, abstractmethod
from src.domain.dtos.delete_user_dto import DeleteUserDTO

class IDeleteUser(ABC):

    @abstractmethod
    def delete(self, username:str) -> DeleteUserDTO:pass