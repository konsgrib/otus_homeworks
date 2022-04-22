import user_crud
import article_crud
import comment_crud

from database import get_session


def main():
    session = get_session()
    # user_crud.create_user(session, "test.user2@test.com", "password123")
    user = user_crud.get_user(session, "test.user2@test.com")
    # print(user.password)
    # user_crud.delete_user(session, "test.user2@test.com")
    # fields = {"password": "NewPassword121", "is_active": False}
    # user_crud.update_user(session, "test.user2@test.com", **fields)
    # article_crud.create_article(
    #     session,
    #     "Yet Another Title",
    #     "Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blahLorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blahLorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blahLorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blahLorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah",
    #     user,
    # )
    # print(article_crud.get_article_by_id(session, 1))
    # print(article_crud.get_articles_by_user(session, user))
    # print(comment_crud.get_comments_by_user(session, user))
    print(user_crud.get_user_articles_comments(session, user.email))
    session.close()


if __name__ == "__main__":
    main()
