from src.domain.dtos.interfaces.i_dto import IDTO
from typing import Dict

class ChangeUsernameDTO(IDTO):

    def __init__(self, username:str, new_username:str) -> None:
        self.__username = username
        self.__new_username = new_username
    
    def to_dict(self) -> Dict:
        return {
            'type': 'Users',
            'attrs': {
                'username': self.__username,
            },
            'new_username': self.__new_username
        }