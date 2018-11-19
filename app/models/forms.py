from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, IntegerField
from wtforms.validators import DataRequired


class Login(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    remember_me = BooleanField("remember_me")
    
    
class SignUp(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    email = StringField("email", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    accept_terms = BooleanField("accept_terms", validators=[DataRequired()])
    
    
class NewPin(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    pin = IntegerField("pin", validators=[DataRequired()])
    
class EditPin(FlaskForm):
    name = StringField("name", validators=[DataRequired()], description="Pin name")
    pin = IntegerField("pin", validators=[DataRequired()], description="Number pin")
    
class ChangePassword(FlaskForm):
    current_password = PasswordField("current_password", validators=[DataRequired()])
    new_password = PasswordField("new_password", validators=[DataRequired()])
    confirm_password = PasswordField("confirm_password", validators=[DataRequired()])