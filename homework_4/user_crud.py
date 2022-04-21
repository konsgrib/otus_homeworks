from database import Base, Session, SessionType
from models import User, Article

from utils import hash_password

# Create user
def create_user(session: SessionType, email: str, password: str) -> User:
    user = User(email=email, password=hash_password(password.encode("utf-8")))
    print("create user", user)
    session.add(user)
    session.commit()
    print("saved ", user)
    return user


def get_user(session: SessionType, email: str) -> User:
    user = session.query(User).filter_by(email=email).first()
    print(user)
    return user


# Update user
def update_user(session: SessionType, email, **kwargs) -> User:
    user = get_user(session, email)
    password = kwargs.get("password", None)
    is_active = kwargs.get("is_active", None)
    if password:
        password = hash_password(password)
        setattr(user, "password", password)
    if is_active != None:
        setattr(user, "is_active", is_active)
    session.commit()
    return user


# Delete user
def delete_user(session: SessionType, email: str) -> bool:
    user = get_user(session, email)
    try:
        session.delete(user)
        session.commit()
        print("user deleted")
        return True
    except Exception as e:
        print("Failed to delete user", str(e))
        return False
