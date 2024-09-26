from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.dependencies.authentication.fastapi_user_router import current_user
from api.dependencies.todo_item import get_id_item
from api.dependencies.todo_list import get_id_list
from crud.todo_item import (
    get_all_todo_item,
    create_todo_item,
    del_todo_item,
    update_todo_item,
    get_all_item_list,
)
from core.models.db_helper import db_helper
from core.models import ToDoItem, ToDoList, User
from core.schemas.todo import (
    ToDoItemCreate,
    ToDoItemUpdate,
)


router = APIRouter(tags=["Todo Item"], dependencies=[Depends(current_user)])


@router.get("/item", response_model=list[ToDoItemCreate])
async def get_todo_item(
    session: AsyncSession = Depends(db_helper.session_getter),
):
    return await get_all_todo_item(session=session)


@router.get("/{list_id}/", response_model=list[ToDoItemUpdate])
async def get_all_list_item(
    list_at: ToDoList = Depends(get_id_list),
    session: AsyncSession = Depends(db_helper.session_getter),
    user: User = Depends(current_user),
):
    return await get_all_item_list(
        list_id=list_at,
        session=session,
        user=user,
    )


@router.post("/item", response_model=ToDoItemCreate)
async def create_item_todo(
    item: ToDoItemCreate, session: AsyncSession = Depends(db_helper.session_getter)
):
    return await create_todo_item(
        todo_item=item,
        session=session,
    )


@router.patch("/item/{item_id}/", response_model=ToDoItemUpdate)
async def update_item(
    todo_item_update: ToDoItemUpdate,
    item: ToDoItem = Depends(get_id_item),
    session: AsyncSession = Depends(db_helper.session_getter),
    user: User = Depends(current_user),
):
    return await update_todo_item(
        item=item,
        item_update=todo_item_update,
        session=session,
        user=user,
    )


@router.delete("/item/{item_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item_todo(
    item: ToDoItem = Depends(get_id_item),
    session: AsyncSession = Depends(db_helper.session_getter),
    user: User = Depends(current_user),
):
    return await del_todo_item(
        todo_item=item,
        session=session,
        user=user,
    )
