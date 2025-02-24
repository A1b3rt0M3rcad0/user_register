from abc import ABC, abstractmethod
from typing import Dict

class IDecoder(ABC):

    @abstractmethod
    def encode(self, token:str) -> Dict:pass