from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.user_repository import UserRepository
from src.controllers.user_list_controller import UserListController
from src.views.list_users_view import ListUsersView

def user_list_composer():
    model = UserRepository(db_connection_handler)
    controller  = UserListController(model)
    view = ListUsersView(controller)

    return view

