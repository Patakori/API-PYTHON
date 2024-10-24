import pytest
from src.models.sqlite.settings.connection import db_connection_handler
from .user_repository import UserRepository

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="database interaction")
def test_list_user():
    repo = UserRepository(db_connection_handler)
    response = repo.user()
    print(response)
