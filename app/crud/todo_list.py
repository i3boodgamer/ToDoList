from typing import Sequence

from sqlalchemy import Select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import ToDoList
from core.schemas.todo import (
    ToDoListCreate,
    ToDoListUpdate,
)

from .todo_item import get_all_item_list, del_todo_item


async def get_all_todo_list(
    session: AsyncSession,
) -> Sequence[ToDoList]:
    stmt = Select(ToDoList).order_by(ToDoList.id)
    result = await session.scalars(stmt)
    return result.all()


async def get_todo_list(
    item_id: int,
    session: AsyncSession,
) -> ToDoList | None:
    return await session.get(ToDoList, item_id)


async def create_todo_list(
    session: AsyncSession,
    todo_item: ToDoListCreate,
) -> ToDoList:
    todo_list = ToDoList(**todo_item.model_dump())
    session.add(todo_list)
    await session.commit()
    return todo_list


async def del_todo_list(todo_list: ToDoList, session: AsyncSession) -> None:
    full_item = await get_all_item_list(list_id=todo_list, session=session)
    if full_item is not None:
        for item in full_item:
            await del_todo_item(todo_item=item, session=session)

    await session.delete(todo_list)
    await session.commit()


async def update_title_list(
    list_at: ToDoList,
    list_update: ToDoListUpdate,
    session: AsyncSession,
) -> ToDoList:
    new_title = list_update.model_dump().get("title")
    list_at.title = new_title

    await session.commit()

    return list_at


async def full_todo(session: AsyncSession):
    stmt = (
        Select(ToDoList).options(selectinload(ToDoList.todo_item)).order_by(ToDoList.id)
    )
    result = await session.scalars(stmt)
    return result.all()
