from typing import TYPE_CHECKING


from fastapi_users.db import SQLAlchemyUserDatabase, SQLAlchemyBaseUserTable
from sqlalchemy.orm import relationship

from .base import Base
from .mixins.int_id_pk import IntIDPkMixin


if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class User(Base, IntIDPkMixin, SQLAlchemyBaseUserTable[int]):

    # todo_list = relationship("ToDoList", back_populates="users")

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, cls)
