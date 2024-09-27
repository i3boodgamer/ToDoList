from fastapi import (
    HTTPException,
    status,
)
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import ToDoList, ToDoItem, User


async def presence_user(
        session: AsyncSession,
        item: ToDoItem,
        user: User
) -> None:
    result = (await session.get(ToDoList, item.list_id))
    if result is None or result.user != user.id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item mission at user"
        )
