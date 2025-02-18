from src.infra.db.tests.utils.clear_database import set_up
from src.infra.db.tests.utils.select_user import select_user
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