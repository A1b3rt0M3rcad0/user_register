from abc import ABC, abstractmethod
from src.domain.dtos.login_case_dto import LoginDTO

class ILoginCase(ABC):

    @abstractmethod
    def login(self, username:str, password:str) -> LoginDTO:pass