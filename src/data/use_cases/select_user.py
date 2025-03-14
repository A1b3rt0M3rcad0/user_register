from src.domain.use_cases.i_select_user import ISelectUser
from src.domain.dtos.select_user_dto import SelectUserDTO
from src.data.interfaces.i_users_repository import IUsersRepository
from src.validators.username_validator import UsernameValidator
from src.errors.types.http_bad_request_error import BadRequestError
from src.log.loggers.info_logger import InfoLogger
from src.log.loggers.error_logger import ErrorLogger

class SelectUser(ISelectUser):
    
    def __init__(self, user_repository:IUsersRepository) -> None:
        self.__user_repository = user_repository
    
    def select(self, username:str) -> SelectUserDTO:
        UsernameValidator.valid(username)
        try:
            user = self.__user_repository.select(username)[0]
            created_at = user.created_at
            response = SelectUserDTO(username, created_at)
            InfoLogger.log(f"SelectUser: {username} selected")
            return response
        except Exception as e:
            ErrorLogger.log(f"SelectUser: Error in SelectUser use_case {str(e)}")
            raise BadRequestError(f"Error in select user {e}") from e
