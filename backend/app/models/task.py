from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from sqlalchemy import func
from sqlalchemy.orm import relationship
from db.base import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, autoincrement=True)

    done = Column(Boolean, default=False, nullable=False)
    done_at = Column(DateTime)
    done_by = Column(String(100))

    created_at = Column(DateTime, server_default=func.now())
    created_by = Column(String(100), nullable=False)

    title = Column(String(250), nullable=False)
    description = Column(Text)

    comments = relationship('Comment', back_populates='task')