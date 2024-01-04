import bcrypt
from random import choice
from string import ascii_uppercase


def authenticate(pwd: str, pwd_salt: str, token_salt: str, auth_token: str):
    print(f"pdw --> /{pwd}/ ")
    print(f"pwd_salt --> /{pwd_salt}/ ")
    print(f"token_salt --> /{token_salt}/ ")
    print(f"auth_token --> /{auth_token}/ ")
    password = pwd.encode("utf-8")
    # Hash a password for the first time, with a randomly-generated salt
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    # Check that an un-hashed password matches one that has previously been
    # hashed
    if bcrypt.checkpw(password, hashed):
        print("It Matches!")
    else:
        print("It Does not Match :(")
    return True


def create_password_salt_token(pwd: str,) -> dict:
    print(f"pdw --> /{pwd}/ ")
    pwd_salt = ''.join(choice(ascii_uppercase) for _ in range(12))
    token_salt = ''.join(choice(ascii_uppercase) for _ in range(24))
    salted_password = pwd.join(pwd_salt)
    print(f"salted_password --> /{salted_password}/ ")
    password = salted_password.encode("utf-8")
    # Hash a password for the first time, with a randomly-generated salt
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    return {'password': hashed, 'pwd_salt': pwd_salt, 'token_salt': token_salt}


def verify_password_token(pwd: str, pdw_salt: str, hashed: bytes) -> bool:
    print(f"pdw --> /{pwd}/ ")
    salted_password = pwd.join(pdw_salt)
    print(f"salted_password --> /{salted_password}/ ")
    password = salted_password.encode("utf-8")
    if bcrypt.checkpw(password, hashed):
        print("It Matches!")
        return True
    else:
        print("It Does not Match :(")
        return False
