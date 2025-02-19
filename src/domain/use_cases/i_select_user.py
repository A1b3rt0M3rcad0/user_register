from abc import ABC, abstractmethod
from src.domain.dtos.select_user_dto import SelectUserDTO

class SelectUser(ABC):

    @abstractmethod
    def select(self, username:str) -> SelectUserDTO:pass