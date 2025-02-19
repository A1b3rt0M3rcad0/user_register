from src.domain.dtos.interfaces.i_dto import IDTO
from typing import Dict

class DeleteUserDTO(IDTO):

    def __init__(self, username:str) -> None:
        self.__username = username
    
    def to_dict(self) -> Dict:
        return {
            'type': 'Users',
            'attrs': {
                'username': self.__username,
            }
        }