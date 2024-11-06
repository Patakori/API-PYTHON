from pydantic import ValidationError
from src.models.user_model import UserModel
from src.views.http_types.http_request import HttpRequest
from src.erros.error_types.http_unprocessable_entity import HttpUnprocessableEntityError

def create_user_validator(http_request: HttpRequest) -> None:
    try:
        validated_data = UserModel(**http_request)
        return validated_data.model_dump()
    except ValidationError as e:
        raise HttpUnprocessableEntityError from e
