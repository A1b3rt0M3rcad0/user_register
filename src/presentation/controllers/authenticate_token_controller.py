from src.domain.use_cases.i_authenticate_token import IAuthenticateToken
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.errors.types.http_unauthorized_error import UnauthorizedError

class AuthenticateTokenController(ControllerInterface):

    def __init__(self, use_case:IAuthenticateToken) -> None:
        self.__use_case = use_case
    
    def handle(self, http_request:HttpRequest) -> HttpResponse:
        headers = http_request.headers
        authorization:str = headers["Authorization"]

        if not authorization or not authorization.startswith("Bearer"):
            return HttpResponse(status_code=401, body={
                'error': "Invalid Token"
            })
        
        token = authorization.replace("Bearer ", "").strip()

        try:
            self.__use_case.authenticate(token)
            return HttpResponse(
                status_code=200,
                body={
                    "message": "valid token"
                }
            )
        except UnauthorizedError as e:
            return HttpResponse(
                status_code=e.status_code,
                body={
                    'error': e.message
                }
            )