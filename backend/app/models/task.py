from sqlalchemy import Integer, String, Text, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import func
from sqlalchemy.orm import relationship
from db.base import Base
from datetime import datetime


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    done: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    done_at: Mapped[datetime] = mapped_column(DateTime)
    done_by: Mapped[str] = mapped_column(String(100))

    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    created_by: Mapped[datetime] = mapped_column(String(100), nullable=False)

    title = mapped_column(String(250), nullable=False)
    description: Mapped[str] = mapped_column(Text)

    comments = relationship('Comment', back_populates='task')