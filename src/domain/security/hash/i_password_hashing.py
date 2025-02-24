from abc import ABC, abstractmethod

class IPasswordHashing(ABC):

    @staticmethod
    @abstractmethod
    def hash(password:str) -> str:pass