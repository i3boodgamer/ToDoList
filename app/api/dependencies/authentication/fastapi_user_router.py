from fastapi_users import FastAPIUsers

from core.models import User
from .user_manager import get_user_manager
from .backend import auth_backend


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user(active=True)
current_super_user = fastapi_users.current_user(active=True, superuser=True)