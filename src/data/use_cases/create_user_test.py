from src.data.use_cases.create_user import CreateUser
from src.infra.db.repositories.users_repository import UsersRepository
from src.infra.db.config.database_connection.connection.test_string_connection import TestStringConnection
from src.infra.db.tests.utils.clear_database import set_up
from src.infra.db.tests.utils.select_user import select_user
from src.errors.types.http_bad_request_error import BadRequestError

@set_up
def test_create_user() -> None:
    mocked_username = 'username'
    mocked_password = 'to_long_password'

    test_string_connection = TestStringConnection()
    user_repository = UsersRepository(test_string_connection)
    db_connection_handler = user_repository.get_db_connection_handler()
    engine = db_connection_handler.get_engine()
    create_user = CreateUser(user_repository)

    create_user.create(mocked_username, mocked_password)

    users = select_user(engine)
    user = users[0]

    assert user.username == mocked_username
    assert user.password == mocked_password

@set_up
def test_create_user_username_validator() -> None:
    mocked_username_less_equal = '12345'
    mocked_username_empty_characters = '123 123'
    mocked_empty_username = ''
    mocked_password = 'to_long_password'

    test_string_connection = TestStringConnection()
    user_repository = UsersRepository(test_string_connection)
    create_user = CreateUser(user_repository)

    try:
        create_user.create(mocked_username_less_equal, mocked_password)
    except BadRequestError as e:
        assert e.message == 'The username length is less than or equal to 5'
    
    try:
        create_user.create(mocked_username_empty_characters, mocked_password)
    except BadRequestError as e:
        assert e.message == 'The username has empty characters'
    try:
        create_user.create(mocked_empty_username, mocked_password)
    except BadRequestError as e:
        assert e.message == 'The username is empty'

@set_up
def test_create_user_password_validator() -> None:
    mocked_username = 'username'
    mocked_password_less_equal = '12345678'
    mocked_password_empty_characters = '12345 123'
    mocked_empty_password = ''

    test_string_connection = TestStringConnection()
    user_repository = UsersRepository(test_string_connection)
    create_user = CreateUser(user_repository)

    try:
        create_user.create(mocked_username, mocked_password_less_equal)
    except BadRequestError as e:
        assert e.message == 'The password length less then or equal to 8'
    try:
        create_user.create(mocked_username, mocked_password_empty_characters)
    except BadRequestError as e:
        assert e.message == 'The password has empty characters'
    try:
        create_user.create(mocked_username, mocked_empty_password)
    except BadRequestError as e:
        assert e.message == 'The password is empty'

@set_up
def test_create_user_response() -> None:
    mocked_username = 'username'
    mocked_password = 'to_long_password'

    test_string_connection = TestStringConnection()
    user_repository = UsersRepository(test_string_connection)
    create_user = CreateUser(user_repository)

    response = create_user.create(mocked_username, mocked_password)
    response_dict = response.to_dict()

    assert response_dict['attrs']['username'] == mocked_username
    assert response_dict['attrs']['password'] == mocked_password
    assert response_dict['type'] == 'Users'
    
