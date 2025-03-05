import jwt
from src.errors.types.http_unauthorized_error import UnauthorizedError
from src.domain.auth.cryptography.i_decoder import IDecoder
from src.domain.auth.config.i_auth_algoritm import IAuthAlgoritm
from src.domain.auth.config.i_auth_secret_key import ISecretKey
from src.log.loggers.info_logger import InfoLogger
from src.log.loggers.error_logger import ErrorLogger
from jwt.exceptions import ExpiredSignatureError
from typing import Dict

class Decoder(IDecoder):

    def __init__(self, auth_algortim:IAuthAlgoritm, secret_key:ISecretKey) -> None:
        self.__auth_algoritm = auth_algortim.get_algoritm()
        self.__secret_key = secret_key.get_sercret_key()
    
    def decode(self, token:str) -> Dict:
        try:
            response = jwt.decode(jwt=token, key=self.__secret_key, algorithms=self.__auth_algoritm)
            InfoLogger.log(f"Decoder: token {token} decoded")
            return response
        except ExpiredSignatureError as e:
            ErrorLogger.log("Decoder: Token expired")
            raise UnauthorizedError("Token expired") from e
