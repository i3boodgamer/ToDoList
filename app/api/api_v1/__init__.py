from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer

from core.config import settings
from .todo_list import router as router_todo_list
from .todo_item import router as router_todo_item
from .auth import router as router_auth
# from .user import router as router_user


http_bearer = HTTPBearer(auto_error=False)

router = APIRouter(
    prefix=settings.api.v1.prefix,
    dependencies=[Depends(http_bearer)]
)
router.include_router(router_todo_list)
router.include_router(router_todo_item)
router.include_router(router_auth)
# router.include_router(router_user)



