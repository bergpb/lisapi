import os


basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    # generate a key in python 3.6
    # python3 -c 'import secrets; print(secrets.token_hex(16))'
    SECRET_KEY = '70d6fbdc84bfeebdbba563c0b4dbdcc8'

class production(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'storage.db')

class development(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'storage_dev.db')
