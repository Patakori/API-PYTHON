from abc import ABC, abstractmethod

class CreateUserControllerInterface(ABC):
    @abstractmethod
    def create(self, new_user: dict) -> dict:
        pass
