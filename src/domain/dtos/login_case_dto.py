from src.domain.dtos.interfaces.i_dto import IDTO

class LoginDTO(IDTO):

    def __init__(self, username:str, token:str) -> None:
        self.__username = username
        self.__token = token
    
    def to_dict(self):
        return {
            'type': 'Auth',
            'attrs': {
                'username': self.__username,
                'token': self.__token
            }
        }