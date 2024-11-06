from src.controllers.interfaces.create_user import CreateUserControllerInterface
from src.validator.create_user_validator import create_user_validator
from .http_types.http_response import HttpResponse
from .http_types.http_request import HttpRequest
from .interfaces.view_interface import ViewInterface

class CreateUsersView(ViewInterface):
    def __init__(self, controller: CreateUserControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        user_data = create_user_validator(http_request.body)
        body_response = self.__controller.create(user_data)
        return HttpResponse(status_code=201, body=body_response)
