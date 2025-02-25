from src.domain.auth.cryptography.i_decoder import IDecoder
from src.domain.use_cases.i_authenticate_token import IAuthenticateToken

class AuthenticateToken(IAuthenticateToken):

    def __init__(self, decoder:IDecoder) -> None:
        self.__decoder = decoder
    
    def authenticate(self, token:str) -> None:
        self.__decoder.decode(token)