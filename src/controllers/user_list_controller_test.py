from sqlalchemy import BIGINT
from src.models.sqlite.entities.user import UserTable
from .user_list_controller import UserListController

class MockUserRepository:
    def list_user(self, user_id: BIGINT, name: str, email: str) -> list[UserTable]:
        return {
            "id": user_id,
            "name": name,
            "email": email
        }


def test_list():
    controller = UserListController(MockUserRepository())
    user_info = {"id": 1, "name": "Test User", "email": "test@example.com"}
    response = controller.list(user_info)

    # Verificação do tipo de retorno
    assert isinstance(response, dict)

    # Verificação dos valores retornados no dicionário
    assert response["id"] == user_info["id"]
    assert response["name"] == user_info["name"]
    assert response["email"] == user_info["email"]

    # Verificação de chaves no dicionário
    assert "id" in response
    assert "name" in response
    assert "email" in response
