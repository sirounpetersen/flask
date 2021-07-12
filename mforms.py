from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('siroun',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('siroun.petersen@bison.howard.edu',
                        validators=[DataRequired(), Email()])
    password = PasswordField('02938966', validators=[DataRequired()])
    confirm_password = PasswordField('02938966',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
