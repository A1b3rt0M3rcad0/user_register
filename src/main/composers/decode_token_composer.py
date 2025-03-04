from src.auth.cryptography.decoder import Decoder
from src.auth.config.auth_algoritm import AuthAlgoritm
from src.auth.config.auth_secret_key import SecretKey
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from typing import Callable
from src.data.use_cases.decode_token import DecodeToken
from src.presentation.controllers.decode_token_controller import DecodeTokenController

def decode_token_composer() -> Callable[[HttpRequest], HttpResponse]:
    decoder = Decoder(AuthAlgoritm, SecretKey)
    decode_token = DecodeToken(decoder)
    decode_token_controller = DecodeTokenController(decode_token)
    return decode_token_controller.handle