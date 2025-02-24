from src.domain.validators.i_username_equal_validator import IUsarnameEqualValidator
from src.errors.types.http_bad_request_error import BadRequestError

class UsarnameEqualValidator(IUsarnameEqualValidator):

    @staticmethod
    def valid(username:str, new_username:str) -> None:
        if username == new_username:
            raise BadRequestError('the username is equal to your old username')