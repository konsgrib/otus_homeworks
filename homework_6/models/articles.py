from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    Text,
)
from .database import db


class Article(db.Model):
    id = Column(Integer, primary_key=True)
    author = Column(Integer, nullable=False)
    title = Column(String(80), unique=True, nullable=False)
    text = Column(Text, nullable=False)

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, title={self.title}, text={self.text})"

    def __repr__(self):
        return str(self)
