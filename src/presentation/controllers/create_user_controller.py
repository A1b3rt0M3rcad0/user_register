from src.domain.use_cases.i_create_user import ICreateUser
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpReponse
from src.presentation.interfaces.controller_interface import ControllerInterface

class CreateUserController(ControllerInterface):

    def __init__(self, use_case:ICreateUser) -> None:
        self.__use_case = use_case

    def handle(self, http_request:HttpRequest) -> HttpReponse:

        username = http_request.body["username"]
        password = http_request.body["password"]

        response = self.__use_case.create(username, password).to_dict()

        return HttpReponse(
            status_code=200,
            body = response
        )
