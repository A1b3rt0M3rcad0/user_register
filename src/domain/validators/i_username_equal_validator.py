from abc import ABC, abstractmethod

class IUsarnameEqualValidator(ABC):

    @staticmethod
    @abstractmethod
    def valid(username:str, new_username:str) -> None:pass