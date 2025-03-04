from abc import ABC, abstractmethod

class IAuthenticatedTokenValidator(ABC):

    @staticmethod
    @abstractmethod
    def valid(request:any) -> None:pass