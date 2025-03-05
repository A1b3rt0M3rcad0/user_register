from src.infra.db.repositories.users_repository import UsersRepository
from src.data.use_cases.login_case import LoginCase
from src.auth.cryptography.encoder import Encoder
from src.auth.config.auth_algoritm import AuthAlgoritm
from src.auth.config.auth_secret_key import SecretKey
from src.presentation.controllers.login_case_controller import LoginCaseController
from src.main.config import DatabaseStringConnection
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.security.hash.sha224.password_check import PasswordHashChecker
from typing import Callable

def login_case_composer() -> Callable[[HttpRequest], HttpResponse]:
    repository = UsersRepository(DatabaseStringConnection)
    encoder = Encoder(AuthAlgoritm, SecretKey)
    login_case = LoginCase(repository, encoder, PasswordHashChecker)
    login_case_controller = LoginCaseController(login_case)
    return login_case_controller.handle