from typing import AsyncGenerator


from fastapi_users.db import SQLAlchemyUserDatabase, SQLAlchemyBaseUserTable
from sqlalchemy import (ForeignKey, Integer,)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.asyncio import AsyncSession

from .base import Base
from .mixins.int_id_pk import IntIDPkMixin


class User(Base, IntIDPkMixin, SQLAlchemyBaseUserTable[int]):

    todo_list = relationship("ToDoList", back_populates="users")
    @classmethod
    def get_db(cls, session: AsyncSession):
        return SQLAlchemyUserDatabase(session, cls)
