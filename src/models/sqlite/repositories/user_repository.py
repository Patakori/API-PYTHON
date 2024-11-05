from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.interfaces.user_repository_interface import UserInterface
from src.models.sqlite.entities.user import UserTable


class UserRepository(UserInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def list_user(self) -> list[UserTable]:
        with self.__db_connection as database:
            try:
                users = database.session.query(UserTable).all()
                # return [user.to_dict() for user in users]
                return users
            except NoResultFound:
                return []

    def delete_user(self, email: str) -> list[UserTable]:
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
