import os
from src.domain.auth.config.i_auth_algoritm import IAuthAlgoritm

class AuthAlgoritm(IAuthAlgoritm):

    @staticmethod
    def get_algoritm() -> str:
        return os.getenv("AUTH_ALGORITM")