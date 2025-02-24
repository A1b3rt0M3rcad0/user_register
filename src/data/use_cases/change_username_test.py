from src.data.use_cases.change_username import ChangeUsername
from src.infra.db.repositories.users_repository import UsersRepository
from src.infra.db.config.database_connection.connection.test_string_connection import TestStringConnection
from src.infra.db.tests.utils.clear_database import set_up
from src.infra.db.tests.utils.insert_user import insert_user
from src.infra.db.tests.utils.select_user import select_user
from datetime import datetime, timezone
from src.errors.types.http_bad_request_error import BadRequestError

@set_up
def test_change_username() -> None:
    username = 'username'
    password = 'to_long_password'
    created_at = datetime.now(timezone.utc)
    new_username = 'new_username'

    repository = UsersRepository(TestStringConnection)
    engine = repository.get_db_connection_handler().get_engine()
    insert_user(username, password, created_at, engine)
    
    change_username = ChangeUsername(repository)
    change_username.update(username, new_username)

    response = select_user(engine)

    assert response[0].username == new_username

@set_up
def test_change_username_valid_username() -> None:
    username = '12345'
    new_username = 'new_username'

    repository = UsersRepository(TestStringConnection)
    change_username = ChangeUsername(repository)

    try:
        change_username.update(username, new_username)
    except BadRequestError as e:
        assert "The username length is less than or equal to 5" == e.message

@set_up
def test_change_username_valid_new_username() -> None:
    username = 'username'
    new_username = '12345'

    repository = UsersRepository(TestStringConnection)
    change_username = ChangeUsername(repository)

    try:
        change_username.update(username, new_username)
    except BadRequestError as e:
        assert "The username length is less than or equal to 5" == e.message

@set_up
def test_change_username_equal_validator() -> None:
    username = 'username'
    new_username = 'username'

    repository = UsersRepository(TestStringConnection)
    change_username = ChangeUsername(repository)

    try:
        change_username.update(username, new_username)
    except BadRequestError as e:
        assert "the username is equal to your old username" == e.message

@set_up
def test_change_username_dto() -> None:
    username = 'username'
    password = 'to_long_password'
    created_at = datetime.now(timezone.utc)
    new_username = 'new_username'

    repository = UsersRepository(TestStringConnection)
    engine = repository.get_db_connection_handler().get_engine()
    insert_user(username, password, created_at, engine)
    
    change_username = ChangeUsername(repository)
    change_username_dto = change_username.update(username, new_username).to_dict()

    assert change_username_dto["type"] == 'Users'
    assert change_username_dto["attrs"]["username"] == username
    assert change_username_dto["new_username"] == new_username
