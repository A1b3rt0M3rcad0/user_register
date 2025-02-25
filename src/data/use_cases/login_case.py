from src.domain.dtos.login_case_dto import LoginDTO
from src.domain.use_cases.i_login_case import ILoginCase
from src.data.interfaces.i_users_repository import IUsersRepository
from src.domain.auth.cryptography.i_encoder import IEncoder
from src.domain.security.hash.i_password_check import IPasswordHashChecker
from src.errors.types.http_bad_request_error import BadRequestError

#MOCKED DATETIME EXP
from datetime import datetime, timezone, timedelta

class LoginCase(ILoginCase):

    def __init__(self, 
                 user_repository:IUsersRepository, 
                 encoder:IEncoder,
                 password_hash_checker:IPasswordHashChecker
                 ) -> None:
        self.__user_repository = user_repository
        self.__encoder = encoder
        self.__password_hash_checker = password_hash_checker

    def login(self, username:str, password:str) -> LoginDTO:
        try:
            users = self.__user_repository.select(username)
            user = users[0]
        except IndexError as e:
            raise BadRequestError("User does not exists") from e
        except Exception as e:
            raise RuntimeError(f"Unexpected error occurred during login: {str(e)}") from e
        
        database_password = user.password

        if not self.__password_hash_checker.check(password, database_password):
            raise BadRequestError("Invalid Password")
        
        params = {
            "username": username,
            "exp": datetime.now(timezone.utc) + timedelta(days=3) # Mocked EXP TIME
        }
        token = self.__encoder.encode(params)
        return LoginDTO(
            username=username,
            token=token
        )