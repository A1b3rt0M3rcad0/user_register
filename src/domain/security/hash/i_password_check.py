from abc import ABC, abstractmethod

class IPasswordHashChecker(ABC):

    @staticmethod
    @abstractmethod
    def check(password:str, database_password:str) -> bool:pass