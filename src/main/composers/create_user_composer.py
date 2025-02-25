from src.main.config import DatabaseStringConnection
from src.infra.db.repositories.users_repository import UsersRepository
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from typing import Callable
from src.data.use_cases.create_user import CreateUser
from src.presentation.controllers.create_user_controller import CreateUserController
from src.security.hash.sha224.password_hashing import PasswordHashing

def create_user_composer() -> Callable[[HttpRequest], HttpResponse]:
    repository = UsersRepository(DatabaseStringConnection)
    create_user = CreateUser(repository, PasswordHashing)
    create_user_controller = CreateUserController(create_user)
    return create_user_controller.handle
