from src.domain.validators.i_authenticated_token_validator import IAuthenticatedTokenValidator
from src.errors.types.http_unauthorized_error import UnauthorizedError
from src.main.composers.decode_token_composer import decode_token_composer
from src.main.adapters.request_adapter import request_adapter

class AuthenticatedTokenValidator(IAuthenticatedTokenValidator):

    @staticmethod
    def valid(request:any) -> None:
        username = request_adapter(request, decode_token_composer()).body["username"]
        if username != request.json["username"]:
            raise UnauthorizedError(f"Unauthorized Token, you are {username} not {request.json["username"]}")