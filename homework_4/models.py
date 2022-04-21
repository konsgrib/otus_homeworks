from database import Base
from datetime import datetime

from sqlalchemy import (
    ForeignKey,
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
)

from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True)
    password = Column(String(200), unique=True)
    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    articles = relationship("Article", backref="user")

    def __str__(self) -> str:
        return (
            f"user_id: {self.id}, email: {self.email}, created at: {self.created_at}, "
        )

    def __repr__(self) -> str:
        return str(self)


class Article(Base):
    __tablename__ = "article"

    id = Column(Integer, primary_key=True)
    title = Column(String(120), nullable=False)
    text = Column(String)
    visible = Column(Boolean, default=True, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"))

    def __str__(self):
        return f"title: {self.title}, text={self.text},  created by: {self.user_id}"

    def __repr__(self) -> str:
        return str(self)
