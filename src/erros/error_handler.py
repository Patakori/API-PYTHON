from src.views.http_types.http_response import HttpResponse
from .error_types.http_bad_request import HttpBadRequestError
from .error_types.http_unprocessable_entity import HttpUnprocessableEntityError
from .error_types.http_not_found import HttpNotFoundError

def handle_errors(error: Exception) -> HttpResponse:
    if isinstance(error, (HttpBadRequestError, HttpUnprocessableEntityError, HttpNotFoundError)):
        return HttpResponse(
            status_code=error.status_code,
            body={
                "erros": [{
                    "title": error.name,
                    "detail": error.message
                }]
            }
        )
    return HttpResponse(
        status_code=500,
            body={
                "erros": [{
                    "title": "Server Error",
                    "detail": str(error)
                }]
            }
    )