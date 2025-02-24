from src.domain.dtos.change_username_dto import ChangeUsernameDTO
from abc import ABC, abstractmethod

class IChangeUsername(ABC):

    @abstractmethod
    def update(self, username:str, new_username:str) -> ChangeUsernameDTO:pass