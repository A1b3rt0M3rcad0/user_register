from abc import ABC, abstractmethod
from typing import Dict

class IEncoder(ABC):

    @abstractmethod
    def encode(self, params:Dict) -> str:pass