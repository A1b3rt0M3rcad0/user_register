from src.domain.use_cases.i_decode_token import IDecodeToken
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.presentation.interfaces.controller_interface import ControllerInterface

class DecodeTokenController(ControllerInterface):

    def __init__(self, use_case:IDecodeToken) -> None:
        self.__use_case = use_case

    def handle(self, http_request:HttpRequest) -> HttpResponse:

        token = http_request.headers["Authorization"]

        response = self.__use_case.decode(token).to_dict()

        return HttpResponse(
            status_code=200,
            body = response
        )
