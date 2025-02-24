from abc import ABC, abstractmethod

class IAuthAlgoritm(ABC):

    @staticmethod
    @abstractmethod
    def get_algoritm() -> str:pass