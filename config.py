import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

# setting env vars from .env file
for line in open('.env'):
    env_ = line.strip().split('=')
    if len(env_) == 2:
        os.environ[env_[0]] = env_[1].replace("\"", "")

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    # generate a key in python 3.6: python3 -c 'import secrets; print(secrets.token_hex(16))'
    SECRET_KEY = os.getenv('SECRET_KEY')
        

class production(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'storage.db')

class development(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'storage_dev.db')

class testing(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'storage_test.db')

