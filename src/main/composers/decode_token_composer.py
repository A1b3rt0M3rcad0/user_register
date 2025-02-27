from src.auth.cryptography.decoder import Decoder
from src.auth.config.auth_algoritm import AuthAlgoritm
from src.auth.config.auth_secret_key import SecretKey
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from typing import Callable
from src.data.use_cases.decode_token import DecodeToken
from src.presentation.controllers.delete_user_controller import DeleteUserController

def decode_token_composer() -> Callable[[HttpRequest], HttpResponse]:
    decoder = Decoder(AuthAlgoritm, SecretKey)
    decode_token = DecodeToken(decoder)
    delete_user_controller = DeleteUserController(decode_token)
    return delete_user_controller.handle