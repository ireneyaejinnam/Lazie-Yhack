from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
#from wtforms_components import PhoneNumberField

class LoginForm(FlaskForm):
	name = StringField('Name')
	uni = StringField('UNI')
	password = PasswordField('Password')
	email = StringField('Email')
	#phone = PhoneNumberField('Phone')
	phone = StringField('Phone')
	submit = SubmitField('Login')


class AskForm(FlaskForm):
	task = StringField('Task')
	descr = StringField('Description')
	reward = StringField('Reward')
	submit = SubmitField('Submit')


"""
class SignupForm(FlaskForm):
	name = StringField('Name')
	uni = StringField('UNI')
	password = PasswordField('Password')
	email = StringField('Email')
	#phone = PhoneNumberField('Phone')
	phone = StringField('Phone')
	submit = SubmitField('Sign Up')
"""


"""
class EntryForm(FlaskForm):
	author = StringField()
	content = StringField()
	submit = SubmitField()
"""