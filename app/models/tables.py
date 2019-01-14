from app import db, bcrypt
from flask_login import UserMixin


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(50))

    def __init__ (self, username, email, password):
        self.username = username
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def __repr__(self):
        return "<User %r>" % self.username

class Pin(db.Model):
    __tablename__ = "pins"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    pin = db.Column(db.Integer, unique=True)
    state = db.Column(db.Boolean, default=False)
    color = db.Column(db.String(30), default=False)
    icon = db.Column(db.String(30), default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', foreign_keys=user_id)

    def __init__ (self, name, pin, state, color, icon, user_id):
        self.name = name
        self.pin = pin
        self.state = state
        self.color = color
        self.icon = icon
        self.user_id = user_id

    def __repr__(self):
        return "<Pin %r>" % self.id
