import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'), verbose=True)


class Config(object):
    TESTING = False
    DEBUG = os.environ.get('FLASK_DEBUG', True)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # generate a key in python3.6: python3 -c 'import secrets; print(secrets.token_hex(16))'
    SECRET_KEY = os.environ.get('SECRET_KEY', 'this_is_secret')

class production(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'storage.db')


class development(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'storage_dev.db')


class testing(Config):
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'storage_test.db')

