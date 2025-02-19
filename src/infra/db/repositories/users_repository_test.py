from src.infra.db.tests.utils.clear_database import set_up
from src.infra.db.tests.utils.select_user import select_user
from src.infra.db.tests.utils.insert_user import insert_user
from datetime import datetime, timezone
from src.infra.db.repositories.users_repository import UsersRepository
from src.infra.db.config.database_connection.connection.test_string_connection import TestStringConnection


@set_up
def test_insert_user_repository() -> None:

    mocked_username = 'username'
    mocked_password = 'password'

    user_repository = UsersRepository(TestStringConnection)
    user_repository.insert(mocked_username, mocked_password)
    engine = user_repository.get_db_connection_handler().get_engine()

    users = select_user(engine)

    assert users[0].username == mocked_username
    assert users[0].password == mocked_password

@set_up
def test_select_user_repository() -> None:

    mocked_username = 'username'
    mocked_password = 'password'
    mocked_created_at = datetime.now(timezone.utc)

    user_repository = UsersRepository(TestStringConnection)
    engine = user_repository.get_db_connection_handler().get_engine()
    insert_user(mocked_username, mocked_password, mocked_created_at, engine)

    selected_user = user_repository.select(mocked_username)
    user = selected_user[0]

    assert user.username == mocked_username
    assert user.password == mocked_password
    assert user.created_at == mocked_created_at

@set_up
def test_delete_user_repository() -> None:

    mocked_username = 'username'
    mocked_password = 'password'
    mocked_created_at = datetime.now(timezone.utc)

    user_repository = UsersRepository(TestStringConnection)
    engine = user_repository.get_db_connection_handler().get_engine()
    insert_user(mocked_username, mocked_password, mocked_created_at, engine)
    users = select_user(engine)
    assert users
    user_repository.delete(mocked_username)
    users = select_user(engine)
    assert not users

@set_up
def test_update_user_repository() -> None:

    mocked_username = 'username'
    mocked_username_2 = 'username_2'
    mocked_password = 'password'
    mocked_created_at = datetime.now(timezone.utc)

    user_repository = UsersRepository(TestStringConnection)
    engine = user_repository.get_db_connection_handler().get_engine()
    insert_user(mocked_username, mocked_password, mocked_created_at, engine)

    user_repository.update(mocked_username, {'username': mocked_username_2})

    users = select_user(engine)
    user = users[0]

    assert user.username == mocked_username_2