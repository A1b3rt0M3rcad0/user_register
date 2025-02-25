from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.i_login_case import ILoginCase
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse


class LoginCaseController(ControllerInterface):

    def __init__(self, use_case:ILoginCase) -> None:
        self.__use_case = use_case
    
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        username = body["username"]
        password = body["password"]
        login_dto = self.__use_case.login(username, password).to_dict()
        token = login_dto["attrs"]["token"]
        return HttpResponse(
            status_code=200,
            body={
                "token": token
            }
        )