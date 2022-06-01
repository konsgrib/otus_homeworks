from os import getenv

SQLALCHEMY_DATABASE_URI = getenv(
    "SQLALCHEMY_DATABASE_URI",
    "postgresql+psycopg2://username:passwd!@localhost:5432/blog",
)


class Config:
    ENV = "development"
    DEBUG = False
    TESTING = False
    SECRET_KEY = "safdtrryrthrbvcnghjk9iotfgjuy678hygbs"
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


class ProductionConfig(Config):
    ENV = "production"


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    ENV = "testing"
    TESTING = True
