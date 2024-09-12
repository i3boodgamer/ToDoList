from fastapi import (
    APIRouter,
    Depends,
)
from sqlalchemy.ext.asyncio import AsyncSession

from crud.todo_list import (
    get_all_todo_list,
    create_todo_list,
    get_all_todo_item,
    create_todo_item,
    full_todo,

)
from core.models.db_helper import db_helper
from core.schemas.todo import (
    ToDoListCreate,
    ToDoItemCreate,
    TodoResponse
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
    todo_item: ToDoItemCreate, session: AsyncSession = Depends(db_helper.session_getter)
):
    return await create_todo_item(todo_item=todo_item, session=session)


@router.get("/todo/")
async def get_todo(session: AsyncSession = Depends(db_helper.session_getter)):
    return await full_todo(session=session)
