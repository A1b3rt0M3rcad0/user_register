from src.presentation.interfaces.controller_interface import ControllerInterface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpReponse
from src.domain.use_cases.i_change_username import IChangeUsername

class ChangeUsernameController(ControllerInterface):

    def __init__(self, use_case:IChangeUsername) -> None:
        self.__use_case = use_case
    
    def handle(self, http_request:HttpRequest) -> HttpReponse:
        username = http_request.body["username"]
        new_username = http_request.body["new_username"]
        response = self.__use_case.update(username, new_username).to_dict()
        return HttpReponse(
            status_code=200,
            body = response
        )