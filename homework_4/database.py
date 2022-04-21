from sqlalchemy import create_engine

from sqlalchemy.orm import (
    declarative_base,
    sessionmaker,
    scoped_session,
    Session as SessionType,
)


DB_URL = "postgresql+pg8000://username:passwd!@localhost:5432/blog"
DB_ECHO = True
engine = create_engine(url=DB_URL, echo=DB_ECHO)

Base = declarative_base(bind=engine)

session_factory = sessionmaker(bind=engine)

Session = scoped_session(session_factory)


def get_session():
    session: SessionType = Session()
    return session
