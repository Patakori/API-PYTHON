from pydantic import BaseModel, ValidationError, constr
from src.views.http_types.http_request import HttpRequest
from src.erros.error_types.http_unprocessable_entity import HttpUnprocessableEntityError

def get_user_validator(http_request: HttpRequest) -> None:

    class BodyData(BaseModel):
        email: constr(min_length=1) # type: ignore

    try:
        BodyData(**http_request.body)
    except ValidationError as e:
        raise HttpUnprocessableEntityError from e
