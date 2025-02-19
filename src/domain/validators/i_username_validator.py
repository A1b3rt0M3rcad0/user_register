from abc import ABC, abstractmethod

class IUsernameValidator(ABC):

    @staticmethod
    @abstractmethod
    def valid(username:str) -> None:pass