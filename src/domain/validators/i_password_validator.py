from abc import ABC, abstractmethod

class IPasswordValidator(ABC):

    @staticmethod
    @abstractmethod
    def valid(password:str) -> None:pass