import os

import pytest
from sqlalchemy import create_engine

from sqlalchemy.orm import (
    declarative_base,
    sessionmaker,
    scoped_session,
    Session as SessionType,
)

import models
import user_crud
import article_crud
from utils import check_password
from make_db import fill_database

DB_NAME = "blog_test.db"
DB_URL = f"sqlite:///{DB_NAME}"
DB_ECHO = True
email = "test.user2@test.com"
password = "TestPassword123"
new_password = "NewPassword121"
fields = {"password": new_password, "is_active": False}


@pytest.fixture
def connection():
    engine = create_engine(url=DB_URL, echo=DB_ECHO)
    return engine


@pytest.fixture
def db_setup(connection):
    models.Base.metadata.bind = connection
    models.Base.metadata.create_all()

    yield
    print("DELETING TABLES...")
    models.Base.metadata.drop_all()
    print("DELETING FILE...")
    os.remove(DB_NAME)


@pytest.fixture
def db_session(db_setup, connection):
    session_factory = sessionmaker(bind=connection)
    session = scoped_session(session_factory)
    yield session
    session.close()


def test_create_user(db_session):
    user = user_crud.create_user(db_session, email, password)
    assert isinstance(user, models.User)


def test_get_user(db_session):
    new_user = user_crud.create_user(db_session, email, password)
    user = user_crud.get_user(db_session, email)
    assert user == new_user


def test_update_user(db_session):
    new_user = user_crud.create_user(db_session, email, password)
    user_crud.update_user(db_session, email, **fields)
    user = user_crud.get_user(db_session, email)
    assert check_password(new_password, user.password)
    assert user.is_active == False


def test_delete_user(db_session):
    user_crud.create_user(db_session, email, password)
    res = user_crud.delete_user(db_session, email)
    assert res == True


# Article unit tests


def test_get_article_by_id(db_session):
    fill_database(db_session)
    article = article_crud.get_article_by_id(db_session, 1)
    print(article)
    assert isinstance(article, models.Article)


def test_get_article_by_user(db_session):
    fill_database(db_session)
    user = user_crud.get_user(db_session, email)
    articles = article_crud.get_articles_by_user(db_session, user)
    assert len(articles) == 7
