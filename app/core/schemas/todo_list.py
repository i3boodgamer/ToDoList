from datetime import datetime
from typing import List, TYPE_CHECKING

from pydantic import BaseModel

from .todo_item import TodoItemResponse


class ToDoListCreate(BaseModel):
    title: str


class ToDoListResponse(BaseModel):
    title: str
    create_at: datetime
    todo_item: List[TodoItemResponse]


class ToDoListUpdate(BaseModel):
    title: str

