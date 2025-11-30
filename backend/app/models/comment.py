from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy import func
from sqlalchemy.orm import relationship
from db.base import Base
from task import Task


class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True, autoincrement=True)

    task_id = Column(Integer, ForeignKey(Task.id))
    task = relationship('tasks.id', back_populates='comments')

    created_at = Column(DateTime, server_default=func.now())
    created_by = Column(String(100), nullable=False)

    description = Column(Text, nullable=False)