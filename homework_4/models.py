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
    password = Column(String(200))
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
    created_at = Column(DateTime, default=datetime.utcnow)
    comments = relationship("Comment", backref="article")

    def __str__(self):
        return f"title: {self.title}, text={self.text},  created by: {self.user_id}"

    def __repr__(self) -> str:
        return str(self)


class Comment(Base):
    __tablename__ = "comment"

    id = Column(Integer, primary_key=True)
    text = Column(String(300))
    user_id = Column(Integer, ForeignKey("user.id"))
    article_id = Column(Integer, ForeignKey("article.id"))
    created_at = Column(DateTime, default=datetime.utcnow)

    def __str__(self):
        return f"title:  text={self.text},  created by: {self.user_id} created at: {self.created_at}"

    def __repr__(self) -> str:
        return str(self)
