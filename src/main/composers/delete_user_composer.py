from src.main.config import DatabaseStringConnection
from src.infra.db.repositories.users_repository import UsersRepository
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from typing import Callable
from src.data.use_cases.delete_user import DeleteUser
from src.presentation.controllers.delete_user_controller import DeleteUserController

def delete_user_composer() -> Callable[[HttpRequest], HttpResponse]:
    repository = UsersRepository(DatabaseStringConnection)
    delete_user = DeleteUser(repository)
    delete_user_controller = DeleteUserController(delete_user)
    return delete_user_controller.handle