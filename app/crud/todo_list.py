from typing import Sequence

from fastapi import HTTPException, status
from sqlalchemy import Select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import ToDoList, User
from core.schemas.todo import (
    ToDoListCreate,
    ToDoListUpdate,
)

from .todo_item import get_all_item_list, del_todo_item


async def get_all_todo_list(
    session: AsyncSession,
    user: User,
) -> Sequence[ToDoList]:
    stmt = Select(ToDoList).where(ToDoList.user == user.id).order_by(ToDoList.id)
    result = await session.scalars(stmt)
    return result.all()


async def get_todo_list(
    list_id: int,
    session: AsyncSession,
) -> ToDoList | None:
    return await session.get(ToDoList, list_id)


async def create_todo_list(
    session: AsyncSession,
    todo_item: ToDoListCreate,
    user: User,
) -> ToDoList:
    todo_list = ToDoList(**todo_item.model_dump(), user=user.id)
    session.add(todo_list)
    await session.commit()
    return todo_list


async def del_todo_list(
        todo_list: ToDoList,
        session: AsyncSession,
        user: User,
) -> None:
    full_item = await get_all_item_list(list_id=todo_list, session=session, user=user)
    if full_item is not None:
        for item in full_item:
            await del_todo_item(todo_item=item, session=session, user=user)

    if todo_list.user == user.id:
        await session.delete(todo_list)
        await session.commit()
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="List missing at user"
        )


async def update_title_list(
    list_at: ToDoList,
    list_update: ToDoListUpdate,
    user: User,
    session: AsyncSession,
) -> ToDoList:
    if list_at.user == user.id:
        new_title = list_update.model_dump().get("title")
        list_at.title = new_title
        list_at.user = user.id

        await session.commit()

        return list_at

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="List missing at user"
    )


async def full_todo(
        session: AsyncSession,
        user: User
):
    stmt = (
        Select(ToDoList).options(selectinload(ToDoList.todo_item)).where(ToDoList.user == user.id).order_by(ToDoList.id)
    )
    result = await session.scalars(stmt)
    return result.all()
