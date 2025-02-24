import jwt
from src.domain.auth.cryptography.i_encoder import IEncoder
from src.domain.auth.config.i_auth_algoritm import IAuthAlgoritm
from src.domain.auth.config.i_auth_secret_key import ISecretKey
from typing import Dict

class Encoder(IEncoder):

    def __init__(self, auth_algortim:IAuthAlgoritm, secret_key:ISecretKey) -> None:
        self.__auth_algoritm = auth_algortim.get_algoritm()
        self.__secret_key = secret_key.get_sercret_key()
    
    def encode(self, params:Dict) -> str:
        jwt.encode(payload=params, key=self.__secret_key, algorithm=self.__auth_algoritm)