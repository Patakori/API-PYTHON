from abc import ABC, abstractmethod

from src.models.sqlite.entities.user import UserTable

class UserInterface(ABC):

    @abstractmethod
    def list_user(self) -> list[UserTable]:
        pass

    @abstractmethod
    def create_user(self, new_user: dict) -> dict:
        pass

    @abstractmethod
    def delete_user(self, email: str) -> list[UserTable]:
        pass
