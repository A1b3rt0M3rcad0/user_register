from src.domain.dtos.interfaces.i_dto import IDTO
from typing import Dict

class UpdateUserDTO(IDTO):

    def __init__(self, username:str, update_params:Dict) -> None:
        self.__username = username
        self.__update_params = update_params
    
    def to_dict(self) -> Dict:
        return {
            'type': 'Users',
            'attrs': {
                'username': self.__username,
            },
            'update_params': self.__update_params
        }