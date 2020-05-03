from flask_wtf import FlaskForm

from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField

from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError





class PostForm(FlaskForm):
	title=StringField('Title',validators=[DataRequired()])
	content=TextAreaField('content',validators=[DataRequired()])
	submit=SubmitField('Post')

