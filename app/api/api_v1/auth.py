from fastapi import APIRouter

from api.dependencies.authentication.fastapi_user_router import fastapi_users
from api.dependencies.authentication.backend import auth_backend
from core.schemas.user import UserRead, UserCreate


router = APIRouter(tags=['Auth'], prefix="/auth")

router.include_router(
    fastapi_users.get_auth_router(auth_backend, requires_verification=False),
)

router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate)
)

router.include_router(
    fastapi_users.get_verify_router(UserRead)
)

router.include_router(
    fastapi_users.get_reset_password_router()
)