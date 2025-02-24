from src.presentation.http_types.http_response import HttpReponse
from src.errors.types.http_bad_request_error import BadRequestError

def error_handler(error: Exception) -> HttpReponse:

    if isinstance(error, (BadRequestError)):
        return HttpReponse(
            status_code=error.status_code,
            body={
                "errors": [{
                    "title": error.title,
                    "detail": error.message
                }]
            }
        )
    return HttpReponse(
        status_code=500,
        body = {
            "errors": [{
                "title": "Internal Server Error",
                "detail": str(error)
            }]
        }
    )