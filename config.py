import os


basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.urandom(24)

class production(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    URL_API = 'http://localhost:5000/api/status'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'storage.db')

class development(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    URL_API = 'http://localhost:5000/api/status'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'storage_dev.db')
