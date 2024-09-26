from datetime import datetime, timezone

from sqlalchemy import (
    String,
    DateTime,
    func,
    Boolean,
    ForeignKey,
    Integer,
    UniqueConstraint
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)
from sqlalchemy.ext.asyncio import AsyncSession

from .base import Base
from .mixins.int_id_pk import IntIDPkMixin


class ToDoList(IntIDPkMixin, Base):
    title: Mapped[str] = mapped_column(String(50))
    create_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        default=datetime.now(),
    )
    user: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"))
    todo_item = relationship("ToDoItem", back_populates="todo_list")
    users = relationship("User", back_populates="todo_list")

    __table_args__ = (
        UniqueConstraint('user', 'id', name='uix_user_list'),
    )


class ToDoItem(IntIDPkMixin, Base):
    title: Mapped[str] = mapped_column(String(50))
    list_id: Mapped[int] = mapped_column(Integer, ForeignKey(ToDoList.id))
    completed: Mapped[bool] = mapped_column(Boolean, default=False)
    create_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        default=datetime.now(),
    )
    todo_list: Mapped[ToDoList] = relationship("ToDoList", back_populates="todo_item")

    __table_args__ = (
        UniqueConstraint('list_id', 'id', name='uix_item_list'),
    )
