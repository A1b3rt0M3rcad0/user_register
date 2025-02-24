from src.domain.use_cases.i_delete_user import IDeleteUser
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.presentation.interfaces.controller_interface import ControllerInterface

class DeleteUserController(ControllerInterface):

    def __init__(self, use_case:IDeleteUser) -> None:
        self.__use_case = use_case
    
    def handle(self, http_request:HttpRequest) -> HttpResponse:
        username = http_request.body["username"]
        response = self.__use_case.delete(username).to_dict()
        return HttpResponse(
            status_code=200,
            body=response
        )