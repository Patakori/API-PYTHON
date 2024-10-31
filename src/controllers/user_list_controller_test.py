from src.models.sqlite.entities.user import UserTable
from .user_list_controller import UserListController

class MockUserRepository:
    def list_user(self) -> list[UserTable]:
        return [
            {
                "id": '1',
                "name": 'Dilsones',
                "email": 'Dilsones@gmail.com'
            }
        ]


def test_list():
    controller = UserListController(MockUserRepository())
    response = controller.list()

    # Verificação do tipo de retorno
    assert isinstance(response, list)

    # Verificação dos valores retornados no dicionário
    user_data = response[0]
    assert user_data["id"] == "1"
    assert user_data["name"] == "Dilsones"
    assert user_data["email"] == "Dilsones@gmail.com"

    # Verificação de chaves no dicionário
    assert "id" in user_data
    assert "name" in user_data
    assert "email" in user_data
