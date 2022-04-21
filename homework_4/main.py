import user_crud
import article_crud

from database import get_session


def main():
    session = get_session()
    # user_crud.create_user(session, "user3@test.com", "password123")
    user = user_crud.get_user(session, "user3@test.com")
    # print(user.password)
    # user_crud.delete_user(session, "Muha")
    # fields = {"password": "NewPassword121", "is_active": False}
    # user_crud.update_user(session, "Muha1", **fields)
    # article_crud.create_article(
    #     session,
    #     "Yet Another Title",
    #     "Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blahLorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blahLorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blahLorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blahLorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah",
    #     user,
    # )
    # print(article_crud.get_article_by_id(session, 1))
    print(article_crud.get_articles_by_user(session, user))
    session.close()


if __name__ == "__main__":
    main()
