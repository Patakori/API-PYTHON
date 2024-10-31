from abc import ABC, abstractmethod

class UserListControllerInterface(ABC):
    @abstractmethod
    def list(self) -> dict:
        pass
