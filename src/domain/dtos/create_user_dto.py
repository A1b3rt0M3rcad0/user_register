from src.domain.dtos.interfaces.i_dto import IDTO
from typing import Dict
from datetime import datetime

class CreateUserDTO(IDTO):

    def __init__(self, username:str, password:str, created_at:datetime) -> None:
        self.__username = username
        self.__password = password
        self.__created_at = created_at
    
    def to_dict(self) -> Dict:
        return {
            'type': 'Users',
            'attrs': {
                'username': self.__username,
                'password': self.__password,
                'created_at': self.__created_at
            }
        }