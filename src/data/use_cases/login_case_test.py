from src.infra.db.repositories.users_repository import UsersRepository
from src.infra.db.config.database_connection.connection.test_string_connection import TestStringConnection
from src.infra.db.tests.utils.clear_database import set_up
from src.infra.db.tests.utils.insert_user import insert_user
from src.auth.config.auth_algoritm import AuthAlgoritm
from src.auth.config.auth_secret_key import SecretKey
from src.errors.types.http_bad_request_error import BadRequestError
from src.data.use_cases.login_case import LoginCase
from src.auth.cryptography.encoder import Encoder
from src.auth.cryptography.decoder import Decoder
from src.security.hash.sha224.password_check import PasswordHashChecker
from src.security.hash.sha224.password_hashing import PasswordHashing
from datetime import datetime, timezone


@set_up
def test_login_case() -> None:
    username = 'username'
    password = 'password'
    created_at = datetime.now(timezone.utc)
    hashed_password = PasswordHashing.hash(password)

    repository = UsersRepository(TestStringConnection)
    engine = repository.get_db_connection_handler().get_engine()

    insert_user(username, hashed_password, created_at, engine)

    encoder = Encoder(AuthAlgoritm, SecretKey)
    login_case = LoginCase(repository, encoder, PasswordHashChecker)
    login_case_dto = login_case.login(username, password).to_dict()
    token = login_case_dto["attrs"]["token"]

    decoder = Decoder(AuthAlgoritm, SecretKey)

    response = decoder.decode(token)
    
    assert response["username"] == "username"

@set_up
def test_login_case_user_does_not_exists() -> None:
    username = 'username'
    password = 'password'

    repository = UsersRepository(TestStringConnection)
    encoder = Encoder(AuthAlgoritm, SecretKey)
    login_case = LoginCase(repository, encoder, PasswordHashChecker)

    try:
        login_case.login(username, password)
    except BadRequestError as e:
        assert e.message == "User does not exists"

@set_up
def test_login_case_invalid_password() -> None:
    username = 'username'
    password = 'password'
    test_password = 'test_password'
    created_at = datetime.now(timezone.utc)
    hashed_password = PasswordHashing.hash(password)

    repository = UsersRepository(TestStringConnection)
    engine = repository.get_db_connection_handler().get_engine()

    insert_user(username, hashed_password, created_at, engine)

    try:
        encoder = Encoder(AuthAlgoritm, SecretKey)
        login_case = LoginCase(repository, encoder, PasswordHashChecker)
        login_case.login(username, test_password).to_dict()
    except BadRequestError as e:
        assert e.message == "Invalid Password"