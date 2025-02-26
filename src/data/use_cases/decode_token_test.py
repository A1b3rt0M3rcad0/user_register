from src.auth.config.auth_algoritm import AuthAlgoritm
from src.auth.config.auth_secret_key import SecretKey
from src.auth.cryptography.decoder import Decoder
from src.data.use_cases.decode_token import DecodeToken

MOCKED_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IkFsYmVydG8iLCJleHAiOjE3NDA4MzU1NDB9.SUawS3_ufdJ9tXLRCwUT_LXQurVu8s-TmHXZnKKZ6mQ'

def test_docode_token() -> None:

    decoder = Decoder(AuthAlgoritm, SecretKey)
    decode_token = DecodeToken(decoder)
    decoded_token = decode_token.decode(MOCKED_TOKEN)

    assert decoded_token.username == "Alberto"
