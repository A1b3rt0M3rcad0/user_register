from src.errors.types.http_unprocessable_entity_error import HttpUnprocessableEntityError
from cerberus import Validator

def select_user_validator(request:any) -> None:
    
    query_validator = Validator({
        "username": {"type": "string", "required": True, "empty": False}
    })

    response = query_validator.validate(request.json)

    if response is False:
        raise HttpUnprocessableEntityError(query_validator.errors)