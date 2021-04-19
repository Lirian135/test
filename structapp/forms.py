from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length, email_validator



class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=18)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=50)])
    remember_me = BooleanField('remember me')
    
class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=18)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=50)])
    

#forms#fddfddf

