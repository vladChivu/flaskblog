from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    # Username it's going to be used as the tag name in our HTML
    # we want to put some limitations, checks, validators like characters long input
    # DataRequired meaning that it can't be empty and Length for limitations
    # so these are classes that are used to transpile python code to html forms
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

    # now we need a submit field
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    # using a secure cookie this will allow users to stay logged in even if they close their browswers
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

# when we use these forms we need to set a secret key for our application
# a secret key will protect against modifying cookies & cross site requests forgery attacks