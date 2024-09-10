from fastapi import (APIRouter, Depends,)
from sqlalchemy.ext.asyncio import AsyncSession

from crud.todo_list import get_all_todo_list
from core.models.db_helper import db_helper
from core.schemas.todo import (
    ToDoListCreate,
    ToDoItemCreate,
)


router = APIRouter()


@router.get("/", response_model=list[ToDoListCreate])
async def get_todo_list(session: AsyncSession = Depends(db_helper.session_getter)):
    return await get_all_todo_list(session=session)

