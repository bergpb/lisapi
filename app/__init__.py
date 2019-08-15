import os
import config
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO, emit


app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config.from_object('config.' + os.getenv('FLASK_ENV'))


db = SQLAlchemy(app)
migrate = Migrate(app, db)
socketio = SocketIO(app)

login = LoginManager()
login.init_app(app)


from app.models import tables, forms
from app.controllers import default
from app.errors import errors
from app.helpers import helpers


@socketio.on('updateStatus')
def on_update(data):
    """Update content in page, receive updateStatus and emit statusUpdated"""
    data = helpers.statusInfo()
    emit('statusUpdated', data.json)


@app.cli.command()
def db_init():
    """Start migrations and seeds."""
    os.system('flask db init && flask db migrate && flask db upgrade')
    admin = tables.User.query.filter_by(username='admin').first()
    if not admin:
        print('Creating user admin.')
        admin = tables.User('admin', 'admin@email.com', 'admin')
        db.session.add(admin)
        db.session.commit()
        print('User created.')
    else:
        print('User exists.')

@app.cli.command()
def db_drop():
    """Remove migrations and databases."""
    os.system('rm -rf migrations && rm storage*')
    print('Databases and migrations removed.')
