from src.data.use_cases.authenticate_token import AuthenticateToken
from src.auth.cryptography.decoder import Decoder
from src.auth.cryptography.encoder import Encoder
from src.auth.config.auth_algoritm import AuthAlgoritm
from src.auth.config.auth_secret_key import SecretKey
from src.errors.types.http_unauthorized_error import UnauthorizedError
from datetime import datetime, timezone

def test_authenticate_token_case() -> None:

    response_dict = {
        'username': 'username',
        'exp': datetime.now(timezone.utc)
    }

    encoder = Encoder(AuthAlgoritm, SecretKey)
    token = encoder.encode(response_dict)

    decoder = Decoder(AuthAlgoritm, SecretKey)
    authenticate_token = AuthenticateToken(decoder)

    try:
        authenticate_token.authenticate(token)
    except UnauthorizedError as e:
        assert e.message == "Token expired"