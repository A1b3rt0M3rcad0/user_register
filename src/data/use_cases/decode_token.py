from src.domain.auth.cryptography.i_decoder import IDecoder
from src.domain.dtos.decode_token_dto import DecodeTokenDTO

class DecodeToken(IDecoder):

    def __init__(self, decoder:IDecoder) -> None:
        self.__decoder = decoder
    
    def decode(self, token:str) -> DecodeTokenDTO:
        token_decoded = self.__decoder.decode(token)
        username = token_decoded["username"]
        return DecodeTokenDTO(username=username)