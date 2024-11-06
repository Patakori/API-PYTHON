from pydantic import BaseModel, ValidationError, constr
from src.views.http_types.http_request import HttpRequest
from src.erros.error_types.http_unprocessable_entity import HttpUnprocessableEntityError

def get_user_validator(http_request: HttpRequest) -> None:

    class BodyData(BaseModel):
        email: constr(min_length=1) # type: ignore

    try:
        validated_data = BodyData(**http_request).model_dump()
        return validated_data
    except ValidationError as e:
        raise HttpUnprocessableEntityError from e
