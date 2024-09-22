from typing import Annotated

from fastapi import Depends, Path, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import ToDoList
from core.models.db_helper import db_helper
from crud.todo_list import get_todo_list


async def get_id_list(
    item_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.session_getter),
) -> ToDoList:
    todo_list = await get_todo_list(item_id=item_id, session=session)

    if todo_list is not None:
        return todo_list

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"List {item_id} is not found",
    )
