from src.controllers.interfaces.user_list_controller import UserListControllerInterface
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class ListUsersView(ViewInterface):
    def __init__(self, controller: UserListControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request) -> HttpResponse:
        users = self.__controller.list()
        body_response=[user.dict() for user in users]
        return HttpResponse(status_code=201, body=body_response)
