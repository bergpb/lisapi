from lisapi import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(50))

    def __init__ (self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        
    def __repr__(self):
        return "<User %r>" % self.username

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Pin(db.Model):
    __tablename__ = "pins"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    pin = db.Column(db.Integer, unique=True)
    state = db.Column(db.Boolean, default=False)
    color = db.Column(db.String(30))
    icon = db.Column(db.String(30))
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
