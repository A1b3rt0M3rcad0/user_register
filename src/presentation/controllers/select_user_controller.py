from src.domain.use_cases.i_select_user import ISelectUser
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.presentation.interfaces.controller_interface import ControllerInterface

class SelectUserController(ControllerInterface):

    def __init__(self, use_case:ISelectUser) -> None:
        self.__use_case = use_case
    
    def handle(self, http_request:HttpRequest) -> HttpResponse:
        username = http_request.body["username"]
        response = self.__use_case.select(username).to_dict()
        return HttpResponse(
            status_code=200,
            body=response
        )