from abc import ABC, abstractmethod
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpReponse


class ControllerInterface(ABC):

    @abstractmethod
    def handle(self, http_request: HttpRequest) -> HttpReponse: pass