from abc import ABC, abstractmethod
from typing import Dict

class IDecoder(ABC):

    @abstractmethod
    def decode(self, token:str) -> Dict:pass