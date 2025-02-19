from src.domain.dtos.interfaces.i_dto import IDTO
from typing import Dict
from datetime import datetime

class SelectUserDTO(IDTO):

    def __init__(self, username:str, created_at:datetime) -> None:
        self.__username = username
        self.__created_at = created_at
    
    def to_dict(self) -> Dict:
        return {
            'type': 'Users',
            'attrs': {
                'username': self.__username,
                'created_at': self.__created_at
            }
        }