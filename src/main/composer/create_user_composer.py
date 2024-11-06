from src.controllers.create_user_controller import CreateUserController
from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.user_repository import UserRepository
from src.views.create_user_view import CreateUsersView

def create_user_composer():
    model = UserRepository(db_connection_handler)
    controller = CreateUserController(model)
    view = CreateUsersView(controller)

    return view
