from src.data.use_cases.select_user import SelectUser
from src.infra.db.config.database_connection.connection.test_string_connection import TestStringConnection
from src.infra.db.repositories.users_repository import UsersRepository
from src.errors.types.http_bad_request_error import BadRequestError
from src.infra.db.tests.utils.clear_database import set_up
from src.infra.db.tests.utils.insert_user import insert_user
from datetime import datetime, timezone

@set_up
def test_select_user_dto() -> None:
    username = "username"
    password = "password"
    created_at = datetime.now(timezone.utc)

    repository = UsersRepository(TestStringConnection)
    engine = repository.get_db_connection_handler().get_engine()
    insert_user(username, password, created_at, engine)
    select_user_case = SelectUser(repository)

    response = select_user_case.select(username).to_dict()
    assert response["type"] == "Users"
    assert response["attrs"]["username"] == username
    assert response["attrs"]["created_at"] == created_at

@set_up
def test_select_user_valid_username() -> None:
    username = "12345"

    repository = UsersRepository(TestStringConnection)
    select_user_case = SelectUser(repository)
    try:
        select_user_case.select(username)
    except BadRequestError as e:
        assert e.message == 'The username length is less than or equal to 5'
