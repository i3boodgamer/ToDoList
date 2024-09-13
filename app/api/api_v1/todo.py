from fastapi import (
    APIRouter,
    Depends,
    status
)
from sqlalchemy.ext.asyncio import AsyncSession

from api.dependencies.todo_item import get_id_item
from crud.todo_list import (
    get_all_todo_list,
    create_todo_list,
    full_todo,
)
from crud.todo_item import (
    get_all_todo_item,
    create_todo_item,
    del_todo_item
)
from core.models.db_helper import db_helper
from core.models import ToDoItem
from core.schemas.todo import (
    ToDoListCreate,
    ToDoItemCreate,
    ToDoListResponse,
)


router = APIRouter()


@router.get("/list", response_model=list[ToDoListCreate])
async def get_todo_list(session: AsyncSession = Depends(db_helper.session_getter)):
    return await get_all_todo_list(session=session)


@router.post("/list", response_model=ToDoListCreate)
async def create_list_todo(
    todo_list: ToDoListCreate, session: AsyncSession = Depends(db_helper.session_getter)
):
    return await create_todo_list(todo_item=todo_list, session=session)


@router.get("/item", response_model=list[ToDoItemCreate])
async def get_todo_item(session: AsyncSession = Depends(db_helper.session_getter)):
    return await get_all_todo_item(session=session)


@router.post("/item", response_model=ToDoItemCreate)
async def create_item_todo(
    item: ToDoItemCreate, session: AsyncSession = Depends(db_helper.session_getter)
):
    return await create_todo_item(todo_item=item, session=session)


@router.get("/todo/", response_model=list[ToDoListResponse])
async def get_todo(session: AsyncSession = Depends(db_helper.session_getter)):
    return await full_todo(session=session)


@router.delete("/{item_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item_todo(
    item: ToDoItem = Depends(get_id_item),
    session: AsyncSession = Depends(db_helper.session_getter),
):
    return await del_todo_item(todo_item=item, session=session)
