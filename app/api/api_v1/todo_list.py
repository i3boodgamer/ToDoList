from fastapi import (
    APIRouter,
    Depends,
    status

)
from sqlalchemy.ext.asyncio import AsyncSession

from api.dependencies.todo_list import get_id_list
from crud.todo_list import (
    get_all_todo_list,
    create_todo_list,
    full_todo,
    del_todo_list
)
from core.models.db_helper import db_helper
from core.models.todo_models import ToDoList
from core.schemas.todo import (
    ToDoListCreate,
    ToDoListResponse,
)


router = APIRouter(tags=["Todo List"])


@router.get("/list", response_model=list[ToDoListCreate])
async def get_todo_list(session: AsyncSession = Depends(db_helper.session_getter)):
    return await get_all_todo_list(session=session)


@router.post("/list", response_model=ToDoListCreate)
async def create_list_todo(
    todo_list: ToDoListCreate, session: AsyncSession = Depends(db_helper.session_getter)
):
    return await create_todo_list(todo_item=todo_list, session=session)


@router.get("/todo/", response_model=list[ToDoListResponse])
async def get_todo(session: AsyncSession = Depends(db_helper.session_getter)):
    return await full_todo(session=session)


@router.delete("/{list_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_list(
        todo_list: ToDoList = Depends(get_id_list),
        session: AsyncSession = Depends(db_helper.session_getter)
):
    return await del_todo_list(todo_list=todo_list, session=session)
