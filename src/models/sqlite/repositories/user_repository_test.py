from unittest import mock
import pytest
from sqlalchemy.orm.exc import NoResultFound
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from src.models.sqlite.entities.user import UserTable
from .user_repository import UserRepository

class MockConnection:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(UserTable)],
                    [
                        UserTable(
                            id='66e30531-75be-4b7c-b958-a0ed83da7b99',
                            name='Dilsones',
                            email='dilsones@gmail.com'
                        )
                    ]
                )
            ]
        )
    def __enter__(self): return self
    def __exit__(self, exc_type, exc_val, exc_tb): pass

class MockConnectionNotResult:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock()
        self.session.query.side_effect = self.__raise_no_result_found

    def __raise_no_result_found(self, *args, **kwargs):
        raise NoResultFound('No result found')
    def __enter__(self): return self
    def __exit__(self, exc_type, exc_val, exc_tb): pass

def test_list_user():
    mock_connection = MockConnection()
    repo = UserRepository(mock_connection)
    response = repo.list_user()

    mock_connection.session.query.assert_called_once_with(UserTable)
    mock_connection.session.all.assert_called_once()
    mock_connection.session.filter.assert_not_called()

    assert response[0].name == 'Dilsones'

def test_list_user_not_result():
    mock_connection = MockConnectionNotResult()
    repo = UserRepository(mock_connection)
    response = repo.list_user()

    mock_connection.session.query.assert_called_once_with(UserTable)
    mock_connection.session.all.assert_not_called()
    mock_connection.session.filter.assert_not_called()

    assert response == []

def test_delete_user():
    mock_connection = MockConnection()
    repo = UserRepository(mock_connection)

    repo.delete_user("dilsones@gmail.com")

    mock_connection.session.query.assert_called_once_with(UserTable)
    mock_connection.session.filter.assert_called_once_with(UserTable.email == 'dilsones@gmail.com')
    mock_connection.session.delete.assert_called_once()

def test_delete_user_error():
    mock_connection = MockConnectionNotResult()
    repo = UserRepository(mock_connection)

    with pytest.raises(Exception):
        repo.delete_user("dilsones@gmail.com")

    mock_connection.session.rollback.assert_called_once()


