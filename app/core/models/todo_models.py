from datetime import datetime, timezone

from sqlalchemy import (
    String,
    DateTime,
    func,
    Boolean,
    ForeignKey,
    Integer,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from .base import Base
from .mixins.int_id_pk import IntIDPkMixin


class ToDoList(IntIDPkMixin, Base):
    title: Mapped[str] = mapped_column(String(50))
    create_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        default=datetime.now(),
    )


class ToDoItem(IntIDPkMixin, Base):
    title: Mapped[str] = mapped_column(String(50))
    list_id: Mapped[int] = mapped_column(Integer, ForeignKey(ToDoList.id))
    completed: Mapped[bool] = mapped_column(Boolean, default=False)
    create_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        default=datetime.now(),
    )
