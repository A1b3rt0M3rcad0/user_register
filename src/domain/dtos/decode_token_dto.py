from src.domain.dtos.interfaces.i_dto import IDTO

class DecodeTokenDTO(IDTO):

    def __init__(self, username:str) -> None:
        self.username = username
    
    def to_dict(self):
        return {
            "username": self.username
        }