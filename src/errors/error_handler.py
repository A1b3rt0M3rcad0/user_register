from src.presentation.http_types.http_response import HttpResponse
from src.errors.types.http_bad_request_error import BadRequestError
from src.errors.types.http_unauthorized_error import UnauthorizedError
from src.errors.types.http_unprocessable_entity_error import HttpUnprocessableEntityError

def error_handler(error: Exception) -> HttpResponse:

    if isinstance(error, (BadRequestError, UnauthorizedError, HttpUnprocessableEntityError)):
        return HttpResponse(
            status_code=error.status_code,
            body={
                "errors": [{
                    "title": error.title,
                    "detail": error.message
                }]
            }
        )
    return HttpResponse(
        status_code=500,
        body = {
            "errors": [{
                "title": "Internal Server Error",
                "detail": str(error)
            }]
        }
    )