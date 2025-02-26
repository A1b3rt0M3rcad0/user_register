from abc import ABC, abstractmethod
from src.domain.dtos.decode_token_dto import DecodeTokenDTO

class IDecodeToken(ABC):

    @abstractmethod
    def decode(self, token:str) -> DecodeTokenDTO:pass
