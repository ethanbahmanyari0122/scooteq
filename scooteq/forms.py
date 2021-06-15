from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from scooteq.models import User


class RegistrationForm(FlaskForm):
    firstname = StringField('First name', validators=[DataRequired()])
    lastname = StringField('Last name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired(),
                                                   Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     Length(min=6, max=20)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(),
                                                                     EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('The username is taken. Please choose another one')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('The email is taken. Please choose another one')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),
                                                   Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     Length(min=6, max=20)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
