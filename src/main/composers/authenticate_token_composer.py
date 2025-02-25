from src.data.use_cases.authenticate_token import AuthenticateToken
from src.presentation.controllers.authenticate_token_controller import AuthenticateTokenController
from src.auth.config.auth_algoritm import AuthAlgoritm
from src.auth.config.auth_secret_key import SecretKey
from src.auth.cryptography.decoder import Decoder
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from typing import Callable


def authenticate_token_composer() -> Callable[[HttpRequest], HttpResponse]:
    decoder = Decoder(AuthAlgoritm, SecretKey)
    authenticate_token = AuthenticateToken(decoder)
    authenticate_token_controller = AuthenticateTokenController(authenticate_token)
    return authenticate_token_controller.handle