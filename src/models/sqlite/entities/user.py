from sqlalchemy import Column, String, BIGINT
from src.models.sqlite.settings.base import Base

class UserTable(Base):
    __tablename__= "user"

    id = Column(BIGINT, primary_key=True)
    name = Column(String, nullable=False,)
    email = Column(String, nullable=False, unique=True)

    def __repr__(self):
        return f"User [name={self.name}, email={self.type}]"

    # def to_dict(self):
    #     return {
    #         "id": self.id,
    #         "name": self.name,
    #         "email": self.email,
    #     }
