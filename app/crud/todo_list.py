from typing import Sequence

from sqlalchemy import Select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import ToDoList, ToDoItem
from core.schemas.todo import ToDoListCreate, ToDoItemCreate


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


async def del_todo_list(
        todo_item: ToDoList,
        session: AsyncSession
) -> None:
    await session.delete(todo_item)
    await session.commit()


async def full_todo(
        session: AsyncSession
):
    stmt = Select(ToDoList).options(selectinload(ToDoList.todo_item)).order_by(ToDoList.id)
    result = await session.scalars(stmt)
    return result.all()


