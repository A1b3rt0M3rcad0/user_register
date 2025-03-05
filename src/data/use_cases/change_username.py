from src.log.loggers.info_logger import InfoLogger
from src.log.loggers.error_logger import ErrorLogger
from src.domain.use_cases.i_change_username import IChangeUsername
from src.validators.username_validator import UsernameValidator
from src.validators.username_equal_validator import UsarnameEqualValidator
from src.data.interfaces.i_users_repository import IUsersRepository
from src.domain.dtos.change_username_dto import ChangeUsernameDTO
from src.errors.types.http_bad_request_error import BadRequestError
from sqlalchemy.exc import IntegrityError

class ChangeUsername(IChangeUsername):

    def __init__(self, user_repository:IUsersRepository) -> None:
        self.__user_repository = user_repository
    
    def update(self, username:str, new_username:str) -> ChangeUsernameDTO:
        UsernameValidator.valid(username)
        UsernameValidator.valid(new_username)
        UsarnameEqualValidator.valid(username, new_username)
        try:
            update_params = {
                "username": new_username
            }
            self.__user_repository.update(username, update_params)
            InfoLogger.log(f"ChangeUsername: {username} changed to {new_username}")
            return ChangeUsernameDTO(username, new_username)
        except IntegrityError as e:
            ErrorLogger.log("ChangeUsername: Username already exists")
            raise BadRequestError("Username already exists") from e
        except Exception as e:
            ErrorLogger.log(f"ChangeUsername: Error in change username {str(e)}")
            raise BadRequestError(f"Error in change username {e}") from e