from src.main.config import DatabaseStringConnection
from src.infra.db.repositories.users_repository import UsersRepository
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from typing import Callable
from src.presentation.controllers.change_username_controller import ChangeUsernameController
from src.data.use_cases.change_username import ChangeUsername

def change_username_composer() -> Callable[[HttpRequest], HttpResponse]:
    repository = UsersRepository(DatabaseStringConnection)
    change_username = ChangeUsername(repository)
    change_username_controller = ChangeUsernameController(change_username)
    return change_username_controller.handle