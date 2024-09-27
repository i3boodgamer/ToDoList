from datetime import datetime

from pydantic import BaseModel


class ToDoItemCreate(BaseModel):
    title: str
    list_id: int
    completed: bool = False


class ToDoItemUpdate(BaseModel):
    title: str | None = None
    completed: bool | None = None


class TodoItemResponse(BaseModel):
    create_at: datetime
    title: str
    completed: bool

