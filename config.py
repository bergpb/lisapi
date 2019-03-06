import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    # to generate a secret key
    # python -c 'import os; os.urandom(24)'
    SECRET_KEY = 'your_secret_key'

class production(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'storage.db')
    URL_API = os.getenv('LISA_API')

class development(Config):
    DEBUG = True
    DEVELOPMENT = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    URL_API = os.getenv('LISA_API_DEV')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'storage_dev.db')
