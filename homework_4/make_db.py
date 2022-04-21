from models import User, Article
from database import get_session, Base


def main():
    session = get_session()
    Base.metadata.create_all()
    session.close()


if __name__ == "__main__":
    main()
