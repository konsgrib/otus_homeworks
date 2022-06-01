from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    Boolean,
    Text,
)
from sqlalchemy.orm import relationship, backref
from .database import db


class Article(db.Model):
    id = Column(Integer, primary_key=True)
    author = Column(Integer, nullable=False)
    title = Column(String(80), unique=True, nullable=False)
    text = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="articles")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, title={self.title}, text={self.text})"

    def __repr__(self):
        return str(self)
