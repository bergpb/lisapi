import os
import settings
from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO, emit

db = SQLAlchemy()
migrate = Migrate()
socketio = SocketIO()
login = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object('settings.' + os.getenv('FLASK_ENV'))

    db.init_app(app)
    migrate.init_app(app, db)
    socketio.init_app(app)
    login.init_app(app)

    from .models import tables, forms
    from .helpers import helpers
    from .routes.auth import auth
    from .routes.main import main
    from .errors.error import error

    app.register_blueprint(auth)
    app.register_blueprint(main)
    app.register_blueprint(error)


    @socketio.on('updateStatus')
    def on_update(data):
        """Update content in page, receive updateStatus and emit statusUpdated"""
        data = helpers.statusInfo()
        emit('statusUpdated', data.json)


    @app.cli.command()
    def db_seed():
        """Add admin user."""
        admin = tables.User.query.filter_by(username='admin').first()
        if not admin:
            print('Creating user admin.')
            admin = tables.User('admin', 'admin@email.com', 'admin')
            db.session.add(admin)
            db.session.commit()
            print('User created.')
        else:
            print('User exists.')

    return socketio, app
