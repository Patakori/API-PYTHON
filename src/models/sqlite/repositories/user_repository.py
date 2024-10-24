from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.user import UserTable


class UserRepository:
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def user(self) -> list[UserTable]:
        with self.__db_connection as database:
            try:
                user = database.session.query(UserTable).all()
                return user
            except NoResultFound:
                return []
