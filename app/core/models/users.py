from typing import AsyncGenerator


from fastapi_users.db import SQLAlchemyUserDatabase, SQLAlchemyBaseUserTable
from sqlalchemy import (ForeignKey, Integer,)
from sqlalchemy.orm import (Mapped, mapped_column,)
from sqlalchemy.ext.asyncio import AsyncSession

from .base import Base
from .mixins.int_id_pk import IntIDPkMixin


class User(Base, IntIDPkMixin, SQLAlchemyBaseUserTable[int]):
    task_list: Mapped[int] = mapped_column(Integer)

    @classmethod
    def get_db(cls, session: AsyncSession):
        return SQLAlchemyUserDatabase(session, cls)
