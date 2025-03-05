from src.validators.username_validator import UsernameValidator
from src.validators.password_validator import PasswordValidator
from src.domain.use_cases.i_create_user import ICreateUser
from src.data.interfaces.i_users_repository import IUsersRepository
from src.domain.dtos.create_user_dto import CreateUserDTO
from src.errors.types.http_bad_request_error import BadRequestError
from src.domain.security.hash.i_password_hashing import IPasswordHashing
from sqlalchemy.exc import IntegrityError
from datetime import datetime, timezone

class CreateUser(ICreateUser):

    def __init__(self, user_repository:IUsersRepository, password_hashing:IPasswordHashing) -> None:
        self.__user_repository = user_repository
        self.__password_hashing = password_hashing
    
    def create(self, username:str, password:str) -> CreateUserDTO:
        UsernameValidator.valid(username)
        PasswordValidator.valid(password)
        try:
            password = self.__password_hashing.hash(password)
            self.__user_repository.insert(username, password)
        except IntegrityError as e:
            raise BadRequestError("Username already exists") from e
        except Exception as e:
            raise BadRequestError(f"Error adding a new user to the database {str(e)}") from e
        created_at = datetime.now(timezone.utc)
        return CreateUserDTO(username, password, created_at)