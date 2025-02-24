from src.domain.auth.config.i_auth_secret_key import ISecretKey
import os

class SecretKey(ISecretKey):

    @staticmethod
    def get_sercret_key() -> str:
        return str(os.getenv("AUTH_SECRET_KEY"))