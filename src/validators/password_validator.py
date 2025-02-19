from src.domain.validators.i_password_validator import IPasswordValidator
from src.errors.types.http_bad_request_error import BadRequestError

class PasswordValidator(IPasswordValidator):

    @staticmethod
    def valid(password:str) -> None:
        length = 8
        if ' ' in password:
            raise BadRequestError('The password has empty characters')
        if not password:
            raise BadRequestError('The password is empty')
        if len(password) <= length:
            raise BadRequestError(f'The password length less then or equal to {length}')