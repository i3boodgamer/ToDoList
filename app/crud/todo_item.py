from typing import Sequence

from fastapi import HTTPException, status
from sqlalchemy import Select
from sqlalchemy.orm import selectinload
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession


from core.models import ToDoItem, ToDoList, User
from core.schemas.todo_item import (
    ToDoItemUpdate,
    ToDoItemСompleted,
    ToDoItemCreate,
)
from utils.presence_user import presence_user


async def get_all_todo_item(
        session: AsyncSession,
) -> Sequence[ToDoItem]:
    stmt = Select(ToDoItem).order_by(ToDoItem.id)
    result = await session.scalars(stmt)
    return result.all()


async def get_all_item_list(
        list_id: ToDoList,
        session: AsyncSession,
        user: User
) -> Sequence[ToDoItem]:
    stmt = (
        Select(ToDoItem)
        .options(selectinload(ToDoItem.todo_list))
        .where((ToDoItem.list_id == list_id.id) & (user.id == list_id.user))
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
    try:
        session.add(todo_item)
        await session.commit()
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="List missing at user"
        )
    return todo_item


async def update_todo_item(
        item: ToDoItem,
        item_update: ToDoItemUpdate,
        session: AsyncSession,
        user: User,
) -> ToDoItem:
    await presence_user(
        session=session,
        item=item,
        user=user,
    )

    item.title = item_update.title
    item.completed = item_update.completed
    await session.commit()
    return item


async def completed_todo_item(
        item: ToDoItem,
        item_update: ToDoItemСompleted,
        session: AsyncSession,
        user: User,
) -> ToDoItem:
    await presence_user(
        session=session,
        item=item,
        user=user,
    )

    item.completed = item_update.completed
    await session.commit()

    return item


async def del_todo_item(
        item: ToDoItem,
        session: AsyncSession,
        user: User,
) -> None:
    await presence_user(
        session=session,
        item=item,
        user=user,
    )

    await session.delete(item)
    await session.commit()

