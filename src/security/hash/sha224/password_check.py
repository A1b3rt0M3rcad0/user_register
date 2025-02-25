#pylint:disable=E0401
from src.domain.security.hash.i_password_check import IPasswordHashChecker
from hashlib import sha224

class PasswordHashChecker(IPasswordHashChecker):

    @staticmethod
    def check(password:str, database_password:str) -> bool:
        hash_password = sha224(password.encode('utf-8')).hexdigest()
        return hash_password == database_password