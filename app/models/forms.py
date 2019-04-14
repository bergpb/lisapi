from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, IntegerField, SelectField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from app.models.tables import Pin


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
    name = StringField("name", validators=[DataRequired()], description="Pin name")
    pin = IntegerField("pin", validators=[DataRequired()], description="Pin number")
    color = SelectField('Select Color', validators=[DataRequired()],
                        choices=[('red', 'Red'), ('green', 'Green'),
                                ('blue', 'Blue'), ('pink', 'Pink'),
                                ('purple', 'Purple'), ('indigo', 'Indigo'),
                                ('cyan', 'Cyan'), ('teal', 'Teal'),
                                ('lime', 'Lime'), ('yellow', 'Yellow'),
                                ('amber', 'Amber'), ('orange', 'Orange'),
                                ('brown', 'Brown'), ('grey  ', 'Grey')])
    icon = StringField("icon", validators=[DataRequired()], description="Card icon")


class EditPin(FlaskForm):
    name = StringField("name", validators=[DataRequired()], description="Pin name")
    pin = IntegerField("pin", validators=[DataRequired()], description="Pin number")
    color = SelectField("color", validators=[DataRequired()],
                        choices=[('red', 'Red'), ('green', 'Green'),
                                ('blue', 'Blue'), ('pink', 'Pink'),
                                ('purple', 'Purple'), ('indigo', 'Indigo'),
                                ('cyan', 'Cyan'), ('teal', 'Teal'),
                                ('lime', 'Lime'), ('yellow', 'Yellow'),
                                ('amber', 'Amber'), ('orange', 'Orange'),
                                ('brown', 'Brown'), ('grey  ', 'Grey')])
    icon = StringField("icon", validators=[DataRequired()], description="Card icon")


class ChangePassword(FlaskForm):
    current_password = PasswordField("current_password", validators=[DataRequired()])
    new_password = PasswordField("new_password", validators=[DataRequired()])
    confirm_password = PasswordField("confirm_password", validators=[DataRequired()])
