from typing import Sequence

from sqlalchemy import Select
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import ToDoItem
from core.schemas.todo import ToDoItemCreate


async def get_all_todo_item(
        session: AsyncSession,
) -> Sequence[ToDoItem]:
    stmt = Select(ToDoItem).order_by(ToDoItem.id)
    result = await session.scalars(stmt)
    return result.all()


async def create_todo_item(
        session: AsyncSession,
        todo_item: ToDoItemCreate,
) -> ToDoItem:
    todo_item = ToDoItem(**todo_item.model_dump())
    session.add(todo_item)
    await session.commit()
    return todo_item



async def update_todo_item():
    pass


async def del_todo_item(
        todo_item: ToDoItem,
        session: AsyncSession
) -> None:
    await session.delete(todo_item)
    await session.commit()