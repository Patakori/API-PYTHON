from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.interfaces.user_repository_interface import UserInterface
from src.models.sqlite.entities.user import UserTable
from src.models.user_model import UserModel


class UserRepository(UserInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def list_user(self) -> list[UserTable]:
        with self.__db_connection as database:
            try:
                list_users = database.session.query(UserTable).all()
                return [UserModel.model_validate(user) for user in list_users]
            except NoResultFound:
                return []

    def create_user(self, new_user: dict) -> dict:
        with self.__db_connection as database:
            try:
                user = UserTable(**new_user)
                database.session.add(user)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    def delete_user(self, email: str) -> None:
        with self.__db_connection as database:
            try:
                (
                database.session
                    .query(UserTable)
                    .filter(UserTable.email == email)
                    .delete()
                )
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
