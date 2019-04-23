from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateTimeField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo

#Create a registration form class
class RegistrationForm(FlaskForm):
	username = StringField('Username', 
		validators=[DataRequired(), Length(min=2, max = 9)])
	email = StringField('Email',
		validators=[DataRequired(), Email()])
	password = PasswordField('Password',
		validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password',
		validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
	email = StringField('Email',
		validators=[DataRequired(), Email()])
	password = PasswordField('Password',
		validators=[DataRequired()])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')

class AddActivityForm(FlaskForm):
	start_time = DateTimeField('Start Time', format='%h:%m', 
		validators=[DataRequired()])
	end_time = DateTimeField('End Time', format='%h:%m', 
		validators=[DataRequired()])
	activity_name = StringField('Activity Name', 
		validators=[DataRequired(), Length(min=2, max=10)])
	priority = SelectField('Priority', 
		choices=[(None, 'Select One'), ('Strict', 'Strict'), ('Loose', 'Loose'), ('Free', 'Free'), ('Optional', 'Optional')], validators=[DataRequired()])
	submit = SubmitField('Submit')

class EditActivityForm(FlaskForm):
	start_time = DateTimeField('Start Time', format='%h:%m', 
		validators=[DataRequired()])
	end_time = DateTimeField('End Time', format='%h:%m', 
		validators=[DataRequired()])
	activity_name = StringField('Activity Name', 
		validators=[DataRequired(), Length(min=2, max=10)])
	priority = SelectField('Priority', 
		choices=[(None, 'Select One'), ('Strict', 'Strict'), ('Loose', 'Loose'), ('Free', 'Free'), ('Optional', 'Optional')], validators=[DataRequired()])
	submit = SubmitField('Submit')

class CreateTemplateForm(FlaskForm):
	start_time = DateTimeField('Start Time', format='%h:%m', 
		validators=[DataRequired()])
	end_time = DateTimeField('End Time', format='%h:%m', 
		validators=[DataRequired()])
	activity_name = StringField('Activity Name', 
		validators=[DataRequired(), Length(min=2, max=10)])
	priority = SelectField('Priority', 
		choices=[(None, 'Select One'), ('Strict', 'Strict'), ('Loose', 'Loose'), ('Free', 'Free'), ('Optional', 'Optional')], validators=[DataRequired()])
	repeat = SelectField('Repeat', 
		choices=[(None, 'Select One'),('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly'), ('Yearly', 'Yearly')], validators=[DataRequired()])
	submit = SubmitField('Submit')

