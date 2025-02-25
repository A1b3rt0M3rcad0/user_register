from abc import ABC, abstractmethod

class IAuthenticateToken(ABC):

    @abstractmethod
    def authenticate(self, token:str) -> bool:pass