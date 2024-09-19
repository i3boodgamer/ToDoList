from typing import Annotated

from fastapi import Depends
from fastapi_users.authentication.strategy.db import AccessTokenDatabase, DatabaseStrategy

from core.models import AccessToken
from core.config import settings
from .access_token import get_access_token_db


def get_database_strategy(
    access_token_db: AccessTokenDatabase[AccessToken] = Depends(get_access_token_db)
) -> DatabaseStrategy:
    return DatabaseStrategy(access_token_db, lifetime_seconds=settings.access_token.lifetime_second)
