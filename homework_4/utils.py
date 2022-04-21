from bcrypt import gensalt, hashpw, checkpw


def hash_password(password) -> str:
    salt = gensalt()
    # password = password.encode("utf-8")
    return hashpw(b"{password}", salt)


def check_password(password, hashed_password) -> bool:
    return checkpw(b"{password}", hashed_password)
