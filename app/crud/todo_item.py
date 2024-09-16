from typing import Sequence

from sqlalchemy import Select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import ToDoItem, ToDoList
from core.schemas.todo import ToDoItemUpdate
from core.schemas.todo import ToDoItemCreate


async def get_all_todo_item(
        session: AsyncSession,
) -> Sequence[ToDoItem]:
    stmt = Select(ToDoItem).order_by(ToDoItem.id)
    result = await session.scalars(stmt)
    return result.all()


async def get_all_item_list(
        list_id: ToDoList,
        session: AsyncSession,
) -> Sequence[ToDoItem]:
    stmt = (
        Select(ToDoItem)
        .options(selectinload(ToDoItem.todo_list))
        .where(ToDoItem.list_id == list_id.id)
        .order_by(ToDoItem.id)
    )
    result = await session.scalars(stmt)
    return result.all()


async def get_todo_item(
        item_id: int,
        session: AsyncSession,
) -> ToDoItem | None:
    return await session.get(ToDoItem, item_id)


async def create_todo_item(
        session: AsyncSession,
        todo_item: ToDoItemCreate,
) -> ToDoItem:
    todo_item = ToDoItem(**todo_item.model_dump())
    session.add(todo_item)
    await session.commit()
    return todo_item


async def update_todo_item(
        item: ToDoItem,
        item_update: ToDoItemUpdate,
        session: AsyncSession,
) -> ToDoItem:
    for title, completed in item_update.model_dump(exclude_unset=True).items():
        setattr(item, title, completed)

    await session.commit()
    return item


async def del_todo_item(
        todo_item: ToDoItem,
        session: AsyncSession
) -> None:
    await session.delete(todo_item)
    await session.commit()
