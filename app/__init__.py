from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object('config.development')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login = LoginManager()
login.init_app(app)


from app.models import tables, forms
from app.controllers import default


@app.cli.command()
def seed():
    admin = tables.User('admin', 'admin@email.com', 'admin')
    db.session.add(admin)
    db.session.commit()
    print('Admin user created.')
