from src.main.config import DatabaseStringConnection
from src.infra.db.repositories.users_repository import UsersRepository
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from typing import Callable
from src.data.use_cases.select_user import SelectUser
from src.presentation.controllers.select_user_controller import SelectUserController

def select_user_composer() -> Callable[[HttpRequest], HttpResponse]:
    repository = UsersRepository(DatabaseStringConnection)
    select_user = SelectUser(repository)
    select_user_controller = SelectUserController(select_user)
    return select_user_controller.handle