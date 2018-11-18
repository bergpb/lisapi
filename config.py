import os
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'storage.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = 'db1e5bdb0a7d47e3bbfa859c8f9f2fc2'