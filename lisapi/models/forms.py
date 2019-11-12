from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, IntegerField, SelectField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from lisapi.models.tables import Pin


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
    pin = SelectField("pin", validators=[DataRequired()],
                       choices=[('4', '4'), ('5', '5'), ('6', '6'),
                                ('12', '12'), ('13', '13'),('16', '16'),
                                ('17', '17'), ('18', '18'), ('20', '21'),
                                ('22', '22'), ('23', '23'), ('24', '24'),
                                ('25', '25'),('26', '26'), ('27', '27')])
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
    pin = SelectField("pin", validators=[DataRequired()],
                       choices=[('4', '4'), ('5', '5'), ('6', '6'),
                                ('12', '12'), ('13', '13'),('16', '16'),
                                ('17', '17'), ('18', '18'), ('20', '21'),
                                ('22', '22'), ('23', '23'), ('24', '24'),
                                ('25', '25'),('26', '26'), ('27', '27')])
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
