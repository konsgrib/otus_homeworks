from models import User, Article, Comment
from database import get_session, Base


def fill_database(db_session):
    users = [
        {"email": "test.user1@test.com", "password": "Password123"},
        {"email": "test.user2@test.com", "password": "Password123"},
        {"email": "test.user3@test.com", "password": "Password123"},
        {"email": "test.user4@test.com", "password": "Password123"},
    ]

    articles = [
        {"title": "Article Number 1", "text": "Some text goes here", "user_id": 1},
        {"title": "Article Number 2", "text": "Some text goes here", "user_id": 1},
        {"title": "Article Number 3", "text": "Some text goes here", "user_id": 1},
        {"title": "Article Number 4", "text": "Some text goes here", "user_id": 2},
        {"title": "Article Number 5", "text": "Some text goes here", "user_id": 2},
        {"title": "Article Number 6", "text": "Some text goes here", "user_id": 2},
        {"title": "Article Number 7", "text": "Some text goes here", "user_id": 2},
        {"title": "Article Number 8", "text": "Some text goes here", "user_id": 2},
        {"title": "Article Number 9", "text": "Some text goes here", "user_id": 2},
        {"title": "Article Number 10", "text": "Some text goes here", "user_id": 2},
        {"title": "Article Number 11", "text": "Some text goes here", "user_id": 3},
    ]

    comments = [
        {"text": "Very good point, I like it!!!", "user_id": 2, "article_id": 1},
        {"text": "Very good point, I like it!!!", "user_id": 2, "article_id": 1},
        {"text": "Very good point, I like it!!!", "user_id": 2, "article_id": 1},
        {"text": "Very good point, I like it!!!", "user_id": 2, "article_id": 1},
        {"text": "Very good point, I like it!!!", "user_id": 3, "article_id": 5},
        {"text": "Very good point, I like it!!!", "user_id": 1, "article_id": 5},
        {"text": "Very good point, I like it!!!", "user_id": 1, "article_id": 5},
    ]

    for user in users:
        new_user = User(**user)
        db_session.add(new_user)
    for article in articles:
        new_article = Article(**article)
        db_session.add(new_article)
    for comment in comments:
        new_comment = Comment(**comment)
        db_session.add(new_comment)
    db_session.commit()


def main():
    session = get_session()
    Base.metadata.create_all()
    fill_database(session)
    session.close()


if __name__ == "__main__":
    main()
