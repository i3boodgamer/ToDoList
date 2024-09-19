from typing import TYPE_CHECKING, Annotated

from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from fastapi import Depends

from core.auth.user_manager import UserManager
from .users import get_user_db


async def get_user_manager(
    user_db: Annotated[
        "SQLAlchemyUserDatabase",
        Depends(get_user_db),
    ]
):
    yield UserManager(user_db)

