from abc import ABC, abstractmethod

class ISecretKey(ABC):

    @staticmethod
    @abstractmethod
    def get_sercret_key() -> str:pass