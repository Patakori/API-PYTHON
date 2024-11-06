from src.controllers.interfaces.create_user import CreateUserControllerInterface
from src.models.sqlite.interfaces.user_repository_interface import UserInterface

class CreateUserController(CreateUserControllerInterface):
    def __init__(self, user_repository: UserInterface) -> None:
        self.__user_repository = user_repository

    def create(self, new_user: dict) -> dict:
        user_data = self.__create_user(new_user)
        print(user_data)
        return user_data

    def __create_user(self, new_user: dict) -> dict:
        return self.__user_repository.create_user(new_user)
