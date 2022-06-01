import flask_sqlalchemy


__all__ = ("db",)

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
