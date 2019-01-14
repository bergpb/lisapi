import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_cors import CORS
from flask_bcrypt import Bcrypt


app = Flask(__name__)
CORS(app)
bcrypt = Bcrypt(app)
app.config.from_object('config.' + os.environ.get('FLASK_ENV'))


db = SQLAlchemy(app)
migrate = Migrate(app, db)

login = LoginManager()
login.init_app(app)


from app.models import tables, forms
from app.controllers import default
from app.errors import errors


@app.cli.command()
def seed():
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
def drop():
    admin = tables.User.query.filter_by(username='admin').first()
    if admin:
        print('Drop admin.')
        db.session.delete(admin)
        db.session.commit()
        print('User removed.')
    else:
        print('User not found.')
