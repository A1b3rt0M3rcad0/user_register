from abc import ABC, abstractmethod

class IStringConnection(ABC):

    @staticmethod
    @abstractmethod
    def get_string_connection() -> str:pass