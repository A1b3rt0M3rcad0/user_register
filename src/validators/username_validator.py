from src.domain.validators.i_username_validator import IUsernameValidator
from src.errors.types.http_bad_request_error import BadRequestError

class UsernameValidator(IUsernameValidator):

    @staticmethod
    def valid(username:str) -> None:
        length = 5
        if ' ' in username:
            raise BadRequestError('The username has empty characters')
        if not username:
            raise BadRequestError('The username is empty')
        if len(username) <= length:
            raise BadRequestError('The username length is less than or equal to {length}')