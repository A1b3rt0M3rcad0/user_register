from src.domain.security.hash.i_password_hashing import IPasswordHashing
from hashlib import sha224

class PasswordHashing(IPasswordHashing):

    @staticmethod
    def hash(password:str) -> str:
        hash_password = sha224(password.encode('utf-8'))
        hash_password = hash_password.hexdigest()
        return hash_password