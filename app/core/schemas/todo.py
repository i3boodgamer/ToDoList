from datetime import datetime
from typing import Any, List

from pydantic import BaseModel


class ToDoListCreate(BaseModel):
    title: str


class ToDoItemCreate(BaseModel):
    title: str
    list_id: int
    completed: bool = False


class TodoItemResponse(BaseModel):
    create_at: datetime
    title: str
    completed: bool


class ToDoListResponse(BaseModel):
    title: str
    create_at: datetime
    todo_item: List[TodoItemResponse]

