from src.log.loggers.info_logger import InfoLogger
from src.log.loggers.error_logger import ErrorLogger
from src.data.interfaces.i_users_repository import IUsersRepository
from src.domain.dtos.delete_user_dto import DeleteUserDTO
from src.validators.username_validator import UsernameValidator
from src.domain.use_cases.i_delete_user import IDeleteUser
from src.errors.types.http_bad_request_error import BadRequestError


class DeleteUser(IDeleteUser):

    def __init__(self, user_repository:IUsersRepository) -> None:
        self.__user_repository = user_repository
    
    def delete(self, username:str) -> DeleteUserDTO:
        UsernameValidator.valid(username)
        try:
            self.__user_repository.delete(username)
            InfoLogger.log(f"DeleteUser: {username} deleted")
            return DeleteUserDTO(username)
        except Exception as e:
            ErrorLogger.log(f"DeleteUser: Error in deleting user {str(e)}")
            raise BadRequestError(f"Error in deleting user {str(e)}") from e