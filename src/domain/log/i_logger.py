from abc import ABC, abstractmethod

class ILogger(ABC):

    @classmethod
    @abstractmethod
    def log(cls, message:str) -> None:pass