from typing import Annotated

from fastapi import Depends, Path, HTTPException, status
from sqlalchemy import Select
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import ToDoItem
from core.models.db_helper import db_helper
from crud.todo_item import get_todo_item


async def get_id_item(
    item_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.session_getter),
) -> ToDoItem:
    todo_item = await get_todo_item(item_id=item_id, session=session)

    if todo_item is not None:
        return todo_item

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product {item_id} is not found",
    )
