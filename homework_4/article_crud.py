from database import Base, Session, SessionType
from models import User, Article


def create_article(session: SessionType, title: str, text: str, user: User):
    article = Article(title=title, text=text, user_id=user.id)
    print("create user", article)
    session.add(article)
    session.commit()
    print("saved ", article)
    return article


def get_article_by_id(session: SessionType, id: int) -> Article:
    article = session.query(Article).filter_by(id=id).first()
    return article


def get_article_by_user(session: SessionType, user: User) -> list[Article]:
    articles = session.query(Article).filter_by(user_id=user.id).all()
    return articles


def update_article():
    pass


def delete_article():
    pass
