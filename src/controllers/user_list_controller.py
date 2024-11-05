from src.controllers.interfaces.user_list_controller import UserListControllerInterface
from src.models.sqlite.interfaces.user_repository_interface import UserInterface
from src.erros.error_types.http_not_found import HttpNotFoundError

class UserListController(UserListControllerInterface):
    def __init__(self, user_repository: UserInterface) -> None:
        self.__user_repository = user_repository

    def list(self) -> dict:
        user_data = self.__list_user()
        print(user_data)
        if not user_data:
            raise HttpNotFoundError('Nenhum usuário foi encontrado')
        return user_data

    def __list_user(self) -> dict:
        return self.__user_repository.list_user()
