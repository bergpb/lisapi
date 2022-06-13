import os
import config
from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO

db = SQLAlchemy()
migrate = Migrate()
socketio = SocketIO()
login = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.' + os.environ.get('FLASK_ENV', 'development'))

    db.init_app(app)
    migrate.init_app(app, db)
    socketio.init_app(app)
    login.init_app(app)

    from lisapi import routes
    routes.init_app(app)

    from lisapi import cli
    cli.init_app(app)

    return app