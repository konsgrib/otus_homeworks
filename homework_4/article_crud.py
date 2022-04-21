from turtle import title
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


def get_articles_by_user(session: SessionType, user: User) -> list[Article]:
    articles = session.query(Article).filter_by(user_id=user.id).all()
    return articles


def update_article(session: SessionType, id: int, **kwargs):
    article = session.query(Article).filter_by(id=id).first()
    title = kwargs.get("title", None)
    text = kwargs.get("text", None)
    visible = kwargs.get("visible", None)
    if title:
        setattr(article, "title", title)
    if text:
        setattr(article, "text", text)
    if visible != None:
        setattr(article, "visible", visible)
    session.commit()


def delete_article(session: SessionType, id: int):
    article = session.query(Article).filter_by(id=id).first()
    try:
        session.delete(article)
        session.commit()
        print("article deleted")
        return True
    except Exception as e:
        print("Failed to delete article", str(e))
        return False
