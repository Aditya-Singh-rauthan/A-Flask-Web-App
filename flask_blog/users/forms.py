from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email,  EqualTo, ValidationError
from flask_login import current_user
from flask_blog.models import User




class RegistrationForm(FlaskForm):
	username=StringField('Username',validators=[DataRequired(),Length(min=2,max=10)])
	email=StringField('Email',validators=[DataRequired(),Email()])
	password=PasswordField('Password',validators=[DataRequired()])
	confirm_password=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
	submit=SubmitField('Sign Up')

	#the following function is a fascility provided by flask
	# validate_field(self,field)


	def validate_username(self,username):
		user=User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError("This username is already taken!!")

	def validate_email(self,email):
		user=User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError("This email is already taken!!")


class LoginForm(FlaskForm):
	#username=StringFeild('Username',validators=[DataRequired(),Length(min=2,max=10)])
	email=StringField('Email',validators=[DataRequired(),Email()])
	password=PasswordField('Password',validators=[DataRequired()])
	#confirm_password=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
	remember=BooleanField('Remember Me')
	submit=SubmitField('Login')

class UpdateAccountForm(FlaskForm):
	username=StringField('Username',validators=[DataRequired(),Length(min=2,max=10)])
	email=StringField('Email',validators=[DataRequired(),Email()])
	picture=FileField('Update Profile Picture',validators=[FileAllowed(['jpg','png'],'Images only!')])
	submit=SubmitField('Update')

	#the following function is a fascility provided by flask
	# validate_field(self,field)


	def validate_username(self,username):
		if username.data!=current_user.username:
			user=User.query.filter_by(username=username.data).first()
			if user:
				raise ValidationError("This username is already taken!!")

	def validate_email(self,email):
		if email.data!=current_user.email:
			user=User.query.filter_by(email=email.data).first()
			if user:
				raise ValidationError("This email is already taken!!")


class RequestResetForm(FlaskForm):
	email=StringField('Email',validators=[DataRequired(),Email()])
	submit=SubmitField('Request password reset')

	def validate_email(self,email):
		user=User.query.filter_by(email=email.data).first()
		if user is None:
			raise ValidationError("There is no account with this email!!")



class ResetPassword(FlaskForm):
	password=PasswordField('Password',validators=[DataRequired()])
	confirm_password=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
	submit=SubmitField('Reset Password')