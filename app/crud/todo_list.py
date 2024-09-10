from typing import Sequence

from sqlalchemy import Select
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import ToDoList
from core.schemas.todo import ToDoListCreate


async def get_all_todo_list(
        session: AsyncSession,
) -> Sequence[ToDoList]:
    stmt = Select(ToDoList).order_by(ToDoList.id)
    result = await session.scalars(stmt)
    return result.all()


async def create_todo_list(
        session: AsyncSession,
        todo_item: ToDoListCreate,
) -> ToDoList:
    todo_list = ToDoList(**todo_item.model_dump())
    session.add(todo_list)
    await session.commit()
    return todo_list
