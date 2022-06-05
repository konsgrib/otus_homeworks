from flask_login import UserMixin


from sqlalchemy import (
    Column,
    Integer,
    String,
)
from sqlalchemy.orm import relationship, backref
from .database import db


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True)
    login = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), unique=False, nullable=False)
    articles = relationship("Article", back_populates="user")

    def __repr__(self):
        return "<User %r>" % self.login
