from src.data.interfaces.i_users_repository import IUsersRepository
from src.infra.db.config.database_connection.interface.i_string_connection import IStringConnection
from src.infra.db.connection.factory.db_connection_handler_factory import DBConnectionHandlerFactory
from src.infra.db.connection.connection_handler.db_connection_handler import DBConnectionHandler
from src.infra.db.entities.users import Users as UsersEntity
from src.domain.models.users import Users
from typing import Dict, List

class UsersRepository(IUsersRepository):

    def __init__(self, string_connection:IStringConnection) -> None:
        self.__db_connection_handler = DBConnectionHandlerFactory.create_connection(string_connection)
    
    def get_db_connection_handler(self) -> DBConnectionHandler:
        return self.__db_connection_handler
    
    def insert(self, username:str, password:str) -> None:
        with self.__db_connection_handler as db:
            try:
                user = UsersEntity(username=username, password=password)
                db.session.add(user)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise e
            
    def select(self, username:str) -> List[Users]:
        with self.__db_connection_handler as db: 
            try:  
                users = db.session.query(UsersEntity)\
                .filter(UsersEntity.username == username)\
                .all()
                return users
            except Exception as e:
                raise e
    
    def delete(self, username:str) -> None:
        with self.__db_connection_handler as db:
            try:
                db.session.query(UsersEntity)\
                .filter(UsersEntity.username == username)\
                .delete()
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception
    
    def update(self, username:str, update_params:Dict) -> None:
        with self.__db_connection_handler as db:
            try:
                db.session.query(UsersEntity)\
                    .filter(UsersEntity.username == username)\
                    .update(update_params)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise e