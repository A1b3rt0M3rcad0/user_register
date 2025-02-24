from flask import Request as FlaskRequest
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from typing import Callable


def request_adapter(request:FlaskRequest, controller:Callable[[HttpRequest], HttpResponse]) -> HttpResponse:
    body = None
    if request.data:
        body = request.json
    
    http_request = HttpRequest(
        body = body,
        headers=request.headers,
        query_params=request.args,
        path_params=request.view_args,
        url=request.full_path
    )
    http_reponse = controller(http_request)
    return http_reponse