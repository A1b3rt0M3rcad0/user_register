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
            return DeleteUserDTO(username)
        except Exception as e:
            raise BadRequestError(f"Error in deleting user {str(e)}") from e