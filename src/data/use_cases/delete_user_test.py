from src.data.use_cases.delete_user import DeleteUser
from src.infra.db.config.database_connection.connection.test_string_connection import TestStringConnection
from src.infra.db.repositories.users_repository import UsersRepository
from src.errors.types.http_bad_request_error import BadRequestError
from src.infra.db.tests.utils.clear_database import set_up
from src.infra.db.tests.utils.insert_user import insert_user
from src.infra.db.tests.utils.select_user import select_user
from datetime import datetime,timezone

@set_up
def test_delete_user() -> None:
    username = "username"
    password = "password"
    created_at = datetime.now(timezone.utc)

    repository = UsersRepository(TestStringConnection)
    engine = repository.get_db_connection_handler().get_engine()

    insert_user(username, password, created_at, engine)

    delete_user = DeleteUser(repository)
    delete_user.delete(username)

    response = select_user(engine)

    assert len(response) == 0

@set_up
def test_delete_user_username_validator() -> None:
    username = '12345'

    repository = UsersRepository(TestStringConnection)
    delete_user = DeleteUser(repository)
    try:
        delete_user.delete(username)
    except BadRequestError as e:
        assert e.message == "The username length is less than or equal to 5"

@set_up
def test_delete_user_dto() -> None:
    username = "username"
    password = "password"
    created_at = datetime.now(timezone.utc)

    repository = UsersRepository(TestStringConnection)
    engine = repository.get_db_connection_handler().get_engine()

    insert_user(username, password, created_at, engine)

    delete_user = DeleteUser(repository)
    delete_user_dto = delete_user.delete(username).to_dict()

    assert delete_user_dto["type"] == "Users"
    assert delete_user_dto["attrs"]["username"] == username
