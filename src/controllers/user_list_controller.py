from sqlalchemy import BIGINT
from src.models.sqlite.interfaces.user_repository_interface import UserInterface

class UserListController:
    def __init__(self, user_repository: UserInterface) -> None:
        self.__user_repository = user_repository

    def list(self, user_info: dict) -> dict:
        user_id = user_info["id"]
        name = user_info["name"]
        email = user_info["email"]

        self.__validate_email(email)
        user_data = self.__list_user(user_id, name, email)
        return user_data

    def __validate_email(self, email: str) -> None:
        pass

    def __list_user(self, user_id: BIGINT, name: str, email: str) -> dict:
        return self.__user_repository.list_user(user_id, name, email)
