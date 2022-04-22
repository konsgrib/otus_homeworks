from database import Base, Session, SessionType
from models import User, Article, Comment


def create_comment(session: SessionType, text: str, article: Article, user: User):
    comment = Comment(text=text, user_id=user.id, article_id=article.id)
    print("create comment", comment)
    session.add(comment)
    session.commit()
    print("saved ", comment)
    return comment


def get_comments_by_user(session: SessionType, user: User) -> list[Comment]:
    comments = session.query(Comment).filter_by(user_id=user.id).all()
    return comments
